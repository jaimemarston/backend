from rest_framework import serializers


from gestionapp.models import Deposito, Articulo


class DepositoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Deposito
		fields = ('id', 'codigo', 'descripcion')


class ArticuloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articulo
		fields = ('id', 'codigo', 'descripcion', 'cantidad', 'color', 'deposito')

