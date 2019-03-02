from django.contrib import admin

# Register your models here.
from gestionapp.models import Articulo, Deposito, Cliente, Proveedor, Unidad, Programagasto,\
  Mcotizacion, Dcotizacion, Clientesdireccion,Banco

admin.site.register(Articulo)
admin.site.register(Deposito)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Programagasto)
admin.site.register(Unidad)
admin.site.register(Mcotizacion)
admin.site.register(Dcotizacion)
admin.site.register(Banco)
