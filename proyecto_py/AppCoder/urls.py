from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicioApp, name="inicioApp"),
    path('crear_paquete/', crear_paquete),

    path("comentarios/", comentarios, name="comentarios"),
    
    path("busquedaMenu/", busquedaMenu, name="busquedaMenu"),
    path("buscar/", buscar, name="buscar"),

    path("suscriptor/", suscriptor, name="suscriptor"),
    path("eliminarSuscriptor/<id>", eliminarSuscriptor, name="eliminarSuscriptor"),

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),

    path('logout', LogoutView.as_view(), name='logout'),

    path('editarPerfil/', editarPerfil, name='editarPerfil'),
]