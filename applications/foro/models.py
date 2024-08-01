from django.db import models
from applications.personas.models import Usuarios
from applications.vehiculos.models import Vehiculo
from django.urls import reverse

# Create your models here.
class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null= True)
    comentario = models.CharField(max_length=50)
    fechaComentario = models.DateTimeField(auto_now=False, auto_now_add=False)
    emocion = models.BooleanField()
    
    def __str__(self):
        return f"{self.usuario} - {self.comentario}"


#class Respuesta(models.Model):

    