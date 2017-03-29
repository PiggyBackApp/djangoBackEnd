from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from customUsers.models import CustomUser
from customUsers.serializers import CustomUserSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        c_user_id = CustomUser.objects.get(user=token.user.id).id
        return Response({'token': token.key, 'id': c_user_id})
