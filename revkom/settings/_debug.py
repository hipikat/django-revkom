# settings/base_debug.py
#
# Base debug settings for a project to include via execfile().

from revkom.settings import base_settings_mixin


# Debugging and development modes
DEBUG = True
TEMPLATE_STRING_IF_INVALID = 'INVALID_CONTEXT[%s]'

# Include our sibling base settings. (Note: this also sets s and g.)
execfile(base_settings_mixin('base'))

# Directory structure
MEDIA_ROOT = globals()['TMP_DIR'].child('media')
