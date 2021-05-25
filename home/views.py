from django.shortcuts import render, redirect
from home.forms import RegisterForm
from django.contrib import messages
from home.backEnd import FaceRecognition
from home.models import UserProfile
from django.contrib.auth.decorators import login_required
import datetime

facerecognition = FaceRecognition()

def home(request):
    return render(request, 'home/home.html')
@login_required
def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully Registerd!')
            addFace(request.POST['face_id'])
            return redirect('/')
        else:
            messages.error(request, "Account Register Failed!")

    form = RegisterForm()
    context = {
        'title' : 'Register Form',
        'form' : form
    }
    return render(request, 'home/register.html', context)
def age_cal(request, date_of_birth):
    date_of_birth = date_of_birth
    todayy = datetime.datetime.now()
    age= int(todayy - date_of_birth)
    return render(request, 'home/profile.html', {'age': age} )

def addFace(face_id):
    face_id = face_id
    facerecognition.faceDetect(face_id)
    facerecognition.trainFace()
    return redirect('/')

@login_required
def identfay(request):
    face_id = facerecognition.recognizeFace()
    print(face_id)
    return redirect('/home/welcome/'+ str(face_id))

def welcome(request, face_id):
    face_id = int(face_id)
    print(face_id)
    data = {
        'user':UserProfile.objects.get(face_id= face_id)
    }
    return render(request, 'home/profile.html', data)
@login_required
def medical(request):
    return render(request, 'home/medical.html')
def age(self):
        return int((datetime.now().date() - self.date_of_birth).days / 365.25)