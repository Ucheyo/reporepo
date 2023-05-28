from django.db import models
import magic
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
ext_validator = FileExtensionValidator(
    accept=['application/msword', 'image/jpeg', 'image/png', 'text/plain', 'application/pdf'],
)

def validateFile(file):
    type = magic.from_file(file)

    if type == "application/msword":
        pass
    elif type == "application/text":
        pass
    else:
        raise ValidationError(
            ("%(file) This file type is not allowed")
        )


# Create your models here.
class Submission(models.Model):
    submissionUpload = models.FileField(upload_to="uploads/%Y/%m/%d/", validators=[validateFile])