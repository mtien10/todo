from rest_framework import serializers
from .models import Post


class TodolistSerializer(serializers.ModelSerializer):
    test = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['todo', 'complete', 'test']


    def get_test(self, obj):
        return obj.todo
