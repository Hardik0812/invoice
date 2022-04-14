from rest_framework import serializers
from .models import *



class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id','name','address',)

class customersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id','name',)

class invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('invoice_id','currency_id',)

class addinvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_detail
        fields = ('__all__')
        #('date','currency_id','customer_id','sr_no','description','rate','quantity','paid','note',)
        