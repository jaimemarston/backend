from django.shortcuts import render
from rest_framework import generics

from gestionapp.models import Deposito, Articulo, Cliente
from gestionapp.serializers import DepositoSerializer, ArticuloSerializer, ClienteSerializer

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class DepositoList(generics.ListCreateAPIView):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer

class DepositoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer

class ArticuloList(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)