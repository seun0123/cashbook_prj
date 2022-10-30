from email import contentmanager
from email.mime import image
from http.client import HTTPResponse
from time import time
from turtle import title
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CashbookForm, CommentForm
from django.utils import timezone
from .models import Cashbook, Comment
from account.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.http import request

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
            form.user = request.user
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

def detail(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.cashbook_id = cashbooks
            comment.author = request.user
            comment.text = form.cleaned_data['text']
            comment.save()
            id = id
            return redirect('detail', id)
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'cashbooks':cashbooks, 'form':form})

@login_required
def edit(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    if request.method == "POST":
        form = CashbookForm(request.POST, request.FILES, instance=cashbooks)
        if form.is_valid():
            form.save(commit = False)
            form.update_at = timezone.now()
            form.save()
            return redirect('read')
    else:
        form = CashbookForm(instance=cashbooks)
        context = {
            'form': form,
            'cashbooks' : cashbooks,
        }
        return render(request, 'edit.html', context)

def delete(request, id):
    cashbooks = get_object_or_404(Cashbook, id=id)
    cashbooks.delete()
    return redirect('read')

def update_comment(request, id, com_id):
    post = get_object_or_404(Cashbook, id=id)
    comment = get_object_or_404(Comment, id=com_id)
    form = CommentForm(instance=comment)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=comment)
        if update_form.is_valid():
            comment = update_form.save(commit = False)
            comment.author = request.user
            comment.post_id = post
            comment.content = update_form.cleaned_data['text']
            update_form.save()
            return redirect('detail', id)
    return render(request, 'update_comment.html', {'form':form, 'post':post, 'comment':comment})        

def delete_comment(request, id, com_id):
    comment = get_object_or_404(Comment,id=com_id)
    comment.delete()
    return redirect('detail', id)