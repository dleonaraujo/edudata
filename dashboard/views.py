from django.shortcuts import render
from datos.models import IndicadorDistrito
import json


def index(request):
    datos_2025 = IndicadorDistrito.objects.filter(anio=2025).order_by('provincia')
    provincias = [d.provincia for d in datos_2025]
    matriculas = [d.total_alumnos for d in datos_2025]
    ratios = [d.ratio_alumno_docente for d in datos_2025]
    alto = sum(1 for r in ratios if r > 14)
    bajo = len(ratios) - alto
    anios = [2022, 2023, 2024, 2025]
    series = []
    for prov in provincias:
        datos_prov = []
        for anio in anios:
            try:
                d = IndicadorDistrito.objects.get(provincia=prov, anio=anio)
                datos_prov.append(d.total_alumnos)
            except Exception:
                datos_prov.append(0)
        series.append({'provincia': prov, 'datos': datos_prov})
    context = {
        'total_provincias': len(provincias),
        'total_alumnos': sum(matriculas),
        'total_docentes': sum([d.total_docentes for d in datos_2025]),
        'ratio_promedio': round(sum(ratios) / len(ratios), 2),
        'provincias_json': json.dumps(provincias),
        'matriculas_json': json.dumps(matriculas),
        'ratios_json': json.dumps(ratios),
        'riesgos_json': json.dumps([alto, bajo]),
        'evolucion_json': json.dumps({'anios': anios, 'series': series}),
    }
    return render(request, 'dashboard/index.html', context)

def comparativo(request):
    from datos.models import IndicadorDistrito
    import json

    todos = IndicadorDistrito.objects.all().values(
        'provincia', 'anio', 'total_alumnos', 
        'total_docentes', 'ratio_alumno_docente'
    )
    
    datos = []
    for d in todos:
        datos.append({
            'provincia': d['provincia'],
            'anio': d['anio'],
            'total_alumnos': d['total_alumnos'],
            'total_docentes': d['total_docentes'],
            'ratio': d['ratio_alumno_docente']
        })

    provincias = list(IndicadorDistrito.objects.values_list(
        'provincia', flat=True
    ).distinct().order_by('provincia'))

    return render(request, 'dashboard/comparativo.html', {
        'provincias': provincias,
        'datos_json': json.dumps(datos)
    })