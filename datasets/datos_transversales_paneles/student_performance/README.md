# Student Performance

## Descripción
Datos de estudiantes para predecir sus calificaciones finales.

## Target
FinalGrade (0-20) - Regresión Continua

## Tamaño
649 registros, 8 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Age | int | Edad del estudiante |
| StudyHours | float | Horas de estudio por semana |
| PreviousGrades | float | Promedio de calificaciones anteriores |
| AbsencesCount | float | Número de ausencias |
| ParentalEducation | int | Educación de padres (1-4) |
| FamilyIncome | int | Ingresos familiares (1-4) |
| HealthStatus | float | Estado de salud (1-5) |
| FinalGrade | float | Target: Calificación final (0-20) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión educacional, predicción de desempeño

## Cómo Usar

```python
import pandas as pd

df = pd.read_csv('datos.csv')
df.head()
df.info()
df.describe()
```

## Notas
- Todos los datos están en formato CSV
- Las variables están en inglés
- No requiere autenticación para acceder
