from django.shortcuts import render
import requests
from django.http import HttpResponse,JsonResponse

# Create your views here.
def indexPageView(request) :
    response = requests.get('https://wger.de/api/v2/exercise/') # https://wger.de/api/v2/exercise-base/ another good endpoint
    response = response.json()
    return JsonResponse(response)

def addingPageView(request) :
    return HttpResponse('Welcome to the adding page!')

def listPageView(request):
    return HttpResponse('Welcome to the listing page!')

def aboutPageView(request):
    return HttpResponse('Welcome to the about page!')

#testing
