from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User_extend
from requests.models import Request
from .models import Estimate

@login_required
def estimatesList(request):
    context = {}
    res_requests = Request.objects.none()
    res_estimates = Estimate.objects.none()
    # 현재 로그인 한 유저 정보 가져오기 (user_type이 필요)
    user_extend = User_extend.objects.get(user=request.user)

    # 견적서와 관련있는 요청서 정보 가져오기 (id가 필요)
    my_requests = Request.objects.filter(reqr_username=user_extend.user)

    # 요청자로 로그인 했을 때
    if user_extend.user_type == 'R':
        # 견적서의 요청이 본인 소유인 것만

        # 내 요청에 달린 견적서 정보 가져오기
        for my_request in my_requests:
            if Estimate.objects.filter(req_id=my_request.id).filter(del_yn='N'): # 해당 요청서에 견적서가 있을 때만
                estimates = Estimate.objects.filter(req_id=my_request.id)
                res_estimates = res_estimates.union(estimates)

    # 파트너로 로그인 했을 때
    elif user_extend.user_type == 'P':
        # 견적서의 작성자가 본인인 것만
        res_estimates = Estimate.objects.filter(ptr_username=user_extend.user).filter(del_yn='N')

        # # 견적서의 요청서 정보 가져오기
        # for res_estimate in res_estimates:
        #     tmp_request = Request.objects.get(id=res_estimate.req_id)
        #     res_requests = res_requests.union(tmp_request)

    
    context = {
        'user_extend' : user_extend,
        'estimates' : res_estimates,
    }

    return render(request, 'estimates/estimates.html', context)

@login_required
def detail(request, estimate_id):
    estimate = Estimate.objects.get(id=estimate_id)
    user_extend = User_extend.objects.get(user=request.user)
    context = {
        'estimate' : estimate,
        'user_extend' :user_extend,
    }
    return render(request, 'estimates/detail.html', context)

@login_required
def new(request):
    user_extend = User_extend.objects.get(user=request.user)
    if user_extend.user_type == 'R':
        return redirect('home:home')
    else:
        return render(request, 'estimates/new.html')

@login_required
def create(request, request_id):
    ptr_username = request.user
    req_id = request_id
    title = request.POST['title']
    price = request.POST['price']
    cont = request.POST['cont']

    estimate = Estimate(ptr_username=ptr_username, req_id=req_id, price=price, title=title, cont=cont, del_yn='N')
    estimate.save()

    return redirect('estimates:detail', estimate_id = estimate.id)


@login_required
def edit(request, estimate_id):
    try:
        estimate = Estimate.objects.get(id=estimate_id, ptr_username=request.user)
    except Estimate.DoesNotExist:
        return redirect('home:home')
    
    # POST 방식일때
    if request.method == 'POST':

        estimate.title = request.POST.get('title')
        estimate.price = request.POST.get('price')
        estimate.cont = request.POST.get('cont')

        estimate.save()
        return redirect('estimates:detail', estimate_id=estimate.id)

    # GET 방식일때    
    else:
        context = {'estimate' : estimate}
        return render(request, 'estimates/edit.html', context)


@login_required
def delete(request, estimate_id):
    try:
        estimate = Estimate.objects.get(id=estimate_id, ptr_username=request.user)
    except Estimate.DoesNotExist:
        return redirect('home:home')
    estimate.delete()
    return redirect('estimates:list')