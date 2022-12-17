from django.contrib.auth.models import User
from django.db import models

PERMISSION_CHOICES = (
    (1, 'Read Packages'),
    (2, 'Update Packages'),
    (3, 'Create Packages'),
    (4, 'Administrator'),
)
PERMISSION_NAMES = (
    'read_packages',
    'update_packages',
    'create_packages',
    'admin',
)

class TeamMember(models.Model):
    """
    A User working as part of a Team (which is a User unlogginable account)
    """
    team = models.ForeignKey(User, related_name="members")
    user = models.ForeignKey(User, related_name="memberships")
    permission = models.IntegerField(choices=PERMISSION_CHOICES)
    creator = models.BooleanField(default=False)
    
    def __unicode__(self):
        return f"{self.user.username} on team {self.team.username}"
    
    def save(self, *args, **kwargs):
        """
        Give the user proper permissions so django guardian can check them
        """
        from guardian.shortcuts import assign
        super(TeamMember, self).save(*args, **kwargs)
        assign(PERMISSION_NAMES[self.permission - 1], self.user, self.team)
    
    @models.permalink
    def get_absolute_url(self):
        return ('userrouter-index', [self.team.username])
