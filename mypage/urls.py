from django.urls import path
from django.contrib import admin
from . import views

app_name= 'mypage'
urlpatterns = [
    path('', views.index, name ='mypage'),
    #path('<int:user_id>/', views.detail, name ='detail'),
]