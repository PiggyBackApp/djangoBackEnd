from customUsers.models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        # TODO: HASH THE PASSWORD
    # def create(self, validated_data):
    #     user = User(
    #         email=validated_data['email'],
    #         username=validated_data['username']
    #     )
    #     user.set_password(make_password(validated_data['password']))
    #     user.save()
    #     return user

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True);
    class Meta:
        model = CustomUser
        fields = ('user', 'rating', 'school', 'car', 'phoneNumber')
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        newUser = User.objects.create(**user_data)
        customUser = CustomUser.objects.create(user=newUser, **validated_data)
        return customUser
