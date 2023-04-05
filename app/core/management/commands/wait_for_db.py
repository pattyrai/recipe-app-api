"""
Django command to wait for  the database to be available
"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError

class Command(BaseCommand):
    """ Django command to wait for database """
    
    def handle(self, *args, **options):
        """ Entrypoint for command """
        self.stdout.write("Waiting for database ....")
        db_up = False

        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20pError, OperationalError): 
                self.stdout.write("Database not initialized yet, waiting 1 sec ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))

