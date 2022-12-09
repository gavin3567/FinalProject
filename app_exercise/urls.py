from django.urls import path
from .views import indexPageView, loginPageView
from .views import addingPageView
from .views import listPageView
from .views import aboutPageView
from .views import dashboardPageView
urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),
    path("adding/", addingPageView, name ="adding"),
    path("listing/", listPageView, name ="listing"),
    path("about/", aboutPageView, name ="about"),
    path("dashboard/", dashboardPageView, name ="dashboard"),
]