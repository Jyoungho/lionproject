from django.urls import path
from django.contrib import admin
from . import views

app_name= 'mypage'
urlpatterns = [
    path('', views.detail, name ='detail'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 8a2dd7926e19728eaa56e153f0cabe24f420c534
