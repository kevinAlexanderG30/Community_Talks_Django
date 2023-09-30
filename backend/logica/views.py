from django.shortcuts import render
from django.http import JsonResponse
from .models import Productos


def obtener_productos(request):
    productos = Productos.objects.all()
    data = {'productos': list(productos.values())}
    return JsonResponse(data)