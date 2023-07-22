import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for the database."""
    help = "Django command to wait for the database"

    def add_arguments(self, parser):
        parser.add_argument('--retries', type=int, default=60,
                            help='Maximum number of retries \
                                to wait for the database.')
        parser.add_argument('--retry-delay', type=int, default=5,
                            help='Delay (in seconds) between retries.')

    def handle(self, *args, **options):
        """Entrypoint for the command."""
        self.stdout.write("Waiting for the database...")

        max_retries = options['retries']
        retry_delay = options['retry_delay']

        for retry in range(1, max_retries + 1):
            try:
                for db_alias in connections:
                    self.check_database_connection(db_alias)
                self.stdout.write(self.style.SUCCESS('Database available!'))
                return

            except (OperationalError, Psycopg2Error) as ex:
                self.stdout.write(f"Attempt {retry}/{max_retries}: {ex}")
                time.sleep(retry_delay)

        self.stdout.write(self.style.ERROR(
            f"Database not available after {max_retries} retries."))
        raise SystemExit(1)

    def check_database_connection(self, db_alias):
        """Check the database connection."""
        conn = connections[db_alias]
        c = conn.cursor()
        c.execute("SELECT 1")
        c.fetchone()
        c.close()
