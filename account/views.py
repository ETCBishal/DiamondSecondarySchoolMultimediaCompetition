from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Room, Message


def delete_rooms(request):
    room_details = Room.objects.all()
    message_details = Message.objects.all()

    if room_details.exists() == False and message_details.exists() == False:
        messages.info(request, 'No such rooms')
        return redirect('/')

    else:
        room_details.delete()
        message_details.delete()

        messages.success(
            request, 'All Rooms along with the messages has been deleted successfully!')
        return redirect('/')


def home(request):
    rooms = Room.objects.all()  # fetching out all the rooms in the database
    total_rooms = len(rooms)    # counting the no. of rooms
    return render(request, 'home.html', {
        'rooms': rooms,
        'total_rooms': total_rooms
    })


def signupUser(request):
    if request.method == "POST":
        # fetching out all the details filled by the user while signing up

        fname = request.POST.get('fName')
        lname = request.POST.get('lName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        if pass1 == pass2:  # confirming the password
            user = User.objects.create_user(
                username=username, email=email, password=pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(
                request, "Your YourRoom login account has been successfully created!")
            return redirect('/')

    return HttpResponse("404 - Bag Gateway")


def loginUser(request):
    if request.method == "POST":
        # fetching out all the details filled by the user while signing in

        loginusername = request.POST.get('loginusername')
        loginpass = request.POST.get('loginpass')

        user = authenticate(request, username=loginusername,
                            password=loginpass)  # returns an object

        if user is not None:  # authenticating the user
            login(request, user=user)
            messages.success(
                request, f"Welcome {loginusername}! You have successfully logged in into YourRoom!")
            return redirect('/')

        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect('/')

    return HttpResponse("404 - Bad Gateway")


def logoutUser(request):
    if request.user.is_anonymous:  # checking if the user is not logged in
        messages.error(request, "You've not logged in yet")
        return redirect('/')
    else:
        logout(request)
        messages.success(
            request, "You've successfully logged out from YourRoom!")
        return redirect('/')


# f(x) for the chatting room
def room(request, room):
    username = request.GET.get('username')
    try:
        room_details = Room.objects.get(name=room)
        return render(request, 'room.html', {

            'username': username,
            'room': room,
            'room_details': room_details,
        })
    except Exception as e:
        print(e)
        return redirect('/')


def checkview(request):
    if request.user.is_anonymous:
        messages.info(
            request, 'Please login before entering or creating any room!')
        return redirect('/')
    else:
        room = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room).exists():
            return redirect('/'+room+'/?username='+username)
        else:
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    if message != '':
        new_message = Message.objects.create(
            value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse("Hi, Message Sent Successfully!!")
    else:
        return HttpResponse("Message can't be blank")


def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
