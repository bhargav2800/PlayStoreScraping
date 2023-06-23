# Configure Celery
import os
import celery
from django.conf import settings

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlayStoreScraping.settings')

# Create Celery app
app = celery.Celery('PlayStoreScraping')

# Load Celery settings from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover asynchronous tasks in Django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
