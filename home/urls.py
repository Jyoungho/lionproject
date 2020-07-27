from django.urls import path
from django.contrib import admin
from . import views

app_name= 'home'
urlpatterns = [
    path('', views.index, name ='home'),
]