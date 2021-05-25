from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime, date
from django.db.models.signals import post_save
from django.utils.timezone import now
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from .managers import CustomUserManager
from  datetime import date
from bootstrap_datepicker_plus import DatePickerInput

sex_choice = (
     ('Male', 'Male'),
     ('Female', 'Female')
 )
class UserProfile(models.Model):
    user = models.OneToOneField(User, null='True', on_delete = models.CASCADE)
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=sex_choice, default='Male')
    date_of_birth = models.DateField(default=timezone.now)
    job = models.CharField(max_length = 15)
    phone = models.CharField(max_length =  10)
    religion = models.CharField(max_length = 100)
    region = models.CharField(max_length = 20)
    zone = models.CharField(max_length = 20)
    woreda = models.CharField(max_length = 20)
    kebele = models.CharField(max_length = 200)
    image = models.ImageField(default='default.jpg', upload_to="profile_image/", blank=False)
    mother_name = models.CharField(max_length = 200)
    emergnency_case = models.CharField(max_length = 200)
    emergnency_number = models.CharField(max_length = 200)
    DisplayFields = ['name', 'gender', 'age', 'job', 'phone', 'religion', 'region', 'zone', 'woreda', 'kebele', 'image', 'mother_name', 'emergnency_case', 'emergnency_number']
    SearchableFields = ['face_id', 'phone']


     
    def __str__(self):
        return self.name 
# Create your models here.
    @property
    def age(self):
        if (self.date_of_birth != None):
            age = date.today().year -self.date_of_birth.year
            return age
    