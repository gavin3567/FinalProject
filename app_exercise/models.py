from django.db import models
from datetime import datetime
# Create your models here.

class Wokout_Group(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self) :
        return (self.category_name)
    
    class Meta:
        db_table = 'workout_cat'

class Workout(models.Model):
    workout_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(Wokout_Group, on_delete = models.CASCADE)
    # main_photo = models.ImageField(upload_to='photos')          
    # leave_date = models.DateField(default=datetime.today, blank=True)

    def __str__ (self):
        return (self.workout_name)
    
    class Meta:
        db_table = 'workout'
    
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)    
    phone = models.CharField(max_length=13, blank=True)
    workout = models.ManyToManyField(Workout, blank=True)

    def __str__(self):
        return (self.full_name)
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    #override the save method
    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Person, self).save() # Call the "real" save() method.              

    class Meta:
        db_table = 'person'