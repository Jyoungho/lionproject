from django.db import models
from django.contrib.auth.models import User
from accounts.models import User_extend

def set_none():
    return 'none'

class Request(models.Model):
    reqr_username = models.ForeignKey(User, null=False, on_delete=models.SET(set_none))
    title = models.CharField(max_length=100)
    cont = models.TextField()
    area_sido = models.CharField(max_length=50, null=False, default='서울특별시')
    area_sigungu = models.CharField(max_length=50, null=False, default='강남구')
    svc_cd = models.CharField(max_length=6, null=False)
    work_spc_kind = models.CharField(max_length=20, null=False)
    elev_psb_yn = models.CharField(max_length=1, null=False)
    size = models.IntegerField()
    floor = models.IntegerField(null=False)
    req_exp_stt_dt = models.DateField(null=True)
    req_exp_end_dt = models.DateField(null=True)
    work_stt_dt = models.DateField()
    work_end_dt = models.DateField()
    del_yn = models.CharField(max_length=1, default='N', null=False)
    reg_dtti = models.DateTimeField(auto_now_add=True)
    mod_dtti = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reqr_username}, Request_id:{self.id}, {self.title}'

class Request_img(models.Model):
    req_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='requests')
    main_yn = models.CharField(max_length=1, null=False, default='N')
    
    def __str__(self):
        return f'{self.req_id} : {self.img} ({self.main_yn})'
