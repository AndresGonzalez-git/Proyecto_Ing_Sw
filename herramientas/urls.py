from django.urls import path
from . import views

urlpatterns = [
    path('ficha/<int:id>/', views.ficha_herramienta, name='ficha_herramienta'),
    path('lista/', views.lista_herramientas, name='lista_herramientas'),
    path('privacidad/', views.aviso_privacidad, name='aviso_privacidad'),
] 

