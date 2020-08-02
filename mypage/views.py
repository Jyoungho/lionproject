from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from accounts.models import User_extend
from django.contrib import auth
#from .models import Mypage

# Create your views here.
def index(request):
    user_extend = User_extend.objects.get(user=request.user)
    context = {'user_extend': user_extend}
    return render(request, 'mypage/index.html', context)

def change_pw(request):
    context= {}

    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("home:home")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
        else:
            context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "mypage/change_pw.html",context)

def edit(request):
    user_extend = User_extend.objects.get(user=request.user)
    context = {'user_extend': user_extend}
    return render(request, 'mypage/edit.html', context)

def update(request):
    user_extend = User_extend.objects.get(user=request.user)
    user_extend.nickname=request.POST['nickname']
    user_extend.tel=request.POST['tel']
    if 'prof_img' in request.FILES:
        user_extend.prof_img = request.FILES['prof_img']
    if user_extend.user_type == 'P':
        user_extend.actv_area=request.POST['actv_area']
        user_extend.svc_cd=request.POST['svc_cd']
        user_extend.work_spc_kind=request.POST['work_spc_kind']
    user_extend.save()
    return redirect('mypage:index')