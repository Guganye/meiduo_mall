from celery import Celery
import os

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mall.settings')
# 实例化(目录) celery
app = Celery('celery_tasks')
# broker
app.config_from_object('celery_tasks.config')
# 自动检测指定包的任务 tasks
app.autodiscover_tasks(['celery_tasks.sms'])
# worker
# celery -A 实例化脚本路径 worker -l info
# celery -A celery_tasks.main worker -l info

# 精简版
# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# @app.task
# def add(x, y):
#   return x+y
