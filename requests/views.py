from django.shortcuts import render

# Create your views here.

def requests(request):
    context = {}
    return render(request, 'requests/requests.html', context)