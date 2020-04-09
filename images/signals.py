from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from . import models


@receiver(m2m_changed, sender=models.Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
