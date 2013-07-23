# pylint: disable=R0904
# R0904 - More than 20 public methods
"""
Test revkom's tools for working with static files.
"""

import tempfile
from unipath import Path
from django.test import SimpleTestCase


class CustomFileFinderTests(SimpleTestCase):
    """
    Tests for the custom file finder class which cherry-picks static
    files from a filesystem based on the ``REVKOM_STATICFILES`` setting.
    """
    base_test_settings = [
        'lib/foundation'
    ]
    def test_custom_static_find(self):
        with self.settings(REVKOM_STATICFILES=base_test_settings):
            pass

    def test_custom_static_list(self):
        pass
