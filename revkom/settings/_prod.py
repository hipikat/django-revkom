# settings/base_prod.py
#
# Base production settings for a project to include via execfile().

from revkom.settings import base_settings_mixin


# Debugging and development modes
DEBUG = False

# Include our sibling base settings. (Note: this also sets s and g.)
execfile(base_settings_mixin('base'))
