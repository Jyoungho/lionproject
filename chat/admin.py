from django.contrib import admin
from .models import Chat_room, Chat_message

admin.site.register(Chat_room)
admin.site.register(Chat_message)