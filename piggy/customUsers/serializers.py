from customUsers.models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True);
    class Meta:
        model = CustomUser
        fields = ('id', 'user', 'rating', 'school', 'car', 'phoneNumber')
    def create(self, validated_data):
        # create method is overriden to create user in django users table and also make sure password is hashed
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        newUser = User.objects.create(**user_data)
        customUser = CustomUser.objects.create(user=newUser, **validated_data)
        return customUser
