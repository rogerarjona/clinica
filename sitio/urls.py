#!
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from sitio import views
from django.views.generic import TemplateView

urlpatterns = [
	#Inicio y demas
	url(r'^$', login_required(TemplateView.as_view(template_name="inicio.html")), name="index"),
	url(r'^servicios/$', login_required(TemplateView.as_view(template_name="servicios.html")), name="servicios"),
	url(r'^quienes-somos/$', login_required(TemplateView.as_view(template_name="nosotros.html")), name="nosotros"),

	url(r'^contacto/$', views.contacto, name="contacto" ),
	url(r'^mapa-de-sitio/$', views.mapa_sitio, name="mapa_sitio" ),
	
	#Parte Backend
	url(r'^dashboard/$', login_required(views.dashboard), name="dashboard"),
	url(r'^perfil/$', login_required(views.perfilusuario), name="perfilusuario"),
	
	url(r'^citas/$', login_required(views.lista_citas), name="lista_citas"),
	url(r'^citas/agregar/$', login_required(views.agregar_cita), name="agregar_cita"),
	url(r'^citas/editar/([0-9]+)/$', login_required(views.editar_cita), name="editar_cita"),
	url(r'^citas/eliminar/([0-9]+)/$', login_required(views.eliminar_cita), name="eliminar_cita"), 
	url(r'^documentacion/$', (views.documentacion), name="documentacion"),
]

