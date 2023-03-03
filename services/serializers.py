from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    service = serializers.ReadOnlyField()

    class Meta:
        model = Service
        fields = [
            'id',
            'service',
            'image',
            'content'
        ]