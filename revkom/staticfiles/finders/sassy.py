


class SassyFileFinder(BaseFinder):
    """
    A static files finder that builds CSS files using PyScss.
    """
    def __init__(self, *args, **kwargs):
        """
        Save the settings in ``REVKOM_SASSYFILES``.
        """
        try:
            self.mappings = settings.REVKOM_SASSYFILES
        except AttributeError:
            raise ImproperlyConfigured(
                "SassyFileFinder is installed in STATICFILES_FINDERS "
                "but REVKOM_SASSYFILES is missing.")
        super(SassyFileFinder, self).__init__(*args, **kwargs)

    def find(self, rel_path, all=False):
        

    def list(self, ignore_patterns=None):
        return NotImplementedError()
