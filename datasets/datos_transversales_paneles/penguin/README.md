# Penguin

## Descripción
Características físicas de pingüinos de tres especies diferentes.

## Target
Species (Adelie, Chinstrap, Gentoo) - Clasificación Multiclase

## Tamaño
344 registros, 5 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| CulmenLength | float | Largo del culmen (mm) |
| CulmenDepth | float | Profundidad del culmen (mm) |
| FlipperLength | float | Largo de la aleta (mm) |
| BodyMass | int | Masa corporal (g) |
| Species | string | Target: Especie de pingüino |

## Valores Faltantes
Ninguno

## Casos de Uso
Clasificación multiclase, análisis exploratorio

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
