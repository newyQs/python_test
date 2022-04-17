"""
如果你使用的 Redis 版本大于等于 2.6.12 版本，加锁的过程就可以进行简化。因为这个版本以后的 Redis set 操作支持 EX 和 NX 参数，是一个原子性的操作。

EX seconds ： 将键的过期时间设置为 seconds 秒。 执行 SET key value EX seconds 的效果等同于执行 SETEX key seconds value 。
NX ： 只在键不存在时， 才对键进行设置操作。 执行 SET key value NX 的效果等同于执行 SETNX key value 。
"""
import uuid
import math
import time

from redis import WatchError


def acquire_lock_with_timeout(conn, lock_name, acquire_timeout=3, lock_timeout=2):
    """
    基于 Redis 实现的分布式锁

    :param conn: Redis 连接
    :param lock_name: 锁的名称
    :param acquire_timeout: 获取锁的超时时间，默认 3 秒
    :param lock_timeout: 锁的超时时间，默认 2 秒
    :return:
    """

    identifier = str(uuid.uuid4())
    lockname = f'lock:{lock_name}'
    lock_timeout = int(math.ceil(lock_timeout))

    end = time.time() + acquire_timeout

    while time.time() < end:
        # 如果不存在这个锁则加锁并设置过期时间，避免死锁
        if conn.set(lockname, identifier, ex=lock_timeout, nx=True):
            return identifier

        time.sleep(0.001)

    return False


def release_lock(conn, lockname, identifier):
    """
    释放锁

    :param conn: Redis 连接
    :param lockname: 锁的名称
    :param identifier: 锁的标识
    :return:
    """
    # python中redis事务是通过pipeline的封装实现的
    with conn.pipeline() as pipe:
        lockname = 'lock:' + lockname

        while True:
            try:
                # watch 锁, multi 后如果该 key 被其他客户端改变, 事务操作会抛出 WatchError 异常
                pipe.watch(lockname)
                iden = pipe.get(lockname)
                if iden and iden.decode('utf-8') == identifier:
                    # 事务开始
                    pipe.multi()
                    pipe.delete(lockname)
                    pipe.execute()
                    return True

                pipe.unwatch()
                break
            except WatchError:
                pass
        return False
