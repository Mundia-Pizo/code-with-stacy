from django.contrib import admin
from .models import UserMembership, Membership, Subscription

admin.site.register(Membership)
admin.site.register(UserMembership)
admin.site.register(Subscription)

