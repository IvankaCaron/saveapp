from django.contrib import admin

from .models import Spot
from leaflet.admin import LeafletGeoAdmin

class SpotAdmin(LeafletGeoAdmin):
    pass
    list_display = ('name', 'location', 'description')




admin.site.register(Spot, SpotAdmin)


# Register your models here.