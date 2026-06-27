import unittest
import pandas as pd
import numpy as np

class TestModuloIntegracionDatos(unittest.TestCase):

    def setUp(self):
        """Simular un DataFrame con la estructura del Censo Escolar del MINEDU."""
        self.datos_provinciales_mock = pd.DataFrame({
            'PROVINCIA': ['AREQUIPA', 'CAYLLOMA', 'CONDESUYOS'],
            'RATIO_ALU_DOC': [18.2, 12.4, 14.1],
            'SERVICIOS_BASICOS': [92.5, 45.0, 38.2],
            'CONECTIVIDAD': [88.0, 20.5, 15.0]
        })

    def test_limpieza_valores_nulos(self):
        """Asegurar que el script detecte o elimine filas con valores nulos (Semana 4)."""
        # Insertar un valor nulo de prueba
        df_corrupto = self.datos_provinciales_mock.copy()
        df_corrupto.loc[1, 'RATIO_ALU_DOC'] = np.nan
        
        # Ejecutar tu lógica de limpieza (por ejemplo, imputar con la media o eliminar)
        df_limpio = df_corrupto.dropna() 
        
        # Verificar integridad
        self.assertFalse(df_limpio.isnull().values.any())
        self.assertEqual(len(df_limpio), 2)

    def test_filtrado_exclusivo_arequipa(self):
        """Garantizar que solo se procesen datos correspondientes a la región Arequipa."""
        df_nacional_mock = pd.DataFrame({
            'PROVINCIA': ['AREQUIPA', 'LIMA', 'CUSCO'],
            'RATIO_ALU_DOC': [18.2, 22.0, 19.5]
        })
        
        # Lógica de filtrado regional/provincial aplicada en tu proyecto
        provincias_validas = ['AREQUIPA', 'CAMANA', 'CARAVELI', 'CASTILLA', 'CAYLLOMA', 'CONDESUYOS', 'ISLAY', 'LA UNION']
        df_filtrado = df_nacional_mock[df_nacional_mock['PROVINCIA'].isin(provincias_validas)]
        
        self.assertEqual(len(df_filtrado), 1)
        self.assertNotIn('LIMA', df_filtrado['PROVINCIA'].values)

if __name__ == '__main__':
    unittest.main()