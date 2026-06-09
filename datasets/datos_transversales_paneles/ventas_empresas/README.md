# Ventas Empresas

## Descripción
Datos de empresas con múltiples targets (multi-target learning).

## Target
Revenue (continua), Revenue_Category (categórica), Is_Profitable (binaria)

## Tamaño
500 registros, 16 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Revenue | float | Target 1: Ingresos anuales (USD) |
| Revenue_Category | string | Target 2: Categoría (Bajo/Medio/Alto/Premium) |
| Is_Profitable | int | Target 3: ¿Rentable? (0/1) |

## Valores Faltantes
Ninguno

## Casos de Uso
Multi-target learning, regresión + clasificación simultánea

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
