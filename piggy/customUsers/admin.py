from django.contrib import admin

# Register your models here.
from customUsers.models import CustomUser
admin.site.register(CustomUser)
