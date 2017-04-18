from __future__ import unicode_literals

from django.db import models
from customUsers.models import CustomUser

# Create your models here.
class Post(models.Model):
    postTypes = (
        ('DR', 'driver'),
        ('PA', 'passenger')
    )
    statuses = (
        ('F', 'Full'),
        ('A', 'Available')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    timePosted = models.DateTimeField(auto_now_add=True)
    postType = models.CharField(max_length=20,choices=postTypes)
    creator = models.ForeignKey('customUsers.CustomUser')
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    totalPassengers = models.IntegerField(blank=True, null=True)
    passengerCapacity = models.IntegerField(blank=True, null=True)
    # status = models.CharField(max_length=20,choices=statuses, blank=True)
    travelDate = models.DateTimeField()
    parent_post = models.ForeignKey('posts.Post', related_name='related_posts', blank=True, null=True)

    def __str__(self):
        return CustomUser.objects.get(id=self.creator.id).user.username + ": " + self.origin + " -> " + self.destination

class Request(models.Model):
    # TODO: Find a way to check that duplicate requests were not made
    driver = models.ForeignKey('customUsers.CustomUser', related_name='driver')
    passenger = models.ForeignKey('customUsers.CustomUser', related_name='passenger')
    post = models.ForeignKey(Post, related_name='post')

class Review(models.Model):
    reviewee = models.ForeignKey('customUsers.CustomUser', related_name='reviews')
    reviewer = models.ForeignKey('customUsers.CustomUser')
    request = models.OneToOneField(Request, related_name='requests')
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, default='')
