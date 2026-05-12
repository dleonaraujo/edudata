import joblib
import numpy as np
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Cargar modelo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
modelo = joblib.load(os.path.join(BASE_DIR, 'ml', 'modelo_desercion.pkl'))

@csrf_exempt
def predecir(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        features = np.array([[
            data['docentes'],
            data['matricula'],
            data['ratio_alumno_docente']
        ]])
        
        prediccion = modelo.predict(features)[0]
        probabilidad = modelo.predict_proba(features)[0]
        
        return JsonResponse({
            'riesgo': 'Alto' if prediccion == 1 else 'Bajo',
            'probabilidad_alto': round(float(probabilidad[1]) * 100, 2),
            'probabilidad_bajo': round(float(probabilidad[0]) * 100, 2)
        })
    
    return render(request, 'prediccion/formulario.html')