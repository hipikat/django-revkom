# settings/__init__.py

from inspect import currentframe, getfile
from unipath import Path


__all__ = ['settings_path', 'base_settings_mixin']


settings_path = Path(getfile(currentframe())).parent

def base_settings_mixin(settings='base'):
    return settings_path.child('_%s.py' % settings)
