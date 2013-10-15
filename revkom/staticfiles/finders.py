"""
Finders for static files.
"""

# TODO: Make module loading lazy so importing from PyScss will only
# throw an error if it's not installed if SassyFileFinder is included
# in STATICFILES_FINDERS


"""
A configurable static file finder for cherry-picking files.
"""

import logging
from django.conf import settings
from django.contrib.staticfiles.finders import BaseFinder
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage
from unipath import Path
from revkom.utils import GetSettingsMixin


logger = logging.getLogger(__name__)


class CustomFileFinder(GetSettingsMixin, BaseFinder):
    """
    A static files finder that cherry-picks files out of a filesystem
    according to the ``REVKOM_STATICFILES_CUSTOM`` setting. The setting
    attribute is a mapping of the format:
    {'static/file/alias.ext': '/actual/absolute/file/path.ext', ...}
    """
    def __init__(self, *args, **kwargs):
        """
        Record paths to files in ``REVKOM_STATICFILES_CUSTOM`` which exist,
        and throw warnings for any which do not exist.
        """
        self.mappings = self.get_setting('REVKOM_STATICFILES_CUSTOM')
        self.root_storages = {}
        for rel_path, abs_path in self.mappings.iteritems():
            if not Path(abs_path).exists():
                logger.warning("File %s specified in REVKOM_STATICFILES_CUSTOM "
                               "as path for static alias %s does not exist." %
                               (abs_path, rel_path))
        super(CustomFileFinder, self).__init__(*args, **kwargs)

    def find(self, rel_path, all=False):
        """
        Return the absolute filesystem path for a static file, given its
        relative path under STATIC_URL.
        """
        try:
            return self.mappings[rel_path]
        except KeyError:
            return []

    def list(self, ignore_patterns=None):
        for rel_path, abs_path in self.mappings.iteritems():
            abs_root, abs_dir = Path(abs_path).split_root()
            if abs_root not in self.root_storages:
                self.root_storages[abs_root] = \
                    FileSystemStorage(location=abs_root)
            root_storage = self.root_storages[abs_root]
            return (abs_dir, root_storage)
