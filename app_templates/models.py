from django.db import models

class Snippet(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    file  = models.FileField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    slug  = models.SlugField()


    def __str__(self):
        return self.title



