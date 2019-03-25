#!
# -*- coding: utf-8 -*-

from django import forms
from .forms import *
from .models import *
from django.contrib.auth.models import User

class PerfilUsuarioForm(forms.ModelForm):
	class Meta:
		model = PerfilUsuario
		exclude = ('user',)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class AgregarCitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		exclude = ['created', 'doctor', 'paciente', 'estado']
		widgets = {
			'observacion': forms.Textarea(attrs={'rows':4,}),
		}
	def __init__(self, *args, **kwargs):
		super(AgregarCitaForm, self).__init__(*args, **kwargs)