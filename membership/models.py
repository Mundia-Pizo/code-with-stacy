from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

CHOICES=(
('Free', "free"),
("Professional", 'pro'),
("Enterprise", 'ent')
)

class Membership(models.Model):
    membership_type = models.CharField(max_length=30, choices=CHOICES,  default='free')
    slug            = models.SlugField()
    price           = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.membership_type

class UserMembership(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    membership      = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.user.username


def post_save_usermembership(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)
    user_membership, created =UserMembership.objects.get_or_create(user=instance)
    user_membership.save()

post_save.connect(post_save_usermembership, sender=settings.AUTH_USER_MODEL)

class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)


    def __str__(self):
        return self.user_membership.user.username



