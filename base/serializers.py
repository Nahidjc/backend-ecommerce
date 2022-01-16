from dataclasses import fields
from pyexpat import model
from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = '__all__'
