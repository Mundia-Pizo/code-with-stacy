from django.db.models.signals import post_save, post_connect
from .models import UserMembership, Membership, Subscription
from django.contrib.auth import settings


def post_save_user_membership(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)

    user_membership, created = UserMembership.objects.get_or_create(user=instance)
    ### perform some logic to veryfy payment
    user_membership.save()

post_save.connect(post_save_user_membership, sender=settings.AUTH_USER_MODEL)