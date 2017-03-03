from posts.models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'creator','description', 'timePosted', 'postType', 'origin', 'destination', 'emptySeats', 'passengerCapacity', 'status')
