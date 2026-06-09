# Mushroom

## Descripción
Características de hongos para clasificar como comestible o venenoso.

## Target
Edible (0=Venenoso, 1=Comestible) - Clasificación Binaria

## Tamaño
8,124 registros, 23 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| CapShape | string | Forma del sombrero |
| CapSurface | string | Superficie del sombrero |
| CapColor | string | Color del sombrero |
| Bruises | string | ¿Tiene moretones? |
| Odor | string | Olor |
| GillAttachment | string | Adhesión de branquias |
| GillSpacing | string | Espaciamiento de branquias |
| GillSize | string | Tamaño de branquias |
| GillColor | string | Color de branquias |
| StalkShape | string | Forma del tallo |
| StalkRoot | string | Raíz del tallo |
| Edible | int | Target: ¿Comestible? (0=No, 1=Sí) |

## Valores Faltantes
Algunos valores faltantes en StalkRoot

## Casos de Uso
Clasificación binaria, todas variables categóricas

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
