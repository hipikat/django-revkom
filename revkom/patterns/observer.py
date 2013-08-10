
from itertools import count


class ObservableMixin(object):
    """
    An implementation of the `observer pattern`_, this mixin provide methods
    to attach and detach observer callbacks to an object, and to notify
    observers. This mixin won't do any observer notification by itself.

    .. _`observer pattern`: http://en.wikipedia.org/wiki/Observer_pattern
    """

    __observers = {}
    """
    A dict mapping observer ids to 2-tuples with an observer's callback
    function and an optional token provided to the `attach_observer()` method.
    """

    __observer_next_id = count()

    def attach_observer(callback, token=None):
        """
        Register an observer, to be notified on state changes. Return an
        observer id, which can be passed to ``detach_observer()``. If a
        token is passed, it will be passed back to the observer when it is
        sent notifications.
        """
        observer_id = self.__observer_next_id.next()
        self.__observers[observer_id] = (callback, token)
        return observer_id

    def detach_observer(observer_id):
        """
        Deregister an observer. Raises a KeyError if no such observer is
        registered.
        """
        try:
            del self.__observers[observer_id]
        except KeyError:
            raise KeyError("No observer registered with the id %s" % observer_id)

    def notify_observers(*args, **kwargs):
        """
        Notify observers by calling them with self, ``args`` and ``kwargs``,
        inserting a ``token`` keyword argument if one exists for a given
        observer.
        """
        for observer_func, token in self.__observers.values():
            if token is not None:
                kwargs['token'] = token
            observer[0](self, *args, **kwargs)
