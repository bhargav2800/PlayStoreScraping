from django.core.management.base import BaseCommand
from subprocess import Popen, PIPE
import time


class Command(BaseCommand):
    help = 'Starts Django server and Celery worker simultaneously'

    def handle(self, *args, **options):
        django_server = Popen(['python3', 'manage.py', 'runserver'])
        time.sleep(5)  # Wait for the Django server to start (adjust the time if needed)
        celery_worker = Popen(['celery', '-A', 'PlayStoreScraping', 'worker', '--loglevel=info'])

        try:
            django_server.wait()
        except KeyboardInterrupt:
            django_server.terminate()
            celery_worker.terminate()