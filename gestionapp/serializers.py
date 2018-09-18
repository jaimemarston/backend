from rest_framework import serializers


from gestionapp.models import Deposito, Articulo, Cliente, Unidad, Programagastos


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
