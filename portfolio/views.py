from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User_extend
from requests.models import Request
from estimates.models import Estimate
from .models import Portfolio, Image

@login_required
def portfolioList_forR(request, estimate_id): # 파트너 클릭 시 파트너 정보 넘어옴(User ,User_extend)
    main_images = Image.objects.none()
    # 현재 로그인 한 유저 정보 가져오기 (user_type이 필요)
    user_extend = User_extend.objects.get(user=request.user)

    # 내 요청에 달린 견적서를 작성한 파트너 정보 가져오기
    estimate = Estimate.objects.get(id=estimate_id) 
    ptr_info = User_extend.objects.get(user=estimate.ptr_username)
    # 그 파트너의 포트폴리오 리스트 가져오기
    portfolios = Portfolio.objects.filter(ptr_username=ptr_info.user)
    for portfolio in portfolios:
        main_image = Image.objects.filter(portfolio_id=portfolio.id).filter(main_yn='Y')
        main_images = main_images.union(main_image)
    
    context = {
        'user_extend' : user_extend,
        'ptr_info' : ptr_info,
        'portfolios' : portfolios,
        'main_images' : main_images,
    }
    return render(request, 'portfolio/portfolio.html', context)


def portfolioList_forP(request):
    main_images = Image.objects.none()
    # 현재 로그인 한 유저 정보 가져오기 (user_type이 필요)
    user_extend = User_extend.objects.get(user=request.user)
    # 내 포트폴리오만 불러오기
    portfolios = Portfolio.objects.filter(ptr_username=request.user)
    for portfolio in portfolios:
        main_image = Image.objects.filter(portfolio_id=portfolio.id).filter(main_yn='Y')
        main_images = main_images.union(main_image)
    
    for test in main_images:
        print(type(test))
    
    context = {
        'user_extend' : user_extend,
        'portfolios' : portfolios,
        'main_images' : main_images,
    }
    return render(request, 'portfolio/portfolio.html', context)


def detail(request, portfolio_id):
    user_extend = User_extend.objects.get(user=request.user)
    portfolio = Portfolio.objects.get(id=portfolio_id)
    context = {
        'user_extend' : user_extend,
        'portfolio' : portfolio,
    }
    return render(request, 'portfolio/detail.html', context)


@login_required
def new(request):
   
    context = {
        
    }
    # POST 방식일때
    if request.method == 'POST':
        return redirect('portfolio:list_forP')
    # GET 방식일때    
    else:
        return render(request, 'portfolio/new.html', context)


@login_required
def edit(request, portfolio_id):
    try:
        portfolio = Portfolio.objects.get(id=estimate_id, ptr_username=request.user)
    except Portfolio.DoesNotExist:
        return redirect('home:home')

    # POST 방식일때
    if request.method == 'POST':



        return redirect('portfolio:detail', portfolio_id=portfolio.id)
    # GET 방식일때    
    else:
        context = {'portfolio' : portfolio}
        return render(request, 'portfolio:edit.html', context)
    


@login_required
def delete(request, portfolio_id):
    try:
        portfolio = Portfolio.objects.get(id=estimate_id, ptr_username=request.user)
    except Portfolio.DoesNotExist:
        return redirect('home:home')
    portfolio.delete()
    return redirect('portfolio:list_forP')