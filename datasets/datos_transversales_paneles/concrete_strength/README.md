# Concrete Strength

## Descripción
Componentes de mezcla de concreto y su resistencia.

## Target
Strength (MPa) - Regresión Continua

## Tamaño
1,030 registros, 9 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Cement | int | Contenido de cemento (kg en 1 m³) |
| BlastFurnaceSlag | int | Escoria de horno alto (kg en 1 m³) |
| FlyAsh | int | Ceniza volante (kg en 1 m³) |
| Water | int | Agua (kg en 1 m³) |
| Superplasticizer | float | Superplastificante (kg en 1 m³) |
| CoarseAggregate | int | Árido grueso (kg en 1 m³) |
| FineAggregate | int | Árido fino (kg en 1 m³) |
| Age | int | Edad del concreto (días) |
| Strength | float | Target: Resistencia a compresión (MPa) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión de materiales, ingeniería civil

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
