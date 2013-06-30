
from revkom.settings import settings_path


g = globals()


# Debugging and development modes
DEBUG = True

# Include our sibling base settings. (Note: this also sets s and g.)
execfile(settings_path.child('base.py'))

# Directory structure
MEDIA_ROOT = g.get('MEDIA_ROOT', g['VAR_DIR'].child('media'))

# Databases
DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2'}}
