from django.db import models
from django.contrib.auth.models import User
from accounts.models import User_extend

def set_none():
    return 'none'

class Request(models.Model):
    reqr_username = models.ForeignKey(User, null=False, on_delete=models.SET(set_none))
    title = models.CharField(max_length=100)
    cont = models.TextField()
    img = models.ImageField(upload_to='requests', null=True)
    req_area = models.CharField(max_length=100, null=False)
    svc_cd = models.CharField(max_length=6, null=False)
    work_spc_kind = models.CharField(max_length=20, null=False)
    elev_psb_yn = models.CharField(max_length=1, null=False)
    size = models.IntegerField()
    floor = models.IntegerField(null=False)
    req_exp_stt_dt = models.DateField()
    req_exp_end_dt = models.DateField()
    work_stt_dt = models.DateField()
    work_end_dt = models.DateField()
    del_yn = models.CharField(max_length=1, default='N', null=False)
    reg_dtti = models.DateTimeField(auto_now_add=True)
    mod_dtti = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.reqr_username} : {self.title}'
