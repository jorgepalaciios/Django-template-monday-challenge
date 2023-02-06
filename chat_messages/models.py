from django.db import models
from chats.models import Chat

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    username = models.CharField( max_length=120 )
    body = models.TextField()

    def __str__(self):
        return f"{self.chat.room_name}-{self.username}"
    

