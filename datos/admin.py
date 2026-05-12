from django.contrib import admin
from .models import IndicadorDistrito

@admin.register(IndicadorDistrito)
class IndicadorDistritoAdmin(admin.ModelAdmin):
    list_display = ['provincia', 'anio', 'total_alumnos', 
                    'total_docentes', 'ratio_alumno_docente']
    list_filter = ['anio', 'provincia']
    search_fields = ['provincia']