
from revkom.settings import settings_path


ADMINS = ()
PROJECT_NAME = 'revkom'
SECRET_KEY = '12345'

# Include our sibling default settings.
execfile(settings_path.child('default.py'))
