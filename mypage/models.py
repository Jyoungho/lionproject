from django.db import models
from django.contrib.auth.models import User
#from .models import User_extend

# Create your models here.
class Mypage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #tel = models.ForeignKey(User_extend, on_delete=models.CASCADE)

    def __str__(self):
        if self.user:
            return f'{self.id}: {self.user.get_username()}'
        return f'{self.user.get_username()}'