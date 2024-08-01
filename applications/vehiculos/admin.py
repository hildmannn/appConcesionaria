from django.contrib import admin
from .models import Vehiculo, Modelos, FichasTecnicas, Marcas, Categorias

admin.site.register(Vehiculo)
admin.site.register(Modelos)
admin.site.register(FichasTecnicas)
admin.site.register(Marcas)
admin.site.register(Categorias)


