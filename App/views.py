from .serializers import customersSerializer,invoiceSerializer,invoicedetailSerializer
from .models import Customer,Invoice,increment_invoice_number
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .function import getcurrentfinancialyear
# Create your views here.

# Get customer information by ID
# @api_view(['GET'])
# def customer_info(request,pk):
#     try:
#         customer = Customer.objects.get(customer_id=pk)
#     except Customer.DoesNotExist:
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializers = customerSerializer(customer)
#     return Response(serializers.data,status=status.HTTP_200_OK)

# Get All customers 
class customers(APIView):                  
    def get(self, request):
        customers = Customer.objects.all()     
        serializers = customersSerializer(customers, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)    

# Get Invoice information
class invoice_info(APIView):
    def get(self,request):
        invoice = Invoice.objects.last()
        print(invoice)
        serializers = invoiceSerializer({invoice}, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

# Add customer information
class addcustomer(APIView):
    def post(self,request):
        serializers = customersSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Add invoice information
class add_invoice(APIView):
    def post(self , request):
        serializers = invoicedetailSerializer(data=request.data,many=True)  
        if serializers.is_valid():
            serializers.save()
            return Response({"invoice_id":increment_invoice_number()},status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


#################    Generating PDF   #########################

