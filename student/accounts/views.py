import email
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, auth

def signup(request):
    if request.method == 'POST':
        firstName =request.POST['firstName']
        lastName = request.POST['lastName']
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=uname, email=email, password=password, first_name=firstName, last_name=lastName) 
        print("User created successfully") 
        return redirect('/')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=uname, password=password)
        
        if user is not None:
            auth.login(request,user)
            print("User logged in successfully")
            return redirect('/')
    else:
        return render(request, 'login.html')

def accounts(request):
    return HttpResponse("This is accounts page")


