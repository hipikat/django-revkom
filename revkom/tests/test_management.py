# pylint: disable=R0904
# R0904 - More than 20 public methods
"""
Test revkom's extensions to the django-admin.py (and manage.py) tools.
"""

import tempfile
from unipath import Path
from django.test import SimpleTestCase
from revkom.management.commands import make_secret_key
from . import ManagementCommandMixin


class ManagementCommandsTests(ManagementCommandMixin, SimpleTestCase):
    """
    Tests for revkom's custom management commands.
    """
    def test_make_secret_key(self):
        """
        Test that the make_secret_key management command writes a string of
        fifty characters to the path settings.SECRET_KEY_FILE.
        """
        cmd = self.get_command(make_secret_key)
        with tempfile.NamedTemporaryFile() as key_file:
            key_file_name = key_file.name
            with self.settings(SECRET_KEY_FILE=key_file_name):
                cmd.handle()
                self.assertTrue(Path(key_file_name).exists())
                key_file.seek(0)
                key_contents = key_file.read()
                self.assertIsInstance(key_contents, basestring)
                self.assertTrue(len(key_contents) == 50)
        self.assertFalse(Path(key_file_name).exists())
