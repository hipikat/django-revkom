"""
A static file finder for building SCSS/SASS files.
"""

import os
from django.conf import settings
from django.contrib.staticfiles.finders import BaseFinder
from django.core.files.storage import FileSystemStorage
from unipath import Path
import scss
from revkom.mixins import GetSettingsMixin


class SassyFileFinder(GetSettingsMixin, BaseFinder):
    """
    A static files finder that builds CSS files using PyScss. This finder
    uses the REVKOM_SASSYFILES setting lipsum.
    """
    def __init__(self, *args, **kwargs):
        default_load_paths = []
        self.mappings = self._get_setting('REVKOM_SASSYFILES')
        self.build_dir = Path(self._get_settings(
            'REVKOM_SASSYFILES_BUILD_DIR'))
        # TODO
        scss.config.LOAD_PATHS = getattr(settings,
            'REVKOM_SASSYFILES_LOAD_PATHS', [])
        scss_vars={}
        scss_opts={
            'compress': getattr(settings, 'REVKOM_SASSYFILES_COMPRESS', True),
            'debug_info': getattr(settings, 'REVKOM_SASSYFILES_DEBUG', False),
        }
        self.scss = scss.Scss(scss_vars=scss_vars, scss_opts=scss_opts)
        super(SassyFileFinder, self).__init__(*args, **kwargs)

    def find(self, rel_path, all=False):
        """
        Given a relative path for a static CSS file, build the file into
        a temporary directory from the corresponding SASS/SCSS and return
        its absolute path. TODO: Dir patterns. Caching if it's turned on.
        """
        try:
            sassy_file = self.mappings[rel_path]
        except KeyError:
            return []
        compiled = self.scss.compile(scss_file=sassy_file)
        dest = self.build_dir.child(*os.path.split(rel_path))
        dest.parent.mkdir()
        dest.write_file(compiled)
        return dest

    def list(self, ignore_patterns=None):
        raise NotImplementedError()
