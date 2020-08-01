from django.urls import path
from django.contrib import admin
from . import views

app_name= 'accounts'
urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('signup_partner/', views.signup_partner, name ='signup_partner'),
    path('signup_requester/', views.signup_requester, name ='signup_requester'),
    path('partner/', views.partner, name ='partner'),
    path('requester/', views.requester, name ='requester'),
    path('login/', views.login, name ='login'),
    path('logout/', views.logout, name ='logout'),
    path('exchange/', views.exchange, name='exchange'),
]