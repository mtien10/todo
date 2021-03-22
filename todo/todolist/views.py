from todolist.models import Todolist
from todolist.serializers import TodolistSerializer
from rest_framework import generics


class TodolistList(generics.ListCreateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer


class TodolistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer