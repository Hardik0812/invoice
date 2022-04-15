from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

# Get customer information by ID
@api_view(['GET'])
def customer_info(request,pk):
    try:
        customer = Customer.objects.get(customer_id=pk)
    except Customer.DoesNotExist:
        customer = None
    serializers = customerSerializer(customer)
    return Response(serializers.data)

# Add customer information
@api_view(['POST'])
def addcustomer(request):
    serializers = customerSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Get All customers 
@api_view(['GET'])
def customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializers = customersSerializer(customers, many=True)
    return Response(serializers.data)

# Get Invoice information
@api_view(['GET'])
def invoice_info(request):
    if request.method == 'GET':
        invoice = Invoice.objects.all()
        serializers = invoiceSerializer(invoice, many=True,context={'request': request})
    return Response(serializers.data)

# Add invoice information
@api_view(['POST'])
def add_invoice(request):
    serializers = addinvoiceSerializer(data=request.data,many=True)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)




def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
         return '01-22/23'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('01-22/23')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = '01-22/23' + str(new_invoice_int)
    return new_invoice_no
   
# # @api_view(['GET'])
# # def clientAddress(request,pk):
# #     try:
# #         clientaddress = Clients.objects.get(id=pk)
# #     except Clients.DoesNotExist:
# #         clientaddress = None
# #     serializers = ClientAddressSerializer(clientaddress)
# #     return Response(serializers.data)

# # @api_view(['GET'])
# # def getclientaddress(request):
# #      try:
# #          paramName = request.GET.get('name')
# #          clientnameaddress = Clients.objects.get(name=paramName)
# #      except Clients.DoesNotExist:
# #         return Response("Name Not Found", status=status.HTTP_400_BAD_REQUEST)    
# #      serializers = ClientAddressSerializer(clientnameaddress)
# #      return Response(serializers.data, status=status.HTTP_200_OK)

# # @api_view(['POST'])
# # def addClient(request):
# #     serializers = ClientnameAddressSerializer(data=request.data)
# #     if serializers.is_valid():
# #         serializers.save()
# #         return Response(serializers.data, status=status.HTTP_201_CREATED)
# #     else:
# #         return Response("please enter name and address", status=status.HTTP_400_BAD_REQUEST) 

# # @api_view(['GET'])
# # def getCurrency(request,pk):
# #     try:
# #         currency = Currency.objects.get(id=pk)
# #     except Currency.DoesNotExist:
# #         return Response("Currency Not Found", status=status.HTTP_400_BAD_REQUEST)    
# #     serializers = currencySerializer(currency)
# #     return Response(serializers.data, status=status.HTTP_200_OK)
    