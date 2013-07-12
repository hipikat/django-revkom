
import tempfile
from unittest import TestCase as BaseTestCase
from django.conf import settings
from django.test import SimpleTestCase
from revkom.management.commands import make_secret_key
from . import ManagementCommandMixin


class ManagementCommandsTests(ManagementCommandMixin, SimpleTestCase):
    def test_make_secret_key(self):
        cmd = self.get_command(make_secret_key)
        with tempfile.NamedTemporaryFile() as key_file:
            with self.settings(SECRET_KEY_FILE=key_file.name):
                cmd.handle()
                key_file.seek(0)
                key_contents = key_file.read()
                self.assertIsInstance(key_contents, basestring)
                self.assertTrue(len(key_contents) == 50)
