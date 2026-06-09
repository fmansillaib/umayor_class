# Wine

## Descripción
Características químicas de vinos de diferentes cultivares.

## Target
Cultivar (1, 2, 3) - Clasificación Multiclase

## Tamaño
178 registros, 14 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Alcohol | float | Contenido de alcohol (%) |
| MalicAcid | float | Ácido málico |
| Ash | float | Cenizas |
| AshAlkalinity | float | Alcalinidad de la ceniza |
| Magnesium | int | Magnesio |
| Phenols | float | Fenoles totales |
| Flavanoids | float | Flavonoides |
| NonflavanoidPhenols | float | Fenoles no flavanoides |
| Proanthocyanins | float | Proantocianinas |
| ColorIntensity | float | Intensidad de color |
| Hue | float | Tonalidad |
| OD280 | float | OD280/OD315 |
| Proline | int | Prolina |
| Cultivar | int | Target: Cultivar del vino |

## Valores Faltantes
Ninguno

## Casos de Uso
Clasificación multiclase, análisis químico

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
