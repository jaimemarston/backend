from django.template.defaulttags import register
from django.utils.timezone import now
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from gestionapp.models import (
    Deposito, Articulo, Cliente, Proveedor, Unidad, Mcotizacion,
    Dcotizacion, Clientesdireccion, Banco,
    CotizacionEstado)

from gestionapp.serializers import (
    DepositoSerializer, ArticuloSerializer, ClienteSerializer, ProveedorSerializer, UnidadSerializer,
    McotizacionSerializer, DcotizacionSerializer, ClientesdireccionSerializer,
    ClientesdirecciondetalleSerializer, BancoSerializer,
    CotizacionEstadoSerializer)

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
import base64
from django.templatetags.static import static

# Create your views here.
from gestionapp.utils import render_to_pdf, PDFTemplateView, image_as_base64


@api_view(['GET', 'POST'])
def masivo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BancoList(generics.ListCreateAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer


class UnidadList(generics.ListCreateAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class UnidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


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

    # bloquea permisos para usar token
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(aud_idusu=self.request.user.username)

    # para filtrar datos
    """
    def get_queryset(self):
       
       # This view should return a list of all the purchases
       # for the currently authenticated user.
       
        # para otros filtros desde diccionario
        
        user = self.request.user.username
        return Cliente.objects.filter(aud_idusu=user)
    """


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteListMasivo(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProveedorList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    # bloquea permisos para usar token
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(aud_idusu=self.request.user.username)

    # para filtrar datos
    """
    def get_queryset(self):
       
       # This view should return a list of all the purchases
       # for the currently authenticated user.
       
        # para otros filtros desde diccionario
        
        user = self.request.user.username
        return Cliente.objects.filter(aud_idusu=user)
    """


class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProveedorListMasivo(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class McotizacionList(generics.ListCreateAPIView):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer

    # bloquea permisos para usar token
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(aud_idusu=self.request.user.username)


class McotizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer


class DcotizacionList(generics.ListCreateAPIView):
    queryset = Dcotizacion.objects.all()
    serializer_class = DcotizacionSerializer

    # bloquea permisos para usar token
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(aud_idusu=self.request.user.username)


class DcotizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dcotizacion.objects.all()
    serializer_class = DcotizacionSerializer


class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ClientesDireccionlist(generics.ListCreateAPIView):
    queryset = Clientesdireccion.objects.all()
    serializer_class = ClientesdireccionSerializer


class ClientesDireccionlistdetail(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientesdirecciondetalleSerializer


class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer


class GeneratePDFCotizacionesMaster(PDFTemplateView):
    template_name = 'gestionapp/invoice.html'

    def get_context_data(self, **kwargs):
        maestro_cotizacion = Dcotizacion.objects.filter(master=2)

        return super(GeneratePDFCotizacionesMaster, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            today=now(),
            cotizacion=maestro_cotizacion,
            **kwargs
        )


class GeneratePDFCotizacionesDetail(PDFTemplateView):
    template_name = 'gestionapp/invoice.html'

    def get_context_data(self, pk=None, *args, **kwargs):
        if pk is None:
            fields = ['codigo', 'descripcion', 'unidad medida', 'cantidad', 'precio', 'importe total']
            fields_db = ['codigo', 'descripcion', 'desunimed', 'cantidad', 'precio', 'imptotal']
            queryset = Mcotizacion.objects.all().values()
        else:
            fields = ['codigo', 'fecha', 'ruc', 'nombre', 'Unidad transporte', 'telefono']
            fields_db = ['codigo', 'fechadoc', 'ruc', 'desruc', 'unidadtransporte', 'telruc']
            queryset = Dcotizacion.objects.filter(master=pk).values()

        return super(GeneratePDFCotizacionesDetail, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            today=now(),
            cotizacion=queryset,
            fields=fields,
            fields_db=fields_db,
            **kwargs
        )


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class CotizacionEstadoViewSet(ModelViewSet):
    serializer_class = CotizacionEstadoSerializer
    queryset = CotizacionEstado.objects.all()
