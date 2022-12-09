from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Workout_Group(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self) :
        return (self.category_name)
    
    class Meta:
        db_table = 'workout_cat'

class Workout(models.Model):
    workout = models.BigAutoField(primary_key=True,unique=True,serialize=False)
    workout_name = models.CharField(max_length=50)
    category = models.ForeignKey(Workout_Group, on_delete = models.DO_NOTHING)
    # main_photo = models.ImageField(upload_to='photos')          
    # leave_date = models.DateField(default=datetime.today, blank=True)

    def __str__ (self):
        return (self.workout_name)
    
    class Meta:
        db_table = 'workout'
    
    
class Person(models.Model):
    person = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE,serialize=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)    
    phone = models.CharField(max_length=13, blank=True)
    workout = models.ManyToManyField(Workout, blank=True,through='Person_Workout')

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

class Person_Workout(models.Model):
    person_workout = models.BigAutoField(primary_key=True,unique=True,serialize=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    class Meta:
        db_table = 'person_workout'
        constraints = [
        models.UniqueConstraint(fields=['person', 'workout'], name='person_workout_pk')
    ]

    def __str__(self):
        return f'{self.person} {self.workout}'

class Person_Workout_Data(models.Model):

    person_workout = models.ForeignKey(Person_Workout,on_delete=models.CASCADE)
    workout_date = models.DateField(default=datetime.today, blank=True)
    num_sets = models.SmallIntegerField(default=0, blank=True)
    num_reps = models.SmallIntegerField(default=0, blank=True)
    weight_used = models.SmallIntegerField(default=0, blank=True)

    class Meta:
        db_table = 'person_workout_data'

    def __str__(self):
        return f'{self.person_workout} {self.workout_date}'
