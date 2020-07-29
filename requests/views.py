from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    render(requset, 'requests/index.html', context)