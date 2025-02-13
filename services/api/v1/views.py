from rest_framework.response import Response
from rest_framework.decorators import api_view
from services.models import Services
from rest_framework import status
from .serializer import Serviceserializer


@api_view(['GET'])
def api_services(request):
    if request.method == 'GET':
        service = Services.objects.all() 
        serialz = Serviceserializer(service,many=True)
        return Response(serialz.data,status=status.HTTP_200_OK)