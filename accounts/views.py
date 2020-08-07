from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User_extend
from django.contrib import auth
from django.contrib.auth.decorators import login_required

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
            prof_img = None
            if 'prof_img' in request.FILES:
                prof_img = request.FILES['prof_img']
            nickname=request.POST['nickname'] #닉네임
            tel=request.POST['tel'] #전화번호
            #actv_area=request.POST['postcode_sido']+" "+request.POST['postcode_sigungu'] #활동지역
            biz_nm=request.POST['biz_nm']
            area_sido=request.POST['area_sido']
            area_sigungu=request.POST['area_sigungu']
            svc_cd=request.POST['svc_cd'] #서비스업종
            work_spc_kind=request.POST['work_spc_kind'] #작업가능공간종류
            user_type='P' #파트너로 타입 지정
            ptr_join_yn='Y' #파트너로 가입한 이력 yes로 만들어줌

            new_user = User_extend(user=user, nickname=nickname, prof_img=prof_img, tel=tel, biz_nm=biz_nm, area_sido=area_sido, area_sigungu=area_sigungu, svc_cd=svc_cd, work_spc_kind=work_spc_kind, user_type=user_type, ptr_join_yn=ptr_join_yn)
            new_user.save() #세이브까지!

            auth.login(request, user)
            return redirect('home:home')
        else:
            context['error'] = '정보를 확인해주세요.'

    #GET Method
    return render(request, 'accounts/partner.html', context)

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
            prof_img = None
            if 'prof_img' in request.FILES:
                prof_img = request.FILES['prof_img']
            nickname=request.POST['nickname'] #닉네임
            tel=request.POST['tel'] #전화번호
            #actv_area='N' #활동지역
            area_sido='N'
            area_sigungu='N'
            svc_cd='N' #서비스업종
            work_spc_kind='N'
            user_type='R'
            ptr_join_yn='N'

            new_user = User_extend(user=user, nickname=nickname, prof_img=prof_img, tel=tel, area_sido=area_sido, area_sigungu=area_sigungu, svc_cd=svc_cd, work_spc_kind=work_spc_kind, user_type=user_type, ptr_join_yn=ptr_join_yn)
            new_user.save() #세이브까지!

            auth.login(request, user)
            return redirect('home:home')
        else:
            context['error'] = '정보를 확인해주세요.'

    #GET Method
    return render(request, 'accounts/requester.html', context)

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
        #user_extend = User_extend.objects.get(user=request.user)  
        #context = {'user_extend' : user_extend,}
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('home:home')

@login_required
def exchange(request):
    
    user_extend = User_extend.objects.get(user=request.user)
    if user_extend.user_type == 'R':
        if user_extend.ptr_join_yn == 'Y':
            user_extend.user_type = 'P'
            user_extend.save()
        else: #only 사용자로만 가입한 사람
            context = {}
            context = {
                'user_extend' : user_extend,
                'error' : "파트너로 가입해주세요.",
            }
            return render(request, 'mypage/exchange.html', context)
    else: #파트너로 로그인해서 고객으로 전환 클릭 시,
        user_extend.user_type = 'R'
        user_extend.save()
    return redirect('home:home')

def partner(request):
    
    #GET Method
    return render(request, 'accounts/partner.html')

def requester(request):

    return render(request,'accounts/requester.html')