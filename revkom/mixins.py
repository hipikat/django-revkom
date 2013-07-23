"""
Generic mixins for classes.
"""

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
