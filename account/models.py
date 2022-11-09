from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cashbookapp.models import Cashbook

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=10, null=True, blank=True)
    password1 = models.CharField(max_length=10, null=True, blank=True)
    password2 = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to = 'account/static/images/', blank=True)
    like_posts = models.ManyToManyField(Cashbook, blank=True, related_name='like_users')

