from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User_extend
from requests.models import Request
from estimates.models import Estimate
from .models import Portfolio


def portfolioList(request):
    
    user_extend = User_extend.objects.get(user=request.user)  
    context = {'user_extend' : user_extend,}
    return render(request, 'portfolio/portfolio.html', context)