from django.db import models


# Categorías generales de IA (ej: generación de imágenes, texto, asistentes, etc.)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre




# Modelos de IA específicos
class InteligenciaArtificial(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    usos = models.TextField(help_text="Explica para qué sirve esta IA")
    sitio_web = models.URLField(blank=True, null=True)
    recomendada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='ias')

    def __str__(self):
        return self.nombre
    
    
# Opiniones o reseñas de usuarios sobre una IA
class Reseña(models.Model):
    ia = models.ForeignKey(InteligenciaArtificial, on_delete=models.CASCADE, related_name='reseñas')
    autor = models.CharField(max_length=100)
    comentario = models.TextField()
    puntuacion = models.IntegerField(default=5)  # escala del 1 al 5
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.ia.nombre} por {self.autor}"
    
    
# Recomendaciones personalizadas (por el autor del sitio o automatizadas)
class Recomendacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    ia_relacionadas = models.ManyToManyField(InteligenciaArtificial, blank=True)
    destacada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


# Apartados del sitio web para organizar los temas (como secciones)
class Apartado(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    slug = models.SlugField(unique=True)  # para URL amigables como /apartado/inteligencias-populares

    def __str__(self):
        return self.titulo