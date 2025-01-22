from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, **kwargs):
    user_group = Group.objects.get(name='client'.capitalize())
    instance.groups.add(user_group)
