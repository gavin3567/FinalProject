from django.urls import path
from .views import indexPageView
from .views import addingPageView
from .views import listPageView
from .views import aboutPageView
urlpatterns = [
    path("", indexPageView, name="index"),
    path("adding/", addingPageView, name ="adding"),
    path("listing/", listPageView, name ="listing"),
    path("about/", aboutPageView, name ="about"),
]