pypi:
    https://pypi.org/project/python-redis-lock/

github:
    https://github.com/ionelmc/python-redis-lock
    
document:
    https://python-redis-lock.readthedocs.io/en/latest/

```text
pip install "python-redis-lock[django]
pip install "python-redis-lock[flask]
```

```python
from redis import Redis

conn = Redis()

import redis_lock

lock = redis_lock.Lock(conn, "name-of-the-lock")
if lock.acquire(blocking=False):
    print("Got the lock.")
    lock.release()
else:
    print("Someone else has the lock.")

```

```python
from redis import StrictRedis
import redis_lock
import time

conn = StrictRedis()
with redis_lock.Lock(conn, "name-of-the-lock"):
    print("Got the lock. Doing some work ...")
    time.sleep(5)
```

```python
import socket
import redis_lock
from redis import Redis

conn = Redis()

host_id = "owned-by-%s" % socket.gethostname()

lock = redis_lock.Lock(conn, "name-of-the-lock", id=host_id)

if lock.acquire(blocking=False):
    assert lock.locked() is True
    print("Got the lock.")
    lock.release()
else:
    if lock.get_owner_id() == host_id:
        print("I already acquired this in another process.")
    else:
        print("The lock is held on another machine.")
```