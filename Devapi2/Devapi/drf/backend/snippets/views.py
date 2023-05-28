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
from assignments.models import Assignment
from forum.models import Forum
from comments.models import Comment
from django.contrib.auth.models import User
from .serializers import StudentSerializer, ForumSerializer, AssignmentSerializer
from .permissions import UserIsOwner
from userprofile.forms import classChoices
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from forum.forms import ForumCreationForm
from comments.form import CommentCreationForm
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




# @api_view(['GET','POST']) # new
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         #'snippets': reverse('snippet-list', request=request, format=format)
#     })

def frontpage(request):

    if request.user.is_authenticated:
        context = {}

        students= Student.objects.all()
        id = request.user.id
        myStudent = Student.objects.get(id=id)    
        context['students']= students
        context['currentStudent']= myStudent         
        return render(request, 'frontpage.html', context)
    else:
        return render(request, 'frontpage.html')


def forum(request):
    id = request.user.id
    myStudent = Student.objects.get(id=id)
    forums = Forum.objects.all()
    comments = Comment.objects.all()
    context = {
         'currentStudent': myStudent,
         'forums': forums,
         'comments': comments
    }

    return render(request, 'forum.html', context)


def forumDetail(request, forum_id):
    context = {}
    forum = Forum.objects.get(id=forum_id)
    #forum = Forum.students.get_object
    myComments = Comment.objects.filter(forumID=forum_id)
    commentIdListIntegers  = []  
    testInt = [1,2,3,4,5]
    # for i in range(comment_id_list):
    #     commentIdListIntegers[i] = int(comment_id_list[i])

    # for i in range(comment_id_list):    
    #     comments = Comment.objects.get(forumID=forum, id=commentIdListIntegers[i])    
    context = {
         'forum': forum,
         'comment_list': myComments,
         'tests': testInt
    }

    

    return render(request, 'forum-detail.html', context)




@api_view(['GET','POST']) # new
def progress(request):
    current_user = request.user
    id = current_user.id
    myStudent = Student.objects.get(id=id)
    students= Student.objects.all()
    context = {}
    
    if request.method =='POST':

        form = classChoices(request.POST, instance=myStudent)
        if form.is_valid():

            form.save()
            context['form'] = form

                
            return redirect('frontpage')

        
                
    else:    
        form = classChoices()
        # context = {
        #     'students': students
        # }
        context['students'] = students
        context['currentStudent'] = myStudent
        context['form'] = form
        
        
    return render(request, 'progress.html',context)


def assignments(request):
    students= Student.objects.all()
    id = request.user.id
    myStudent = Student.objects.get(id=id)    
    context = {
         'students': students,
         'currentStudent': myStudent         
    }

    return render(request, 'assignments.html', context)

@api_view(['GET','POST']) # new
def createNewForum(request):
    context = {}
    id = request.user.id
    myStudent = Student.objects.get(id=id)   
    if request.method =='POST':
        form = ForumCreationForm(request.POST )

        if form.is_valid():
        
            #myForm = form.save(commit=False)
            myForm = form.save(commit=False)
            myForm.students = myStudent.user
            myForm.save()
            context['form'] = myForm
        return redirect('forum')
    else:
        form = ForumCreationForm()
        context['form'] = form 
    return render(request, 'create-forum.html', context)


@api_view(['GET','POST']) # new
def comments(request, forum_id, comment_id):
    context = {}
    id = request.user.id
    forum = Forum.objects.get(id=forum_id)
    myStudent = Student.objects.get(id=id)
    context= {'forum':forum,
                'student':myStudent
                }
   
    if request.method =='POST':
        form = CommentCreationForm(request.POST )

        if form.is_valid():
        
            myForm = form.save(commit=False)
            myForm.students = myStudent.user
            myForm.forumID = forum
            myForm.commentID = Comment.objects.get(id=comment_id)
            myForm.save()
        return redirect('forum')
    else:
        form = CommentCreationForm()
        context['form'] = form 
    
    return render(request, 'comments.html', {'form': form})
# def studentSignup(request, format=None):
    
#     if request.method =='POST':

#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.student.church = form.cleaned_data.get('church')
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')

#             username = authenticate(username=username, password=password)
#             login(request,user)

#             return redirect('frontpage')

            
#     else:
#         form = SignUpForm()
    
#     return render(request, 'signup.html', {'form': form})



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