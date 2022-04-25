from rest_framework import serializers
from .models import Customer,Invoice,Item_details


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
        model = Item_details
        fields = ('sr_no','description','rate','quantity',)
   
class invoicedetailSerializer(serializers.ModelSerializer):
    details = addinvoiceSerializer(many=True)
    class Meta:
        model = Invoice
        fields = ('customer_id','currency_id','date','paid','note','details')

    def create(self, validated_data):
        invoice_details = validated_data.pop('details')
        new_details = Invoice.objects.create(**validated_data)
        for i in invoice_details:
            Item_details.objects.create(**i,invoice_id=new_details)
            return new_details
   

      

