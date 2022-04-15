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
        fields = ('id','currency_id',)

class invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('date','id','paid','note','customer_id',)
        

class addinvoiceSerializer(serializers.ModelSerializer):
   #invoice_set = invoiceSerializer(many=True)
    class Meta:
        model = Invoice_detail
        fields = ('sr_no','description','rate','quantity',)


    # def create(self, validated_data):
    #     invoice_details_data = validated_data.pop('invoice_set')
    #     invoice= Invoice.objects.create(**validated_data)
    #     for invoice_detail_data in invoice_details_data :
    #         Invoice.objects.create(invoice=invoice, **invoice_detail_data )
    #     return invoice 


