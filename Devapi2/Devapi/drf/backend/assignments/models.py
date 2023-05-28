from django.db import models
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Assignment(models.Model):
    AssignmentTitle = models.TextField(max_length=100, blank=True, default='')
    students = models.ManyToManyField(User)