from django.urls import path
from django.contrib import admin
from . import views

app_name= 'accounts'
urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('login/', views.login, name ='login'),
    path('logout/', views.logout, name ='logout'),
    path('<int:user_id>/', views.mypage, name ='mypage'),
    
]