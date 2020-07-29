from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User

class User_extend(models.Model): 
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    tel = models.CharField(max_length=15, null=False)
    prof_img = models.ImageField(upload_to='profile', null=True)
    ptr_join_yn = models.CharField(max_length=1, null=False)
    biz_nm = models.CharField(max_length=200, null=True)
    actv_area = models.CharField(max_length=100, null=False)
    svc_cd = models.CharField(max_length=6, null=False)
    work_spc_kind = models.CharField(max_length=20, null=False)
    career = models.IntegerField(null=False)
    lic_img = models.ImageField(upload_to='license', null=True)
    staff_cnt = models.IntegerField(null=True)
    user_type = models.CharField(max_length=1, null=False)
    del_yn = models.CharField(max_length=1, default='N', null=False)
    del_res = models.CharField(max_length=200, null=True)
    reg_dtti = models.DateTimeField(auto_now_add=True)
    mod_dtti = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}, user_type: {self.user_type}'

