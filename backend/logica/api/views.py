from rest_framework import routers, serializers, viewsets
from logica.models import Productos
from .serializers import ProductosSerializers

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializers