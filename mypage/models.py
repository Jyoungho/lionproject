from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mypage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.user:
            return f'{self.id}: {self.user.get_username()}'
        return f'{self.user.get_username()}'