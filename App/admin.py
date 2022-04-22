from django.contrib import admin
from .models import  Currency, Customer,Invoice,Item_details
# Register your models here.

admin.site.register(Customer)
admin.site.register(Currency)
admin.site.register(Invoice)
admin.site.register(Item_details)