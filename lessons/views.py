from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Lesson
from .serializers import LessonSerializer
from drf_api.permissions import IsAdminOrReadOnly

## LESSON LIST VIEWS HERE...

class LessonList(APIView):

## Get method: fetch's all service objects, serializes and returns in Response.

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

## LESSON DETAIL VIEWS HERE...

class LessonDetail(APIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadOnly]
    
## View handling request made for service that doesn't exist, 
# and check_object_permissions. 

    def get_object(self, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            self.check_object_permissions(self.request, lesson)
            return lesson
        except Lesson.DoesNotExist:
            raise Http404

## Get method fetching lesson detail using pk.

    def get(self, request, pk):
        lesson = self.get_object(pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

## Put Method: Updating data. 
# Fetches lesson, calls serializer and saves if serializer is valid.
## Else, 400_BAD_REQUEST

    def put(self, request, pk):
        lesson = self.get_object(pk)
        serializer = LessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)