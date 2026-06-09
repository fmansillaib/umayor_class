# Precios Acciones

## Descripción
Precios históricos diarios de 5 acciones tecnológicas.

## Target
Close (Precio de cierre) - Series de Tiempo

## Tamaño
~27,385 registros, 11 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Date | date | Fecha de transacción |
| Stock_Symbol | string | Símbolo del ticker (AAPL, GOOGL, MSFT, AMZN, TSLA) |
| Open | float | Precio de apertura |
| High | float | Precio máximo del día |
| Low | float | Precio mínimo del día |
| Close | float | Target: Precio de cierre |
| Volume | int | Volumen de transacciones |
| Adj_Close | float | Precio de cierre ajustado |
| Daily_Return | float | Retorno porcentual diario |
| MA_5 | float | Media móvil 5 días |
| MA_20 | float | Media móvil 20 días |

## Valores Faltantes
Ninguno (solo días de bolsa)

## Casos de Uso
Pronóstico de series de tiempo, ARIMA, LSTM

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
