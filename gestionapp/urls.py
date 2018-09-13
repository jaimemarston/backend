from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^deposito$', views.DepositoList.as_view()),
    url(r'^deposito/(?P<pk>[0-9]+)$', views.DepositoDetail.as_view()),
    url(r'^articulo$', views.ArticuloList.as_view()),
    url(r'^articulo/(?P<pk>[0-9]+)$', views.ArticuloDetail.as_view()),
	url(r'^cliente$', views.ClienteList.as_view()),
    url(r'^cliente/(?P<pk>[0-9]+)$', views.ClienteDetail.as_view()),
	url(r'^unidad$', views.UnidadList.as_view()),
    url(r'^unidad/(?P<pk>[0-9]+)$', views.UnidadDetail.as_view()),
]

