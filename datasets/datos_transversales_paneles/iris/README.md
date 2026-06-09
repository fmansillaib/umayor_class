# Iris

## Descripción
Dataset clásico con características de flores de tres especies diferentes.

## Target
Species (setosa, versicolor, virginica) - Clasificación Multiclase

## Tamaño
150 registros, 5 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| SepalLength | float | Largo del sépalo (cm) |
| SepalWidth | float | Ancho del sépalo (cm) |
| PetalLength | float | Largo del pétalo (cm) |
| PetalWidth | float | Ancho del pétalo (cm) |
| Species | string | Target: Especie de flor |

## Valores Faltantes
Ninguno

## Casos de Uso
Clasificación multiclase, PCA, clustering

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
