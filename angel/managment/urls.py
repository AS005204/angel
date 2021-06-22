from django.urls import path
from django.contrib import admin
from . import views
from managment.views import *


urlpatterns = (
    path('', views.index, name='index'),
)
