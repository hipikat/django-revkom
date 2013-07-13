# pylint: disable=R0904
# R0904 - More than 20 public methods
"""
Test revkom's most generic utility functions and classes.
"""

from unittest import TestCase as BaseTestCase
from revkom.utils import flat_list, unique_list


class UtilityFunctionTests(BaseTestCase):
    """
    Tests for utility functions.
    """
    def test_flat_list(self):
        """
        Test flat_list() flattens a bumpy tuple into a flat list.
        """
        tups = (('one', True), ((2, None), 'three'), False, ('four'),)
        flat = ['one', True, 2, None, 'three', False, 'four']
        self.assertEqual(flat_list(tups), flat)

    def test_unique_list(self):
        """
        Test unique_list() returns an ordered, unique list from a tuple
        containing duplicate values. NB: True and False behave like 1 and 0 in
        almost all contexts (this is an implementation detail of Python).
        """
        tups = (1, 'two', 3, False, 0, False, 1, None, 'two', 1, True, None)
        uniq = [1, 'two', 3, False, None]
        self.assertEqual(unique_list(tups), uniq)
