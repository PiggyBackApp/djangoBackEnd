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
    travelDate = models.DateTimeField()

    def __str__(self):
        return CustomUser.objects.get(id=self.creator.id).user.username + ": " + self.origin + " -> " + self.destination

class Request(models.Model):
    # TODO: Find a way to check that duplicate requests were not made
    driver = models.ForeignKey('customUsers.CustomUser', related_name='driver')
    passenger = models.ForeignKey('customUsers.CustomUser', related_name='passenger')
    post = models.ForeignKey(Post, related_name='post')
    passengers = models.IntegerField(blank=True, null=True)
    accepted = models.NullBooleanField(default=None)
    # driver_post = models.ForeignKey('posts.Post', related_name='related_requests', blank=True, null=True)


class Review(models.Model):
    reviewee = models.ForeignKey('customUsers.CustomUser', related_name='reviews')
    reviewer = models.ForeignKey('customUsers.CustomUser')
    request = models.OneToOneField(Request, related_name='requests')
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, default='')

class ConfirmedRequest(models.Model):
    post = models.ForeignKey('posts.Post', related_name='confirmed_requests', blank=True, null=True)
    request = models.ForeignKey('posts.Request')
    passengers = models.IntegerField(blank=True, null=True)
