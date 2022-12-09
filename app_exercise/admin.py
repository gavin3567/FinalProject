from django.contrib import admin
from .models import Person, Workout, Workout_Group, Person_Workout, Person_Workout_Data
# Register your models here.
admin.site.register(Person)
admin.site.register(Workout)
admin.site.register(Workout_Group)
admin.site.register(Person_Workout)
admin.site.register(Person_Workout_Data)

