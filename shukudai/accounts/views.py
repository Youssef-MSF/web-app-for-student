from django.shortcuts import render, redirect
from django.contrib import messages, auth

from .models import Student


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        gender = request.POST['gender']
        age = request.POST['age']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password_confirm']

        if password1 == password2:
            if Student.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return render(request, 'signup.html')
            elif Student.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return render(request, 'signup.html')
            else:
                student = Student.objects.create_user(username=username, fullname=fullname, gender=gender, age=age,
                                                      email=email, password=password1)
                student.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Login')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
