from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .products import products
# Create your views here.


@api_view(['GET', 'POST'])
def getRoutes(request):
    return Response('Routes')


@api_view(['GET', 'POST'])
def getProducts(request):

    return Response(products)
