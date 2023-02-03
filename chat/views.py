from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse
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
def send(request):
    message = request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']

    new_message = Message.objects.create(value = message, user = username,room=room_id)
    new_message.save()
    return HttpResponse('message sent ')
def messages(request,room):
    room_details = Room.objects.get(name = room)

    room_msgs = Message.objects.filter(room=room_details.id)
    return JsonResponse({"room_msgs":list(room_msgs.values())})