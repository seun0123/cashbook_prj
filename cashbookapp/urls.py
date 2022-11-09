"""cashbookprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import cashbookapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', cashbookapp.views.main, name='main'),
    path('write/', cashbookapp.views.write, name='write'),
    path('read/', cashbookapp.views.read, name='read'),
    path('edit/<str:id>', cashbookapp.views.edit, name='edit'),
    path('detail/<str:id>', cashbookapp.views.detail, name='detail'),
    path('delete/<str:id>', cashbookapp.views.delete, name='delete'),
    path('update_comment/<str:id>/<str:com_id>/',cashbookapp.views.update_comment, name='update_comment'),
    path('delete_comment/<str:id>/<str:com_id>/',cashbookapp.views.delete_comment, name='delete_comment'),
    path('hashtag/', cashbookapp.views.hashtag, name='hashtag'),
    path('hashtag_home/', cashbookapp.views.hashtag_home, name="hashtag_home"),
    path('hashtag_detail/<str:id>/<str:hashtag_id>/', cashbookapp.views.hashtag_detail, name="hashtag_detail"),
    path('hashtag_delete/<str:id>/<str:hashtag_id>/', cashbookapp.views.hashtag_delete, name="hashtag_delete"),
    path('post_like/<str:post_id>/', cashbookapp.views.post_like, name="post_like"),
    path('search/', cashbookapp.views.search, name='search'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
