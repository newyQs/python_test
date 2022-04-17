from redis import Redis

conn = Redis()

import redis_lock

lock = redis_lock.Lock(conn, "name-of-the-lock")
if lock.acquire(blocking=False):
    print("Got the lock.")
    lock.release()
else:
    print("Someone else has the lock.")
