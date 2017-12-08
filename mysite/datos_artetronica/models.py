#!/usr/bin/python -tt
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime 

from django.contrib.auth.models import User
#import Image


CATEGORIA = (
			('tarjeta', 'tarjeta'),
			('kits', 'kits'),
			('Software', 'Software'),
			('shields', 'shields'),
			('elementos', 'elementos'),
			('proyecto', 'proyecto'),
			('sensores', 'sensores'),
			('impreso', 'impreso'),

			)

PUNTUACION = (
			('1 de 10', '1 de 10'),
			('2 de 10', '2 de 10'),
			('3 de 10', '3 de 10'),
			('4 de 10', '4 de 10'),
			('5 de 10', '5 de 10'),
			('6 de 10', '6 de 10'),
			('7 de 10', '7 de 10'),
			('8 de 10', '8 de 10'),
			('9 de 10', '9 de 10'),
			('10 de 10', '10 de 10'),

			)

	
ESTADO= (
			('Ya lo vendi', 'Ya lo vendi'),
			('Disponible', 'Disponible'),		

			)		
	


class Producto(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     categoria=models.CharField(max_length=30,choices=CATEGORIA)
	     cantidad         =  models.DecimalField(max_digits=15,decimal_places=0,default=0)
	     nombre           =  models.CharField(max_length=30)
	     
	     #imagen1      = models.ImageField(upload_to='tmp')	     
	    
	     descripcion = models.TextField(max_length=100)
	     puntuacion	 = models.CharField(max_length=30,choices=PUNTUACION) 
	     estado=  models.CharField(max_length=30,choices=ESTADO) 
	     precio_A  = models.FloatField(blank=True,null= True	)	     
	     fecha_ingreso = models.DateField(default=datetime.now,editable = False)
	     def save(self, *args, **kwargs):
         	if self.imagen1:
	            image = Img.open(StringIO.StringIO(self.imagen1.read()))
	            image.thumbnail((600,600), Img.ANTIALIAS)
	            output = StringIO.StringIO()
	            image.save(output, format='JPEG', quality=75)
	            output.seek(0)
	            self.imagen1= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen1.name, 'image/jpeg', output.len, None)
	        super(Producto, self).save(*args, **kwargs)

	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('categoria', 'cantidad', 'nombre','precio_A')
		    		#ordering = ('fecha_ingreso')
		    		#search_fields = ('nombre')#

class Buscar(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     item_de_busqueda=models.CharField(max_length=30)

	     def __str__(self):
		    		return  self.item_de_busqueda
	     class Admin:
		    		list_display = ('item_de_busqueda')

class Empresa(models.Model):
	     id_usuario=models.CharField(max_length=30,blank=True)
	     empresa=models.CharField(max_length=30)

	     def __str__(self):
		    		return  self.empresa
	     class Admin:
		    		list_display = ('empresa')

class Categoria(models.Model):
		 id_usuario=models.CharField(max_length=30,blank=True)
		 categoria=models.CharField(max_length=30)
		 def __str__(self):
		 	return  self.categoria
		 class Admin:
		 	list_display = ('categoria')

class UsuarioW(models.Model):
	     id_usuario=models.CharField(max_length=30)
	     clave=models.CharField(max_length=4)
	     email = models.EmailField()
	     ubicacion=models.CharField(max_length=30,blank=True)
	     plan=models.CharField(max_length=30,blank=True)
	     publicidad=models.CharField(max_length=30,blank=True)
	     #imagen1      = models.ImageField(upload_to='tmp')	
	     plan_tienda=models.CharField(max_length=30)
	     plan_publicidad=models.CharField(max_length=30) 

	     def save(self, *args, **kwargs):
         	if self.imagen1:
	            image = Img.open(StringIO.StringIO(self.imagen1.read()))
	            image.thumbnail((600,600), Img.ANTIALIAS)
	            output = StringIO.StringIO()
	            image.save(output, format='JPEG', quality=75)
	            output.seek(0)
	            self.imagen1= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen1.name, 'image/jpeg', output.len, None)
	        super(Producto, self).save(*args, **kwargs)
	     
	     def __str__(self):
		    		return  self.id_usuario
	     class Admin:
		    		list_display = ('id_usuario')


