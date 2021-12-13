from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    code_name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    id_hotel = models.CharField(max_length=3)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


