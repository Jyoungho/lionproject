from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.

def requests(request):
    context = {}
    return render(request, 'requests/requests.html', context)

def new(request):
    context = {}
    return render(request, 'requests/new.html', context)

def create(request):
    context = {}
    return render(request, 'requests/requests.html', context)

def detail(request):
    context = {}
    return render(request, 'requests/detail.html', context)

def edit(request):
    context = {}
    return render(request, 'requests/edit.html', context)

def delete(request):
    context = {}
    return redirect('requests:requests')