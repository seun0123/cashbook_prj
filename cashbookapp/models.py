from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.
class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published', default=datetime.now, editable=False)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank=True, null=True, default='')
    feeling = models.CharField(max_length = 20, blank=True, null=True, default='')

    def __str__(self):
        return self.title

    def clean(self):
        title = self.title
        if title == "":
            raise ValidationError("글을 작성해주세요")
        return super(Cashbook,self).clean()

    def clean_feeling(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.feeling
        else:
            return self.cleaned_data['feeling']