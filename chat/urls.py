from django.urls import path
from . import views

app_name= 'chat'
urlpatterns = [
    path('', views.chat_rooms, name='chat_rooms'),
    # path('<int:chat_room_id>/', views.chat, name='chat'),
    path('<int:reqr_id>/<int:ptr_id>/', views.chat, name='chat'),
    path('<int:reqr_id>/<int:ptr_id>/send_message', views.send_message, name='send_message'),
]