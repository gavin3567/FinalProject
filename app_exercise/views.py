from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse('Welcome to the exercise app!')

def addingPageView(request) :
    return HttpResponse('Welcome to the adding page!')

def listPageView(request):
    return HttpResponse('Welcome to the listing page!')

def aboutPageView(request):
    return HttpResponse('Welcome to the about page!')

#testing
