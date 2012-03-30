from django.db import models
from django.contrib.auth.models import User

from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(
        User,
        unique=True,
        related_name='profile')
    organization = models.BooleanField(default=False)
    members = models.ManyToManyField(
        User, 
        blank=True, 
        related_name="organizations")
    creator_id = models.IntegerField(blank=True, null=True)
