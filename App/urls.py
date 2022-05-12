from django.urls import  path
from .views import *
urlpatterns = [ 

# path('customer/<str:pk>',views.customer_info, name = "customer_info"),
#path('customer',views.addcustomer, name = "add_customer_info"),
#path('customers',views.customers, name = "customers_name_id"),
#path('info',views.invoice_info, name = "invoice_info"),
#path('invoice',views.add_invoice, name = "add_invoice_details"),

path('info',invoice_info.as_view()),
path('customers', customers.as_view()),
path('customer',addcustomer.as_view()),
path('invoice',add_invoice.as_view()),
]

