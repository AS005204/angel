
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('catalog/', include('managment.urls')), #Теперь в главном URLconf подключим модуль managment
    path('', RedirectView.as_view(url='/catalog/', permanent=True)), # перенаправим корневой URL
    path('admin/', admin.site.urls, name = 'admin'),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
]


