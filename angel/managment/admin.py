from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SearchSquad)
admin.site.register(Event)
admin.site.register(Crew)
admin.site.register(Education)
#admin.site.register(Volunteers)
admin.site.register(Equipment_hisrory)
admin.site.register(Equipment)
admin.site.register(Missing_people)
admin.site.register(Found_people)

# Define the Volunteers class
class VolunteersAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Volunteers, VolunteersAdmin)