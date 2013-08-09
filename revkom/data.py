
from itertools import count

def ObservableMixin(object):
    __observers = {}
    __observer_next_id = count()

    def attach_observer(event, callback):
        """
        Register an observer for an event.
        """
        observer_id = self.__observer_next_id.next()
        self.__observers[event][observer_id] = callback
        return observer_id

    def detach_observer(observer_id):
        for event_observers in self.__observers.values():
            try:
                del event_observers[observer_id]
            except KeyError:
                pass

    def notify_event():
