from django.db.models import Avg
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
    reviews = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    average_rating = serializers.SerializerMethodField()
    user = UserSerializer(required=True)
    class Meta:
        fields = ('id', 'user', 'rating', 'school', 'car', 'phoneNumber', 'reviews', 'average_rating' )
        model = CustomUser

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
        if average is None:
            return 0

        return round(average*2) / 2

    def create(self, validated_data):
        # create method is overriden to create user in django users table and also make sure password is hashed
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        newUser = User.objects.create(**user_data)
        customUser = CustomUser.objects.create(user=newUser, **validated_data)
        return customUser
