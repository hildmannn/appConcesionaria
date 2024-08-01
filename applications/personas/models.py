from django.db import models
from django.urls import reverse

# Create your models here.
class Usuarios(models.Model): #puede ser tanto cliente como usuario 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    dni = models.CharField(max_length=12)
    mail = models.EmailField(max_length=70, null= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_absolute_url(self):
        return reverse('usuarios-detail', args=[str(self.id)])


class Empleados(models.Model):
    PUESTO_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    dni = models.CharField(max_length=12)
    puesto = models.CharField( max_length=1, choices=PUESTO_CHOICES)
    mutual = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.get_puesto_display()}"


