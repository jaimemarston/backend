from django.contrib import admin

# Register your models here.
from gestionapp.models import Articulo, Deposito, Cliente, Unidad, Programagasto, Mcotizacion, Dcotizacion, Clientesdireccion

admin.site.register(Articulo)
admin.site.register(Deposito)
admin.site.register(Cliente)
admin.site.register(Programagasto)
admin.site.register(Unidad)
admin.site.register(Mcotizacion)
admin.site.register(Dcotizacion)
