# Boston Housing

## Descripción
Precios de viviendas en Boston con variables socioeconómicas.

## Target
MEDV (Precio mediano en miles) - Regresión Continua

## Tamaño
506 registros, 14 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| CRIM | float | Tasa de criminalidad per cápita |
| ZN | float | % de tierra zoneada para lotes >25,000 sq.ft |
| INDUS | float | % de acres no minoristas |
| CHAS | int | ¿Limita con río Charles? (1=Sí, 0=No) |
| NOX | float | Concentración de óxidos de nitrógeno |
| RM | float | Número promedio de habitaciones |
| AGE | int | % de unidades construidas antes de 1940 |
| DIS | float | Distancia ponderada a centros de empleo |
| RAD | int | Índice de accesibilidad a carreteras radiales |
| TAX | int | Tasa de impuesto a la propiedad |
| PTRATIO | float | Ratio estudiante-profesor |
| B | float | 1000(Bk - 0.63)^2 donde Bk es proporción de afroamericanos |
| LSTAT | float | % de población de estatus bajo |
| MEDV | float | Target: Precio mediano (miles de dólares) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión lineal, análisis socioeconómico

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
