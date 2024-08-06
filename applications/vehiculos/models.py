from django.db import models
from applications.inventario.models import Proveedor
from django.urls import reverse

# Create your models here.
class Categorias(models.Model):
    CATEGORIA_CHOICES = (
        ('0','chata'),
        ('1','auto'),
        ('2','moto'),
        ('3','cuatri'),
    )
    tipoVehiculo = models.CharField( max_length=1, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.get_tipoVehiculo_display()

class Marcas(models.Model):
    marca = models.CharField( max_length=50)

    def __str__(self):
        return self.marca
class FichasTecnicas(models.Model):
    CANTIDAD_CHOICES = (
        ('0','2'),
        ('1','3'),
        ('2','4'),
        ('3','5'),
        
    )
    puertas = models.CharField( null=True, blank=True, max_length=1, choices=CANTIDAD_CHOICES)
    cilindradas = models.CharField(max_length=50)
    TIPO_CHOICES = (
        ('0','electricidad'),
        ('1','nafta'),
        ('2','diesel'),
        ('3','gas'),
    )
    combustible = models.CharField( null=True,max_length=1, choices=TIPO_CHOICES)
    paisFabrica = models.CharField( max_length=50)
    
    def __str__(self):
        return f"{self.cilindradas} - {self.get_combustible_display()}"


class Modelos(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    marcas = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    modelo = models.CharField('Nombre del modelo', max_length=50)
    fichaTecnica = models.ForeignKey(FichasTecnicas, on_delete=models.CASCADE)
    año = models.DateField()
    #portada = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f"{self.modelo} ({self.año.strftime('%Y')})"


class Vehiculo(models.Model):
    modelos = models.ForeignKey(Modelos, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    km = models.PositiveIntegerField()
    detalles = models.CharField(max_length=50, null=True, blank=True)
    #---------------------------------------------------
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    compra = models.PositiveIntegerField('precio compra',null=True)
    venta = models.PositiveIntegerField('precio venta')
    disponibilidad = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.modelos} - {self.color}"







    