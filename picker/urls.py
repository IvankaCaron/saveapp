from django.conf.urls import include, url
from django.urls import path

from .views import MapPageView, point_datasets, insertData, MapSearchView, MapSearchNewView, MapSearchSampleView

urlpatterns = [
    #url(r'^$', MapPageView.as_view(), name= 'myMap'),
    #path('',  MapPageView.as_view(), name= 'myMap'),
    path('',  MapPageView.as_view(), {'template_name': 'templates/map.html'}, name= 'myMap'),
    path('search',  MapSearchView.as_view(), name= 'mySearch'),
    path('searchNew',  MapSearchNewView.as_view(), name= 'mySearchNew'),
    path('searchSample',  MapSearchSampleView.as_view(), name= 'mySearchSample'),
    #url(r'^spot_data/$', point_datasets, name='spot'),
    path('spot_data/', point_datasets, name='spot'),

    path('insertdata/', insertData, name="insertdata"),

    ]