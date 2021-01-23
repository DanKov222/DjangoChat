from rest_framework import serializers

from django.contrib.auth.models import User
from .models import *


class UserSerializers(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнаты чата"""
    creator = UserSerializers()
    invited = UserSerializers(many=True)

    class Meta:
        model = Room
        fields = ("id", "creator", "invited", "date")


class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializers()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация чата"""

    class Meta:
        model = Chat
        fields = ("text", "room")
