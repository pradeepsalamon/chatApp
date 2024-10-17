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