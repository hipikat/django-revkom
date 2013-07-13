# pylint: disable=R0904
# R0904 - More than 20 public methods
"""
Test revkom's abstract base settings and settings config helpers.
"""

from unittest import TestCase as BaseTestCase
from django.core.exceptions import ImproperlyConfigured


class SettingsFileTests(BaseTestCase):
    """
    Tests for abstract base settings files.
    """
    def test_abstract_settings_files(self):
        """
        Test that abstract base files throw an ImproperlyConfigured exception
        when they don't find required names in their globals() dict.
        """
        try:
            __import__("revkom.settings._base")
        except ImproperlyConfigured:
            pass
        else:
            self.fail("Importing abstract base settings without required " +
                      "globals set should raise ImproperlyConfigured.")


class SettingsUtilsTests(BaseTestCase):
    """
    Tests for revkom's utilities for settings file configuration.
    """
    def test_log_settings_deep_update(self):
        """
        Test LoggingSettings instances' deep_update method doesn't overwrite
        existing deeply-nested mappings in the dict when updated with others.
        """
        # TODO
    def test_add_logfile_handler(self):
        """
        Test that the add_logfile_handler method on LoggingSettings instances
        creates an appropriate logfile handler using logfile defaults passed to
        the instance constructor, revkom.settings.utils.LOGFILE_DEFAULTS, or
        logfile_defaults passed to the method.
        """
        # TODO
    def test_add_many_logfile_handlers(self):
        """
        Test the method for setting multiple logfile handlers simultaneously.
        """
        # TODO
