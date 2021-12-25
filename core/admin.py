from django.contrib import admin
from .models import Course, Lesson, MailSubscription, Contact, Project

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(MailSubscription)
admin.site.register(Contact)
admin.site.register(Project)

