from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='topics')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('topic-detail', kwargs={
            'slug':self.slug
        })

    @property
    def articles(self):
        return self.article_set.all().order_by('position')

class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='articles')
    description = models.TextField()
    position = models.PositiveIntegerField()
    slug =models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('post-detail', kwargs={
            'topic_slug':self.topic.slug,
            'post_slug':self.slug
        })