from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User_extend
from portfolio.models import Portfolio
from .models import Chat_room, Chat_message


@login_required
def chat_rooms(request): # dropmenu에서 채팅 눌렀을때만
    user_extend = User_extend.objects.get(user=request.user)
    context = {
        'user_extend' : user_extend,
    }
    return render(request, 'chat/index.html', context)

# chat_room_id = 요청자 id & 파트너 id  >> 문자형???
@login_required
def chat(request, reqr_id, ptr_id): 
    # 채팅방 생성
    # 요청자로 로그인해서 파트너에게 채팅을 요청할때 (견적서 보고나서)
    # 파트너로 로그인해서 요청자에게 채팅을 요청할때 (요청서 보고나서)

    user_extend = User_extend.objects.get(user=request.user)
    context = {
        'user_extend' : user_extend,
    } # >> 이 던저주는걸 dictionry가 아닌 json 으로 던지기
    return render(request, 'chat/chatting.html', context)
    

