from django.forms import ModelForm
from forum.models import Forum
class ForumCreationForm(ModelForm):
    class Meta:
        model = Forum
        fields = ["ContentTitle", "ContentBody"]