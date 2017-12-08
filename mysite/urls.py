#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#from mysite.views import Index

############################################
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns,url,include

from django.contrib import admin


from django.conf import settings
import settings

from django.contrib.auth.views import login, logout

from django.conf.urls.static  import static 


from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mysite.views import *



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'artetronica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',include(admin.site.urls)),
     url(r'^$', Index.as_view(), name='index'),
    (r'^accounts/login/$', login,{'template_name': 'login.html'}),
    (r'^accounts/logout/$', logout),
)

#r'^admin/', include(admin.site.urls)


urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += patterns('',	(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}))
urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}))

urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL)


urlpatterns += patterns('',(r'^principal/$', pagina_principal),(r'^catalogo/(\d+)$', catalogo),(r'^informacion/$', informacion)) + staticfiles_urlpatterns()
urlpatterns += patterns('',(r'^listado/([a-z]+)$', listado),(r'^editar/(\d+)/$', editar),)
urlpatterns += patterns('',(r'^entrada_usuario/$', entrada_usuario),(r'^entrada_mensaje/(\d+)$', entrada_mensaje),(r'^descargar_material/$', descargar_material),)
urlpatterns += patterns('',(r'^add_to_cart_PCB/(\d+)/([^/]+)/$', add_to_cart_PCB),(r'^get_cart/$', get_cart),)





