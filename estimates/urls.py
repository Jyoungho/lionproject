from django.urls import path
from . import views

app_name= 'estimates'
urlpatterns = [
    path('', views.estimatesList, name='list'),
    path('<int:estimate_id>/', views.detail, name='detail'),
    path('<int:request_id>/new/', views.new, name='new'),
    path('<int:request_id>/create/', views.create, name='create'),
    path('<int:estimate_id>/edit/', views.edit, name='edit'),
    path('<int:estimate_id>/delete/', views.delete, name='delete'),
]