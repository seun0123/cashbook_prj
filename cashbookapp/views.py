from email import contentmanager
from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CashbookForm
from django.utils import timezone
from .models import Cashbook
from account.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

# Create your views here.
def main(request):
    return render(request, 'main.html')

@login_required
def write(request):
    user = request.user
    user_id = str(user.id)
    if (user.is_authenticated == True) and (user_id == id): # user.id 는 진짜 id이고 html에서 받아온 id는 생긴건 id지만 str이라서 str(user.id)==id로 해줘야 함.
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return render(request, 'write.html')
    else:
        msg = " 글작성 페이지는 로그인 후 접근 가능합니다."
        form = AuthenticationForm()
        context = {
            'msg':msg,
            'form':form
        }
    return render(request, 'login.html', context)

def read(request):
    cashbooks = Cashbook.objects
    return render(request, 'read.html', {'cashbooks':cashbooks})

def detail(request, id=id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    return render(request, 'detail.html', {'cashbooks':cashbooks})

@login_required
def edit(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.user == Cashbook.user :
        if request.method == "POST":
            form = CashbookForm(request.POST, request.FILES, instance=cashbooks)
            if form.is_valid():
                form.save()
                return redirect('read')
        else:
            form = CashbookForm(instance=cashbooks)
    context = {
        'form': form,
        'cashbooks' : cashbooks,
    }
    return render(request, 'edit.html', context)

@require_POST
def delete(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.user.is_authenticated :
        if request.user == Cashbook.user:
            cashbooks.delete()
            return redirect('non_login_index')
    return redirect('detail', id)