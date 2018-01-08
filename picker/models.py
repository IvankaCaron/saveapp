from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User


class TypeProduct(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to='icon_image', blank=True)


    def __str__(self):
        return self.name


class Spot(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    typeProduct = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, related_name='typeProduct', null=True)
    location = models.PointField(srid=4326)

    objects = models.Manager()


    def __str__(self):
        return self.name


