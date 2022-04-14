from rest_framework import serializers
from .models import *



class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name','address',)

class customersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name',)

class invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields= ('id','currency_id',)
    