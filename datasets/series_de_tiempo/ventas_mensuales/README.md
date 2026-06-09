# Ventas Mensuales

## Descripción
Ventas mensuales de múltiples categorías y regiones.

## Target
Sales (USD) - Series de Tiempo Multiseries

## Tamaño
3,000 registros, 13 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Date | string | Mes (YYYY-MM) |
| Year | int | Año |
| Month | int | Mes (1-12) |
| Quarter | int | Trimestre (1-4) |
| Product_Category | string | Categoría de producto |
| Region | string | Región geográfica |
| Sales | float | Target: Ventas (USD) |
| Units_Sold | int | Unidades vendidas |
| Marketing_Spend | float | Gasto en marketing (USD) |
| Promotions | int | Número de promociones |
| Price_Per_Unit | float | Precio unitario (USD) |
| Customer_Count | int | Número de clientes |
| Previous_Month_Sales | float | Ventas del mes anterior |

## Valores Faltantes
Ninguno

## Casos de Uso
SARIMA, Prophet, análisis de estacionalidad

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
