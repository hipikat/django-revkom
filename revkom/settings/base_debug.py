
from revkom.settings import settings_path


g = globals()


# Debugging and development modes
DEBUG = True
TEMPLATE_STRING_IF_INVALID = 'INVALID_CONTEXT[%s]'

# Include our sibling base settings. (Note: this also sets s and g.)
execfile(settings_path.child('base.py'))

# Directory structure
MEDIA_ROOT = g.get('MEDIA_ROOT', g['TMP_DIR'].child('media'))
