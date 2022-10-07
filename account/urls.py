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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', account.views.mypage, name='mypage'),
    path('signup/', account.views.signup, name='signup'),
    path('login/',account.views.login, name='login'),
    path('mypage/<str:id>',account.views.mypage, name='mypage'),
    path('logout/', account.views.logout, name='logout'),
    path('user_update/', account.views.user_update, name='user_update'),
    path('user_update_password/',account.views.user_update_password, name='user_update_password'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
