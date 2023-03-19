from django.db import models
from students.models import Student

# Create your models here.
class Forum(models.Model):
    ContentTitle = models.TextField(max_length=100, blank=True, default='')
    ContentBody = models.TextField(max_length=100, blank=True, default='')
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
