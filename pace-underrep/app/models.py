"""
Definition of models.
"""

from django.db import models
from enum import Enum, auto
import os
from django.conf import settings

CHOICE_DIR = os.path.join(settings.BASE_DIR, 'app/choices/')

with open(os.path.join(CHOICE_DIR, 'gender.txt')) as f:
        genders = f.read().splitlines()
Gender = Enum('Gender', genders)

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    age = models.IntegerField();
    #gender = models.



