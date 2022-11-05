from django.contrib import admin
from .models import Cashbook, Comment, Hashtag

# Register your models here.
admin.site.register(Cashbook)
admin.site.register(Comment)
admin.site.register(Hashtag)