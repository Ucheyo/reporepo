from django.db import models
from datetime import date, datetime, time
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

CLASS_ONE = "C1"
CLASS_TWO = "C2"
CLASS_THREE = "C3"
CLASS_FOUR = "C4"
CLASS_FIVE = "C5"
CLASS_SIX = "C6"
CLASS_SEVEN = "C7"

FOUNDATION_CLASS_CHOICES = [
(CLASS_ONE, "Class one - 'put subject name here' "),
(CLASS_TWO, "Class two - 'put subject name here'"),
(CLASS_THREE, "Class three - 'put subject name here'"),
(CLASS_FOUR, "Class four - 'put subject name here'"),
(CLASS_FIVE, "Class five - 'put subject name here'"),
(CLASS_SIX, "Class six - 'put subject name here'"),
(CLASS_SEVEN, "Class seven - 'put subject name here'"),
]
#Why did i do a snippet model and student model? ans: separate student model and teacher model
class Student(models.Model):
    #user is the link in the database to the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    name = models.CharField(max_length=100, null=True, blank=True, default='')
#    email = models.EmailField(null=True, blank=True)
    church = models.CharField(max_length=100, null=True, blank=True, default='')
#    password = models.CharField(max_length=100, blank=True, default='')



    foundation_class_choices = models.CharField(
        max_length=2,
        choices=FOUNDATION_CLASS_CHOICES,
        default=CLASS_ONE,
    )

    # def __str__():
    #     return User.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()