from django.urls import path
from django.conf.urls import url
from rest_framework import routers
from . import views


urlpatterns = [
    url(r'^deposito$', views.DepositoList.as_view()),
    url(r'^deposito/(?P<pk>[0-9]+)$', views.DepositoDetail.as_view()),
    url(r'^articulo$', views.ArticuloList.as_view()),
    url(r'^articulo/(?P<pk>[0-9]+)$', views.ArticuloDetail.as_view()),
	url(r'^cliente$', views.ClienteList.as_view()),
    url(r'^cliente/(?P<pk>[0-9]+)$', views.ClienteDetail.as_view()),
    url(r'^clientemasivo$', views.masivo_list),

	url(r'^unidad$', views.UnidadList.as_view()),
    url(r'^unidad/(?P<pk>[0-9]+)$', views.UnidadDetail.as_view()),
    url(r'^mcotizacion$', views.McotizacionList.as_view()),
    url(r'^mcotizacion/(?P<pk>[0-9]+)$', views.McotizacionDetail.as_view()),
    url(r'^dcotizacion$', views.DcotizacionList.as_view()),
    url(r'^dcotizacion/(?P<pk>[0-9]+)$', views.DcotizacionDetail.as_view()),

    url(r'^clientesdireccion$', views.ClientesDireccionlist.as_view()),
    url(r'^clientesdirecciondetail$', views.ClientesDireccionlistdetail.as_view()),
    
]

