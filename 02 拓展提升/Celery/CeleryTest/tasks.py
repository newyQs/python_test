"""

"""
import time
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def send(msg):
    print(f'send {msg}')
    time.sleep(3)

    return
