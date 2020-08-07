from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import User_extend
from portfolio.models import Portfolio
from .models import Chat_room, Chat_message
from django.core import serializers
from django.http import HttpResponse, JsonResponse



@login_required
def chat_rooms(request): # navigation에서 채팅 눌렀을때만
    user_extend = User_extend.objects.get(user=request.user)
    ptr_info_extends = User_extend.objects.none() 
    reqr_info_extends = User_extend.objects.none()

    # 요청자일때 reqr = request.user 인 chat_room 찾아서 list로 뿌리기
    if user_extend.user_type == 'R':
        chat_rooms = Chat_room.objects.filter(reqr=request.user) # 내 채팅방들 가져오기(여러건)
        # 각 채팅방의 상대방 정보. 즉, 파트너의 정보 가져오기
        for chat_room in chat_rooms:
            ptr_info = User.objects.get(id=chat_room.ptr.id)
            ptr_info_extend = User_extend.objects.filter(user_id=ptr_info.id) #1건
            ptr_info_extends = ptr_info_extends.union(ptr_info_extend)

    # 파트너일때 ptr = request.user인 chat_room을 찾아서 list로 뿌리기
    elif user_extend.user_type == 'P':
        chat_rooms = Chat_room.objects.filter(ptr=request.user)
        print(chat_rooms)
        # 채팅방의 상대방 정보. 즉, 요청자의 정보 가져오기
        for chat_room in chat_rooms:
            reqr_info = User.objects.get(id=chat_room.reqr.id)
            reqr_info_extend = User_extend.objects.filter(user_id=reqr_info.id)
            reqr_info_extends = reqr_info_extends.union(reqr_info_extend)

    context = {
        'user_extend' : user_extend,
        'chat_rooms' : chat_rooms,
        'ptr_info_extends' : ptr_info_extends,
        'reqr_info_extends' : reqr_info_extends,
    }
    return render(request, 'chat/chat_rooms.html', context)


# 채팅방 찾아서 새로운 메세지 입력받고 DB에 저장(POST)
@login_required
def send_message(request, reqr_id, ptr_id):
    # 채팅방 정보
    chat_room = Chat_room.objects.get(reqr_id=reqr_id, ptr_id=ptr_id)
    writer_id = request.user.id
    message = request.POST['message']
    chat_message = Chat_message(chat_room=chat_room, writer_id=writer_id, message=message)
    chat_message.save()

    return redirect('chat:chat', reqr_id, ptr_id)



# 요청자로 로그인해서 파트너에게 채팅을 요청할때 (견적서 보고나서)
# 파트너로 로그인해서 요청자에게 채팅을 요청할때 (요청서 보고나서)
# navigation 메뉴에서 채팅방에 들어올때 
@login_required
def chat(request, reqr_id, ptr_id):
    user_extend = User_extend.objects.get(user=request.user)
    
    chat_room = Chat_room.objects.get(reqr_id=reqr_id, ptr_id=ptr_id)
    chat_messages = Chat_message.objects.filter(chat_room=chat_room)
    chat_messages_list = serializers.serialize('json', chat_messages)
    context = {
            'user_extend' : user_extend,
            'chat_room' : chat_room,
            'chat_messages' : chat_messages,
            'chat_messages_list' : json.loads(chat_messages_list),
    }
    return render(request, 'chat/chatting.html', context)
    
    
    
    
    # chat_messages = Chat_message.objects.filter(chat_room=chat_room)
    # chat_messages_list = serializers.serialize('json', chat_messages)
    # return HttpResponse(chat_messages_list, content_type="text/json-comment-filtered")

    
    # print(context)

    
