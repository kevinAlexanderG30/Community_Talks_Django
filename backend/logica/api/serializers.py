from django.urls import path, include
from logica.models import Productos
from rest_framework import routers, serializers, viewsets


class ProductosSerializers(serializers.ModelSerializer):
    class Meta():
        model = Productos
        fields = '__all__'