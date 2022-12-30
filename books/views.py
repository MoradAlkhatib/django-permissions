from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import BookSerializer,PostSerializer
# Create your views here.
from .models import Book,Post
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

class BookListView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    # permission_classes=[IsOwnerOrReadOnly]


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[IsOwnerOrReadOnly]


class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[AllowAny]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[AllowAny]