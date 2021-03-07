import os

from celery import Celery
# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings')

app = Celery('LMS', backend='rpc')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'delete_yesterday_logs': {
        'task': 'academy.tasks.delete_yesterday_logs',
        'schedule': crontab(minute=30, hour=9),
        # 'schedule': crontab(minute='*/2'),
        # это для теста было
    },
}
app.conf.timezone = 'UTC'
