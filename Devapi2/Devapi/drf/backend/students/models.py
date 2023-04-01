from django.db import models
from datetime import date, datetime, time
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Why did i do a snippet model and student model? ans: separate student model and teacher model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    name = models.CharField(max_length=100, null=True, blank=True, default='')
#    email = models.EmailField(null=True, blank=True)
    church = models.CharField(max_length=100, null=True, blank=True, default='')
#    password = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()