from django.db import models
from django.contrib.auth.models import User
from forum.models import Forum
# Create your models here.

class Comment(models.Model):
    forumID= models.ForeignKey(Forum, on_delete=models.CASCADE, blank=True)
    message = models.TextField(max_length=100, blank=True, default='')
    commentID = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    students = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
# id
# forumid : connect to forum id
# message
# picture
# commentid : connecting comment id
# userid :connect to the user