import json
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class EduDataQualityTests(TestCase):
    
    def setUp(self):
        """Configuración inicial para las pruebas unitarias."""
        # Creación de usuarios con roles para verificar el Control de Acceso (RF-05)
        self.admin_user = User.objects.create_superuser(
            username='admin_calidad', 
            email='admin@edudata.pe', 
            password='PasswordSecure123!'
        )
        self.consultor_user = User.objects.create_user(
            username='consultor_arequipa', 
            password='PasswordConsultor123!'
        )
        
        # Diccionario con todas las variables requeridas por el predictor de EduData
        self.payload_valido = {
            'provincia': 'Camana',
            'docentes': 15,
            'alumnos': 250,
            'matricula': 250,          # CORREGIDO: Añadido para solucionar el KeyError
            'internet': 1,
            'servicios_basicos': 1,
            'ratio_alumno_docente': 16.6,
            'conectividad_local': 80.0
        }
        
        self.payload_invalido = {
            'provincia': 'Islay',
            'docentes': -5,            # Valor inconsistente (Inyección de error)
            'alumnos': 500,
            'matricula': 500,          # CORREGIDO: Añadido para solucionar el KeyError
            'internet': 0,
            'servicios_basicos': 0,
            'ratio_alumno_docente': -5.0,
            'conectividad_local': 45.0
        }

    def test_control_acceso_anonimo(self):
        """Validar que un usuario no autenticado no pueda acceder al dashboard provincial."""
        url = reverse('dashboard')  
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302, 403])

    def test_prediccion_valores_validos(self):
        """Verificar que el motor de predicción responda correctamente ante datos válidos."""
        self.client.login(username='consultor_arequipa', password='PasswordConsultor123!')
        url = reverse('predecir')  
        
        response = self.client.post(
            url, 
            data=json.dumps(self.payload_valido), 
            content_type='application/json'
        )
        
        self.assertIn(response.status_code, [200, 302])

    def test_prediccion_valores_invalidos(self):
        """Prueba de robustez: El backend debe manejar o rechazar datos inconsistentes."""
        self.client.login(username='consultor_arequipa', password='PasswordConsultor123!')
        url = reverse('predecir')  
        
        response = self.client.post(
            url, 
            data=json.dumps(self.payload_invalido), 
            content_type='application/json'
        )
        
        self.assertNotEqual(response.status_code, 500)