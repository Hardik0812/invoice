from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view(['GET'])
def Customer_info(request,pk):
    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        customer = None
    serializers = customerSerializer(customer)
    return Response(serializers.data)

@api_view(['POST'])
def addCustomer(request):
    serializers = customerSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response("please enter {name} and {address}", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Customers(request):
    customers = Customer.objects.all()
    serializers = customersSerializer(customers)
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
    