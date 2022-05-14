from celery import (
    Celery,
    task,
    shared_task,
    current_app,
    current_task,
    maybe_signature,
    chain,
    chord,
    chunks,
    group,
    signature,
    xmap,
    xstarmap,
    uuid
)

import uuid

"""
UUID（Universally Unique Identifier）是通用唯一识别码
"""

print(uuid.uuid1())

print(uuid.uuid3())

print(uuid.uuid4())

print(uuid.uuid5())
