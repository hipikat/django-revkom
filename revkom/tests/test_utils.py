
from unittest import TestCase as BaseTestCase
from django.test import SimpleTestCase
from revkom.utils import flat_list, unique_list


class UtilityFunctionTests(BaseTestCase):
    def test_flat_list(self):
        tups = (('one', True), ((2, None), 'three'), False, ('four'),)
        flat = ['one', True, 2, None, 'three', False, 'four',]
        self.assertEqual(flat_list(tups), flat)

    def test_unique_list(self):
        """
        NB: True and False behave like 1 and 0 in almost all contexts.
        """
        tups = (1, 'two', 3, False, 0, False, 1, None, 'two', 1, True, None)
        uniq = [1, 'two', 3, False, None]
        self.assertEqual(unique_list(tups), uniq)
