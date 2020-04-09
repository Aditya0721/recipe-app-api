import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pauce execution until databse is available"""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database ....')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(self.style.ERROR('Databse not available, waiting for 1 second ....'))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
