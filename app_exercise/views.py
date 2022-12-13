from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Workout_Group, Workout, Person, Person_Workout, Person_Workout_Data
from django.contrib.auth.models import User

# Create your views here.
def loginPageView(request):
    return render(request,'login/login-index.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def createUserPageView(request) :
    return render(request, 'login/create_user.html')

def accountCreatedView(request) :
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        person = Person()

        person.person = user
        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.phone = request.POST['phone']
        person.email = request.POST['email']


        user.save()
        person.save()

    return render(request,'login/login-index.html')

def loginAuth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Invalid username or password!')
    return render(request,'login/login-index.html')

@login_required
def indexPageView(request) :
    return render(request, 'app_exercise/index.html')


@login_required
def listPageView(request):
   current_user = request.user.id
   group = Workout.objects.all()
   person_workout = Person_Workout.objects.filter(person=current_user).distinct().values_list("workout")
   workout = group.exclude(workout__in=person_workout) 
   category = Workout_Group.objects.all()
   context = {
       'group': group,
       'person_workout':person_workout,
       'workout':workout,
       'category':category
   }
   return render(request, 'app_exercise/list_workout.html',context)

@login_required
def workoutSelection(request):
    current_user = request.user.id
    person = Person.objects.get(person = current_user)

    group = Workout.objects.all()
    test= request.POST
    workout= request.POST.getlist("workout")
    for id in workout:
        workout = Workout.objects.get(workout = id)
        person_workout = Person_Workout()
        person_workout.person = person
        person_workout.workout = workout
        person_workout.save()
 
  
    return redirect('/dashboard/')
@login_required 
def dashboardPageView(request):
    # How do I make sure the person logged in will get the information they need?
    current_user = request.user.id

    person = Person.objects.all()
    person_workout = Person_Workout.objects.filter(person=current_user)
    person_workout_data = Person_Workout_Data.objects.filter(person_workout__in=person_workout).order_by('-workout_date')
    workout = Person_Workout.objects.values('workout').distinct()
    workout_cat = Workout_Group.objects.all()

    user_name = request.user.username

    context ={
        'person' : person,
        'current_user' : current_user,
        'user_name' : user_name,
        'person_workout' : person_workout,
        'person_workout_data' : person_workout_data,
        'workout' : workout,
        'workout_cat' : workout_cat,
    }
    
    return render(request, 'app_exercise/dashboard.html', context)

def aboutPageView(request):
    return HttpResponse('Welcome to the about page!')

def storeWorkoutView(request) :
    if request.method == 'POST':

        workout = Workout()
        workout_groups = Workout_Group.objects.all()

        workout.workout_name = request.POST['workout_name']
        workout.category = workout_groups.get(category_name=request.POST['category'])

        
        workout.save()

    return render(request, 'app_exercise/list_workout.html')    

def deleteWorkoutView(request, id) :
    person_workout = Person_Workout_Data.objects.get(id=id)
    person_workout.delete()
    return redirect('/dashboard/')

def deleteWorkoutView2(request, id) :
    data = Workout.objects.get(id=id)
    data.delete()
    return redirect('/listing/')

def updateWorkoutView(request,id):
    current_user = request.user.id
    person_workout_data = Person_Workout_Data.objects.get(id=id)
    person_workout = Person_Workout.objects.filter(person=current_user)
    context = {
        'person_workout_data': person_workout_data,
        'person_workout': person_workout,
    }
    
    return render(request, 'app_exercise/update_workout.html',context)

def updateView(request):

    updated_sets = request.POST['num_sets']
    updated_reps = request.POST['num_reps']
    updated_weight = request.POST['weight_used']
    updated_date = request.POST['date_entered']
    id = int(request.POST['person_workout_id'])

    person_workout_data = Person_Workout_Data.objects.get(id=id)

    person_workout_data.workout_date = updated_date
    person_workout_data.num_sets = updated_sets
    person_workout_data.num_reps = updated_reps
    person_workout_data.weight_used = updated_weight
    person_workout_data.save()

    return redirect('/dashboard/')


def addWorkoutView(request, id) :
    current_user = request.user.id
    person_workout_data = Person_Workout_Data.objects.get(id=id)
    person_workout = Person_Workout.objects.filter(person=current_user)

    context = {
        'person_workout_data': person_workout_data,
        'person_workout': person_workout,
    }

    return render(request, 'app_exercise/add_workout_data.html',context)

def addView(request) :
    if request.method == 'POST':
        updated_sets = request.POST['num_sets']
        updated_reps = request.POST['num_reps']
        updated_weight = request.POST['weight_used']
        updated_date = request.POST['date_entered']
        id = int(request.POST['person_workout_id'])

        person_workout_data = Person_Workout_Data()

        person_workout_data.workout_date = updated_date
        person_workout_data.num_sets = updated_sets
        person_workout_data.num_reps = updated_reps
        person_workout_data.weight_used = updated_weight
        person_workout_data.person_workout_id = id
        person_workout_data.save()

    return redirect('/dashboard/')