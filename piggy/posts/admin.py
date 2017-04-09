from django.contrib import admin

# Register your models here.
from posts.models import Post
from posts.models import Request
from posts.models import Review
admin.site.register(Post)
admin.site.register(Request)
admin.site.register(Review)
