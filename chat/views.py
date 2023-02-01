from django.shortcuts import render,redirect
from .models import Room,Message
# Create your views here.
def index(request):
    return render(request,'index.html')
def room(request,room):
    room = room
    return render(request,'room.html',{'room':room})
def checkview(request):
    room = request.POST['room_name']
    user = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+user)
    else:
        new_room = Room.objects.create(name = room).save()
        return redirect('/'+room+'/?username='+user)