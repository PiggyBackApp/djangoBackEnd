from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from posts.models import Post
from posts.models import Request
from posts.models import Review
from posts.serializers import PostSerializer
from posts.serializers import RequestSerializer
from posts.serializers import ReviewSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RequestViewSet(viewsets.ModelViewSet):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
