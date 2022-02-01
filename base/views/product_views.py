from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from base.products import products
from base.models import Product
from django.http import HttpResponse, JsonResponse
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

from rest_framework import status
# Create your views here.

from rest_framework import generics




@api_view(['GET', 'POST'])
def getProducts(request):
    if request.method == 'GET':
        products = Product.objects.all()
        # print(len(products))
        serializer = ProductSerializer(products, many=True)
        # print(serializer.data)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    print("Nahid", product)
    serializer = ProductSerializer(product)

    return Response(serializer.data)
