
from inspect import currentframe, getfile
from unipath import Path


__all__ = ['settings_path']


settings_path = Path(getfile(currentframe())).parent
