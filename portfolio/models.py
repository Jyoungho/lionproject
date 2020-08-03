from django.db import models
from django.contrib.auth.models import User
from accounts.models import User_extend

def set_none():
    return 'none'

class Portfolio(models.Model):
    ptr_username = models.ForeignKey(User, null=False, on_delete=models.SET(set_none))
    area = models.CharField(max_length=200, null=False)
    svc_cd = models.CharField(max_length=30, null=False)
    work_spc_kind = models.CharField(max_length=20, null=False)
    work_ym = models.CharField(max_length=6, null=False)
    title = models.CharField(max_length=100)
    cont = models.TextField()
    reg_dtti = models.DateTimeField(auto_now_add=True)
    mod_dtti = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ptr_username} : {self.title}'

class Portfolio_img(models.Model):
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='portfolio')
    main_yn = models.CharField(max_length=1, null=False, default='N')
    
    def __str__(self):
        return f'{self.portfolio_id} : {self.img} ({self.main_yn})'