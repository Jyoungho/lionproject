from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import User_extend
from .models import Mypage

# Create your views here.

def detail(request):
    user_extend = User_extend.objects.get(user=request.user)
    context = {'user_extend': user_extend}
    return render(request, 'mypage/detail.html', context)
