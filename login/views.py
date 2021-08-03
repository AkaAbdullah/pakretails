from login.models import Products
from django.shortcuts import redirect, render
from .signupform import myLoginForm, myUserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .profile import UserProfileForm
from django.contrib.auth.models import User


def home(request):
    pro = Products.objects.all()
    return render(request, 'login/home.html',{'pro':pro})


def signupuser(request):
    if request.method =='GET':
        fm = myUserCreationForm()
        return render(request,'login/signup.html',{'form':fm})
    elif request.method =='POST':
        fm = myUserCreationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            login(request,user)
            return redirect('home')
        else:
            fm = myUserCreationForm()
            return render(request,'login/signup.html',{'form':fm})

def loginuser(request):
    if request.method =='GET':
        lg=myLoginForm()
        return render(request,'login/login.html',{'form':lg})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user == None:
            lg=myLoginForm()
            messages.add_message(request, messages.SUCCESS,'Invalid Username or password')
            return render(request,'login/login.html',{'form':lg})
        else:
            login(request,user)
            return redirect('home')


def profile(request):
    return render(request,'login/profile.html')

def updateinfo(request):
    fm = UserProfileForm()
    return render(request,'login/updateinfo.html',{'form':fm})

