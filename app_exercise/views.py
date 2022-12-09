from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def loginPageView(request):
    return render(request,'login/login-index.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def loginAuth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Invalid username or password!')
    return render(request,'login/login-index.html')

@login_required
def indexPageView(request) :
    return render(request, 'app_exercise/index.html')

@login_required 
def addingPageView(request) :
    return render(request, 'app_exercise/add_workout.html')

@login_required 
def listPageView(request):
    return render(request, 'app_exercise/list_workout.html')

def dashboardPageView(request):
    return render(request, 'app_exercise/dashboard.html')

def aboutPageView(request):
    return HttpResponse('Welcome to the about page!')

#testing
