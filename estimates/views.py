from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User_extend
from requests.models import Request
from .models import Estimate

def estimatesList(request):
    context = {}
    res_estimates = Estimate.objects.none()
    # 현재 로그인 한 유저 정보 가져오기 (user_type이 필요)
    user_info = User_extend.objects.get(user=request.user)
    # 견적서와 관련있는 요청서 정보 가져오기 (id가 필요)
    my_requests = Request.objects.filter(reqr_username=user_info.user)
    # all_requests = Request.objects.all()

    if user_info.user_type == 'R':
        # 견적서의 관련 요청이 본인 소유인 것만
        # 1) 요청자가 작성한 요청서의 id 가져오기 
        for my_request in my_requests:
            if Estimate.objects.filter(req_id=my_request.id): # 해당 요청서에 견적서가 있을 때만
                estimates = Estimate.objects.filter(req_id=my_request.id)
                print(estimates)
                res_estimates = res_estimates.union(estimates)
        print(res_estimates)

    elif user_info.user_type == 'P':
        # 견적서의 작성자가 본인인 것만
        res_estimates = Estimate.objects.filter(ptr_username=user_info.user)
    
    context = {
        'user_info' : user_info,
        'estimates' : res_estimates,
    }

    return render(request, 'estimates/estimates.html', context)


def detail(request, estimate_id):
    context = {}
    return render(request, 'estimates/detail.html', context)


def new(request):
    
    if request.method == 'POST':
        return redirect('estimates:detail')
    else:
        return render(request, 'estimates/new.html')


def edit(request, estimate_id):

    if request.method == 'POST':
        return redirect('estimates:detail') # estimate_id 추가 필요
    else:
        return render(request, 'estimates/edit.html')


def delete(request, estimate_id):
    return redirect('estimates:list') # estimate_id 추가 필요