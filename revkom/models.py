"""
TODO: Helpers and mixins for Django models.
"""

from django.conf import settings
from django.db.models import Model
from model_utils.managers import PassThroughManager


class ProjectManager(PassThroughManager):
    pass


class ProjectModel(Model):
    objects = ProjectManager()

    class Meta:
        app_label = settings.PROJECT_MODULE
        abstract = True
