#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import View
from django import get_version
from django.http import HttpResponse



class Index(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Running Django ' + str(get_version()) + " on OpenShift")


from django.template.loader import get_template
from django.template import Context

from django.template import RequestContext, loader

from django.http import HttpResponse
import datetime

#from books.models import Publisher
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from miPagina.books.models import Book
from settings import MEDIA_URL


from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.contrib.auth.decorators import login_required



from forms import *
from datos_artetronica.models import *

from django.contrib.auth.models import User  
from django.core.mail import send_mail


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/principal")


@login_required
def entrada_producto(request):                

        #if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
        #            form = ProductoForm(request.POST,request.FILES)   
        #            if form.is_valid():
        #                form.save() # Guardar los datos en la base de datos 
        #                #return render_to_response('principal.html', locals() ,context_instance=RequestContext(request))
        #                return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
        #else:            
                       
        #                form = ProductoForm()
        #                username2 = request.user.id
        #                form = ProductoForm(initial={'id_usuario': username2})

        
        return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))


@login_required
def entrada_mensaje(request,bandera):               

        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = MensajeForm(request.POST)  

                    if form.is_valid():
                        mensajero = form.save(commit=False)
                        # commit=False tells Django that "Don't send this to database yet.
                        # I have more things I want to do with it."
                        mensajero.id_usuario = request.user.id # Set the user object here
                        mensajero.save() # Now you can send it to DB
                     

                        return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
        else:            
                        form = MensajeForm()


                        
        if bandera=="0": 
                  

                  mensajes_anteriores=Mensaje.objects.filter(id_usuario=request.user.id).order_by("-id")    
                  
        else:
                  
                  mensajes_anteriores=Mensaje.objects.all().order_by("-id") 
    
        

        return render_to_response('mensajes.html', locals() ,context_instance=RequestContext(request))



def entrada_usuario(request): 
       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    
                    form = UserProfile1Form(request.POST,request.FILES)  
                    
                    
                    if form.is_valid() :                  

                            
                            
                            mail = form.cleaned_data['email']
                            contra = form.cleaned_data['pasword'] 
                            first =form.cleaned_data['nombres']                      
                                             
                                                                            
                            
                            user = User.objects.create_user(username=mail, email=mail,password=contra,first_name=first)
                            user.save()

                            
                            usuario = form.save(commit=False)
                            # commit=False tells Django that "Don't send this to database yet.
                            # I have more things I want to do with it."
                            usuario.id_usuario = user.id # Set the user object here
                            usuario.save() # Now you can send it to DB
                            form.save() # Guardar los datos en la base de datos  print 
                                                      
                            return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
        else:            
                        

                         form=UserProfile1Form()

       
        return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))
    



def listado_producto(request,bandera):          
    productos=Producto.objects.filter(categoria=bandera)
     
    

    return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))

   
def listado(request,bandera):

    if bandera=="usuario":     
        #usuarios=User.objects.all() 
        productos= UserProfile1.objects.all() 
        return render_to_response('usuarios.html', locals(),context_instance=RequestContext(request))
    
    elif bandera=="staff":     
        productos= Staff.objects.all() 
        return render_to_response('staff.html', locals(),context_instance=RequestContext(request))
    
    elif bandera=="producto":     
        productos= Producto.objects.all() 
        return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
    
    else:     
        productos= Producto.objects.all() 
        return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
    
   

    
@login_required
def editar(request, acid):
    #f = Producto.objects.get(pk=acid)    
    ##message = Pedido.objects.get(pk=id)
    #if request.method == 'POST':
    #    form = ProductoForm(request.POST,instance=f)
    #    if form.is_valid():
    #        form.save() 
    #        return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))          
    #else:
    #    form = ProductoForm(instance=f)    
    #    
    return render_to_response('formulario.html',locals(),context_instance=RequestContext(request))



    
      
        
import datetime
#@login_required
def pagina_principal(request):
    current_date = datetime.datetime.now()
    

    if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                     
                    form = BuscarForm(request.POST,request.FILES)  
                    
                    
                    if form.is_valid() :                      
                            
                            form.save() # Guardar los datos en la base de datos  print 
                                                      
                            return render_to_response('catalogo.html', locals() ,context_instance=RequestContext(request))
       
    else:            
                        

                         form=BuscarForm()
               
                         return render_to_response('principal.html', locals(),context_instance=RequestContext(request))

def catalogo(request, var):
	current_date = datetime.datetime.now()	
	
	return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))

def informacion(request):
	current_date = datetime.datetime.now()
	
	return render_to_response('informacion.html', locals(),context_instance=RequestContext(request))




from datos_artetronica.cart import Cart
@login_required
def add_to_cart_PCB(request,product_id, quantity,precio):
    #print request  
   
    #product =(quantity,precio,"hola amigos")
    product = Pcb.objects.get(id=product_id)   

    cart = Cart(request)
    cart.add(product, precio, quantity)
    total=cart.summary()    
    

    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))


@login_required
def add_to_cart(request, product_id): 

    quantity= request.POST["cant"]
    product = Producto.objects.get(id=product_id)   



    if quantity==1:
        precio=product.precio_A
    elif quantity>=2 and quantity <=5:
        precio=product.precio_B
    elif quantity>=6:
        precio=product.precio_C
    else :
        precio=product.precio_A

    print  "########"
    print  quantity, product, precio 
    cart = Cart(request)
    cart.add(product, precio, quantity)
    total=cart.summary()
    

    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))

@login_required
def remove_from_cart(request, product_id):
    product = Producto.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

@login_required
def get_cart(request):
    print "getcqr" 
    cart = Cart(request)
    cart.view()
    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))

@login_required
def pedido(request):    
    cart = Cart(request)
    cart.view()    
    fecha= datetime.datetime.now()
    
    mensaje= str(fecha)+"  "+str(request.user.first_name) + "  "+str(request.user.last_name) +"  "+ str(request.user.id)+"  "+"\n"

    for item in cart:
        mensaje=mensaje+"  "+ str(item.product)+ "  "+ str(item.unit_price)+ "  "+str(item.quantity)+"  "+ str(item.total_price)+"  "+"\n"

                                
    mensaje=mensaje+"\n" 
     
    sender =str(request.user.email)

    send_mail('Pedido ', mensaje,"artetronica@gmail.com",(sender,), fail_silently=False)
   
    
    return render_to_response('cotizacion.html', locals(),context_instance=RequestContext(request))
 

####libreria de algun fulano que se utiliza para calcular el CRC de on byte
table = tuple()
# crc16_Init() - Initialize the CRC-16 table (crc16_Table[])
def init_table( ):
    global table

    if( (len( table) == 256) and (table[1] == 49345)):
        # print "Table already init!"
        return
   
    lst = []
    i = 0
    while( i < 256):
        data = (i << 1)
        crc = 0
        j = 8
        while( j > 0):
            data >>= 1
            if( (data ^ crc) & 0x0001):
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
            j -= 1
           
        lst.append( crc)
        # print "entry %d = %x" % ( i, table[i])
        i += 1

    table = tuple( lst)       
    return

# given a Byte, Calc a modbus style CRC-16 by look-up table
def calcByte( ch, crc):
    init_table( )
    if( type(ch) == type("c")):
        by = ord( ch)
    else:
        by = ch
    crc = (crc >> 8) ^ table[(crc ^ by) & 0xFF]
    return (crc & 0xFFFF)


###############################################################

def calcular(id_maquina):

                print "cjcjcjcjcjc"
                dato=id_maquina
                letras=""
                crc=0xffff
                for i in dato:
                     try:
                       x=eval(i)
                       crc= calcByte( x, crc)
                     except:
                       letras=letras+i
                     
                contrasena=str(crc)+letras   

                return  contrasena



@login_required
def descargar_serial_key(request):
       

        ide_de_usuario = request.user.id   
        x=ide_de_usuario #sumo uno pq USER y USUARIO no es igual
       
        #f = UserProfile.objects.get(pk=x)
        f=UserProfile1.objects.get(id_usuario=x)       

        cant_bonos=f.bonos
        
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                   
                   
                    if cant_bonos>0:                                
                                  
                               cant_bonos=cant_bonos-1
                               f.bonos=cant_bonos
                               f.save()

                               form = Seriales_pymblockForm(request.POST)                      

                               if form.is_valid():

                                    seriales = form.save(commit=False)
                                    # commit=False tells Django that "Don't send this to database yet.
                                    # I have more things I want to do with it."
                                    seriales.id_usuario = request.user.id # Set the user object here
                                    seriales.save() # Now you can send it to DB

                                   
                                                                        
                    else:
                            mensaje= "usted no tiene bonos"  
 
                    return render_to_response('principal.html', locals() ,context_instance=RequestContext(request))
        else:            
                        
                        form = Seriales_pymblockForm()
                       
        
        
        contrasenas=[] 
        print "ULO"      
            
        
        seriales_keys_anteriores=Seriales_pymblock.objects.filter(id_usuario=ide_de_usuario).order_by("-id") 

            
        for i in seriales_keys_anteriores:
                 
                b = calcular(i.id_usuario_pymblock)
                a = i.id_usuario_pymblock
                contrasenas.append( (a,b) )
                                     
        return render_to_response('descargas.html', locals() ,context_instance=RequestContext(request))

def descargar_material(request):
       
                                           
        return render_to_response('descargar_material.html', locals() ,context_instance=RequestContext(request))


def calcular_precio(cantidad,ancho,largo,n_caras):

                               precia=(ancho)*(largo)*n_caras

                               if cantidad<=2:
                                    precio=precia*0.20

                               elif cantidad>2 and cantidad<=4:
                                     precio=precia*0.16

                               elif cantidad>4 and cantidad<=6:
                                     precio=precia*0.14 
                              
                               elif cantidad>6 and cantidad<=20:
                                     precio=precia*0.08
                               
                               elif cantidad>21 and cantidad<=50:
                                     precio=precia*0.075
                               
                               elif cantidad>51 and cantidad<=99:
                                     precio=precia*0.07

                               elif cantidad>51 and cantidad<=99:
                                     precio=precia*0.068

                               elif cantidad>99: 
                                     precio=precia*0.066                                 
                               
                               else:  
                                    precio=precia*0.09

                        
                               total=precio*cantidad




                               return precio,total


tarjetaPCB=[]
@login_required
def pcb(request):

                       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                                      
                   form = PcbForm(request.POST)

                   if form.is_valid():
                               nom=form.cleaned_data['nombre'] 
                               cant=form.cleaned_data['cantidad'] 
                               ancho=form.cleaned_data['ancho_cm'] 
                               largo=form.cleaned_data['largo_cm'] 
                               n_caras=form.cleaned_data['caras'] 
                               #fecha=form.cleaned_data['fecha_ingreso'] 
                              
                               #precio cm2 = 0.15 ctvs
                               if n_caras=="Pcb_una_cara":
                                    n_c=1
                               else:
                                     n_c=2
                               
                               precio,total=calcular_precio(cant,ancho,largo,n_c)
                               #x=add_to_cart_PCB(request,id_producto,precio)
                               

                               return render_to_response('pcb_pedido.html', locals() ,context_instance=RequestContext(request))
        else:            
                        
                        form = PcbForm()   
                            

                                                
        return render_to_response('pcb.html', locals() ,context_instance=RequestContext(request))


@login_required
def pcb_pedido(request):
            
        
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                                                              

                   form = PcbForm(request.POST)

                   if form.is_valid():
                               nom=form.cleaned_data['nombre'] 
                               cant=form.cleaned_data['cantidad'] 
                               ancho=form.cleaned_data['ancho_cm'] 
                               largo=form.cleaned_data['largo_cm'] 
                               n_caras=form.cleaned_data['caras'] 
                               #fecha=form.cleaned_data['fecha_ingreso'] 
                              
                               #precio cm2 = 0.15 ctvs
                               if n_caras=="Pcb_una_cara":
                                    n_c=1
                               else:
                                     n_c=2

                               tarjeta = form.save(commit=False)
                               # commit=False tells Django that "Don't send this to database yet.
                               # I have more things I want to do with it."
                               tarjeta.id_usuario = request.user.id # Set the user object here
                               tarjeta.save() # Now you can send it to DB
                               
                               precio,total=calcular_precio(cant,ancho,largo,n_c)
                               x=add_to_cart_PCB(request,tarjeta.id,cant,precio)
                               

                               return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
        else:            
                        
                        form = PcbForm()   
                            

                                                
        return render_to_response('pcb_pedido.html', locals() ,context_instance=RequestContext(request))






def catalogos(request):
   productos= Producto.objects.all()       
   return render_to_response('catalogo2.html', locals() ,context_instance=RequestContext(request))

def catalogos2(request):
   productos= Producto.objects.all()        
   return render_to_response('catalogo.html', locals() ,context_instance=RequestContext(request))



def listado_cursos(request,bandera): 
     
      if bandera=="mios":
            
            id_de_usuario=request.user.id 

            inscritos=Alumno4.objects.filter(id_usuario=id_de_usuario) 
            cursos=[]

            for i in inscritos:
                    cursos.append(i.nombre_curso)
                       
            return render_to_response('mostrar_cursos.html', locals() ,context_instance=RequestContext(request))
  

      else:
            form = Alumno4Form() 
            cursos=Curso.objects.all()         
            return render_to_response('mostrar_cursos.html', locals() ,context_instance=RequestContext(request))
  
      
        
def inscribirme_en_el_curso(request,cursoid):
      
      if request.method == 'POST': # si el usuario est enviando el formulario con datos
         
             id_de_usuario=request.user.id 
             inscritos=Alumno4.objects.filter(id_usuario=id_de_usuario) 

            
             for i in inscritos:
              
                  if i.nombre_curso== Curso.objects.get(pk=cursoid):  

                        ir_al_curso(request,cursoid)  

                        #return render_to_response('ir_al_curso.html', locals() ,context_instance=RequestContext(request))
  


             form = Alumno4Form(request.POST)                      

             if form.is_valid():

                    inscripcion = form.save(commit=False)
                    # commit=False tells Django that "Don't send this to database yet.
                    # I have more things I want to do with it."
                    inscripcion.id_usuario = request.user.id # Set the user object here
                    inscripcion.nombre_curso=Curso.objects.get(pk=cursoid)
                    
                    inscripcion.capitulo_actual = Capitulo.objects.filter(nombre_curso=inscripcion.nombre_curso).first().nombre
                    inscripcion.seccion_actual = Seccion3.objects.filter(nombre_curso=inscripcion.nombre_curso).first().parte
                 

                    inscripcion.save() # Now you can send it to DB
                    form.save()
                  
      return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
               
 


def ir_al_curso(request,id_del_curso):



    id_del_curso=int(eval(id_del_curso))
    curso=Curso.objects.get(id=id_del_curso)  
    capitulos=Capitulo.objects.filter(nombre_curso=curso)  

    n_cap=capitulos.count()
    porcentaje_cap=100.0/n_cap
    porcentaje_cap=round(porcentaje_cap, 2)
    
    alumno=Alumno4.objects.get(nombre_curso=curso, id_usuario=request.user.id)
    
    if  alumno.capitulo_actual=="FINALIZADO":
        return render_to_response('diploma.html', locals() ,context_instance=RequestContext(request))
   

    nombre_capitulo_actual=alumno.capitulo_actual
    nombre_seccion_actual=alumno.seccion_actual

    a=0
    avance=0.00

    for i in capitulos:
      a=a+1
      if  nombre_capitulo_actual==i.nombre:
          avance=a*porcentaje_cap
          alumno.nota_temp=avance
          alumno.save()
          break


    capitulo=Capitulo.objects.get(nombre=nombre_capitulo_actual)
    secciones=Seccion3.objects.filter(nombre_capitulo= capitulo)

       
    secciones_cap=Seccion3.objects.filter(nombre_capitulo= capitulo,parte=nombre_seccion_actual)


     
    return render_to_response('curso.html', locals() ,context_instance=RequestContext(request))
    


def hacer_un_curso(request):
     #!/usr/bin/python
     # -*- coding: latin-1 -*-
     import os, sys
    

    
     if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                         
            if request.POST.get("bcurso"):

                  formCur=CursoForm(request.POST,request.FILES)  
                  
                  if formCur.is_valid():
                          cursillos = formCur.save(commit=False)
                          # commit=False tells Django that "Don't send this to database yet.
                          # I have more things I want to do with it."
                          cursillos.id_usuario = request.user.id # Set the user object here
                                           
                          cursillos.save() # Now you can send it to DB
                          formCur.save()
            else:        

                      if request.POST.get("bcapitulo"):

                            formCap=CapituloForm(request.POST,request.FILES)

                            if formCap.is_valid():
                                 formCap.save()


                      
                      else:

                                if request.POST.get("bseccion"):                                  
                                     
                                     form_seccion=Seccion3Form(request.POST,request.FILES)
                                     
                                     if form_seccion.is_valid():
                                         
                                         form_seccion.save
                                         print "hou"

                                         return render_to_response('principal.html', locals() ,context_instance=RequestContext(request))
                                       
                                
                                

            return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
     else:            
                        
                          formCur=CursoForm()
                          formCap=CapituloForm() 
                          
                          form_seccion=Seccion3Form()   
                                             

     return render_to_response('hacer_un_curso.html', locals() ,context_instance=RequestContext(request))



def calificar_curso(request,id_del_curso,id_seccion):


    if request.method == 'POST': # si el usuario est enviando el formulario con datos
                       
                seccion=Seccion3.objects.get(id=id_seccion)
                respuesta=[]
              
                if seccion.pregunta1:
                       respuesta1=request.POST.getlist('selec1')
                       respuesta1=eval(respuesta1[0])
                       respuesta.append(respuesta1)

                if seccion.pregunta2:
                       respuesta2=request.POST.getlist('selec2')
                       respuesta2=eval(respuesta2[0])
                       respuesta.append(respuesta2)

                if seccion.pregunta3:
                       respuesta3=request.POST.getlist('selec3')
                       respuesta3=eval(respuesta3[0])
                       respuesta.append(respuesta3)

                if seccion.pregunta4:
                       respuesta4=request.POST.getlist('selec4')
                       respuesta4=eval(respuesta4[0])
                       respuesta.append(respuesta4)

                if seccion.pregunta5:
                       respuesta5=request.POST.getlist('selec5')
                       respuesta5=eval(respuesta5[0])
                       respuesta.append(respuesta5)




                respuestafv=[]
                if seccion.preguntafv1:                       
                      a=2
                      if request.POST.get('fv1')==seccion.respuestafv1:
                          a=1
                      respuestafv.append(a)  


                if seccion.preguntafv2:
                      a=2              
                      if request.POST.get('fv2')==seccion.respuestafv2: 
                          a=1
                      respuestafv.append(a)


                if seccion.preguntafv3:
                      a=2                
                      if request.POST.get('fv3')==seccion.respuestafv3:
                          a=1 
                      respuestafv.append(a)

                if seccion.preguntafv4:
                      a=2                                     
                      if request.POST.get('fv4')==seccion.respuestafv4: 
                          a=1
                      respuestafv.append(a)

                if seccion.preguntafv5:
                      a=2                                     
                      if request.POST.get('fv5')==seccion.respuestafv5: 
                          a=1
                      respuestafv.append(a)






                respuestas_seleccion=[]
                a=1

                if respuesta:
                      for i in respuesta:
                        if i==1:
                            respuestas_seleccion.append("Correcta")
                            a=a*1
                        else:
                            respuestas_seleccion.append("Incorrecta")
                            a=a*2


                respuestas_fv=[]

                if respuestafv:
                        for i in respuestafv:
                          if i==1:
                              respuestas_fv.append("Correcta")
                              a=a*1
                          else:
                              respuestas_fv.append("Incorrecta")
                              a=a*2
                  



                if a != 1:
                     
                     estado_seccion = "REPROBADO"

                else:
                        estado_seccion = "APROBADO"

                        #id_del_curso=int(eval(id_del_curso))
                        curso=Curso.objects.get(id=id_del_curso)  
                        capitulos=Capitulo.objects.filter(nombre_curso=curso)  
                        
                        alumno=Alumno4.objects.get(nombre_curso=curso,id_usuario=request.user.id)
                        nombre_capitulo_actual=alumno.capitulo_actual
                        nombre_seccion_actual=alumno.seccion_actual


                        capitulo=Capitulo.objects.get(nombre=nombre_capitulo_actual)
                        secciones=Seccion3.objects.filter(nombre_capitulo= capitulo)

                           
                        secciones_cap=Seccion3.objects.filter(nombre_capitulo= capitulo,parte=nombre_seccion_actual)
 
                        #xa=capitulos.index(capitulo)
                        #b=secciones.index()

                        a=0
                        for i in capitulos:  
                          a=a+1                       
                          if i.nombre==nombre_capitulo_actual:
                             break
                          
                        b=0
                        for i in secciones:   
                          b=b+1                      
                          if i.parte==nombre_seccion_actual:
                             break
                          
                        n_cap=capitulos.count()
                        n_sec=secciones.count()


                        if b < n_sec:
                                
                                alumno.seccion_actual=secciones[b].parte
                                alumno.save()
                        else:
                            if a <  n_cap:
                                  
                                  alumno.capitulo_actual=capitulos[a].nombre
                                  secciones=Seccion3.objects.filter(nombre_capitulo= capitulos[a])
                                  alumno.seccion_actual=secciones[0].parte
                                  alumno.save()
                            else:
                                  estado_curso="CURSO FINALIZADO EXITOSAMENTE  10.00"
                                  alumno.seccion_actual="FINALIZADO"
                                  alumno.capitulo_actual="FINALIZADO"
                                  alumno.save()                
                 


    return render_to_response('calificar_curso.html', locals() ,context_instance=RequestContext(request))
    


def pymblock(request):
   productos= Producto.objects.all()       
   return render_to_response('pymblock.html', locals() ,context_instance=RequestContext(request))
