from django.db import models

# Create your models here.
from students.models import Student

# Create your models here.
class Assignment(models.Model):
    AssignmentTitle = models.TextField(max_length=100, blank=True, default='')
    students = models.ManyToManyField(Student)