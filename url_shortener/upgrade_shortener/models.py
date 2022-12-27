import django
from django.db import models
from django.utils import timezone
# Create your models here.


class LinkInfo(models.Model):
    username = models.CharField(max_length=50)
    destination = models.CharField(max_length=200)
    title = models.CharField(max_length=30)
    domain = models.CharField(default='short.ly', max_length=20, choices=[('short.ly', 'short.ly')])
    custom_half = models.CharField(max_length=20, unique=True, primary_key=True)
    date = models.DateField(default=django.utils.timezone.now)
    datetime = models.DateTimeField(default=django.utils.timezone.now)
