
import warnings
from django.conf import settings
from .mixins import GetSettingsMixin


def _debug_pdb():
    """
    Return a pdb module if settings.DEBUG is True. Otherwise, issue
    an ImportWarning and return a stub object with a set_trace method
    that does nothing.
    """
    class StubPdb(object):
        def set_trace():
            pass

    if settings.DEBUG:
        import pdb
        return pdb
    else:
        return StubPdb()
debug_pdb = _debug_pdb()
