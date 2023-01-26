from ast import Pass
from typing import Generic
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new

from rest_framework import generics, permissions
from .models import Snippet
from students.models import Student
from django.contrib.auth.models import User
from .serializers import SnippetSerializer, UserSerializer, StudentSerializer
from .permissions import UserIsOwner

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
def studentSignup(request, *args, **kwargs):
    if request.method =='POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            church = serializer.validated_data.get('church')

            serializer.save(email=email, password=password, church=church)

            user = authenticate(request, name=name, email=email, password=password)

            #if user is not None:
            login(request, user)
            return render(request, 'frontpage.html')

            #owner = serializer.PrimaryKeyRelatedField(
            #many=False,
            #queryset=Student.objects.all()
            #)
            
            #redirect('frontpage')
    
    return render(request, 'signup.html')





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