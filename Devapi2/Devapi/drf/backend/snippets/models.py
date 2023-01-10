from django.db import models
from datetime import date, datetime, time
from django.utils import timezone

# class Snippet(models.Model):
#     title = models.CharField(unique=True, max_length=100, blank=True, default='')
#     name = models.CharField(unique=True, max_length=100, blank=True, default='')
#     email = models.CharField(unique=True, max_length=100, blank=True, default='')
#     church = models.CharField(unique=True, max_length=100, blank=True, default='')
#     owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, unique=True) # new

#     def __str__(self):
#         return self.title

class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    church = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE) # new
    nextClass = models.DateField(max_length=100, blank=True)
    nextClassTime = models.TimeField(default=time(9, 30))
    courseID = models.CharField(max_length=100, blank=True, default='')


    def __str__(self):
        return self.title

#Why did i do a snippet model and student model?
class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    courseID = models.CharField(max_length=100, blank=True, default='')    
    classesAttended = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='progress', on_delete=models.CASCADE) # new
    email = models.EmailField()
    church = models.CharField(max_length=100, blank=True, default='')
    post = models.TextField(max_length=100, blank=True, default='')







