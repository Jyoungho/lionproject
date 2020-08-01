from django.urls import path
from django.contrib import admin
from . import views

app_name= 'accounts'
urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('signup/partner/', views.partner, name ='partner'),
    path('requester/', views.requester, name ='requester'),
    path('login/', views.login, name ='login'),
    path('logout/', views.logout, name ='logout'),
    path('exchange/', views.exchange, name='exchange'),
]