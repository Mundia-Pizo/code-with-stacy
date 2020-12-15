from django.db import models
from core.models import Course
from django.contrib.auth.models import User

class CoursePayment(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    course_payed = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user} payed for {self.course_payed}"


class SnippetPayment(models.Model):
    pass




