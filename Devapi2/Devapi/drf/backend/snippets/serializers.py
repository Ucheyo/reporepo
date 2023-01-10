from rest_framework import serializers
from .models import Snippet, Student
from django.contrib.auth.models import User
#from rest_framework.validators import UniqueValidator
from datetime import date, datetime, timedelta
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

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets', 'url')

class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
#    user_detail = serializers.HyperlinkedIdentityField( # new
#    view_name='prog-detail')

    lookup_field = "email"
    
    class Meta:
        model = Student
        fields = ('id', 'courseID', 'classesAttended', 'owner', 'email', 'church', 'post')

    def validate_email(self, value):
        query_set = Snippet.objects.filter(email__exact=value)
        if query_set.exists():
            raise serializers.ValidationError(f"{value} is already a name")
        return value


    





