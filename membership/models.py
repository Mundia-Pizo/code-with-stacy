from django.db import models
from django.contrib.auth.models import User

CHOICES=(
('Free', "free"),
("Professional", 'pro'),
("Enterprise", 'ent')
)

class Membership(models.Model):
    membership_type = models.CharField(max_length=30, choices=CHOICES)
    slug            = models.SlugField()
    price           = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.membership_type

class UserMembership(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    membership      = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)


    def __str__(self):
        return self.user_membership.user.username



