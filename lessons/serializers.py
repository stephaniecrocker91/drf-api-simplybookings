from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = [
            'id',
            'lesson',
            'service',
            'image',
            'description',
            'teacher',
            'location',
            'starts_at',
            'ends_at',
            'created_at',
        ]