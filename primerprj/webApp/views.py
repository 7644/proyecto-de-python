from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import UsuarioFrm, RegistroForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from django.urls import reverse_lazy



import json
from django.core import serializers
from django.db.models import Q
from django.forms import modelform_factory


# Create your views here.




def index(request):
    return render(request,'smartbookapp/index.html')





def formulario(request):
    return render(request, 'smartbookapp/formulario.html')




def login(request):
    if request.method == 'POST':
        print("hola")
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')

        try:
            usu = Usuarios.objects.get(email=correo)
            rol = str(usu.rol)
            print(rol)
            if clave == usu.clave:
                if rol == 'usuario':
                    print('marisolllll')
                    request.session['sesion_usuario'] = str(usu.nombre)
                    id = str(usu.id)
                    return HttpResponseRedirect('home/'+id)
                else:

                    request.session['sesion_usuario'] = str(usu.nombre)


                    id = str(usu.id)
                    print(rol)
                    return HttpResponseRedirect('administrador_listar/'+id)
            else:
                mensaje = "usuario o contraseña incorrecta..."
                return HttpResponse(mensaje)

        except Exception as ex:
            mensaje = "usuario o contraseña incorrecta..."
            return HttpResponse(mensaje)

        # finally:
        # context = {'nombre':usuario,'rol':rol}
        # return render(request,'smggapp/admin.html',context)

    # else:
    # print("hola de nuevo")


prueba = Usuarios.objects.all()


def administrador_listar(request, id):

    if('sesion_usuario' in request.session):
        sesionUsuario=request.session['sesion_usuario']
        print(sesionUsuario)
        if(sesionUsuario!=""):
            prueba = Usuarios.objects.all()
            usuarios = Usuarios.objects.filter(id=id).first()
            context = {'usuario': usuarios.nombre, 'prueba': prueba}
            return render(request, 'smartbookapp/admin.html', context)
        else:
            return render(request, 'smartbookapp/formulario.html')

    else:
        return render(request, 'smartbookapp/formulario.html')



def barraBusqueda(request):
    admin=request.session.get('sesion_usuario')
    if request.method=='POST':
        busqueda = request.POST.get('buscar')
        if(busqueda!=""):
            verificarSession
            usu = Usuarios.objects.filter(nombre=busqueda)
            usu = [usuario_serializer(usuario) for usuario in usu]
            print(usu)
            context= {'prueba':usu,'usuario':admin}

            return render(request, 'smartbookapp/admin.html', context)
        else:
            prueba = Usuarios.objects.all()
            context = {'prueba': prueba,'usuario':admin}
            return render(request, 'smartbookapp/admin.html',context)
    else:
        print("ese usuario no existe")


def usuario(request):
    if request.method == 'POST':
        form = UsuarioFrm(request.POST)

        if form.is_valid():
            try:
                form.save()

                return redirect('/administrador_listar/1')
            except:
                pass

    else:
        form = UsuarioFrm()

        return render(request, 'smartbookapp/inicio.html', {'usuarioFrm': form})


def editar(request, id):
    print(request.method)
    usuario = Usuarios.objects.filter(id=id).first()
    estado = Estado.objects.all()
    rol = Rol.objects.all()
    print(usuario)
    return render(request, 'smartbookapp/editar.html', {'usuario': usuario, 'estado':estado,'rol':rol})


def actualizar(request, id):
    usuario = get_object_or_404(Usuarios, id=id)
    if request.method == 'POST':
        form = UsuarioFrm(request.POST, instance=usuario)
        print(request.POST)
        print(usuario)
        if form.is_valid():
            form.save()
            print(id)
            return redirect('/administrador_listar/1')
        else:
            print(form.errors)
    else:
        usuario = Usuarios.objects.filter(id=id).values()
        print(usuario)
    estado = Estado.objects.all()
    rol = Rol.objects.all()
    return render(request, 'smartbookapp/editar.html', {'usuario': usuario,'estado':estado,'rol':rol})


def eliminar(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    return redirect('/administrador_listar/1')

def buscar(request):
    busqueda= request.GET['buscar']
    usu= Usuarios.objects.filter(nombre__startswith= busqueda)
    usu= [usuario_serializer(usuario) for usuario in usu]

    return HttpResponse(json.dumps(usu),content_type='application/json')

def usuario_serializer(usuario):
    return { 'nombre': usuario.nombre,'email': usuario.email,'estado':usuario.estado,'rol':usuario.rol}

def logout(request):
   request.session['sesion_usuario']=""
   return render(request,'smartbookapp/index.html')


def verificarSession(request):
    if('sesion_usuario' in request.session):
        return
    else:
        return render(request, 'smartbookapp/formulario.html')



def home(request,id):
    if ('sesion_usuario' in request.session):
        sesionUsuario = request.session['sesion_usuario']
        print(sesionUsuario)
        if (sesionUsuario != ""):
            usu= Usuarios.objects.filter(id=id).first()
            context = {'usuario': usu.nombre}
            return render(request,'smartbookapp/home.html',context)
        else:
            return render(request,'smartbookapp/formulario.html')

    else:
        return render(request,'smartbookapp/formulario.html')


class Registro(CreateView):
    model= Usuarios
    template_name ="smartbookapp/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('webApp:formulario')










