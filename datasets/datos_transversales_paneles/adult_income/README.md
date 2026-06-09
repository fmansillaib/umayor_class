# Adult Income

## Descripción
Datos demográficos para predecir si el ingreso es mayor a 50K.

## Target
Income (0=<=50K, 1=>50K) - Clasificación Binaria

## Tamaño
32,561 registros, 12 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Age | int | Edad en años |
| WorkClass | string | Tipo de trabajo |
| Education | string | Nivel de educación |
| EducationNum | int | Número de años de educación |
| MaritalStatus | string | Estado civil |
| Occupation | string | Ocupación |
| Race | string | Raza/Etnicidad |
| Gender | string | Género |
| CapitalGain | int | Ganancia de capital |
| CapitalLoss | int | Pérdida de capital |
| HoursPerWeek | int | Horas trabajadas por semana |
| Income | int | Target: Ingreso (0=<=50K, 1=>50K) |

## Valores Faltantes
Algunos valores '?' en variables categóricas

## Casos de Uso
Clasificación binaria con variables categóricas, desbalanceo de clases

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
