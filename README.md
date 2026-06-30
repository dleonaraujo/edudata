# edudata

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

## 🚀 Tecnologías

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

## 📁 Estructura del Proyecto
