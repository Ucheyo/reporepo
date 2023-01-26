from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import StudentForm

def signup(request):
    if request.method =='POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            newStudent = form.save()

            login(request,newStudent)

            return redirect('frontpage')
    else:
        form = StudentForm()
    
    return render(request, 'signup.html', {'form': form})