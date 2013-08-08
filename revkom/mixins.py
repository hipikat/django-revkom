"""
Generic mixins for classes.
"""

from functools import partial
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class GetSettingsMixin(object):
    """
    A generic class mixin which adds a _get_settings() method, which will
    return a tuple of settings or throw appropriate errors if they aren't
    defined. TODO: Extend to allow default settings or warn instaed of error.
    """
    def _get_setting(self, setting):
        try:
            return getattr(settings, setting)
        except AttributeError:
            raise ImproperlyConfigured(
                "%s requires the setting %s to be defined." %
                (self.__class__.__name__, setting))

    def _get_settings(self, *get_list, **default_list):
        setting_list = []
        for setting in get_list:
            setting_list.append(self._get_setting(setting))
        for setting, default in default_list.iteritems():
            setting_list.append(getattr(settings, setting, default))
        return setting_list


class InstanceProp(object):

    def accessors(self):
        access = [self.getter]
        if hasattr(self, setter):
            access.append(self.setter)
            if hasattr(self, deleter):
                access.append(self.deleter)

    def getter(self):
        raise NotImplementedError


class BooleanProp(InstanceProp):

    def __init__(self, default):
        self._value = bool(default) if default else None

    def getter(self):
        return self._value

    def setter(self, value):
        self._value = bool(value)


class StringProp(InstanceProp):
    # TODO: Should this be unicode or something?

    def __init__(self, default):
        self._value = str(default) if default else None

    def getter(self):
        return self._value

    def setter(self, value):
        self._value = str(value)


class PropMetaclass(type):
    _prop_types = {
        'boolean': BooleanProp,
        'string': StringProp,
    }

    def __new__(mcls, name, bases, attrs):
        #def print_foo(self):
        #    print('foo')
        #attrs['print_bar'] = print_foo

        def _add_prop(ptype_class, self, prop_name, *init_args, **init_kwargs):
            """
            Add a property called prop_name to self. The property's getter, setter
            and deleter are taken from methods (with those names) attached to a new
            instance of ``ptype_class``, where they exist. The propety is
            initialised with ``init_args`` and ``init_kwargs``.
            """
            # TODO: Warn if property already exists?
            import pdb; pdb.set_trace()
            prop_instance = ptype_class(*init_args, **init_kwargs)
            accessors = [prop_instance.getter]
            if hasattr(prop_instance, 'setter'):
                accessors.append(prop_instance.setter)
                if hasattr(prop_instance, 'deleter'):
                    accessors.append(prop_instance.deleter)
            prop = property(*accessors)
            setattr(self, prop_name, prop)

        #attrs['_add_prop'] = _add_prop
        for ptype_name, ptype_class in mcls._prop_types.iteritems():
            prop_adder_name = "add_%s_prop" % ptype_name
            prop_adder_func = partial(_add_prop, ptype_class)
            attrs[prop_adder_name] = prop_adder_func
            #setattr(instance, prop_adder_name, prop_adder_func)
        return super(PropMetaclass, mcls).__new__(mcls, name, bases, attrs)

#    def __new__(cls, *args, **kwargs):
#        """
#        Return a new instance of cls, with methods like ``add_boolean_prop(...)``
#        attached, ready to be used in the instance's ``__init__(...)`` method.
#        """
#        instance = super(PropMixin, cls).__new__(cls, *args, **kwargs)
#        for ptype_name, ptype_class in cls._prop_types.iteritems():
#            prop_adder_name = "add_%s_prop" % ptype_name
#            prop_adder_func = partial(instance._add_prop, ptype_class)
#            setattr(instance, prop_adder_name, prop_adder_func)
#        return instance

