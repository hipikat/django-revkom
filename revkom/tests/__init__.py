# pylint: disable=R0904
# R0904 - More than 20 public methods
"""
The revkom.tests base package contains convenience functions and mixins
for writing tests using the standard Django test framework, built on
Python's unittest framework. The sub-modules beginning with 'test_' are
the actual tests for the revkom app itself.

https://docs.djangoproject.com/en/dev/topics/testing/overview/
"""

from unittest import TestCase as BaseTestCase


class ManagementCommandMixin(BaseTestCase):
    """
    Class mixin for TestCase sub-classes that test Django management commands.
    """
    def get_command(self, cmd_module):
        """
        Get an instance of the Command class from a management command module,
        which should be a sub-class of django.core.management.base.BaseCommand.
        Test that the class has a 'help' attribute; a non-empty string.
        """
        cmd = cmd_module.Command()
        self.assertIn('help', dir(cmd))
        self.assertIsInstance(cmd.help, basestring)
        self.assertTrue(len(cmd.help))
        return cmd
