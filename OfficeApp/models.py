from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    telefon = models.CharField(max_length=15, blank=True)
    data_nastere = models.DateField(null=True)
    cod_postal = models.IntegerField(null=True)
    adresa = models.CharField(null=True)
    date = models.BooleanField(null=True)
    blocat = models.BooleanField(null=True)
    pic = models.ImageField(width_field=400, height_field=400)