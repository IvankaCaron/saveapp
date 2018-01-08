from django.contrib import admin

from .models import Spot, TypeProduct
from leaflet.admin import LeafletGeoAdmin

class SpotAdmin(LeafletGeoAdmin):
    pass
    list_display = ('name', 'location', 'description')
    search_fields = ('name', 'description')


admin.site.register(Spot, SpotAdmin)


class TypeProductAdmin(admin.ModelAdmin):
    pass
    list_display = ('name',)



admin.site.register(TypeProduct, TypeProductAdmin)


# Register your models here.