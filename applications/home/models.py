from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

ROLE_CHOICES = [
    ('user', 'User'),
    ('employee', 'Employee'),
    ('admin', 'Admin'),
]

class Usuarios(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    dni = models.CharField(max_length=10)
    mail = models.EmailField(unique=True)

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
