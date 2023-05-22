from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RoomSerializer(serializers.ModelSerializer):
    creator = UserSerializers()
    invited = UserSerializers(many = True)
    class Meta:
        model = Room
        fields = ['id', 'creator', 'invited', 'date']

class ChatSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Chat
        fields = ['user', 'text', 'date']

class ChatPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['room', 'text']
