from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=1000,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
      
    def __str__(self):
        return self.name 
              
class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    symbol = models.TextField(max_length=1)
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_id = models.CharField(primary_key=True,max_length=1000)
    date = models.DateField()
    currency_id = models.ForeignKey(Currency,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    paid = models.IntegerField()
    note = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    

class Invoice_detail(models.Model):
    invoice_detail_id = models.AutoField(primary_key=True)
    sr_no = models.IntegerField()
    description = models.TextField(max_length=1000)
    rate = models.FloatField()
    quantity = models.IntegerField()
    invoice_id = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

