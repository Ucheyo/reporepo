from rest_framework import serializers
from .models import Snippet
from students.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.validators import UniqueValidator
from datetime import date, datetime, timedelta
from django.contrib.auth.password_validation import validate_password
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    user_detail = serializers.HyperlinkedIdentityField( # new
    view_name='user-detail')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'name', 'email',
                  'church', 'owner', 'user_detail', 'url', 'nextClass', 'nextClassTime', 'courseID')
        
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
            username=validated_data['username'],
            name=validated_data['name'],            
            email=validated_data['email'],
            password=validated_data['password'],
            church=validated_data['church']
        )

        
        #user.set_password(validated_data['password'])
        user.save()

        return user


class StudentSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #user_detail = serializers.HyperlinkedIdentityField( # new
    #view_name='student-detail')

    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        password = attrs.get('password')
        church = attrs.get('church')

        # Take username and password from request

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'

    lookup_field = "email"
    
    class Meta:
        model = Student
        #fields = ('id', 'email', 'church', 'password')
        fields = ('id', 'name', 'email', 'church', 'password')





    





