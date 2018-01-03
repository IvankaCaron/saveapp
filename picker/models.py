from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User



class Spot(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    location = models.PointField(srid=4326)

    objects = models.Manager()


    def __str__(self):
        return self.name
