from models import Student

def userToModel(request):
    if request.user.is_authenticated:
        Student.order = request.user