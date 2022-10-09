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

def write(request):
    context = {}
    if request.method == 'POST':
        form = CashbookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_at = timezone.now()
            form.save()
            return redirect('read')
        
        else:
            context = {
                'form':form,
            }
            return render(request, 'write.html', context)
    else:
        form = CashbookForm
        return render(request, 'write.html', {'form': form})

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