# Salary Prediction

## Descripción
Datos de empleados para predicción de salarios.

## Target
Salary (USD) - Regresión Continua

## Tamaño
1,000 registros, 8 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| YearsExperience | int | Años de experiencia |
| DegreeType | string | Tipo de grado (HighSchool, Bachelor, etc) |
| Major | string | Carrera profesional |
| GPA | float | Promedio de calificaciones (0-4) |
| YearsAtCompany | int | Años en la empresa actual |
| Department | string | Departamento |
| JobLevel | int | Nivel de trabajo (1-5) |
| Salary | float | Target: Salario anual (USD) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión de recursos humanos, predicción salarial

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
