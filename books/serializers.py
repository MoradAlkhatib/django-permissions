from rest_framework import serializers
from .models import Post,Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name','page','description','owner']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
