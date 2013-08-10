
from revkom.patterns import ObservableMixin


class BaseData(ObservableMixin):
    """
    ABC for Data objects, which are designed to work as controlled instance
    properties on classes.
    """


class BooleanData(BaseData):
    """
    A boolean state - True or False. If a default value is not passed into
    the constructor, the data is considered uninitialised until a value is
    set, and attempting to access the data will raise an AttributeError.
    """
    _value = None

    def __init__(*args, **kwargs):
        """Set self to the truth of the ``default`` kwarg, if it exists."""
        try:
            self = kwargs['default']
        except KeyError:
            pass

    def __get__(self, obj, obj_type=None):
        """Return our value or raise an AttributeError if we aren't initialised."""
        if self._value is None:
            raise AttributeError("%s has not been initialised" % self.__class__)
        return self._value

    def __set__(self, obj, value):
        """Set our value to the boolean truth of the passed-in value."""
        self._value = bool(value)
