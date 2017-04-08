from posts.models import Post
from posts.models import Request
from posts.models import Review
from customUsers.models import CustomUser
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
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
            'emptySeats',
            'passengerCapacity',
            'status',
            'travelDate'
        )
    def get_username(self, obj):
        # user = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
        user = CustomUser.objects.get(id=obj.creator.id)
        # print user.user.username
        # return user.username
        return user.user.username

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = (
            'id',
            'driver',
            'passenger',
            'post'
        )

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
