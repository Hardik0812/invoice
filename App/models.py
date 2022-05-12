from django.db import models
from .function import getcurrentfinancialyear
# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=1000,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
      
    def __str__(self):
        return self.name 
              
class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True,auto_created=True)
    symbol = models.TextField(max_length=1)
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Invoice(models.Model):
    def increment_invoice_number():
        last_invoice = Invoice.objects.all().order_by('invoice_id').last()
        if not last_invoice:
            return '01' + "-" + getcurrentfinancialyear()
        invoice_no = str(last_invoice)
        invoice_str = invoice_no.split('-')[:1]
        new_invoice_int = int(invoice_str[0])
        new_invoice_str = str(new_invoice_int + 1)
        if int(new_invoice_str)<10:
            new_invoice_no = str("0" + new_invoice_str + "-" + getcurrentfinancialyear())
        else:
            new_invoice_no = str(new_invoice_str + "-" + getcurrentfinancialyear())
        return new_invoice_no

    invoice_id = models.CharField(primary_key=True,max_length=20000,default=increment_invoice_number)
    currency_id = models.ForeignKey(Currency,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.IntegerField()
    note = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.invoice_id


class Item_details(models.Model):
    invoice_id = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name="details")
    sr_no = models.IntegerField()
    description = models.TextField(max_length=1000)
    rate = models.FloatField()
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.invoice_id)[:2] + "--" + (self.description)
        
def increment_invoice_number():
        last_invoice = Invoice.objects.all().order_by('invoice_id').last()
        if not last_invoice:
            return '01' + "-" + getcurrentfinancialyear()
        invoice_no = str(last_invoice)
        invoice_str = invoice_no.split('-')[:1]
        new_invoice_int = int(invoice_str[0])
        new_invoice_str = str(new_invoice_int + 1)
        if int(new_invoice_str)<10:
            new_invoice_no = str("0" + new_invoice_str + "-" + getcurrentfinancialyear())
        else:
            new_invoice_no = str(new_invoice_str + "-" + getcurrentfinancialyear())
        return new_invoice_no