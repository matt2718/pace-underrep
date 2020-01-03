"""
Definition of models.
"""

from django.db import models
from enum import Enum, auto
import os
from django.conf import settings

#CHOICE_DIR = os.path.join(settings.BASE_DIR, 'app/choices/')

#with open(os.path.join(CHOICE_DIR, 'gender.txt')) as f:
#        genders = f.read().splitlines()
#Gender = Enum('Gender', genders)

#switch this to just a string?
class Visibility(Enum):
    PUBLIC = 1
    AUTHED = 2
    SHARED = 3

#no need for unique field types, but seperating them for type management is helpful
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class Identity(Tag):
    pass

class Circuit(Tag):
    pass

class Involvement(Tag):
    pass

class Person(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    facebook = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    date_of_birth = models.DateTimeField()
    bio = models.TextField()
    propic = models.ImageField()
    identities = models.ManyToManyField(Identity)
    visibility = models.PositiveSmallIntegerField(default=Visibility.PUBLIC)
    circuits = models.ManyToManyField(Circuit)
    involvements = models.ManyToManyField(Involvement)
    #TODO: add location field


    people = models.Manager()

    def __str__(self):
        return self.last_name + ", " + self.first_name

    class Meta:
        ordering= ["last_name", "first_name"]




