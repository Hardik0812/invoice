from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date
# Create your views here.

# Get customer information by ID
@api_view(['GET'])
def customer_info(request,pk):
    try:
        customer = Customer.objects.get(customer_id=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializers = customerSerializer(customer)
    return Response(serializers.data,status=status.HTTP_200_OK)

# Get All customers 
@api_view(['GET'])
def customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializers = customersSerializer(customers, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


# Get Invoice information
@api_view(['GET'])
def invoice_info(request):
    if request.method == 'GET':
        invoice = Invoice.objects.all().order_by('invoice_id')
        serializers = invoiceSerializer(invoice, many=True,context={'request': request})
    return Response(serializers.data,status=status.HTTP_200_OK)



# Add customer information
@api_view(['POST'])
def addcustomer(request):
    serializers = customerSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Add invoice information
@api_view(['POST'])
def add_invoice(request):
    serializers = invoicedetailSerializer(data=request.data,many = True)                      
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
   
    if serializers.is_valid() == False:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializers.is_valid()
        serializers.save()

    #serializers.save()
    #serializers = addinvoiceSerializer(items,many=True,instance=items)
        return Response(serializers.data,status=status.HTTP_202_ACCEPTED)


