# California Housing

## Descripción
Datos de viviendas de California para predicción de precios.

## Target
MedianHouseValue (100K USD) - Regresión Continua

## Tamaño
20,640 registros, 9 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Longitude | float | Longitud geográfica |
| Latitude | float | Latitud geográfica |
| HousingMedianAge | int | Edad mediana de la vivienda (años) |
| TotalRooms | int | Número total de habitaciones |
| TotalBedrooms | int | Número total de dormitorios |
| Population | int | Población del bloque |
| Households | int | Número de hogares |
| MedianIncome | float | Ingreso mediano del hogar |
| MedianHouseValue | float | Target: Valor mediano de vivienda (100K USD) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión geoespacial, predicción de precios inmobiliarios

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
