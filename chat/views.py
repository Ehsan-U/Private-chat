from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.


def room(request):
    if request.user.is_authenticated:
        return render(request, "room.html")
    else:
        return redirect('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            user_obj = User.objects.get(username=username)
            login(request, user_obj)
            # return redirect('room')
            return JsonResponse({"flag":True})
        else:
            return JsonResponse({"flag": False})
            # return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')