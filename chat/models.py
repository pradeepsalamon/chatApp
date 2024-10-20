from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.room_name)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self) -> str:
        return str(self.room)
    
from django.db import models

class ChatMessage(models.Model):
    user = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.message[:50]} ({self.timestamp})"
