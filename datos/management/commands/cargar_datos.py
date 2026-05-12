from django.core.management.base import BaseCommand
import pandas as pd
from datos.models import IndicadorDistrito

class Command(BaseCommand):
    help = 'Carga datos del CSV a la base de datos'

    def handle(self, *args, **kwargs):
        df = pd.read_csv('data/arequipa_educacion.csv')
        df = df[df['provincia'] != 'Total']
        
        contador = 0
        for _, fila in df.iterrows():
            obj, creado = IndicadorDistrito.objects.update_or_create(
                provincia=fila['provincia'],
                anio=int(fila['anio']),
                defaults={
                    'total_alumnos': int(fila['matricula']),
                    'total_docentes': int(fila['docentes']),
                    'ratio_alumno_docente': fila['ratio_alumno_docente'],
                }
            )
            contador += 1
        
        self.stdout.write(f'✅ {contador} registros cargados')