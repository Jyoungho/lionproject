from django.urls import path
from . import views

app_name= 'estimates'
urlpatterns = [
    path('', views.estimatesList, name='list'),
    path('<int:estimate_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:estimate_id>/edit/', views.edit, name='edit'),
    path('<int:estimate_id>/delete/', views.delete, name='delete'),
]