from django.urls import path
from . import views

app_name = 'ia'

urlpatterns = [
    path('', views.base, name='base'),
    path('inicio/',views.inicio , name='inicio'),
    path('busqueda/', views.busqueda, name='busqueda'),
    


    path('imagenes/', views.imagenes, name='imagenes'),
    path('mapas-mentales/', views.mapas_mentales, name='mapas-mentales'),
    path('matematicas/', views.matematicas, name='matematicas'),
    path('ppt/', views.ppt, name='ppt'),
    path('programacion/', views.programacion, name='programacion'),
    path('texto/', views.texto, name='texto'),
]
