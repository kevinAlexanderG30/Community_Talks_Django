from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import ProductosViewSet

route = routers.DefaultRouter()

route.register('Productos', ProductosViewSet)