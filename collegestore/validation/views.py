from . models import Dpt, Course
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.

def button(request):
    return render(request, "button.html")


def form(request):
    dept = Dpt.objects.all()
    sub = Course.objects.all()
    return render(request, "form.html", {'dept': dept, 'sub': sub})


def msg(request):
    if request.method == 'POST':
        messages.info(request, "Form submitted")
    return render(request, "message.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("button")
        else:
            messages.info(request, 'invalid user')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['confirm password']

        if password == password1:

            if User.objects.filter(username=user_name).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "password and confirm password are not a match")
            return redirect('register')

        return redirect('/')
    return render(request, 'register.html')
