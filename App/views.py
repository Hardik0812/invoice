from .serializers import *
from .models import Clients
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
@api_view(['GET'])
def clientName(request,pk):
    try:
        client = Clients.objects.get(id=pk)
    except Clients.DoesNotExist:
        client = None
    serializers = ClientsSerializer(client)
    return Response(serializers.data)

@api_view(['GET'])
def clientAddress(request,pk):
    try:
        clientaddress = Clients.objects.get(id=pk)
    except Clients.DoesNotExist:
        clientaddress = None
    serializers = ClientAddressSerializer(clientaddress)
    return Response(serializers.data)

@api_view(['GET'])
def clientnameAddress(request,pk):
    try:
        clientnameaddress = Clients.objects.get(id=pk)
    except Clients.DoesNotExist:
        clientnameaddress = None
    serializers = ClientnameAddressSerializer(clientnameaddress)
    return Response(serializers.data)