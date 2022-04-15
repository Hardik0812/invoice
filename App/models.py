from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=1000,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
      
    def __str__(self):
        return self.name 
              
class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.TextField(max_length=1)
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Invoice(models.Model):
    id = models.CharField(primary_key=True,max_length=1000)
    date = models.DateField()
    currency_id = models.ForeignKey(Currency,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    paid = models.IntegerField()
    note = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.id

class Invoice_detail(models.Model):
    id = models.CharField(primary_key=True,max_length=1000)
    sr_no = models.IntegerField()
    description = models.TextField(max_length=1000)
    rate = models.FloatField()
    quantity = models.IntegerField()
    invoice_id = models.ManyToManyField(Invoice)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

