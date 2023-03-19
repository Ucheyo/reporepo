from rest_framework import serializers
from .models import Snippet
from students.models import Student
from forum.models import Forum
from assignments.models import Assignment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.validators import UniqueValidator
from datetime import date, datetime, timedelta
from django.contrib.auth.password_validation import validate_password
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
#    owner = serializers.ReadOnlyField(source='owner.username')
#    user_detail = serializers.HyperlinkedIdentityField( # new
#    view_name='user-detail')



    class Meta:
        model = Snippet
        fields = ('currentClass', 'completedClasses')
#        fields = ('id', 'name', 'email','currentClass', 'completedClasses')
        
    def validate_name(self, value):
        query_set = Snippet.objects.filter(name__exact=value)
        if query_set.exists():
            raise serializers.ValidationError(f"{value} is already a name")
        return value


    def validate_email(self, value):
        query_set = Snippet.objects.filter(email__exact=value)
        if query_set.exists():
            raise serializers.ValidationError(f"{value} is already a name")
        return value


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField( # new
        many=True, view_name='snippet-detail', read_only=True) #add explicit field for 'snippets'. It will store the data objects of the model class  

    students = serializers.HyperlinkedRelatedField( # new
        many=True, view_name='student-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets', 'url', 'students')

class StudentSignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Student
        #fields = ('id', 'email', 'church', 'password')
        fields = ('id', 'name', 'email', 'church', 'password')


    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )


    def register(self, validated_data):

        user = Student.objects.create(
            name=validated_data['name'],            
            email=validated_data['email'],
            password=validated_data['password1'],
            church=validated_data['church']
        )

        
        #user.set_password(validated_data['password'])
        user.save()

        return user


class StudentSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #user_detail = serializers.HyperlinkedIdentityField( # new
    #view_name='student-detail')
    MIN_LENGTH=8
    password = serializers.CharField(
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"password must be longer than {MIN_LENGTH} characters"
        }

    )


    def validate_email(self, value):
        query_set = Student.objects.filter(email__exact=value)
        if query_set.exists():
            raise serializers.ValidationError(f"{value} is already a name")
        return value


    # def create(self, validated_data):
    #     student = Student.objects.create(
    #         name = validated_data["name"],
    #         email = validated_data["email"],
    #         church = validated_data["church"],
    #         password = validated_data["password"]
    #     )

    #     student.save()
    #     return student


    lookup_field = "email"
    
    class Meta:
        model = Student
        fields = ('id', 'name', 'email', 'church', 'password')


class ForumSerializer(serializers.ModelSerializer):

    def validate_ContentTitle(self, value):
        query_set = Forum.objects.filter(ContentTitle__exact=value)
        if query_set.exists():
            raise serializers.ValidationError(f"{value} is already a name")
        return value

    class Meta:
        model = Forum
        fields = ('id', 'ContentTitle', 'ContentBody', 'students')


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ('id', 'AssignmentTitle', 'students')





    





