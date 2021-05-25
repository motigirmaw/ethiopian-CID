from django.contrib import admin
from home.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display=(
       'face_id',
        'name', 
        'gender', 
        'age',
        'job',
        'phone',
        'religion',
        'region',
        'zone',
        'woreda',
        'kebele',
        'image',
        'mother_name',
        'emergnency_case',
        'emergnency_number',
        
    )
admin.site.register(UserProfile,UserProfileAdmin)