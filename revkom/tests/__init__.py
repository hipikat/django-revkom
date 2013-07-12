
from unittest import TestCase as BaseTestCase


class ManagementCommandMixin(BaseTestCase):
    def get_command(self, cmd_module):
        cmd = cmd_module.Command()
        self.assertIn('help', dir(cmd))
        self.assertIsInstance(cmd.help, basestring)
        self.assertTrue(len(cmd.help))
        self.assertTrue(cmd.help[0].isupper())
        return cmd
