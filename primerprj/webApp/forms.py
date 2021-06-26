from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from django import forms

from .models import Usuarios



class UsuarioFrm(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'


class RegistroForm(ModelForm):
    class Meta:
        model= Usuarios
        exclude = ('rol','estado')







