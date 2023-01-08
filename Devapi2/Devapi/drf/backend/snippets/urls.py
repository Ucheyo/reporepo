# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetListInstance.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetModify.as_view(), name='snippet-detail'),
    path('users/', views.UserInstance.as_view(), name='user-list'), # new
    path('users/<int:pk>/', views.UserModify.as_view(), name='user-detail'), # new   
    path('student/', views.StudentListInstance.as_view()),
    path('student/<int:pk>/', views.StudentModify.as_view()), # new   

 
#    path('', views.api_root),    
]

