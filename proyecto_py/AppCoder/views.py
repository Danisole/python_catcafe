from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def  crear_paquete(request):

    nombre_paquete="paquete aventurero"
    cantidad_personas=3

    viaje=Viaje(nombre=nombre_paquete,  personas=cantidad_personas)
    viaje.save()

    respuesta=f"Su paquete  --{nombre_paquete} para {cantidad_personas} personas fue creado satisfactoriamente"

    return HttpResponse(respuesta)


@login_required
def suscriptor(request):

    if request.method =="POST":

        form = SuscriptorForm(request.POST)

        if form.is_valid():
        
            suscriptor = Suscriptor()

            suscriptor.nombre = form.cleaned_data['nombre']
            suscriptor.apellido = form.cleaned_data['apellido']
            suscriptor.email = form.cleaned_data['email']
            suscriptor.save()

            form = SuscriptorForm()

    else:
        form = SuscriptorForm()
    
    suscriptor= Suscriptor.objects.all()
    context = {"suscriptor": suscriptor, "form" : form,"avatar": obtenerAvatar(request)}

   

    return render(request, "AppCoder/suscriptor.html", context)

def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)[0].imagen.url
    if len(avatares)!=0:
        return avatares
    else:
        return "/media/avatars/default.png"
    

@login_required
def eliminarSuscriptor(request, id):
    suscriptor = Suscriptor.objects.get(id=id)
    print(suscriptor)
    suscriptor.delete()
    suscriptor= Suscriptor.objects.all()
    form = SuscriptorForm()
    return render(request, "AppCoder/suscriptor.html", {"suscriptor": suscriptor, "mensaje": "Tu suscripcion fue eliminada con exito", "form" : form, "avatar": obtenerAvatar(request)} )

@login_required
def busquedaMenu(request):
    return render(request, "AppCoder/busquedaMenu.html", {"avatar": obtenerAvatar(request)})

@login_required
def buscar(request):         
    nombre=request.GET["nombre"]
    print(nombre)

    if nombre!="":

        menus=Menus.objects.filter(nombre__icontains=nombre)
        return render(request, "AppCoder/buscar.html", {"menus": menus})
    
    else:
        return render(request, "AppCoder/buscar.html", {"mensaje":"campo vacio", "avatar": obtenerAvatar(request)})

@login_required
def comentarios(request):

    if request.method =="POST":

        form = ComentariosForm(request.POST)

        if form.is_valid():
        
            comentarios = Comentarios()

            comentarios.nombre = form.cleaned_data['nombre']
            comentarios.reseña = form.cleaned_data['reseña']
            comentarios.estrellas = form.cleaned_data['estrellas']
            comentarios.save()

            form = ComentariosForm()

    else:
        form = ComentariosForm()
    
    comentarios= Comentarios.objects.all()
    context = {"comentarios": comentarios, "form" : form, "avatar": obtenerAvatar(request)}

    return render(request, "AppCoder/comentarios.html", context)



def inicio(request):
    return HttpResponse("mi pagina de inicio")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")


def login_request(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {"mensaje": f"Usuario {usu.upper()} logueado correctamentre"})
            else:
                return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})    
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {"form": form})
        
def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Usuario {username.upper()} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
        
    else:
        form=RegistroUsuarioForm()
        return render(request, "AppCoder/register.html", {"form": form})    
    

def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente","avatar": obtenerAvatar(request) })
        
        else:
            return render(request, "AppCoder/editarPerfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obtenerAvatar(request)})
        
    else:
        form=UserEditForm(instance=usuario)    
        return render(request, "AppCoder/editarPerfil.html", {"form":form, "nombreusuario":usuario.username, "avatar": obtenerAvatar(request)})

    

