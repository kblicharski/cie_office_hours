from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cie_office_hours.settings')

app = Celery('cie_office_hours', broker='amqp://', backend='rpc://')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Executes every day at 8:30 a.m.
    'daily-session-management': {
        'task': 'office_hours.tasks.create_daily_office_hour_sessions',
        'schedule': crontab('30', '8')
    },
}
app.conf.timezone = 'America/Chicago'


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
