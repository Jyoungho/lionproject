from django.urls import path
from . import views

app_name= 'portfolio'
urlpatterns = [
    path('', views.portfolioList_forP, name='list_forP'), # 파트너로 로그인 시
    path('<int:estimate_id>/', views.portfolioList_forR, name='list_forR'), # 요청자로 로그인 시
    path('detail/<int:portfolio_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:portfolio_id>/edit/', views.edit, name='edit'),
    path('<int:portfolio_id>/delete/', views.delete, name='delete'),
]