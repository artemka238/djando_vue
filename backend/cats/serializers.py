from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CatsSerializers(serializers.ModelSerializer):
    user = UserSerializers(required = False)
    class Meta:
        model = AboutCats
        fields = ["id",'name', 'breed', 'age', 'image', 'cost', 'user']

class CatsAPISerializers(serializers.ModelSerializer):
    image_url = serializers.CharField(source = 'image.url',default = '')
    class Meta:
        model = AboutCats
        fields = ["id",'name', 'breed', 'age', 'image_url']

class GetUserInfoSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Balance
        fields = ["user", "balance"]

class CatHistorySerializers(serializers.ModelSerializer):
    buyer = UserSerializers()
    seller = UserSerializers()
    cat = CatsSerializers()

    class Meta:
        model = CatHistory
        fields = ["buyer", 'seller', "cost", 'cat', 'date']