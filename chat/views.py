from django.shortcuts import render, redirect
from .models import Room, Message

# def chat(request):
#     return render(request, 'index.html')

def createRoom(request):
    if request.method == 'POST':
        room_name = request.POST['room']
        user_name = request.POST['name']
        try:
            get_room = Room.objects.get(room_name=room_name)
        except Room.DoesNotExist:
            new_room = Room(room_name = room_name)
            new_room.save()
        return redirect('chat', room_name = room_name, user_name = user_name)        
            
    return render(request, 'index1.html')

def messageView(request, room_name, user_name):
    get_room = Room.objects.get(room_name = room_name)
    get_messages = Message.objects.filter(room=get_room)
    context = {
        'messages' : get_messages,
        'username' : user_name,
        'roomame' : room_name
    }
    return render(request, 'message.html', context)