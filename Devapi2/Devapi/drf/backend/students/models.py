from django.db import models
from datetime import date, datetime, time
from django.utils import timezone
from django.contrib.auth.models import User


#Why did i do a snippet model and student model? ans: separate student model and teacher model
class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    courseID = models.CharField(max_length=100, blank=True, default='')    
    email = models.EmailField(null=True, blank=True)
    church = models.CharField(max_length=100, null=True, blank=True, default='')
    post = models.TextField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')




    def __str__(self):
        return self.title