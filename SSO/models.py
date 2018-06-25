from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    words = models.CharField(max_length=50, default='0')

    def __str__(self):
        return self.username