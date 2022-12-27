from django.db import models
# django built in validator
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Url(models.Model):
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)


class MyUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        primary_key=True,
    )
