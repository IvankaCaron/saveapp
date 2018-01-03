from django.conf.urls import include, url
from django.urls import path

from .views import MapPageView, point_datasets, insertData

urlpatterns = [
    #url(r'^$', MapPageView.as_view(), name= 'myMap'),
    #path('',  MapPageView.as_view(), name= 'myMap'),
    path('',  MapPageView.as_view(), {'template_name': 'templates/map.html'}, name= 'myMap'),

    #url(r'^spot_data/$', point_datasets, name='spot'),
    path('spot_data/', point_datasets, name='spot'),
    path('insertdata/', insertData, name="insertdata"),

    ]