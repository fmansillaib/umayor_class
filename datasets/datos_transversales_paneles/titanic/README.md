# Titanic

## Descripción
Dataset histórico del naufragio del RMS Titanic con información sobre pasajeros.

## Target
Survived (0=No, 1=Sí) - Clasificación Binaria

## Tamaño
891 registros, 12 variables

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| PassengerId | int | Identificador único |
| Survived | int | Target: ¿Sobrevivió? (0=No, 1=Sí) |
| Pclass | int | Clase del pasaje (1, 2, 3) |
| Name | string | Nombre del pasajero |
| Sex | string | Sexo (male, female) |
| Age | float | Edad en años |
| SibSp | int | Hermanos/cónyuge a bordo |
| Parch | int | Padres/hijos a bordo |
| Ticket | string | Número de boleto |
| Fare | float | Tarifa pagada |
| Cabin | string | Número de cabina (muchos faltantes) |
| Embarked | string | Puerto de embarque (C, Q, S) |

## Valores Faltantes
Age (177), Cabin (687), Embarked (2)

## Casos de Uso
Clasificación binaria, manejo de valores faltantes, feature engineering

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
