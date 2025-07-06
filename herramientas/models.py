from django.db import models

# HU02: Definición de categorías predefinidas para el filtrado
CATEGORIAS_IA = [
    ("texto", "Texto"),
    ("imagen", "Imagen"),
    ("audio", "Audio"),
    ("video", "Video"),
    ("codigo", "Código"),
]

NIVELES_EDUCATIVOS = [
    ("basica", "Básica"),
    ("media", "Media"),
    ("superior", "Superior"),
]

# Create your models here.

class HerramientaIA(models.Model):
    nombre = models.CharField(max_length=100)
    # HU02: Cambio a choices para categorías predefinidas
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_IA)
    nivel_educativo = models.CharField(max_length=50, choices=NIVELES_EDUCATIVOS)
    descripcion = models.TextField()
    diferencias = models.TextField(help_text="Diferencias con otras herramientas similares")
    ejemplos = models.TextField(help_text="Ejemplos prácticos de uso")

    def __str__(self):
        return self.nombre
