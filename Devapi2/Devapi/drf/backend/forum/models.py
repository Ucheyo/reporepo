from django.db import models
from django.contrib.auth.models import User
from students.models import Student
from comments.models import Comment
# Create your models here.
class Forum(models.Model):
    ContentTitle = models.TextField(max_length=100, blank=True, default='')
    ContentBody = models.TextField(max_length=100, blank=True, default='')
    students = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
