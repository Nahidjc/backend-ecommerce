from unicodedata import category
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    print("Nahid", product)
    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    print("Nahid", product)
    product.delete()
    # serializer = ProductSerializer(product)
    detail = 'Successfully Delete the Product'

    return Response(detail)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    data = request.data
    print('data', data)
    product = Product.objects.create(
        user=user,
        name=data['name'],
        brand=data['brand'],
        category=data['category'],
        description=data['description'],
        rating=0,
        numReviews=0,
        price=data['price'],
        countInStock=data['countInStock']
    )
    print("Product created Successfully", product)
    serializer = ProductSerializer(product)

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    user = request.user
    data = request.data
    product = Product.objects.get(_id=pk)
    product.name = data['name']
    product.brand = data['brand']
    product.category = data['category']
    product.description = data['description']
    product.rating = data['rating']
    product.numReviews = data['numReviews']
    product.price = data['price']
    product.countInStock = data['countInStock']
    print("Product created Successfully", product)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['POST'])
def uploadImage(request):
    data = request.data

    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)

    product.image = request.FILES.get('image')
    product.save()
    serializer = ProductSerializer(product)
    print(serializer.data)

    return Response(serializer.data)
