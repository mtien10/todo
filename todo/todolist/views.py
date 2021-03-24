from todolist.models import Todolist
from todolist.serializers import TodolistSerializer
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    # suggest APIView

    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # suggest APIView
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer

