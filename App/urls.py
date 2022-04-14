from django.urls import  path
from . import views

urlpatterns = [
path('customer/<str:pk>',views.Customer_info, name = "customer_info"),
path('customer',views.addCustomer, name = "add_customer_info"),
path('customers',views.Customers, name = "customers_name_id"),
 
]



