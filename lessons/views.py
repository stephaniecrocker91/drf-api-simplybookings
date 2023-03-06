from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Lesson
from .serializers import LessonSerializer

## LESSON LIST VIEWS HERE...

class LessonList(APIView):

## Get method: fetch's all service objects, serializes and returns in Response.

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)