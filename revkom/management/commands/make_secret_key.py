"""
Produces a secret key file, required by Django. The Revkom app will by
default set settings.SECRET_KEY_FILE to SECRET_KEY under a conf
directory, which defaults to var/ under the suggested project structure.

https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
"""

import random
from django.core.management.base import BaseCommand
from django.conf import settings


SECRET_KEY_LENGTH = 50
SECRET_KEY_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'


class Command(BaseCommand):
    """
    Creates a file with the full path name taken from settings.SECRET_KEY_FILE,
    which contains 50 random characters.
    """
    help = "Generate a secret key in %s" % settings.SECRET_KEY_FILE

    def handle(self, *args, **options):
        secret_key = ''.join(
            [random.SystemRandom().choice(SECRET_KEY_CHARS)
                for _ in range(SECRET_KEY_LENGTH)])
        with open(settings.SECRET_KEY_FILE, 'w') as key_file:
            key_file.write(secret_key)
