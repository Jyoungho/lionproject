from django.urls import path
from . import views

app_name= 'chat'
urlpatterns = [
    path('<int:user_id>', views.chat_rooms, name='chat_rooms'),
    path('<int:reqr_id>/<int:ptr_id>/', views.chat, name='chat'),
]