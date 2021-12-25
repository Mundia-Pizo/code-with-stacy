from django.db.models.signals import post_save
from .models import UserMembership, Membership, Subscription
from django.contrib.auth import settings
from django.dispatch import receiver


def post_save_user_memebrship(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.create(user=instance)
    user_membership, created = UserMembership.objects.get_or_create(user=instance)
    if not created:
        user_membership.membership= Membership.objects.first()
    user_membership.save()
    

post_save.connect(post_save_user_memebrship, sender=settings.AUTH_USER_MODEL)

