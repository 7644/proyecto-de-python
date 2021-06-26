

from django.urls import path

from webApp.views import *

app_name = 'webApp'



urlpatterns = [

path('', index, name='index'),
path('despedida/', despedida ),
path('login', login,name='login'),
path('formulario/', formulario, name='formulario'),
path('administrador_listar/usuario' ,usuario, name='usuario'),
path('administrador_listar/<int:id>', administrador_listar, name='administrador_listar'),
path('administrador_listar/editar//<int:id>', editar, name='editar'),
path('actualizar/<int:id>', actualizar, name='actualizar'),
path('administrador_listar/eliminar//<int:id>', eliminar, name='eliminar'),
path('PlantillaHija/', PlantillaHija, name='PlantillaHija'),
path('barraBusqueda',barraBusqueda , name='buscar'),
path('administrador_listar/logout', logout, name="logout" ),
path('home/<int:id>',home,name="home"),
path('formulario/Registro/', Registro.as_view(), name="registrar"),
path('formulario/formulario', formulario, name="formulario"),
path('home/logout', logout, name="logout"),
path('administrador_listar/formulario/', formulario, name="formulario"),
path('administrador_listar/formulario/Registro',Registro.as_view(), name="registro" ),
path('home/formulario/', formulario, name="formulario"),
path('administrador_listar/formulario/formulario', formulario, name="formulario")



#path('buscar' ,buscar ,name='buscar'),

]