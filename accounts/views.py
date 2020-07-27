from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from .models import User_extend
from django.contrib import auth

# Create your views here.
def signup(request):
    context = {}

    #POST method
    if request.method == 'POST':
        if(request.POST['user'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):

            new_user = User.objects.create_user(
                username=request.POST['user'],
                password=request.POST['password'],
            )
            actv_area=request.POST['actv_area'], #활동지역
            svc_cd=request.POST['svc_cd'], #서비스업종
            work_spc_kind=request.POST['work_spc_kind'], #작업가능공간종류
            new_user.save() #세이브까지!


            auth.login(request, new_user)
            return redirect('home:home')
        else:
            context['error'] = '정보를 확인해주세요.'

    #GET Method
    return render(request, 'accounts/signup.html', context)

def login(request):
    context = {}

    #POST Method
    if request.method == 'POST':
        if(request.POST['user'] and request.POST['password']):

            user = auth.authenticate(
                request,
                username=request.POST['user'],
                password=request.POST['password'],
            )

            if user is not None:
                auth.login(request, user)
                return redirect('home:home')
            else:
                context['error'] = "로그인 정보를 확인해주세요."
        
        else:
            context['error'] = "로그인 정보를 확인해주세요."

    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('home:home')