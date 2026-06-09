# Breast Cancer

## Descripción
Características de tumores de mama para diagnóstico.

## Target
Diagnosis (0=Benigno, 1=Maligno) - Clasificación Binaria

## Tamaño
569 registros, 11 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| MeanRadius | float | Radio medio del tumor |
| MeanTexture | float | Textura media |
| MeanPerimeter | float | Perímetro medio |
| MeanArea | float | Área media |
| MeanSmoothness | float | Suavidad media |
| MeanCompactness | float | Compacidad media |
| MeanConcavity | float | Concavidad media |
| MeanConcavePoints | float | Puntos cóncavos medios |
| MeanSymmetry | float | Simetría media |
| MeanFractalDimension | float | Dimensión fractal media |
| Diagnosis | int | Target: Diagnóstico (0=Benigno, 1=Maligno) |

## Valores Faltantes
Ninguno

## Casos de Uso
Clasificación binaria, diagnóstico médico

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
