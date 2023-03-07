from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role
from .serializers import RoleSerializer

## ROLE LIST VIEWS HERE...

class RoleList(APIView):

## Get method: fetch's all role objects, serializes and returns in Response.

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)