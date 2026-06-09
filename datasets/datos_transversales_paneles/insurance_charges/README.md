# Insurance Charges

## Descripción
Datos personales para predicción de costos de seguros.

## Target
Charges (USD) - Regresión Continua

## Tamaño
1,338 registros, 7 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Age | int | Edad (18-64) |
| Sex | string | Género (male/female) |
| BMI | float | Índice de masa corporal |
| Children | int | Número de hijos |
| Smoker | int | ¿Fuma? (0/1) |
| Region | string | Región de residencia |
| Charges | float | Target: Costo del seguro (USD) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión asegurada, pricing

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
