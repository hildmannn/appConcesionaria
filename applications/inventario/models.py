from django.db import models
from django.urls import reverse


# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    mail = models.EmailField(max_length=70)
    paginaWeb = models.URLField(max_length=200)
    estado = models.BooleanField()

    # Importa Vehiculo solo cuando se necesite
    def get_vehiculos(self):
        from applications.vehiculos.models import Vehiculo
        return Vehiculo.objects.filter(proveedor=self)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
class Compras(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) 
    cantidad = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False, null= True)

    def get_vehiculos(self):
        from applications.vehiculos.models import Vehiculo #ver m to m con relacion proveedor
        return Vehiculo.objects.filter(proveedor=self)
    
    def __str__(self):
        return f"Compra de {self.cantidad} - {self.vehiculo}"

    
   