from django.db import models
from django.contrib.auth.models import User, Group

from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(
        User,
        unique=True,
        related_name='profile')
    organization = models.BooleanField(default=False)
    # group = models.ForeignKey(Group, blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    

