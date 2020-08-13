from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterUserForm
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('login:home')
    
    context = {
        
    }

    return render(request, 'login/index.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('login:home')
    
    form = RegisterUserForm()
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:login')
    context = {
        'form' : form
    }
    return render(request, 'registration/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('login:home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login:home')
        else:
            messages.info(request, 'Username or Password is incorrect')



    context = {
        
    }
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login:login')

@login_required(login_url='login:login')
def home(request):
    context = {

    }

    return render(request, 'login/home.html', context)