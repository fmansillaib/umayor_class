# Determinantes del Salario

## Descripción
Dataset para analizar los factores que determinan el salario de los trabajadores, incluyendo años de educación, experiencia laboral y variables demográficas. Es ideal para modelos de regresión lineal y ecuaciones de Mincer.

## Target
salario - Regresión (Variable continua)

## Tamaño
525 registros, 9 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| salario | float | Salario (Target) |
| educ | int | Años de educación |
| exper | int | Años de experiencia laboral |
| perm | int | Años de permanencia/antigüedad en el trabajo actual |
| marr | int | Estado civil: casado (1=Sí, 0=No) |
| #dep | int | Número de dependientes |
| nort | int | Vive en la región Norte (1=Sí, 0=No) |
| sur | int | Vive en la región Sur (1=Sí, 0=No) |
| oeste | int | Vive en la región Oeste (1=Sí, 0=No) |

## Valores Faltantes
No tiene valores nulos aparentes.

## Casos de Uso
Regresión lineal, análisis econométrico (Ecuación de Mincer), inferencia estadística.

## Cómo Usar

```python
import pandas as pd

df = pd.read_csv('datos.csv')
df.head()
df.info()
df.describe()
```

## Notas
- Los datos están en formato CSV.
- Algunas variables numéricas como "salario" pueden contener comas (",") como separador decimal en su formato original.
