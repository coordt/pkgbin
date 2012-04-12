from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import create_user_container

@receiver(post_save, sender=User)
def new_user_handler(sender, instance, created, **kwargs):
    if created:
        create_user_container.delay(instance)

    