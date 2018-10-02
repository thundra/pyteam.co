"""
Created by Sergii Gromovyi October of 2018
PyTeam.co
"""

from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class Profile(models.Model):
    """User's profile model"""
    user = models.OneToOneField(USER_MODEL)
    about = models.TextField()
    image = models.ImageField()
