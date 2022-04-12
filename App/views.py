
import imp
from rest_framework import viewsets
from .serializers import ClientsSerializer,ClientAddressSerializer
from .models import Clients
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.




class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.filter().order_by('id')
    serializer_class = ClientsSerializer

            


class ClientaddressViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.filter().order_by('id')
    serializer_class = ClientAddressSerializer
