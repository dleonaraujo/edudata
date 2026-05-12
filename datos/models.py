from django.db import models

class IndicadorDistrito(models.Model):
    provincia = models.CharField(max_length=100)
    anio = models.IntegerField()
    total_alumnos = models.IntegerField(null=True, blank=True)
    total_docentes = models.IntegerField(null=True, blank=True)
    ratio_alumno_docente = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ['provincia', 'anio']
        ordering = ['anio', 'provincia']

    def __str__(self):
        return f"{self.provincia} ({self.anio})"