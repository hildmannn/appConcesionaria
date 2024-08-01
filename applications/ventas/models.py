from django.db import models
from applications.vehiculos.models import Vehiculo
from applications.personas.models import Usuarios,Empleados
from django.urls import reverse
# Create your models here.



class Ventas(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)  
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)   
    MEDIOPAGO_CHOICES = (
        ('0','efectivo'),
        ('1','tarjeta'),
    )
    medioPago = models.CharField( max_length=1, choices=MEDIOPAGO_CHOICES)
    CUOTAS_CHOICES = (
        ('0','1'),
        ('1','3'),
        ('2','6'),
        ('3','12'),
    )
    cuotas = models.CharField(max_length=1, choices=CUOTAS_CHOICES)
    interes = models.PositiveIntegerField()
    montoFinanciado = models.PositiveIntegerField()

    def __str__(self):
        return f"Venta de {self.vehiculo} a {self.cliente} por {self.empleado}"
