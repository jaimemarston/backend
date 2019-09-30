from django.template.defaulttags import register
from django.utils.timezone import now
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum

from gestionapp.models import (
    Deposito, Articulo, Cliente, Proveedor, Unidad, Mcotizacion,
    Dliquidacion,Dcotizacion, Clientesdireccion, Banco, Chofer, Guia,
    CotizacionEstado)

from gestionapp.serializers import (
    DepositoSerializer, ArticuloSerializer, ClienteSerializer, ProveedorSerializer, UnidadSerializer,
    MliquidacionSerializer, McotizacionSerializer, DcotizacionSerializer,DliquidacionSerializer, ClientesdireccionSerializer,
    ClientesdirecciondetalleSerializer, BancoSerializer, ChoferSerializer, GuiaSerializer,
    CotizacionEstadoSerializer)

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
import base64
from django.templatetags.static import static

# Create your views here.
from gestionapp.utils import render_to_pdf, PDFTemplateView, image_as_base64
from procesar import cargar_data

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


# class UseractivoList(generics.ListCreateAPIView):
#     queryset = user.objects.filter(username self.request.user.username)
#     serializer_class = UnidadSerializer


class UnidadList(generics.ListCreateAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class UnidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


# Choferes / Conductores

class ChoferList(generics.ListCreateAPIView):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer

class ChoferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer


# Guia de Turismo
class GuiaList(generics.ListCreateAPIView):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer
class GuiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer


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

    def perform_update(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(idioma='español',pais='Peru')

class ClienteListMasivo(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteUploadFile(APIView):
    parser_classes = (MultiPartParser,)
    def post(self, request):
        file = request.FILES['file']
        file_data = file.read();
        cargar_data(file_data)
        # Parse data
        return Response(status=204)

class ProveedorList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.order_by('nombre')
    serializer_class = ProveedorSerializer

    # para filtrar datos
    """
        # bloquea permisos para usar token
    # permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        # guarda aud_idusu automatically en tabla.
        serializer.save(aud_idusu=self.request.user.username)
        
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


class MliquidacionList(generics.ListCreateAPIView):
    queryset = Dliquidacion.objects.all()
    serializer_class = MliquidacionSerializer


class MliquidacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dliquidacion.objects.all()
    serializer_class = MliquidacionSerializer

class McotizacionList(generics.ListCreateAPIView):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer
       

class McotizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer
    


class DliquidacionList(generics.ListCreateAPIView):
    queryset = Dliquidacion.objects.all()
    serializer_class = DliquidacionSerializer

class DliquidacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dliquidacion.objects.all()
    serializer_class = DliquidacionSerializer

class DcotizacionList(generics.ListCreateAPIView):
    queryset = Dcotizacion.objects.all()
    serializer_class = DcotizacionSerializer

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


class LiquidacionViewSet(viewsets.ModelViewSet):
    queryset = Dcotizacion.objects.all()
    serializer_class = MliquidacionSerializer

class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Mcotizacion.objects.all()
    serializer_class = McotizacionSerializer


class GeneratePDFCotizacionesMaster(PDFTemplateView):
    template_name = 'gestionapp/invoice.html'

    def get_context_data(self, **kwargs):
        maestro_cotizacion = Dcotizacion.objects.filter(master=2)

        return super(GeneratePDFCotizacionesMaster, self).get_context_data(
            pagesize='A4',
            title='Cotizacion Alitour',
            today=now(),
            cotizacion=maestro_cotizacion,
            **kwargs
        )


class GeneratePDFCotizacionesDetail(PDFTemplateView):
    template_name = 'gestionapp/invoice.html'

    def get_context_data(self, pk=None, user=None, *args, **kwargs):
        #username = self.request.user.username
        #username = self.request.user.get_username()
        username = self.request.GET.get('user', None)
        #username = user
        print(username,'current user1')

        if pk is None:
            fields = ['Fecha', 'Hora', 'Descripcion', 'PAX', 'transporte', 'Total']
            fields_db = ['fechaini', 'horaini', 'descripcion', 'cantidad', 'desunimed', 'imptotal']
            headerset = Mcotizacion.objects.all().values()
            queryset = Mcotizacion.objects.all().values()
        else:
            fields = ['Fecha', 'Hora', 'Descripcion', 'PAX', 'Transporte', 'Total']
            fields_db = ['fechaini', 'horaini', 'descripcion', 'cantidad', 'desunimed', 'imptotal']
            headerset = Mcotizacion.objects.filter(id=pk).values()
            datosprin = list(Mcotizacion.objects.filter(id=pk).values_list())

            codruc=datosprin[0][9]

            queryset = Dcotizacion.objects.filter(master=pk).values()
            mcliente = Cliente.objects.filter(ruc=codruc).values()

            cliente_contacto=mcliente[0]['contacto']

            observacion_mater=headerset[0]['obs']

            print ("cliente_contacto",cliente_contacto,codruc)
            rimpsubtotal = list(Mcotizacion.objects.filter(id=pk).aggregate(Sum('impsubtotal')).values())[0] or 0
            rigv         = list(Mcotizacion.objects.filter(id=pk).values_list('impigv')[0])[0]
            rimptotal    = list(Mcotizacion.objects.filter(id=pk).aggregate(Sum('imptotal')).values())[0] or 0
            imagenes = list(Dcotizacion.objects.filter(master=pk).values_list('desunimed')) or ''
            
            
            imagen_obtx = []
            for image in imagenes:
                # imagen_obt = list(Unidad.objects.filter(descripcion=image[0]).values_list('foto1'))
                imagen_obt = Unidad.objects.filter(descripcion=image[0])
                if imagen_obt:
                    for foto in imagen_obt:
                        imagen_obtx.append(foto.foto1.url)
                #print ('imagen_obtx',type(imagen_obtx))  
                #print ('imagen_obt',imagen_obt,imagen_obtx) 

              
            #imagen_obt2 = Unidad.objects.filter(descripcion=image[0])
            imagen_obt2 = ''
        return super(GeneratePDFCotizacionesDetail, self).get_context_data(
            pagesize='A4',
            title='Cotizacion Alitour',
            today=now(),
            cotizacion=queryset,
            cliente_contacto=cliente_contacto,
            observacion_master=observacion_mater,
            headerset=headerset,
            fields=fields,
            fields_db=fields_db,
            resultado_subtotal=rimpsubtotal,
            resultado_dcto=0,
            resultado_igv=rigv,
            resultado_total=rimptotal,
            muestra_imagenes1=imagen_obtx,
            muestra_imagenes2=imagen_obt2,
            username=username,
            **kwargs
        )


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class CotizacionEstadoViewSet(ModelViewSet):
    serializer_class = CotizacionEstadoSerializer
    queryset = CotizacionEstado.objects.all()