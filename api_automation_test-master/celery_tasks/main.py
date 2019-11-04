from celery import Celery
import os

# 1.读取django项目的配置
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_automation_test.settings")

# 2.创建celery对象
app = Celery('api_test_script')

# 3.加载配置
app.config_from_object('celery_tasks.config')

# 4.加载可用的任务
app.autodiscover_tasks([
    'celery_script.start_script',
])
