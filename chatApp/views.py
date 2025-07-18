from django.shortcuts import render,redirect
from chatApp.models import *

# Create your views here.
def create_room(request):
    if request.method == "POST":
        username = request.POST.get("username")
        room = request.POST.get("room")

        try:
            get_room = Room.objects.get(room_name = room)
        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
        return redirect("message", room_name=room, username=username)
    return render(request,"create_room.html")

def message(request,room_name,username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)

    context = {
        "messages" : get_messages,
        "user" : username,
        "room_name" : room_name
    }
    return render(request,"message.html",context)

