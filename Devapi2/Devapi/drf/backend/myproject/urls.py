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

from snippets.views import frontpage, forum, progress, assignments, studentSignup
from userprofile.views import signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('snippets.urls')),
    path('', frontpage, name='frontpage'),
    path('forum/', forum, name='forum'),
    path('progress/', progress, name='progress'),
    path('assignments/', assignments, name='assignments'),

    #Auth
    
    path('signup/', studentSignup, name='studentSignup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login')



    
]
