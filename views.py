from django.shortcuts import render

from rest_framework import generics
from .models import Blog, Comment, Like
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer

# List Blogs
class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Blog Details
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Add Comment
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Like Blog
class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
