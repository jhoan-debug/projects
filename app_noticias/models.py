from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)