from django.shortcuts import render

# Create your views here.

def requests(request):
    context = {}
    render(request, 'requests/index.html', context)