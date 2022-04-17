import uuid
import math
import time


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


def release_lock(conn, lock_name, identifier):
    """
    释放锁

    :param conn: Redis 连接
    :param lockname: 锁的名称
    :param identifier: 锁的标识
    :return:
    """
    unlock_script = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end
    """
    lockname = f'lock:{lock_name}'
    unlock = conn.register_script(unlock_script)
    result = unlock(keys=[lockname], args=[identifier])
    if result:
        return True
    else:
        return False
