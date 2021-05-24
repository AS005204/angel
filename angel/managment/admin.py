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

# Define the Volunteers class
class VolunteersAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Volunteers, VolunteersAdmin)