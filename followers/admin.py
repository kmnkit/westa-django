from django.contrib import admin
from .models import FollowedList, FollowerList

admin.site.register(FollowerList)
admin.site.register(FollowedList)
