from django.urls import path
from .views import obtener_productos

urlpatterns = [
    path('productos/', obtener_productos)
 ]

