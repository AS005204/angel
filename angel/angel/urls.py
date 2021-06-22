
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from managment.views import *


urlpatterns = [
    path('catalog/', include('managment.urls')), #Теперь в главном URLconf подключим модуль managment
    path('', RedirectView.as_view(url='/catalog/', permanent=True), name='catalog'), # перенаправим корневой URL
    path('admin/', admin.site.urls, name = 'admin'),
    path('grappelli/', include('grappelli.urls')), 
    path('missingPeople/', missing, name='missingPeople'),
    path('FoundPeople/', found, name='foundPeople'),
    path('Education/', education, name='education'),
    path('Event/', event, name='event'),
    path('Event/<int:event_id>/', aboutevent, name='aboute'),
    path('Education/<int:education_id>/', abouteducation, name='abouteducation'),
    path('missingPeople//<int:miss_id>/', aboutmiss, name='aboutmiss'),
]


