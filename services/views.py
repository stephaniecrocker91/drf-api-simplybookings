from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer
from drf_api.permissions import IsAdminOrReadOnly

class ServiceList(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceDetail(APIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_object(self, pk):
        try:
            service = Service.objects.get(pk=pk)
            self.check_object_permissions(self.request, service)
            return service
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)