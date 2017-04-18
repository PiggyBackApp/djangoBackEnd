from posts.models import Post
from posts.models import Request
from posts.models import Review
from customUsers.models import CustomUser
from rest_framework import serializers
from django.db.models import Avg, Max, Min, Sum

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    seats_taken = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    related_posts = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'creator',
            'username',
            'description',
            'timePosted',
            'postType',
            'origin',
            'destination',
            'totalPassengers',
            'seats_taken',
            'passengerCapacity',
            'status',
            'travelDate',
            'related_posts',
        )
    def get_status(self, obj):
        taken = obj.related_posts.aggregate(Sum('totalPassengers')).get('totalPassengers__sum')
        if taken is None:
            return 'A'

        if taken >= obj.passengerCapacity:
            return 'F'
            
        return 'A'

    def get_seats_taken(self, obj):
        taken = obj.related_posts.aggregate(Sum('totalPassengers')).get('totalPassengers__sum')
        if taken is None:
            return 0
        return taken

    def get_username(self, obj):
        # user = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
        user = CustomUser.objects.get(id=obj.creator.id)
        # print user.user.username
        # return user.username
        return user.user.username

class RequestSerializer(serializers.ModelSerializer):
    driver_username = serializers.SerializerMethodField()
    passenger_username = serializers.SerializerMethodField()
    origin = serializers.SerializerMethodField()
    destination = serializers.SerializerMethodField()
    travelDate = serializers.SerializerMethodField()
    class Meta:
        model = Request
        fields = (
            'id',
            'driver',
            'passenger',
            'post',
            'driver_username',
            'passenger_username',
            'origin',
            'destination',
            'travelDate'
        )

    def get_driver_username(self, obj):
        user = CustomUser.objects.get(id=obj.driver.id)
        return user.user.username

    def get_passenger_username(self, obj):
        user = CustomUser.objects.get(id=obj.passenger.id)
        return user.user.username

    def get_origin(self, obj):
        post = Post.objects.get(id=obj.post.id)
        return post.origin

    def get_destination(self, obj):
        post = Post.objects.get(id=obj.post.id)
        return post.destination

    def get_travelDate(self, obj):
        post = Post.objects.get(id=obj.post.id)
        return post.travelDate


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'reviewee',
            'reviewer',
            'request',
            'created_at',
            'rating',
            'comment'
        )
