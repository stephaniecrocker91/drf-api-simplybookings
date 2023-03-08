from rest_framework import serializers
from .models import Role

class RoleSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Role
        fields = [
            'id',
            'owner',
            'user',
            'teacher',
            'admin',
            ]
