from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Mypage

# Create your views here.

def index(request):
    users = Mypage.objects.all()
    context = { 'users': users}
    return render(request, 'mypage/index.html', context)

'''
def detail(request, user_id):
    user = Mypage.objects.get(id=user_id)
    context = { 'user': user}
    return render(request, 'mypage/detail.html', context)
'''