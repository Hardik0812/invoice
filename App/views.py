from .serializers import ClientsSerializer,ClientAddressSerializer,ClientnameAddressSerializer
from .models import Clients
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
@api_view(['GET'])
def clientName(request,pk):
    client = Clients.objects.get(id=pk)
    serializers = ClientsSerializer(client)
    return Response(serializers.data)

@api_view(['GET'])
def clientAddress(request,pk):
    clientaddress = Clients.objects.get(id=pk)
    serializers = ClientAddressSerializer(clientaddress)
    return Response(serializers.data)

@api_view(['GET'])
def clientnameAddress(request,pk):
    clientnameaddress = Clients.objects.get(id=pk)
    serializers = ClientnameAddressSerializer(clientnameaddress)
    return Response(serializers.data)