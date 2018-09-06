from rest_framework import serializers


from gestionapp.models import Deposito, Articulo, Cliente, Unidad 


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
		fields = ('id', 'codigo', 'descripcion', 'cantidad', 'color', 'deposito')

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ('id', 'codigo', 'nombre')

