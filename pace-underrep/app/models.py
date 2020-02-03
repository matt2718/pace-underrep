"""
Definition of models.
"""

from django.db import models
from enum import Enum, auto
import os
from django.conf import settings
from django import forms
from django.forms import ModelForm
from django.contrib import admin
from datetime import datetime
import django_tables2 as tables

#CHOICE_DIR = os.path.join(settings.BASE_DIR, 'app/choices/')

#with open(os.path.join(CHOICE_DIR, 'gender.txt')) as f:
#        genders = f.read().splitlines()
#Gender = Enum('Gender', genders)

#switch this to just a string?
Visibility = ("PUBLIC", "AUTHED", "SHARED")

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
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    facebook = models.CharField(max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()
    bio = models.TextField(blank=True)
    propic = models.ImageField(blank=True)
    identities = models.ManyToManyField(Identity, blank=True)
    visibility = models.PositiveSmallIntegerField(default=Visibility.index("PUBLIC"), blank=True)
    circuits = models.ManyToManyField(Circuit, blank=True)
    involvements = models.ManyToManyField(Involvement, blank=True)
    #TODO: add location field

    @property
    def age(self):
        return int((datetime.now().date() - self.date_of_birth).days / 365.25)

    @property
    def minor(self):
        return "Yes" if self.age<18 else "No"

    people = models.Manager()

    def __str__(self):
        return self.last_name + ", " + self.first_name

    class Meta:
        ordering= ["last_name", "first_name"]

admin.site.register(Person)
admin.site.register(Identity)
admin.site.register(Circuit)
admin.site.register(Involvement)

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'identities']
        widgets = {
            'date_of_birth' : forms.DateInput(attrs={'type':'date'})
            }


class PersonTable(tables.Table):
    class Meta:
        model=Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("last_name", "first_name", "email", "minor", "identities")