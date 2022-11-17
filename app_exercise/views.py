from django.shortcuts import render
import requests
from django.http import HttpResponse,JsonResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'app_exercise/index.html')

def addingPageView(request) :
    return render(request, 'app_exercise/add_workout.html')

def listPageView(request):
    return HttpResponse('Welcome to the listing page!')

def aboutPageView(request):
    return HttpResponse('Welcome to the about page!')

#testing
