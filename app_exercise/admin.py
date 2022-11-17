from django.contrib import admin
from .models import Person, Workout, Wokout_Group, Person_Workout_Data, Person_Workout
# Register your models here.
admin.site.register(Person)
admin.site.register(Workout)
admin.site.register(Wokout_Group)
admin.site.register(Person_Workout)
admin.site.register(Person_Workout_Data)
