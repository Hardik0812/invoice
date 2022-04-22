from rest_framework import serializers
from .models import Customer,Invoice,Item_details,Currency


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
        fields = ('invoice_id','date','customer_id','currency_id','paid','note',)







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
        details_data = validated_data.pop('details')
        invoice = Item_details.objects.create(**validated_data)
        for i in details_data:

        return detail_data

https://medium.com/@rushic24/creating-nested-serializers-in-django-rest-framework-5110c6674fba