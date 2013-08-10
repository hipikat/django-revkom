# pylint: disable=R0904
# R0904 - More than 20 public methods
"""
Test the patterns package; implementations of generic software design patterns.
"""

from unittest import TestCase as BaseTestCase
from revkom.patterns import ObservableMixin


class ObserverPatternTests(BaesTestCase):
    """
    Tests for `observer pattern` mixins.

    .. _`observer pattern`: http://en.wikipedia.org/wiki/Observer_pattern
    """
    class ObserverNotified(Exception):
        def __init__(self, *args, **kwargs):
            self.name = kwargs.get('name', None)

    def get_observable_class(self, class_name="AnObservableClass"):
        return type(class_name, (ObservableMixin,), {})

    def get_observer(self, token=None):
        def an_obeserver(observee, *args, **kwargs):

    def test_observers_notifications(self):
        observable_class = self.get_observable_class()
        observable = observable_class()
        observers = [get_observer(name, token) for name, token in
                     (('notoken', None), ('footoken', 'footoken'), ('bartoken', 'bartoken'))]
        for observer in observers:
            observable.attach_observer(observer)
        observer.notify_observers()
