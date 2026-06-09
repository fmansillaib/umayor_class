# Car Prices

## Descripción
Características de autos usados para predicción de precio.

## Target
Price (USD) - Regresión Continua

## Tamaño
1,000 registros, 9 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Year | int | Año del modelo |
| Mileage | int | Kilómetros recorridos |
| EngineSize | float | Tamaño del motor (L) |
| BHP | int | Caballos de potencia |
| Seats | int | Número de asientos |
| Doors | int | Número de puertas |
| Transmission | string | Tipo (Manual/Automatic) |
| FuelType | string | Tipo de combustible |
| Price | float | Target: Precio (USD) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión con variables categóricas, pricing

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
