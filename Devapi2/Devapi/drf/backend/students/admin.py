from django.contrib import admin
from forum.models import Forum
from assignments.models import Assignment
from students.models import Student
# Register your models here.

admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Forum)