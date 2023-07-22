"""
Test custom Django management commands.
"""
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2Error


@patch(
    'core.management.commands.wait_for_db.Command.check_database_connection')
class CommandTests(SimpleTestCase):
    """Test Commands"""

    def test_wait_for_db_ready(self, patched_check_database_connection):
        """Test waiting for database if database is ready"""
        patched_check_database_connection.return_value = True
        call_command('wait_for_db')
        patched_check_database_connection.assert_called_once_with('default')

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep,
                               patched_check_database_connection):
        """Test waiting for database delay"""
        patched_check_database_connection.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_check_database_connection.call_count, 6)
        patched_check_database_connection.assert_called_with('default')
