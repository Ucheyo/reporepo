from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.decorators import api_view # new
from students.models import Student
from .forms import SignUpForm


def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            newStudent = form.save()
            newStudent.refresh_from_db()
            newStudent.student.church = form.cleaned_data.get('church')
            newStudent.save()
            login(request,newStudent)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})