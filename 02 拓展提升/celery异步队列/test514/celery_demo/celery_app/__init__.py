from celery import Celery

app = Celery('demo')  # 生成实例
app.config_from_object('celery_app.celeryconfig')  # 加载配置