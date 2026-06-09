# Air Quality

## Descripción
Mediciones de contaminación del aire y variables meteorológicas.

## Target
PM2_5 (μg/m³) - Regresión Continua

## Tamaño
1,320 registros, 8 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| SO2 | float | Dióxido de azufre (μg/m³) |
| NO2 | float | Dióxido de nitrógeno (μg/m³) |
| O3 | float | Ozono (μg/m³) |
| Temperature | float | Temperatura (°C) |
| Humidity | float | Humedad relativa (%) |
| Pressure | float | Presión atmosférica (hPa) |
| WindSpeed | float | Velocidad del viento (m/s) |
| PM2_5 | float | Target: Partículas PM2.5 (μg/m³) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión ambiental, predicción de contaminación

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
