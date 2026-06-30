#  EduData — Plataforma Web de Predicción de Deserción Escolar

Plataforma web desarrollada con Django y Python que integra datos reales del Censo Escolar del MINEDU para **predecir el riesgo de deserción escolar a nivel provincial en la región Arequipa, Perú**, mediante un modelo de clasificación Random Forest.

---

##  Descripción

EduData procesa datos del portal ESCALE del MINEDU (2022-2025) de las 8 provincias de Arequipa, calcula indicadores clave como el ratio alumno-docente y expone una interfaz web donde el usuario puede:

- Ver un **dashboard interactivo** con gráficos estadísticos
- **Predecir el riesgo** de deserción ingresando indicadores provinciales
- **Comparar** indicadores entre dos provincias
- Gestionar el acceso con **roles diferenciados** (administrador y consultor)

---

##  Tecnologías

| Componente | Tecnología |
|---|---|
| Backend | Python 3.12 + Django 5.x |
| Base de datos | PostgreSQL (Supabase) / SQLite (desarrollo) |
| Machine Learning | Scikit-learn — Random Forest Classifier |
| Visualización | Chart.js |
| Calidad de código | CodeFactor A+ |
| Control de versiones | GitHub |
| Alojamiento BD | Supabase |

---

##  Estructura del Proyecto

---

##  Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/dleonaraujo/edudata.git
cd edudata
```

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
SECRET_KEY=tu-secret-key
DEBUG=True
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=tu-password
DB_HOST=db.xxxx.supabase.co
DB_PORT=5432
```

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Cargar datos del MINEDU
```bash
python manage.py cargar_datos
```

### 7. Crear superusuario
```bash
python manage.py createsuperuser
```

### 8. Correr el servidor
```bash
python manage.py runserver
```

Abre en el navegador: `http://127.0.0.1:8000`

---

##  Pruebas Unitarias

```bash
python manage.py test prediccion
python manage.py test datos
```

**Casos de prueba implementados:**
- `test_control_acceso_anonimo` — Usuario no autenticado es redirigido
- `test_prediccion_valores_validos` — Predictor responde correctamente
- `test_prediccion_valores_invalidos` — Backend no retorna error 500
- `test_limpieza_valores_nulos` — ETL elimina filas con nulos
- `test_filtrado_exclusivo_arequipa` — Solo procesa las 8 provincias arequipeñas

---

##  Modelo de Machine Learning

- **Algoritmo:** Random Forest Classifier (Scikit-learn)
- **Variables de entrada:** total_docentes, total_alumnos, ratio_alumno_docente
- **Variable objetivo:** Riesgo Alto (ratio > 14) / Riesgo Bajo
- **Accuracy:** 100% sobre conjunto de prueba
- **Datos:** 32 registros (8 provincias × 4 años: 2022-2025)
- **Tiempo de respuesta:** < 2 segundos

---

##  URLs del Sistema

| URL | Descripción | Acceso |
|---|---|---|
| `/login/` | Inicio de sesión | Público |
| `/dashboard/` | Dashboard principal | Autenticado |
| `/predecir/` | Motor de predicción | Autenticado |
| `/comparativo/` | Análisis comparativo | Administrador |
| `/admin/` | Panel de administración | Administrador |

---



##  Autor

**Diego Leon Araujo**  
Universidad La Salle — Ingeniería de Software  
Arequipa, Perú — 2026

---

## Licencia

Este proyecto está bajo la licencia MIT.
