from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from requests.models import Request, Request_img
from accounts.models import User_extend
from django.core.paginator import Paginator
# Create your views here.

def requests(request):
    reqs = Request.objects.all().order_by('-id')

    # 페이지 분할#
    pageDivision = 2 #한 페이지에 몇개로 할지
    paginator = Paginator(reqs, pageDivision) 
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    page_container = contacts.number/5
    ###
    
    context = {'reqs' : reqs, 'contacts': contacts,
    'page_container' : page_container}
    return render(request, 'requests/requests.html', context)

@login_required
def new(request):
    user_extend = User_extend.objects.get(user = request.user)
    context = {'user_extend' : user_extend}
    
    return render(request, 'requests/new.html', context)

@login_required
def create(request):
    title = request.POST['title']
    cont = request.POST['cont']
    req_area = request.POST['req_area']
    svc_cd = request.POST['svc_cd']
    work_spc_kind = request.POST['work_spc_kind']
    elev_psb_yn = request.POST['elev_psb_yn']
    size = request.POST['size']
    floor = request.POST['floor']
    req_exp_stt_dt = request.POST['req_exp_stt_dt']
    req_exp_end_dt = request.POST['req_exp_dt']
    work_stt_dt = request.POST['work_stt_dt']
    work_end_dt = request.POST['work_end_dt']
    del_yn = request.POST['del_yn']
    req = Request(title = title, cont = cont, req_area = req_area, svc_cd = svc_cd, work_spc_kind = work_spc_kind, elev_psb_yn = elev_psb_yn, size = size, floor = floor, req_exp_stt_dt = req_exp_stt_dt,req_exp_end_dt = req_exp_end_dt, work_stt_dt = work_stt_dt, del_yn = del_yn)
    return redirect('requests:requests', requests_id=req.id)


def detail(request, requests_id):
    req = Request.objects.get(id=requests_id)
    reqr_info = User.objects.get(id = req.reqr_username.id)
    reqr_info_extend = User_extend.objects.get(user = reqr_info)
    user_extend = User_extend.objects.filter(user_id = req.reqr_username_id)
    context = {'req' : req, 'reqr_info_extend' : reqr_info_extend }
    return render(request, 'requests/detail.html', context)

@login_required
def edit(request):
    context = {}
    return render(request, 'requests/edit.html', context)

@login_required
def delete(request):
    
    return redirect('requests:requests')