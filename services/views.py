from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer

class ServiceList(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceDetail(APIView):
    def get_object(self, pk):
        try:
            service = Service.objects.get(pk=pk)
            return service
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)