from rest_framework import serializers

from gestionapp.models import Deposito, Articulo, Cliente, Unidad, Programagastos, Mcotizacion, Dcotizacion, \
    Clientesdireccion


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ('id', 'codigo', 'descripcion')


class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ('id', 'codigo', 'descripcion')


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'codigo', 'descripcion',
                  'cantidad', 'color', 'deposito')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'codigo', 'nombre', 'ruc',
                  'telefono1', 'telefono2', 'telefono3', 'contacto', 'telcontacto',
                  'direccion', 'correo', 'paginaweb', 'tipocc', 'destipocc',
                  'banco_nombre1', 'banco_cuenta1', 'banco_moneda1', 'banco_nombre2', 'banco_cuenta2',
                  'banco_moneda2', 'fechanac', 'fechaini', 'fechafin')


class DcotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcotizacion
        fields = ('id', 'codigo', 'codpro', 'descripcion', 'unimed', 'desunimed', 'cantidad', 'precio', 'impsubtotal',
                  'impanticipos', 'impdescuentos',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'desgrupo1', 'desgrupo2',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'master')


class McotizacionSerializer(serializers.ModelSerializer):
    cotizaciones = DcotizacionSerializer(many=True, read_only=True)

    class Meta:
        model = Mcotizacion
        fields = ('id', 'codigo', 'descripcion', 'tipdoc', 'destipdoc', 'seriedoc', 'numerodoc', 'fechadoc',
                  'fecentrega', 'ruc', 'desruc', 'telruc', 'paisruc', 'dptoruc', 'provruc', 'distruc', 'codpostalruc',
                  'dirruc', 'conpag', 'desconpag', 'monedapago', 'desmonepago', 'tc_dolares', 'tc_euros', 'tc_yen',
                  'numeroguia', 'numordserv', 'vendidopor', 'fechapago', 'autorizadosunat', 'impsubtotal',
                  'impdescuentos',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'cotizaciones')


class ClientesdireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientesdireccion
        fields = ('direccion', 'telefono')
        # fields = '__all__'


class ClientesdirecciondetalleSerializer(serializers.ModelSerializer):
    clientesdirecciones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cliente
        fields = ('nombre', 'ruc', 'clientesdirecciones')
