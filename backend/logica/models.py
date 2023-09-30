from django.db import models

# Create your models here.
class Productos(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=20, blank=True, decimal_places=2)