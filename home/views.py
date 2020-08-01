from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import User_extend
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        context = {}
    else:
        user_extend = User_extend.objects.get(user=request.user)
        context = {'user_extend' : user_extend}
    return render(request, 'home/index.html', context)
