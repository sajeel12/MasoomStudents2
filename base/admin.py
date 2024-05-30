from django.contrib import admin

# Register your models here.

from .models import Room, Message, Topic, User, ApiKeysForBots, ApiUser

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
admin.site.register(ApiKeysForBots)
admin.site.register(ApiUser)

