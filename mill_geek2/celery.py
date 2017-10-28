import os
from celery import celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mill_geek2.settings')

app = Celery('mill_geek2/myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)