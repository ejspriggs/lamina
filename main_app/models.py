from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=60)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Auxiliary info missing from API
class BugWeather(models.Model):
    name = models.CharField(max_length=100)
    spawn_weather = models.CharField(max_length=100)

class Fossils(models.Model):
    name = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    display_name = models.CharField(max_length = 100)
    is_northern_hemi = models.BooleanField()