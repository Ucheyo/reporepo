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
from rest_framework import status
from rest_framework import generics, permissions
from .models import Snippet
from students.models import Student
from forum.models import Forum
from assignments.models import Assignment
from django.contrib.auth.models import User
from .serializers import StudentSerializer, ForumSerializer, AssignmentSerializer
from .permissions import UserIsOwner
from userprofile.forms import SignUpForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

#class StudentViewset(viewsets.ModelViewSet):

#modified here
#     permission_classes = (IsAuthenticated,)
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()

# class ForumViewset(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ForumSerializer
#     queryset = Forum.objects.all()


# class AssignmentsViewset(viewsets.ModelViewSet):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = AssignmentSerializer
#     queryset = Assignment.objects.all()    
#modified herre




@api_view(['GET','POST']) # new
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

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

def studentSignup(request, format=None):
    
    if request.method =='POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.student.church = form.cleaned_data.get('church')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            username = authenticate(username=username, password=password)
            login(request,user)

            return redirect('frontpage')

            
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})



# @api_view(['GET', 'POST'])
# def studentSignup(request, format=None):

#     if request.method =='GET':
#         return render(request, 'signup.html')

#     else:
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = serializer.validated_data['student']
#             return redirect('frontpage', user)
#         return Response(status=status.HTTP_400_BAD_REQUEST)






#@api_view(['GET', 'POST'])



# class StudentSignUpClass(APIView):

#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'signup.html'

    # def get(self, request, pk):
    #     pk = self.kwargs.get('pk')
    #     student = get_object_or_404(Student, pk=pk)
    #     serializer = StudentSerializer(student)
    #     return Response({'serializer': serializer, 'student': student})


    # def get(self, request, *args, **kwargs):
        # serializer = StudentSerializer()
        # return Response({'serializer': serializer})

        
    # def get(self, request, *args, **kwargs):
    #     # serializer = StudentSerializer()
    #     # return Response({'serializer': serializer})        
    #     pk = self.kwargs.get('pk')
    #     student = get_object_or_404(Student, pk=pk)
    #     serializer = StudentSerializer(student)
    #     return Response({'serializer': serializer, 'student': student})

    # def post(self, request, pk):
    #     student = get_object_or_404(Student, pk=pk)
    #     serializer = StudentSerializer(student, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'student': student})
    #     serializer.save()
    #     login(request, student)
    #     return redirect('frontpage')



# class SnippetListInstance(generics.ListCreateAPIView):
#     queryset= Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, UserIsOwner)    

#     def perform_create(self, serializer): # new
#         serializer.save(owner=self.request.user)


# class SnippetModify(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class UserInstance(generics.ListAPIView): # new
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserModify(generics.RetrieveAPIView): # new
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




# class StudentListInstance(generics.ListCreateAPIView):
#     queryset= Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, UserIsOwner) 
       
#     def perform_create(self, serializer): # new
#         serializer.save(owner=self.request.user)



# class StudentModify(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)