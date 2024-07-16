"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_xd,name='login'),
    path('registro/',views.registro,name='registro'),
    path('trabajador/',views.trabajador,name='trabajador'),
    path('cerrar/',views.cerrar,name='cerrar'),
    path('ver_habitaciones/<id_h>',views.ver_habitaciones,name='ver_habitaciones'),
    path('ver_habitacion/<id_h>',views.ver_habitacion,name='ver_habitacion'),
    path('Reservar/<id>',views.reservar,name='Reservar'),
    path('ver_promos/',views.ver_promos,name='ver_promos'),
    path('editar_promocion/<id>',views.editar_promocion,name='editar_promocion'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)