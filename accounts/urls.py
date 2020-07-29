from django.urls import path
from django.contrib import admin
from . import views

app_name= 'accounts'
urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('login/', views.login, name ='login'),
    path('logout/', views.logout, name ='logout'),
<<<<<<< HEAD
    path('<int:user_id>/', views.mypage, name ='mypage'),
    
=======
    path('exchange/', views.exchange, name='exchange'),
>>>>>>> bd1916eb03d0ab00f88e52e8789ae55a7ddbfec0
]