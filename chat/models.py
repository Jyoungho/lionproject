from django.db import models
from django.contrib.auth.models import User

class Chat_room(models.Model):
    chat_room_nm = models.CharField(max_length=200, null=True)
    reqr = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='ptr_info')
    ptr = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='reqr_info')
    reg_dtti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reqr} -- {self.ptr}'

class Chat_message(models.Model):
    chat_room = models.ForeignKey(Chat_room, null=False, on_delete=models.CASCADE)
    writer_id = models.IntegerField(null=False)
    message = models.TextField(null=False, blank=True)
    reg_dtti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'room : {self.chat_room} // 작성자 : {self.writer_id} // 내용 : {self.message}'