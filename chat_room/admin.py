from django.contrib import admin
from .models import *


class RoomAdmin(admin.ModelAdmin):
    """Комната чата"""
    list_display = ("creator", "invited_user", "date")

    def invited_user(self, obj):
        return '\n'.join(user.username for user in obj.invited.all())


class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date")


admin.site.register(Room, RoomAdmin)
admin.site.register(Chat, ChatAdmin)
