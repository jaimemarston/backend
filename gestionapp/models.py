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
    codigo    = models.CharField(max_length=15,blank=True, null=True)
    ruc       = models.CharField(max_length=15, blank=True, null=True)
    nombre    = models.CharField(max_length=100, blank=True, null=True)
    telefono  = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    correo    = models.CharField(max_length=150, blank=True, null=True)
    paginaweb = models.CharField(max_length=150, blank=True, null=True)
    banco_nombre1 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta1 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda1 = models.CharField(max_length=20,blank=True, null=True)
    banco_nombre2 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta2 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda2 = models.CharField(max_length=20,blank=True, null=True)
    sucursal      = models.CharField(max_length=10, blank=True, null=True)
    fechanac      = models.DateField(null=True, blank=True, help_text="Ingrese si esta activo u otro stado ")  
    estado        = models.IntegerField(default=0)
    anulado       = models.IntegerField(default=0)
    fecregistro   = models.DateField(null=True, blank=True)
    aud_idusu     = models.CharField(max_length=30,blank=True, null=True)
    aud_feccre    = models.DateTimeField(auto_now=True)
    aud_fecmod    = models.DateField(null=True, blank=True)
    aud_feceli    = models.DateField(null=True, blank=True)

class Proveedor(models.Model):
    codigo    = models.CharField(max_length=15,blank=True, null=True)
    ruc       = models.CharField(max_length=15, blank=True, null=True)
    nombre    = models.CharField(max_length=100, blank=True, null=True)
    telefono  = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    correo    = models.CharField(max_length=150, blank=True, null=True)
    paginaweb = models.CharField(max_length=150, blank=True, null=True)
    banco_nombre1 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta1 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda1 = models.CharField(max_length=20,blank=True, null=True)
    banco_nombre2 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta2 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda2 = models.CharField(max_length=20,blank=True, null=True)
    sucursal      = models.CharField(max_length=10, blank=True, null=True)
    estado        = models.IntegerField(default=0)
    fechanac      = models.DateField(null=True, blank=True, help_text="Ingrese si esta activo u otro stado ")  
    fecregistro   = models.DateField(null=True, blank=True)
    aud_idusu     = models.CharField(max_length=30,blank=True, null=True)
    aud_feccre    = models.DateTimeField(auto_now=True)
    aud_fecmod    = models.DateField(null=True, blank=True)
    aud_feceli    = models.DateField(null=True, blank=True)


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




