from rest_framework import serializers
from .models import Customer,Currency



class customerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name','address',)

class customersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name',)