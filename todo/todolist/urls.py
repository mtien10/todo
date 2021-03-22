from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todolist import views

urlpatterns = [
    path('todolist/', views.TodolistList.as_view()),
    path('todolist/<int:pk>/', views.TodolistDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)