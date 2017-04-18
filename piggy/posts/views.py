from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins
from posts.models import Post
from posts.models import Request
from posts.models import Review
from posts.models import ConfirmedRequest
from customUsers.models import CustomUser
from posts.serializers import PostSerializer
from posts.serializers import RequestSerializer
from posts.serializers import ConfirmedRequestSerializer
from posts.serializers import ReviewSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListCreateOriginPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.queryset.filter(origin=self.kwargs.get('origin_query').replace('_',' '))


class ListCreateDestinationPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.queryset.filter(destination=self.kwargs.get('destination_query').replace('_',' '))


class ListCreateBothPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.queryset.filter(origin=self.kwargs.get('origin_query').replace('_',' ')
            ).filter(destination=self.kwargs.get('destination_query').replace('_',' '))

class RequestViewSet(viewsets.ModelViewSet):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    def get_queryset(self):
        user = self.request.user.id
        c_user_id = CustomUser.objects.get(user=user).id
        dr_req = Request.objects.filter(driver=c_user_id)
        pa_req = Request.objects.filter(passenger=c_user_id)
        return dr_req | pa_req

class ListCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(reviewee=self.kwargs.get('reviewee'))

    def perform_create(self, serializer):
        cUser = get_object_or_404(
            models.CustomUser, pk=self.kwargs.get('reviewee'))
        serializer.save(CustomUser=cUser)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            reviewee=self.kwargs.get('reviewee'),
            pk=self.kwargs.get('pk')
        )


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ConfirmedRequestViewSet(viewsets.ModelViewSet):
    queryset = ConfirmedRequest.objects.all()
    serializer_class = ConfirmedRequestSerializer
