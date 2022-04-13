from rest_framework import serializers
from .models import Clients


class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('name',)

class ClientAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('address',)

class ClientnameAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('name','address')