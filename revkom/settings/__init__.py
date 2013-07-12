"""
This package facilitates the provision of organised, pre-configured
Django projects, by providing boilerplate settings for a typical medium-
sized web site (i.e. a modicum of bespoke code, but shy of "web scale",
as a size-queen would call it - your typical skunkworks job).

TODO: Highlight features!
"""

from inspect import currentframe, getfile
from unipath import Path


__all__ = ['SETTINGS_PATH', 'base_settings_mixin']


SETTINGS_PATH = Path(getfile(currentframe())).parent


def base_settings_mixin(settings='base', abstract=True):
    """
    Returns the absolute path to a (presumed existing) settings mixin.
    Intended to be passed to execfile(), when some concrete settings file
    wishes to extend a base file.
    """
    return SETTINGS_PATH.child('%s%s.py' % ('_' if abstract else '', settings))
