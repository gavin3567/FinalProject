from django.contrib import admin
from .models import Person, Workout, Wokout_Group
# Register your models here.
admin.site.register(Person)
admin.site.register(Workout)
admin.site.register(Wokout_Group)
