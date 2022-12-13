from django.urls import path
from .views import indexPageView, loginPageView, loginAuth, logout_view
from .views import listPageView
from .views import aboutPageView
from .views import dashboardPageView
from .views import storeWorkoutView
from .views import deleteWorkoutView
from .views import deleteWorkoutView2
from .views import updateWorkoutView
from .views import updateView
from .views import createUserPageView
from .views import accountCreatedView
from .views import addWorkoutView
from .views import addView
from .views import workoutSelection
from .views import searchWorkouts


urlpatterns = [
    path("", indexPageView, name="index"),
    path("login/", loginPageView, name="login"),
    path("logout/", logout_view, name="logout"),
    path("login-auth/", loginAuth, name="login-auth"),
    path("listing/", listPageView, name ="listing"),
    path("about/", aboutPageView, name ="about"),
    path("dashboard/", dashboardPageView, name ="dashboard"),
    path("addWorkout/",storeWorkoutView, name='addWorkout'),
    path("deleteWorkout/<int:id>/",deleteWorkoutView, name='deleteWorkout'),
    path("deleteWorkout2/<int:id>/",deleteWorkoutView2, name='deleteWorkout2'),
    path("updateWorkout/<int:id>/",updateWorkoutView, name='updateWorkout'),
    path("update/",updateView, name='update-record'),
    path("create-user/",createUserPageView, name='create-user'),
    path("account-created/",accountCreatedView, name='account-created'),
    path("add_workout/<int:id>",addWorkoutView, name='add_workout'),
    path("add/",addView, name='add'),
    path("select-workout/",workoutSelection, name='select-workout'),
    path("search-db-workout/",searchWorkouts, name="search-workout")
]