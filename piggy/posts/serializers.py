from posts.models import Post
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
