# Diabetes

## Descripción
Datos médicos para predicción de diabetes.

## Target
Outcome (0=No, 1=Sí) - Clasificación Binaria

## Tamaño
768 registros, 9 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Pregnancies | int | Número de embarazos |
| Glucose | float | Nivel de glucosa |
| BloodPressure | float | Presión arterial (mmHg) |
| SkinThickness | float | Grosor de la piel (mm) |
| Insulin | float | Nivel de insulina |
| BMI | float | Índice de masa corporal |
| DiabetesPedigreeFunction | float | Función de pedigrí de diabetes |
| Age | int | Edad en años |
| Outcome | int | Target: ¿Tiene diabetes? (0=No, 1=Sí) |

## Valores Faltantes
Ninguno (valores 0 se usan como faltantes)

## Casos de Uso
Clasificación binaria médica, diagnóstico

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
