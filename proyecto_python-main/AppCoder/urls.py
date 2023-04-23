from django.urls import path
from .views import *

urlpatterns = [
    path("", inicioApp, name="inicioApp"),
    path('crear_paquete/', crear_paquete),

    path("comentarios/", comentarios, name="comentarios"),
    
    path("busquedaItinerario/", busquedaItinerario, name="busquedaItinerario"),
    path("buscar/", buscar, name="buscar"),

    path("suscriptor/", suscriptor, name="suscriptor"),
    path("eliminarSuscriptor/<id>", eliminarSuscriptor, name="eliminarSuscriptor"),
]