from asyncore import read
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
    class Meta:
        model = Invoice_detail
        fields = ('sr_no','description','rate','quantity',)
   
class invoicedetailSerializer(serializers.ModelSerializer):
    details = addinvoiceSerializer(many=True)
    class Meta:
        model = Invoice
        fields = ('customer_id','currency_id','date','paid','note','details')
   
    def create(self, validated_data):
        details_data = validated_data.pop('details')
        detail = Invoice.objects.create(**validated_data)
        for details_data in details_data:
            Invoice_detail.objects.create(detail=detail, **details_data)
        return detail

