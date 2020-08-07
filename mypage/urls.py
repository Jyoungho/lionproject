from django.urls import path
from django.contrib import admin
from . import views

app_name= 'mypage'
urlpatterns = [
    path('', views.index, name='index'),
    path('change_pw/', views.change_pw, name ='change_pw'),
    path('edit/', views.edit, name ='edit'),
    path('update/', views.update, name ='update'),
    path('update_exchange/', views.update_exchange, name='update_exchange'),
]