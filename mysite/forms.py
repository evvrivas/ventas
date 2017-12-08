#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class ProductoForm(ModelForm):
	class Meta:
		model= Producto
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 3}),}
		exclude=["id_usuario","puntuacion","fecha_ingreso"]


class BuscarForm(ModelForm):
	class Meta:
		model= Buscar		
		exclude=["id_usuario"]

class EmpresaForm(ModelForm):
	class Meta:
		model= Empresa		
		exclude=["id_usuario"]

class CategoriaForm(ModelForm):
	class Meta:
		model= Categoria		
		exclude=["id_usuario"]


