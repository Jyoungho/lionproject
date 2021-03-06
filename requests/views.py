from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from requests.models import Request, Request_img
from accounts.models import User_extend
from django.core.paginator import Paginator
from .forms import RequestForm, RequestImgForm
import pdb
# Create your views here.

def requests(request):
    reqs = Request.objects.all().order_by('-id')
    user_extend = User_extend.objects.get(user=request.user)
    
    # 페이지 분할#
    page_numbers_range = 5
    pageDivision = 20 #한 페이지에 몇개로 할지
    paginator = Paginator(reqs, pageDivision) 
    page = request.GET.get('page')
    current_page = int(page) if page else 1
    contacts = paginator.get_page(current_page)
    page_obj = paginator.page(current_page)
    ###
    start_index = int((current_page -1)/page_numbers_range)*page_numbers_range
    end_index = start_index+page_numbers_range
    max_index = len(paginator.page_range)
    if end_index >= max_index:
        end_index = max_index
    page_range = paginator.page_range[start_index:end_index]
    
    if not request.user.is_authenticated:
        context = {'reqs' : reqs, 'contacts': contacts, 'page_obj':page_obj, 'page':page, 'page_range': page_range, }
    else:
        context = {'reqs' : reqs, 'contacts': contacts, 'page_obj':page_obj, 'page':page, 'page_range': page_range, 'user_extend': user_extend}

    return render(request, 'requests/requests.html', context)

@login_required
def new(request):
    user_extend = User_extend.objects.get(user = request.user)
    context = {'user_extend' : user_extend}
    
    return render(request, 'requests/new.html', context)

@login_required
def create(request):
    reqr_username = request.user
    title = request.POST['title']
    cont = request.POST['cont']
    area_sido = request.POST['area_sido']
    area_sigungu = request.POST['area_sigungu']
    svc_cd = request.POST['svc_cd']
    work_spc_kind = request.POST['work_spc_kind']
    elev_psb_yn = request.POST['elev_psb_yn']
    size = request.POST['size']
    floor = request.POST['floor']
    work_stt_dt = request.POST['work_stt_dt']
    work_end_dt = request.POST['work_end_dt']
    req = Request(reqr_username = reqr_username, title = title, cont = cont, area_sido = area_sido, area_sigungu = area_sigungu , svc_cd = svc_cd, work_spc_kind = work_spc_kind, elev_psb_yn = elev_psb_yn, size = size, floor = floor, work_stt_dt = work_stt_dt, work_end_dt = work_end_dt)
    req.save()
    form = RequestImgForm(request.POST, request.FILES)
    
    if not form.is_valid():
        for field in request.FILES.keys():
            for i, formfile in enumerate(request.FILES.getlist(field)):
                if i == 0:
                    main_yn = 'Y'
                else:
                    main_yn = 'N'
                request_img = Request_img(req_id=req, img=formfile, main_yn=main_yn)
                request_img.save()
                
    return redirect('requests:requests')


def detail(request, requests_id):
    req = Request.objects.get(id=requests_id)
    reqr_info = User.objects.get(id = req.reqr_username.id)
    reqr_info_extend = User_extend.objects.get(user = reqr_info)
    user_extend = User_extend.objects.get(user = request.user)
    # 이미지 추가
    images = Request_img.objects.filter(req_id=requests_id)
    
    if not request.user.is_authenticated:
        context = {
            'req' : req,
            'reqr_info_extend' : reqr_info_extend,
            'images' : images,
        }

    else:
        context = {
            'req' : req,
            'reqr_info_extend' : reqr_info_extend,
            'user_extend' : user_extend,
            'images' : images,
        }
    return render(request, 'requests/detail.html', context)

@login_required
def edit(request, requests_id):
    try:
        req = Request.objects.get(id = requests_id, reqr_username = request.user)
        req_img = Request_img.objects.filter(req_id = req.id)
    except Request.DoesNotExist:
        return redirect('requests:requests')
    context = {'req':req, 'images': req_img}
    return render(request, 'requests/edit.html', context)

@login_required
def update(request, requests_id):
    reqr_username = request.user
    title = request.POST['title']
    cont = request.POST['cont']
    area_sido = request.POST['area_sido']
    area_sigungu = request.POST['area_sigungu']
    svc_cd = request.POST['svc_cd']
    work_spc_kind = request.POST['work_spc_kind']
    elev_psb_yn = request.POST['elev_psb_yn']
    size = request.POST['size']
    floor = request.POST['floor']
    work_stt_dt = request.POST['work_stt_dt']
    work_end_dt = request.POST['work_end_dt']
    req = Request(reqr_username = reqr_username, title = title, cont = cont, area_sido = area_sido, area_sigungu = area_sigungu , svc_cd = svc_cd, work_spc_kind = work_spc_kind, elev_psb_yn = elev_psb_yn, size = size, floor = floor, work_stt_dt = work_stt_dt, work_end_dt = work_end_dt)
    req.save()
    form = RequestImgForm(request.POST, request.FILES)
    
    if not form.is_valid():
        for field in request.FILES.keys():
            for i, formfile in enumerate(request.FILES.getlist(field)):
                if i == 0:
                    main_yn = 'Y'
                else:
                    main_yn = 'N'
                request_img = Request_img(req_id=req, img=formfile, main_yn=main_yn)
                request_img.save()
                
    return redirect('requests:requests')
 



@login_required
def delete(request, requests_id):
    try:
        req = Request.objects.get(id = requests_id, reqr_username = request.user)
    except Request.DoesNotExist:
        return redirect('requests:requests')
    req.delete()
    return redirect('requests:requests')



@login_required
def search_requests(request):
    qs = Request.objects.all() #모든 요청서를 불러옵니다.
    search_one=request.GET['search_one']
    
    if search_one == '제목':
        q = request.GET['q'] #검색어를 받아요
        if q: #검색어가 있다면
            qs = qs.filter(title__contains=q) #그 검색어가 속해있는 것만 필터링합니다.

    elif search_one == '작성자':
        q = request.GET['q'] #검색어를 받아요
        if q: #검색어가 있다면
            qs = qs.filter(reqr_username__in=q) #username이 왜 숫자로 박혀있죠..?
    return render(request, 'requests/requests_search.html', {'qs':qs}) #그리고 그 정보를 가지고 저 PATH로 가요!
