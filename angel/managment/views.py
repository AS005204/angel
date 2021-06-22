from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Volunteers
from .models import Missing_people
from .models import Found_people
from .models import Education
from .models import Event
from django.contrib.auth.models import User


def index(request):
    return render(request,'base.html')

def missing(request):
    missing = Missing_people.objects.all()
    return render(request,'Missing.html',
    {'missing' : missing})

def found(request):
    founds = Found_people.objects.all()
    return render(request,'Found.html',
    {'founds' : founds})


def education(request):
    educations = Education.objects.all()
    return render(request,'Education.html',
    {'educations' : educations})

def event(request):
    events = Event.objects.all()
    return render(request,'Event.html',{'events' : events})

def aboutevent(request, event_id):
    events = Event.objects.get(id=event_id)
    return render(request, 'CardForEvent.html',{'events' : events})

def abouteducation(request, education_id):
    educations = Education.objects.get(id=event_id)
    return render(request, 'CardForEducation.html',{'educations' : educations})

def aboutmiss(request, miss_id):
    miss = Education.objects.get(id=miss_id)
    return render(request, 'CardForMiss.html',{'miss' : miss})