from django.contrib import admin
from .models import Volunteers, SearchSquad, Event, Crew, Education, Equipment_hisrory, Equipment

admin.site.register(Volunteers)
admin.site.register(SearchSquad)
admin.site.register(Event)
admin.site.register(Crew)
admin.site.register(Education)
admin.site.register(Equipment_hisrory)
admin.site.register(Equipment)