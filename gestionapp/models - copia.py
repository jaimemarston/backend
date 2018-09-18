from django.db import models

# Create your models here.

COLORES = (
    ('0', 'Blanco'),
    ('1', 'Negro'),
    ('2', 'Rojo'),
    ('3', 'Amarillo'),
    ('4', 'Azul'),
)


class Camposcomunes_masterdoc(models.Model):
    codigo =  models.IntegerField(default=0)
    descripcion = models.CharField(max_length=30,null=True, blank=True)
    tipdoc = models.CharField(max_length=30,null=True, blank=True)
    destipdoc = models.CharField(max_length=30,null=True, blank=True)
    seriedoc = models.CharField(max_length=30,null=True, blank=True)
    numerodoc = models.CharField(max_length=30,null=True, blank=True)
    fechadoc = models.DateField(null=True, blank=True)
    fecentrega = models.DateField(null=True, blank=True) # Fecha entrega pedido
    ruc      = models.CharField(max_length=30,null=True, blank=True)
    desruc   = models.CharField(max_length=150,null=True, blank=True)
    telruc   = models.CharField(max_length=30,null=True, blank=True)
    paisruc  = models.CharField(max_length=30,null=True, blank=True)
    dptoruc  = models.CharField(max_length=30,null=True, blank=True)
    provruc  = models.CharField(max_length=30,null=True, blank=True)
    distruc  = models.CharField(max_length=30,null=True, blank=True)
    codpostalruc = models.CharField(max_length=30,null=True, blank=True)
    dirruc   = models.CharField(max_length=150,null=True, blank=True)
    posmapruc= models.IntegerField(default=0) 
    conpag   = models.CharField(max_length=30,null=True, blank=True)
    desconpag  = models.CharField(max_length=50,null=True, blank=True)
    monedapago = models.IntegerField(default=0)  # soles,dolares,euros,yen
    tc_dolares = models.IntegerField(default=0)
    tc_euros   = models.IntegerField(default=0)
    tc_yen     = models.IntegerField(default=0)
    numeroguia = models.IntegerField(default=0)
    numordserv  = models.IntegerField(default=0)
    vendidopor = models.CharField(max_length=30,null=True, blank=True)
    fechapago  = models.DateField(null=True, blank=True)
    autorizadosunat = models.IntegerField(default=0)
    
    impsubtotal  = models.IntegerField(default=0)
    impanticipos = models.IntegerField(default=0)
    impdescuentos  = models.IntegerField(default=0)
    impvalorventa  = models.IntegerField(default=0)
    impisc  = models.IntegerField(default=0)
    impigv  = models.IntegerField(default=0)
    nvaligv  = models.IntegerField(default=0)
    impotroscargos  = models.IntegerField(default=0)
    impotrostributos  = models.IntegerField(default=0)
    imptotal    = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Camposcomunes(models.Model):
    zsucursal      = models.CharField(max_length=10, blank=True, null=True)
    zestado        = models.IntegerField(default=0)
    zanulado       = models.IntegerField(default=0)
    zfecregistro   = models.DateField(null=True, blank=True)
    zaud_idusu     = models.CharField(max_length=30,blank=True, null=True)
    zaud_feccre    = models.DateTimeField(auto_now=True)
    zaud_fecmod    = models.DateField(null=True, blank=True)
    zaud_feceli    = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


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

class Cliente(Camposcomunes):
    codigo    = models.CharField(max_length=15,blank=True, null=True)
    ruc       = models.CharField(max_length=15, blank=True, null=True)
    nombre    = models.CharField(max_length=100, blank=True, null=True)
    telefono  = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    correo    = models.CharField(max_length=150, blank=True, null=True)
    paginaweb = models.CharField(max_length=150, blank=True, null=True)
    tipocc    = models.IntegerField(default=0)
    destipocc = models.CharField(max_length=100,blank=True, null=True)
    condcompvent =  models.CharField(max_length=100,blank=True, null=True)
    banco_nombre1 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta1 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda1 = models.CharField(max_length=20,blank=True, null=True)
    banco_nombre2 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta2 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda2 = models.CharField(max_length=20,blank=True, null=True)
    fechanac      = models.DateField(null=True, blank=True, help_text="Ingrese si esta activo u otro stado ")  

class Proveedor(Camposcomunes):
    codigo    = models.CharField(max_length=15,blank=True, null=True)
    ruc       = models.CharField(max_length=15, blank=True, null=True)
    nombre    = models.CharField(max_length=100, blank=True, null=True)
    telefono  = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    correo    = models.CharField(max_length=150, blank=True, null=True)
    paginaweb = models.CharField(max_length=150, blank=True, null=True)
    tipocc    = models.IntegerField(default=0)
    destipocc = models.CharField(max_length=100,blank=True, null=True)
    condcompvent =  models.CharField(max_length=100,blank=True, null=True)
    banco_nombre1 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta1 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda1 = models.CharField(max_length=20,blank=True, null=True)
    banco_nombre2 = models.CharField(max_length=100,blank=True, null=True)
    banco_cuenta2 = models.CharField(max_length=100,blank=True, null=True)
    banco_moneda2 = models.CharField(max_length=20,blank=True, null=True)
    fechanac      = models.DateField(null=True, blank=True, help_text="Ingrese si esta activo u otro stado ")
   

class Transporte(Camposcomunes):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30,blank=True, null=True)

class Chofer(Camposcomunes):
    codigo =  models.IntegerField()
    descripcion = models.CharField(max_length=30,blank=True, null=True)


# ARCHIVOS DE MOVIMIENTO

class Mcotizacion(Camposcomunes,Camposcomunes_masterdoc):
    pass

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


