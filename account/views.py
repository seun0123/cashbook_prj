from ast import Pass
from multiprocessing import context
from multiprocessing.reduction import duplicate
from nntplib import NNTPPermanentError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import CustomUserChangeForm, User
from account.forms import CustomUserCreationForm
from .models import User
from cashbookapp.models import Cashbook
from cashbookapp.views import write
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('mypage', user.id)
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('mypage', user.id)
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        context = {
            'form':form,
        }
        return render(request, 'login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('main')

def mypage(request, id):
    user = request.user
    user_id = str(user.id)
    if (user.is_authenticated == True) and (user_id == id) :
        user = User.objects.get(id=id)
        context = {
            'user':user,
        }
        return render(request, 'mypage.html', context)
    else:
        msg = "내 정보 페이지는 로그인 후 접근 가능합니다."
        form = AuthenticationForm()
        context = {
            'msg':msg,
            'form':form
        }
        return render(request, 'login.html', context)

@login_required
def user_update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else : 
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'user_update.html', context)

def user_update_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save() # 로그아웃됨. session정보랑 로그인정보까지 날아감.
            update_session_auth_hash(request, user)
            messages.success(request, '성공적으로 비밀번호를 변경되었습니다.')
            return redirect('mypage')
        else:
            messages.error(request, '비밀번호가 변경되지 않았습니다.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'user_update_password.html', context)