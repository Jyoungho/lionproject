from django.db import models
from django.contrib.auth.models import User
from accounts.models import User_extend
from requests.models import Request

def set_none():
    return 'none'

class Estimate(models.Model):
    ptr_username = models.ForeignKey(User, null=False, on_delete=models.SET(set_none))
    req_id = models.ForeignKey(Request, null=False, on_delete=models.SET(set_none), related_name='related_request')
    price = models.IntegerField()
    title = models.CharField(max_length=100)
    cont = models.TextField(null=False, blank=True)
    del_yn = models.CharField(max_length=1, default='N', null=False)
    reg_dtti = models.DateTimeField(auto_now_add=True)
    mod_dtti = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ptr_username} : {self.title}'