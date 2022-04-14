from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view(['GET'])
def customer_info(request,pk):
    try:
        customer = Customer.objects.get(customer_id=pk)
    except Customer.DoesNotExist:
        customer = None
    serializers = customerSerializer(customer)
    return Response(serializers.data)

@api_view(['POST'])
def addcustomer(request):
    serializers = customerSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response("please enter {name} and {address}", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializers = customersSerializer(customers, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def invoice_info(request):
    if request.method == 'GET':
        invoice = Invoice.objects.all()
        serializers = invoiceSerializer(invoice, many=True,context={'request': request})
    return Response(serializers.data)

@api_view(['POST'])
def add_invoice(request):
    serializers = addinvoiceSerializer(data=request.data,many=True)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response("please enter all values", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def add_invoice_get(request):
    if request.method == 'GET':
        invoice = Invoice_detail.objects.all()
        serializers = addinvoiceSerializer(invoice, many=True,context={'request': request})
    return Response(serializers.data)
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
    