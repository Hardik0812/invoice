from doctest import debug_script
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
        fields = ('id','date','customer_id','currency_id','paid','note',)
        
class addinvoiceSerializer(serializers.ModelSerializer):
    items = invoiceSerializer(many=True)
    class Meta:
        model = Invoice_detail
        fields = ('sr_no','description','rate','quantity','items',)



