from django.db import models
from django.utils import timezone


class input(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)
