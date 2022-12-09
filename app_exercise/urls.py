from django.urls import path
from .views import indexPageView, loginPageView, loginAuth, logout_view
from .views import addingPageView
from .views import listPageView
from .views import aboutPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),
    path("logout/", logout_view, name="logout"),
    path("login-auth/", loginAuth, name="login-auth"),
    path("adding/", addingPageView, name ="adding"),
    path("listing/", listPageView, name ="listing"),
    path("about/", aboutPageView, name ="about"),
]