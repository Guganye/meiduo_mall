import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mall.settings')

# 实例化celery
app = Celery('celery_tasks')

# broker配置
app.config_from_object('celery_tasks.config')

# 自动检测指定包的任务
app.autodiscover_tasks(['celery_tasks.sms', 'celery_tasks.email', 'celery_tasks.timed'])

# worker
# celery -A 实例化脚本路径 worker -l info
# Windows权限限制（管理员身份运行） or celery -A celery_tasks.main worker --pool=solo
# celery -A celery_tasks.main worker -l info

# 精简版
# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# @app.task
# def add(x, y):
#   return x+y


