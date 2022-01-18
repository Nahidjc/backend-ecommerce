
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.products import products
from base.models import Product

from django.http import HttpResponse, JsonResponse
from .serializers import ProductSerializer
# Create your views here.

from rest_framework import generics


@api_view(['GET', 'POST'])
def getRoutes(request):
    return Response('Routes')


@api_view(['GET', 'POST'])
def getProducts(request):
    if request.method == 'GET':
        products = Product.objects.all()
        print(len(products))
        serializer = ProductSerializer(products, many=True)
        print(serializer.data)
    return Response(serializer.data)


# class getProducts(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


@api_view(['GET', 'POST'])
def getProduct(request, pk):
    for product in products:
        if product['_id'] == pk:
            pd = product

    return Response(pd)
