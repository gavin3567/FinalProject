from django.urls import path
from .views import indexPageView
from .views import addingPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("adding/", addingPageView, name ="adding"),
]