"""
Tools for working with static files.
"""

import logging
from django.conf import settings
from django.contrib.staticfiles.finders import BaseFinder
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage
from unipath import Path


logger = logging.getLogger(__name__)


class CustomFileFinder(BaseFinder):
    """
    A static files finder that cherry-picks files out of a filesystem
    according to the ``REVKOM_STATICFILES`` setting. The setting
    attribute is a mapping of the format:
    {'static/file/alias.ext': '/actual/absolute/file/path.ext', ...}
    """
    def __init__(self, *args, **kwargs):
        """
        Record paths to files in ``REVKOM_STATICFILES`` which exist and throw
        warnings for any which do not exist.
        """
        try:
            self.mappings = settings.REVKOM_STATICFILES
            self.root_storages = {}
        except AttributeError:
            raise ImproperlyConfigured(
                "CustomFileFinder is installed in STATICFILES_FINDERS "
                "but REVKOM_STATICFILES is missing.")
        for rel_path, abs_path in self.mappings.iteritems():
            if not Path(abs_path).exists():
                logger.warning("File %s specified in REVKOM_STATICFILES as "
                               "path for static alias %s does not exist." %
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
