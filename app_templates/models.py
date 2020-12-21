from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Snippet(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    file  = models.FileField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    slug  = models.SlugField()
    details = RichTextUploadingField()


    def __str__(self):
        return self.title



