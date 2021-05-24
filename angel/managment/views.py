from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Volunteers
from django.contrib.auth.models import User


def index(request):
    return render(request,'index.html')

def open(request, user_id, Volunteers): 
    user = User.objects.create_user(request.POST.get(str('username')), request.POST.get(str('mypassword')))
    return HttpResponseRedirect('index.html')
