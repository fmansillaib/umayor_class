# Energy Efficiency

## Descripción
Características de edificios para predecir carga térmica.

## Target
Y1 (Heating Load), Y2 (Cooling Load) - Regresión Multi-salida

## Tamaño
768 registros, 10 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| X1 | float | Compacidad (relativa) |
| X2 | int | Área de superficie |
| X3 | float | Área de pared |
| X4 | float | Área de techo |
| X5 | float | Orientación |
| X6 | float | Área de acristalamiento |
| X7 | int | Distribución del área de acristalamiento |
| X8 | float | Área de superficie del edificio |
| Y1 | float | Target: Carga de calefacción (kWh) |
| Y2 | float | Target: Carga de refrigeración (kWh) |

## Valores Faltantes
Ninguno

## Casos de Uso
Regresión multi-salida, eficiencia energética

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
