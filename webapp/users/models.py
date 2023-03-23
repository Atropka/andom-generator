from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class RandomNumber(models.Model):
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)