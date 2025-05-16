from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
#    imagen = models.ImageField(upload_to='proyectos/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
