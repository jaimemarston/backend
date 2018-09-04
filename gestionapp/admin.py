from django.contrib import admin

# Register your models here.
from gestionapp.models import Articulo, Deposito, Cliente

admin.site.register(Articulo)
admin.site.register(Deposito)
admin.site.register(Cliente)