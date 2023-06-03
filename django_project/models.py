from django.db import models

from pathlib import Path
import os
from django.contrib.auth.models import User

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Pet(models.Model):
    name = models.CharField(help_text='Enter the name of the pet', max_length=15)
    species = models.CharField(help_text='Enter the species of the pet', max_length=10)
    breed = models.CharField(help_text='Enter the breed of the pet', max_length=15)
    age = models.IntegerField(help_text='Enter the age of the pet in years')
    gender = models.CharField(help_text='Enter the gender of the pet', max_length=15)
    description1 = models.CharField(max_length=1500)
    description2 = models.CharField(max_length=150)
    description3 = models.CharField(max_length=150)
    image = models.ImageField(upload_to='static/images/')

class Favorite(models.Model):
  user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
  pet = models.ForeignKey(Pet, related_name='favorites', on_delete=models.CASCADE)
