# Precios Casas

## Descripción
Características de viviendas para predicción de precio.

## Target
SalePrice (USD) - Regresión Continua

## Tamaño
1,460 registros, 20 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| SalePrice | int | Target: Precio de venta (USD) |
| GrLivArea | int | Área de vivienda sobre tierra (sq ft) |
| YearBuilt | int | Año de construcción |
| YearRemodAdd | int | Año de remodelación |
| BedroomAbvGr | int | Número de dormitorios |
| BathroomAbvGr | int | Número de baños completos |
| GarageCars | int | Capacidad del garaje (número de autos) |

## Valores Faltantes
LotFrontage (~18%)

## Casos de Uso
Regresión inmobiliaria, feature engineering

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
