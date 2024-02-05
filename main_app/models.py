from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=60)
    image = models.CharField(max_length=256)
    time_of_year = models.CharField(max_length=100)
    south_hemi_toy = models.CharField(max_length=100)
    time_of_day = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    shadow_size = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    value = models.IntegerField()
    misc = models.TextField(max_length=500)

    # user = models.ForeignKey(User, on_delete=models.CASCADE)

class Fossils(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=256)
    value = models.IntegerField()

    # user = models.ForeignKey(User, on_delete=models.CASCADE)