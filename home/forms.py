from django import forms
from .models import * 
#from home.models importUserProfile

class RegisterForm(forms.ModelForm):

    class Meta:
        model =UserProfile
        fields = ( 'face_id', 'name', 'gender', 'date_of_birth', 'job', 'phone', 'religion', 'region', 'zone', 'woreda', 'kebele', 'image', 'mother_name', 'emergnency_case', 'emergnency_number' )