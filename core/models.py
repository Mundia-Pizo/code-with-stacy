from django.db import models
from django.shortcuts import reverse
from membership.models import Membership

class Course(models.Model):
    title        = models.CharField(max_length=200)
    description = models.TextField()
    image        = models.ImageField(upload_to="course-images")
    slug         = models.SlugField(null=True, blank=True)
    allowed_membership = models.ManyToManyField(Membership, default='free')
    enroled      = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('course-details', kwargs={
            "slug":self.slug
        })
    @property
    def lessons(self):
        return self.lesson_set.all().order_by('-date')

class Lesson(models.Model):
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to="lesson-images")
    slug        = models.SlugField(null=True, blank=True)
    date        = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    video_url   = models.CharField(max_length=400)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('lesson-details', kwargs={
            "course_slug":self.course.slug,
            "lesson_slug":self.slug
        })
    @property
    def topic(self):
        return self.topic_set.objects.all()
        

class MailSubscription(models.Model):
    email = models.EmailField()