from django.db import models

# Create your models here.
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    completa = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
