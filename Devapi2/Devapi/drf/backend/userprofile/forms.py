from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from students.models import Student
from students.models import Student
from snippets.serializers import StudentSerializer
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    church = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)

   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']