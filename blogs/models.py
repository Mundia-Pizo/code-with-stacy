from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

from django.db.models import Q
from django.contrib.postgres.search import(
    SearchVector,
    SearchQuery,
    SearchRank)


class ProductQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            vector = SearchVector('title', weight='A') \
                + SearchVector('description', weight='B')\
                + SearchVector('slug', weight='C')
            query = SearchQuery(query)
            result = Article.objects.annotate(rank=SearchRank(vector,
                                                              query)).filter(rank__gte=0.3).order_by('rank').order_by('-rank')
        return result


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='topics')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('topic-detail', kwargs={
            'slug': self.slug
        })

    @property
    def articles(self):
        return self.article_set.all().order_by('position')


class Article(models.Model):
    title = models.CharField(max_length=62)
    body = HTMLField()
    image = models.ImageField(upload_to='articles')
    description = models.CharField(max_length=300)
    # topic = models.ManyToManyField(Topic)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('post-detail', kwargs={
            'post_slug': self.slug
        })
