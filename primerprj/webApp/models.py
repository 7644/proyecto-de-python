from django.db import models

# Create your models here.
class Estado (models.Model):
    tipo_estado= models.CharField(max_length=50)
    def __str__(self):
        return self.tipo_estado

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=60)
    def __str__(self):
         return self.nombre_rol



class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    clave = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, default=1)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, default=2)

    def __str__(self):
         return f'{self.nombre},{self.apellidos},{self.email},{self.clave},{self.estado},{self.rol}'





class Subir_img(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="img", null=True)
    def __str__(self):
     return self.nombre



