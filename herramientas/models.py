from django.db import models

# Create your models here.

class HerramientaIA(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    diferencias = models.TextField(help_text="Diferencias con otras herramientas similares")
    ejemplos = models.TextField(help_text="Ejemplos prácticos de uso")

    def __str__(self):
        return self.nombre
