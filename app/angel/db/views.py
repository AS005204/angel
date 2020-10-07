from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import View
from .models import Volunteers

def hello(requests):
    search_querry = requests.GET.get('search','')

    if search_querry:
        volunteers = Volunteers.objects.filter( Q(user_idd__icontains = search_querry) | Q(user_name__icontains = search_querry) | Q(br__icontains = search_querry))
    else: 
        volunteers = Volunteers.objects.all()
    return render(requests, 'db/index.html',
    {'volunteers' : volunteers})