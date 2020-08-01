from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User_extend
from django.contrib import auth

# Create your views here.
def signup(request):
    #GET Method
    return render(request, 'accounts/signup.html')

def signup_partner(request):

    context = {}
    
    #POST method
    if request.method == 'POST':
        if(request.POST['username'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):

            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            nickname=request.POST['nickname'] #닉네임
            tel=request.POST['tel'] #전화번호
            actv_area=request.POST['actv_area'] #활동지역
            svc_cd=request.POST['svc_cd'] #서비스업종
            work_spc_kind=request.POST['work_spc_kind'] #작업가능공간종류
            user_type='P'
            ptr_join_yn='Y'

            new_user = User_extend(user=user, nickname=nickname, tel=tel, actv_area=actv_area, svc_cd=svc_cd, work_spc_kind=work_spc_kind, user_type=user_type, ptr_join_yn=ptr_join_yn)
            new_user.save() #세이브까지!

            auth.login(request, user)
            return redirect('home:home')
        else:
            context['error'] = '정보를 확인해주세요.'

    #GET Method
    return render(request, 'accounts/signup.html', context)

def signup_requester(request):
    
    context = {}
    
    #POST method
    if request.method == 'POST':
        if(request.POST['username'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):

            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            nickname=request.POST['nickname'] #닉네임
            tel=request.POST['tel'] #전화번호
            print('##################전화번호까지')
            actv_area='N' #활동지역
            svc_cd='N' #서비스업종
            work_spc_kind='N'
            user_type='R'
            ptr_join_yn='N'
            print("#####################데이터입력")

            new_user = User_extend(user=user, nickname=nickname, tel=tel, actv_area=actv_area, svc_cd=svc_cd, work_spc_kind=work_spc_kind, user_type=user_type, ptr_join_yn=ptr_join_yn)
            print('####################DATA 저장')
            new_user.save() #세이브까지!
            print('####################SAVE')

            auth.login(request, user)
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

        # 아래 두 줄 꼭 기입하고 return시 context로 전달하기
        user_extend = User_extend.objects.get(user=request.user)  
        context = {'user_extend' : user_extend,}
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('home:home')

def exchange(request):
    user_extend = User_extend.objects.get(user=request.user)
    if user_extend.user_type == 'R':
        if user_extend.ptr_join_yn == 'Y':
            user_extend.user_type = 'P'
            user_extend.save()
        else:
            context = {}
            context['error'] = '파트너로 가입해주세요'
            return render(request, 'accounts/signup.html', context)
    else:
        user_extend.user_type = 'R'
        user_extend.save()
    return redirect('home:home')

def partner(request):
    
    #GET Method
    return render(request, 'accounts/partner.html')

def requester(request):

    return render(request,'accounts/requester.html')