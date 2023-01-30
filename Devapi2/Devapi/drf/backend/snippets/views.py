from ast import Pass
from typing import Generic
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new

from rest_framework import generics, permissions
from .models import Snippet
from students.models import Student
from django.contrib.auth.models import User
from .serializers import SnippetSerializer, UserSerializer, StudentSerializer, StudentSignupSerializer
from .permissions import UserIsOwner
from userprofile.forms import SignUpForm

# @api_view(['GET']) # new
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })

def frontpage(request):
    return render(request, 'frontpage.html')

def forum(request):
    students= Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'forum.html', context)

def progress(request):
    return render(request, 'progress.html')

def assignments(request):
    return render(request, 'assignments.html')

@api_view(['GET', 'POST'])
def studentSignup(request, format=None):
    if request.method =='POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            newStudent = form.save()

            login(request,newStudent)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})





class SnippetListInstance(generics.ListCreateAPIView):
    queryset= Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, UserIsOwner)    

    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)


class SnippetModify(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserInstance(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserModify(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer




class StudentListInstance(generics.ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, UserIsOwner) 
       
    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)



class StudentModify(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)