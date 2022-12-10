from django.urls import path
from .views import indexPageView, loginPageView, loginAuth, logout_view
from .views import addingPageView
from .views import listPageView
from .views import aboutPageView
from .views import dashboardPageView
from .views import storeWorkoutView
from .views import deleteWorkoutView
from .views import updateWorkoutView
from .views import updateView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),
    path("logout/", logout_view, name="logout"),
    path("login-auth/", loginAuth, name="login-auth"),
    path("adding/", addingPageView, name ="adding"),
    path("listing/", listPageView, name ="listing"),
    path("about/", aboutPageView, name ="about"),
    path("dashboard/", dashboardPageView, name ="dashboard"),
    path("addWorkout/",storeWorkoutView, name='addWorkout'),
    path("deleteWorkout/<int:id>/",deleteWorkoutView, name='deleteWorkout'),
    path("updateWorkout/<int:id>/",updateWorkoutView, name='updateWorkout'),
    path("update/",updateView, name='update-record'),
]