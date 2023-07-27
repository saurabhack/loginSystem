from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    return render(request,'index.html')
@csrf_protect
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['confirm_password']

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('/')
    return render(request,'signup.html')
@csrf_protect
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user!=None:
            auth.login(request,user)
    return render(request,'signin.html')
def signout(request):
    auth.logout(request)
    return redirect('/')


