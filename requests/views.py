from django.shortcuts import render, redirect
from django.utils import timezone
from requests.models import Request, Request_img
# Create your views here.

def requests(request):
    reqs = Request.objects.all()
    context = {'reqs' : reqs}
    return render(request, 'requests/requests.html', context)

def new(request):
    context = {}
    return render(request, 'requests/new.html', context)

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
    context = {'req' : req }
    return render(request, 'requests/detail.html', context)

def edit(request):
    context = {}
    return render(request, 'requests/edit.html', context)

def delete(request):
    
    return redirect('requests:requests')