from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User_extend
from requests.models import Request
from estimates.models import Estimate
from .models import Portfolio, Portfolio_img
from .forms import PortfolioForm, PortfolioImgForm


def portfolioList_forAll(request, ptr_id): # 파트너 클릭 시 파트너 정보 넘어옴(User ,User_extend)
    main_images = Portfolio_img.objects.none()
    ptr_info = User_extend.objects.get(id=ptr_id)
    portfolios = Portfolio.objects.filter(ptr_username_id=ptr_id)

    for portfolio in portfolios:
        main_image = Portfolio_img.objects.filter(portfolio_id=portfolio.id).filter(main_yn='Y')
        main_images = main_images.union(main_image)

    if not request.user.is_authenticated:
        context = {
            'ptr_info' : ptr_info,
            'portfolios' : portfolios,
            'main_images' : main_images,
        }
    else:
        user_extend = User_extend.objects.get(user=request.user)
        context = {
            'ptr_info' : ptr_info,
            'user_extend' : user_extend,
            'portfolios' : portfolios,
            'main_images' : main_images,
        }
    return render(request, 'portfolio/portfolioAll.html', context)


@login_required
def portfolioList_forR(request, estimate_id): # 파트너 클릭 시 파트너 정보 넘어옴(User ,User_extend)
    main_images = Portfolio_img.objects.none()
    # 현재 로그인 한 유저 정보 가져오기 (user_type이 필요)
    user_extend = User_extend.objects.get(user=request.user)

    # 내 요청에 달린 견적서를 작성한 파트너 정보 가져오기
    estimate = Estimate.objects.get(id=estimate_id) 
    ptr_info = User_extend.objects.get(user=estimate.ptr_username)
    # 그 파트너의 포트폴리오 리스트 가져오기
    portfolios = Portfolio.objects.filter(ptr_username=ptr_info.user)
    for portfolio in portfolios:
        main_image = Portfolio_img.objects.filter(portfolio_id=portfolio.id).filter(main_yn='Y')
        main_images = main_images.union(main_image)
    
    context = {
        'user_extend' : user_extend,
        'ptr_info' : ptr_info,
        'portfolios' : portfolios,
        'main_images' : main_images,
    }
    return render(request, 'portfolio/portfolio.html', context)


@login_required
def portfolioList_forP(request):
    main_images = Portfolio_img.objects.none()
    # 현재 로그인 한 유저 정보 가져오기 (user_type이 필요)
    user_extend = User_extend.objects.get(user=request.user)
    # 내 포트폴리오만 불러오기
    portfolios = Portfolio.objects.filter(ptr_username=request.user)
    for portfolio in portfolios:
        main_image = Portfolio_img.objects.filter(portfolio_id=portfolio.id).filter(main_yn='Y')
        main_images = main_images.union(main_image)
          
    context = {
        'user_extend' : user_extend,
        'portfolios' : portfolios,
        'main_images' : main_images,
    }
    return render(request, 'portfolio/portfolio.html', context)

@login_required
def detail(request, portfolio_id):
    user_extend = User_extend.objects.get(user=request.user)
    portfolio = Portfolio.objects.get(id=portfolio_id)
    images = Portfolio_img.objects.filter(portfolio_id=portfolio.id)
    
    context = {
        'user_extend' : user_extend,
        'portfolio' : portfolio,
        'images' : images,
    }
    return render(request, 'portfolio/detail.html', context)


@login_required
def new(request):
    # 접속한 유저가 포트폴리오 글 쓴 유저와 같고 유저 타입이 파트너일때만 가능
    if request.method == 'POST':
        ptr_username = request.user 
        title = request.POST['title']
        # area_sido = request.POST['postcode_sido']
        # area_sido = request.POST['postcode_sigungu']
        area = request.POST['postcode_sido'] + " " + request.POST['postcode_sigungu']
        svc_cd = request.POST['svc_cd']
        work_spc_kind = request.POST['work_spc_kind']
        work_yyyy = request.POST['yyyy']
        if not len(request.POST['mm']) == 2:
            work_mm = '0' + request.POST['mm']
        else:
            work_mm = request.POST['mm']
        work_ym = work_yyyy + work_mm
        cont = request.POST['cont']
        portfolio = Portfolio(ptr_username=ptr_username, title=title, area=area, svc_cd=svc_cd, work_spc_kind=work_spc_kind, work_ym=work_ym, cont=cont)
        portfolio.save()
        
        form = PortfolioImgForm(request.POST, request.FILES)
        if form.is_valid():
            for field in request.FILES.keys():
                for i, formfile in enumerate(request.FILES.getlist(field)):
                    if i == 0:
                        main_yn = 'Y'
                    else:
                        main_yn = 'N'
                    portfolio_img = Portfolio_img(portfolio_id=portfolio, img=formfile, main_yn=main_yn)
                    portfolio_img.save()
                
        return redirect('portfolio:detail', portfolio_id=portfolio.id)
        
    # GET 방식일때    
    else:
        user_extend = User_extend.objects.get(user=request.user)
        form = PortfolioImgForm()
        context = {
            'user_extend' : user_extend,
            'form' : form,
        }
        return render(request, 'portfolio/new.html', context)
                          

@login_required
def edit(request, portfolio_id):
    try:
        portfolio = Portfolio.objects.get(id=portfolio_id, ptr_username=request.user)
        portfolio_imgs = Portfolio_img.objects.filter(portfolio_id=portfolio.id)
    except Portfolio.DoesNotExist:
        return redirect('home:home')
    
    # POST 방식일때
    if request.method == 'POST':
        portfolio.title = request.POST.get('title')
        portfolio.area = request.POST.get('postcode_sido') + " " + request.POST.get('postcode_sigungu')
        portfolio.svc_cd = request.POST.get('svc_cd')
        portfolio.work_spc_kind = request.POST.get('work_spc_kind')
        work_yyyy = request.POST['yyyy']
        if not len(request.POST['mm']) == 2:
            work_mm = '0' + request.POST['mm']
        else:
            work_mm = request.POST['mm']
        portfolio.work_ym = work_yyyy + work_mm
        portfolio.cont = request.POST['cont']
        portfolio.save()

        # 기존 이미지 제거
        portfolio_imgs.delete()
        # 새로 받을 이미지 폼
        form = PortfolioImgForm(request.POST, request.FILES) 
                    
        if form.is_valid(): # edit.html의 form에서 입력받은 값이 유효하면
            for field in request.FILES.keys():
                for i, formfile in enumerate(request.FILES.getlist(field)):
                    if i == 0:
                        main_yn = 'Y'
                    else:
                        main_yn = 'N'
                    
                    portfolio_img = Portfolio_img(portfolio_id=portfolio, img=formfile, main_yn=main_yn)
                    portfolio_img.save()

        return redirect('portfolio:detail', portfolio_id=portfolio.id)

    # GET 방식일때    
    else:
        user_extend = User_extend.objects.get(user=request.user)
        form = PortfolioImgForm() # 빈 form
        sido = portfolio.area.split()[0]
        sigungu = portfolio.area.split()[1:]

        context = {
            'user_extend' : user_extend,
            'portfolio' : portfolio, # 보여줄 기존 정보
            'portfolio_imgs' :portfolio_imgs, # 보여줄 기존 정보
            'form' : form,
            'sido' : sido,
            'sigungu' : sigungu,
        }
        return render(request, 'portfolio/edit.html', context)
    


@login_required
def delete(request, portfolio_id):
    try:
        portfolio = Portfolio.objects.get(id=portfolio_id, ptr_username=request.user)
    except Portfolio.DoesNotExist:
        return redirect('home:home')
    portfolio.delete()
    return redirect('portfolio:list_forP')