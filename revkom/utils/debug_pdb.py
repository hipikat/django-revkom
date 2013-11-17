
import warnings
from django.conf import settings


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
# TODO: Make this lazy so we can put it back in utils/__init__.py and not have to
# `from revkom.utils.debug_pdb import debug_pdb`, just `from revkom.utils import debug_pdb`.
# (Obviously having to import django.conf.settings gets in the way of most utility
# functions which need to be decoupled from a fully loaded django project.)
debug_pdb = _debug_pdb()
