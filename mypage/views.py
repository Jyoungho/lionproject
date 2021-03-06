from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from accounts.models import User_extend
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from .models import Mypage

# Create your views here.
@login_required
def index(request):
    user_extend = User_extend.objects.get(user=request.user)
    context = {'user_extend': user_extend}
    return render(request, 'mypage/index.html', context)

@login_required
def change_pw(request):
    context= {}
    user_extend = User_extend.objects.get(user=request.user) 
    context = {'user_extend' : user_extend,}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        context = {'user_extend' : user_extend,}
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
                context = {
                    'user_extend' : user_extend,
                    'error':"새로운 비밀번호를 다시 확인해주세요."
                }
        else:
            context = {
                    'user_extend' : user_extend,
                    'error':"현재 비밀번호가 일치하지 않습니다."
            }

    return render(request, "mypage/change_pw.html",context)

@login_required
def edit(request):
    user_extend = User_extend.objects.get(user=request.user)
    context = {'user_extend': user_extend}
    return render(request, 'mypage/edit.html', context)

@login_required
def update(request):
    user_extend = User_extend.objects.get(user=request.user)
    user_extend.nickname=request.POST['nickname']
    user_extend.tel=request.POST['tel']
    if 'prof_img' in request.FILES:
        user_extend.prof_img = request.FILES['prof_img']
    if user_extend.user_type == 'P':
        user_extend.biz_nm=request.POST['biz_nm']
        user_extend.area_sido=request.POST['area_sido']
        user_extend.area_sigungu=request.POST['area_sigungu']
        user_extend.svc_cd=request.POST['svc_cd']
        user_extend.work_spc_kind=request.POST['work_spc_kind']
    user_extend.save()
    return redirect('mypage:index')

@login_required
def update_exchange(request):
    user_extend = User_extend.objects.get(user=request.user)
    user_extend.user_type='P'
    user_extend.ptr_join_yn='Y'
    user_extend.nickname=request.POST['nickname']
    user_extend.tel=request.POST['tel']
    if 'prof_img' in request.FILES:
        user_extend.prof_img = request.FILES['prof_img']
    user_extend.biz_nm=request.POST['biz_nm']
    user_extend.area_sido=request.POST['area_sido']
    user_extend.area_sigungu=request.POST['area_sigungu']
    user_extend.svc_cd=request.POST['svc_cd']
    user_extend.work_spc_kind=request.POST['work_spc_kind']
    user_extend.save()
    return redirect('mypage:index')