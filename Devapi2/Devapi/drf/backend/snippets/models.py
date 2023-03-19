from django.db import models
from datetime import date, datetime, time
from django.utils import timezone
from django.contrib.auth.models import User
from  django import forms
from students.models import Student
# class Snippet(models.Model):
#     title = models.CharField(unique=True, max_length=100, blank=True, default='')
#     name = models.CharField(unique=True, max_length=100, blank=True, default='')
#     email = models.CharField(unique=True, max_length=100, blank=True, default='')
#     church = models.CharField(unique=True, max_length=100, blank=True, default='')
#     owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, unique=True) # new

#     def __str__(self):
#         return self.title

#teacher model
class Snippet(models.Model):
    # title = models.CharField(max_length=100, blank=True, default='')
    # church = models.CharField(max_length=100, blank=True, default='')
    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE) # new
    # nextClass = models.DateField(max_length=100, blank=True)
    # nextClassTime = models.TimeField(default=time(9, 30))
    # courseID = models.CharField(max_length=100, blank=True, default='')
    completedClasses = models.IntegerField(default=0)
    currentClass = models.IntegerField(default=0)
#    email = models.CharField(max_length=100, blank=True, default='')
#    name = models.CharField(max_length=100, blank=True, default='')




    def __str__(self):
        return self.completedClasses





