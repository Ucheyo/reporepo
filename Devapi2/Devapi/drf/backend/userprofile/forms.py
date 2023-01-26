from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from students.models import Student
from snippets.serializers import StudentSerializer
from django.forms import ModelForm

class StudentForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'email', 'church', 'password']
form = StudentForm



# class SignUpForm(UserCreationForm):
#     firstName = forms.CharField(max_length=50, required=True)
#     lastName = forms.CharField(max_length=50, required=True)
#     email = forms.EmailField(max_length=255, required=True)


# class Meta:
#     model = User
#     fields = ['username', 'firstName', 'lastName', 'email', 'password1', 'password2']