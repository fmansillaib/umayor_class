# Diccionario de Datos - Titanic

## Descripción General

Dataset histórico del naufragio del RMS Titanic. Contiene información sobre pasajeros y si sobrevivieron o no. Es un dataset ideal para problemas de **clasificación binaria**.

## Tipo de Target
- **Target:** `Survived` (variable dicotómica)
- **Tipo:** Clasificación Binaria (0 = No sobrevivió, 1 = Sobrevivió)

## Variables

| Variable | Tipo | Descripción | Valores/Rango | Uso |
|----------|------|-------------|---------------|-----|
| PassengerId | int | Identificador único del pasajero | 1-891 | ID |
| Survived | int | Variable objetivo: ¿Sobrevivió? | 0, 1 | **TARGET** |
| Pclass | int | Clase del pasaje | 1, 2, 3 | Feature (categórica ordinal) |
| Name | string | Nombre del pasajero | Texto libre | ID/Feature (extraer título) |
| Sex | string | Sexo del pasajero | male, female | Feature (categórica) |
| Age | float | Edad en años | 0.42-80.0 | Feature (continua) |
| SibSp | int | Número de hermanos/cónyuge a bordo | 0-8 | Feature (discreta) |
| Parch | int | Número de padres/hijos a bordo | 0-6 | Feature (discreta) |
| Ticket | string | Número de boleto | Texto | ID |
| Fare | float | Tarifa pagada | 0-512.33 | Feature (continua) |
| Cabin | string | Número de cabina | Texto | Feature (categórica, muchos faltantes) |
| Embarked | string | Puerto de embarque | C, Q, S | Feature (categórica) |

## Información del Dataset

- **Cantidad de registros:** 891
- **Cantidad de variables:** 12
- **Variables con valores faltantes:** Age (177), Cabin (687), Embarked (2)
- **Formato:** CSV
- **Fuente:** Kaggle Titanic Dataset
- **Período:** 1912
- **Balanceo del target:** ~38% sobrevivió, ~62% no sobrevivió

## Casos de Uso

1. **Clasificación Binaria:** Predecir si un pasajero sobrevivió
2. **Feature Engineering:** Extraer título del nombre, crear variables de familia
3. **Manejo de valores faltantes:** Imputación de Age y Cabin
4. **Desbalanceo de clases:** Tratar el desbalanceo de la variable objetivo

## Notas Importantes

- Imbalancia en la variable objetivo (~62% - 38%)
- Presencia significativa de valores faltantes en Cabin
- Variables categóricas que requieren encoding
- Oportunidad para feature engineering (ej: extraer títulos, tamaño de familia)

## Preprocesamiento típico

1. Remover PassengerId, Ticket (ID)
2. Imputar Age (media, mediana, modelo)
3. Imputar Embarked (moda)
4. Encoding: Sex, Embarked, posiblemente Cabin
5. Feature scaling si es necesario (para algunos modelos)
