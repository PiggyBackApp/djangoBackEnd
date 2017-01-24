from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from customUsers.models import CustomUser
from customUsers.serializers import CustomUserSerializer

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
