import os
from celery import Celery

# default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

# load config from Django settings, using CELERY_prefixed keys 
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-discover tasks in Django apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')