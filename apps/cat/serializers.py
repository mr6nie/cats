from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Cat

class CatsSerializer(ModelSerializer):
    brief_description = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField()

    class Meta:
        model = Cat
        fields = [
            'uuid',
            "title",
            "image",
            "brief_description",
            "added",
            "price"
        ]

    def get_brief_description(self, obj):
        return obj.description[:100] + "..."


class SingleCatSerializer(ModelSerializer):
    ownerinfo = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField()

    class Meta:
        model = Cat
        fields = [
            'uuid',
            "title",
            "image",
            "description",
            "ownerinfo",
            "location",
            "contact_number",
            "birth_date",
            "added", 
            "breed",
            "price"
        ]

    def get_ownerinfo(self, obj):
        userinfo = {
            'id': obj.owner.id,
            'username': obj.owner.username
        }
        return userinfo

    
class CreateCatSerializer(ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Cat
        
        fields = [
            "title",
            "image",
            "description",
            "location",
            "contact_number",
            "owner",
            "breed",
            "birth_date",
            "price"
        ]