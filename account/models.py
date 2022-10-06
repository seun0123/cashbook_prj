from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'user',blank=True)
    def __str__(self):
        return self.username

