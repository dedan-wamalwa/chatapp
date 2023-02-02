from django.shortcuts import render,redirect
from .models import Room,Message
# Create your views here.
def index(request):
    return render(request,'index.html')
def room(request,room):
    user = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request,'room.html',{
        'room':room,
        'room_details':room_details,
        'username':user,
        })
def checkview(request):
    room = request.POST['room_name']
    user = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+user)
    else:
        new_room = Room.objects.create(name = room).save()
        return redirect('/'+room+'/?username='+user)