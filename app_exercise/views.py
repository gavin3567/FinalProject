from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return HttpResponse('This is our amazing home page!')

def aboutPageView(request) :
    sOutput = 'About Page'
    return HttpResponse(sOutput)       