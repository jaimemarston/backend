from django.db import models

# Create your models here.

COLORES = (
    ('0', 'Blanco'),
    ('1', 'Negro'),
    ('2', 'Rojo'),
    ('3', 'Amarillo'),
    ('4', 'Azul'),
)



class Deposito(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30,blank=True, null=True)


class Unidad(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30,blank=True, null=True)


class Articulo(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=60)
    cantidad =  models.IntegerField()
    color = models.CharField(max_length=2, choices=COLORES)
    deposito = models.ForeignKey(Deposito, null=True, on_delete=models.SET_NULL)

class Cliente(models.Model):
    codigo  =  models.IntegerField()
    nombre  =  models.CharField(max_length=100,blank=True, null=True)
    website =  models.URLField(blank=True, null=True)

class Proveedor(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30,blank=True, null=True)


class Transporte(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30,blank=True, null=True)

class Chofer(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30,blank=True, null=True)





# ARCHIVOS DE MOVIMIENTO

class Mcotizacion(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30)

class Dcotizacion(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30)

class Mguia(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30)

class Dguia(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30)

class Mgasto(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30)

class Dgasto(models.Model):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30)




