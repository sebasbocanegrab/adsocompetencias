from django.db import models

# Create your models here.
class CompetenciaLaboral(models.Model):
    nombre = models.CharField(max_length=90)
    resultados_aprendizaje = models.TextField(max_length=930)
    criterios_evaluacion = models.TextField(max_length=3000)

    # Funcion mostrar el nombre en la tabla de admin.
    def __str__(self): # Se declara la funcion para obtener algo.
        return self.nombre # En este caso obtiene el nombre.