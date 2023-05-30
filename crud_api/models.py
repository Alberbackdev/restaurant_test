# pylint: disable=missing-class-docstring
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to="files")


    def __str__(self):
        return self.file.name


class Restaurant(models.Model):
    id = models.TextField(primary_key=True, unique=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    name = models.TextField()
    site = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

