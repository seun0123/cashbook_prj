from socket import fromshare
from django import forms
from django.contrib.auth import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User()
        fields = fields = ['username','password1','password2','age', 'phone', 'address','image']

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = fields = ['username','password1','password2','age', 'phone', 'address','image']
