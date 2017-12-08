
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.


from mysite.datos_artetronica.models import *
#admin.site.unregister(User)
from mysite.forms import *


admin.site.register(Producto)
class RulesAdmin(admin.ModelAdmin):
    form = ProductoForm

admin.site.register(Buscar)
class RulesAdmin(admin.ModelAdmin):
    form = BuscarForm

admin.site.register(Empresa)
class RulesAdmin(admin.ModelAdmin):
    form = EmpresaForm

admin.site.register(Categoria)
class RulesAdmin(admin.ModelAdmin):
    form = CategoriaForm
		

  
    
