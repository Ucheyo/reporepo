"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.contrib.auth import views # built in views for login and logiut

from rest_framework.routers import DefaultRouter
from snippets.views import frontpage, forum, progress, assignments, forumDetail, createNewForum, comments
#from snippets.views import StudentViewset, ForumViewset, AssignmentsViewset
from userprofile.views import signup

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
#    path('api-auth/', include('rest_framework.urls')),
#    path('', include('snippets.urls')),
    path('', frontpage, name='frontpage'),
    path('forum/', forum, name='forum'),
    path('progress/', progress, name='progress'),
    path('assignments/', assignments, name='assignments'),
    path('forum-detail/<int:forum_id>/', forumDetail, name='forum-detail'),
    path('new-forum/', createNewForum, name='create-forum'),
    path('new-comment/forum=<int:forum_id>-comment=<int:comment_id>/',comments,name='new-comment'),
    path("upload_texts/", views.upload_texts),
    #Auth
#    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login')

]

#modified here
# router = DefaultRouter()
# router.register("student", StudentViewset, basename="student")
# router.register("forum", ForumViewset, basename="forum")
# router.register("assignments", AssignmentsViewset, basename="assignments")
# urlpatterns += router.urls
#modified here    

