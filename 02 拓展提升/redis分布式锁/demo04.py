"""
加锁过程

首先需要为锁生成一个唯一标识identifier；
然后使用redis set 命令设置锁，从 v2.6.12 版本开始，set命令支持nx和ex参数，具体内容可点击进行查看；如果锁之前不存在，则加锁成功，并设置锁的过期时间，返回锁唯一标识；
如果锁设置失败，则先判断一下该锁是否有过期时间，如果没有则进行设置；其实这一步可以省略，因为redis的命令都是原子性的。
解锁过程

首先整个解锁操作需要在一个 Redis 的事务中进行，python 中 redis 事务是通过pipeline的封装实现的；
使用WATCH 监听锁，防止在解锁时出现锁被其他客户端修改；
查询锁对应的标识是否与本次解锁的标识相同；
如果标识相同，则在事务中删除锁，如果删除过程中锁自动失效又被其他客户端拿到（即锁标识被其他客户端修改），此时设置了 WATCH 就会删除失败，这样就不会出现删除了其他客户端锁的情况。

https://www.jianshu.com/p/0773a0265e09
"""

import uuid
import time
import math


def acquire_lock(cli, lockname, acquire_timeout=3, lock_timeoout=2):
    """获取锁
    @param cli:   Redis实例
    @param lockname:   锁名称
    @param acquire_timeout: 客户端获取锁的超时时间（秒）, 默认3s
    @param lock_timeout: 锁过期时间（秒）, 超过这个时间锁会自动释放, 默认2s
    """
    lockname = f"lock:{lockname}"
    identifier = str(uuid.uuid4())
    lock_timeoout = math.ceil(lock_timeoout)

    end_time = time.time() + acquire_timeout

    while time.time() <= end_time:
        # 如果不存在当前锁, 则进行加锁并设置过期时间, 返回锁唯一标识
        if cli.set(lockname, identifier, ex=lock_timeoout, nx=True):  # 一条命令实现, 保证原子性
            return identifier
        # 如果锁存在但是没有失效时间, 则进行设置, 避免出现死锁
        elif cli.ttl(lockname) == -1:
            cli.expire(lockname, lock_timeoout)

        time.sleep(0.001)

    # 客户端在超时时间内没有获取到锁, 返回False
    return False


def release_lock(cli, lockname, identifier):
    """释放锁
    @param cli: Redis实例
    @param lock_name:   锁名称
    @param identifier:  锁标识
    """
    with cli.pipeline() as pipe:
        lockname = f"lock:{lockname}"
        while True:
            try:
                pipe.watch(lockname)
                id = pipe.get(lockname)
                if id and id == identifier:
                    pipe.multi()
                    pipe.delete(lockname)
                    pipe.execute()  # 执行EXEC命令后自动执行UNWATCH （DISCARD同理）
                    return True
                pipe.unwatch()  # 没有参数
                break
            except redis.WatchError:
                pass
        return False


if __name__ == '__main__':

    from threading import Thread

    import redis

    # Redis 存字符串返回的是byte,指定decode_responses=True可以解决
    pool = redis.ConnectionPool(host="127.0.0.1", port=6379, socket_connect_timeout=3, decode_responses=True)
    redis_cli = redis.Redis(connection_pool=pool)

    count = 10


    def ticket(i):
        identifier = acquire_lock(redis_cli, 'Ticket')
        print(f"线程{i}--获得了锁")
        time.sleep(1)
        global count
        if count < 1:
            print(f"线程{i}没抢到票, 票已经抢完了")
            return
        count -= 1
        print(f"线程{i}抢到票了, 还剩{count}张票")
        release_lock(redis_cli, 'Resource', identifier)
        print(f"线程{i}--释放了锁")


    for i in range(20):
        t = Thread(target=ticket, args=(i,))
        t.start()
