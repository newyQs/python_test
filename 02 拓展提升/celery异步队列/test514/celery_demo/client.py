from celery_app import task1
from celery_app import task2

res1 = task1.add.delay(2, 8)  # 或者 task1.add.apply_async(args=[2, 8])
res2 = task2.multiply.delay(3, 7)  # 或者 task2.multiply.apply_async(args=[3, 7])
print('hello world')
