# Diccionario de Datos - Precios de Casas

## Descripción General

Dataset con información sobre características de casas y sus precios de venta. Es un dataset ideal para problemas de **regresión continua** y también permite **clasificación de rangos de precios**.

## Tipo de Target
- **Target (Regresión):** `SalePrice` (variable continua)
- **Target (Clasificación):** Categorización de `SalePrice` en rangos
- **Tipo:** Regresión continua con opción de clasificación multiclase

## Variables Principales

| Variable | Tipo | Descripción | Valores/Rango | Uso |
|----------|------|-------------|---------------|-----|
| Id | int | Identificador de la propiedad | Número | ID |
| SalePrice | float | Precio de venta (USD) | 34,900-755,000 | **TARGET** |
| MSSubClass | int | Tipo de vivienda | 20, 30, 40, 45, 50, 60, 70, 75, 80, 85, 90, 120, 150, 160, 180, 190 | Feature (categórica ordinal) |
| MSZoning | string | Clasificación de zona | A, C, FV, I, RH, RL, RP, RM | Feature (categórica) |
| LotFrontage | float | Pies lineales conectados a la calle | 21-313 | Feature (continua, faltantes) |
| LotArea | int | Tamaño del lote (sq ft) | 1,300-215,245 | Feature (continua) |
| Street | string | Tipo de acceso a la calle | Grvl, Pave | Feature (categórica) |
| Alley | string | Tipo de acceso por callejón | Grvl, Pave, NA | Feature (categórica, muchos faltantes) |
| LotShape | string | Forma general del lote | Reg, IR1, IR2, IR3 | Feature (categórica ordinal) |
| LandContour | string | Planitud de la propiedad | Lvl, Bnk, HLS, Low | Feature (categórica) |
| YearBuilt | int | Año de construcción original | 1872-2010 | Feature (continua/temporal) |
| YearRemodAdd | int | Año de remodelación | 1950-2010 | Feature (continua/temporal) |
| GrLivArea | int | Área de vivienda sobre tierra (sq ft) | 334-5,642 | Feature (continua) |
| TotalBsmtSF | float | Área total del sótano (sq ft) | 0-6,110 | Feature (continua) |
| BedroomAbvGr | int | Número de dormitorios | 0-8 | Feature (discreta) |
| BathroomAbvGr | float | Número de baños completos | 0-4 | Feature (discreta) |
| KitchenAbvGr | int | Número de cocinas | 1-3 | Feature (discreta) |
| TotRmsAbvGrd | int | Número total de habitaciones | 2-15 | Feature (discreta) |
| GarageCars | int | Capacidad del garaje (número de autos) | 0-5 | Feature (discreta) |
| GarageArea | int | Área del garaje (sq ft) | 0-1,418 | Feature (continua) |

## Información del Dataset

- **Cantidad de registros:** 1,460 (entrenamiento) + 1,459 (prueba)
- **Cantidad de variables:** 81
- **Variables con valores faltantes:** Múltiples (LotFrontage, Alley, MasVnrType, etc.)
- **Formato:** CSV
- **Fuente:** Kaggle Housing Prices
- **Período:** Casas vendidas 1872-2010

## Tipos de Variables

1. **Continuas:** SalePrice, LotArea, LotFrontage, GrLivArea, TotalBsmtSF, GarageArea, etc.
2. **Discretas:** BedroomAbvGr, BathroomAbvGr, GarageCars, TotRmsAbvGrd, etc.
3. **Ordinales:** MSZoning, LotShape, LandContour, etc.
4. **Nominales:** Street, Alley, CentralAir, PavedDrive, etc.

## Casos de Uso

1. **Regresión Continua:** Predecir SalePrice exacto
2. **Clasificación:** Categorizar casas en rangos de precio (bajo, medio, alto, premium)
3. **Feature Engineering:** Crear variables de área total, edad de la casa
4. **Manejo de valores faltantes:** Múltiples estrategias según variable
5. **Tratamiento de outliers:** Precios inusualmente altos/bajos

## Notas Importantes

- Variable objetivo con distribución sesgada (log-normal)
- Muchas variables categóricas que requieren encoding
- Presencia de outliers en precios
- Variables con muchos valores faltantes (Alley, Fence, MiscFeature)
- Multicolinealidad potencial entre variables de área

## Preprocesamiento típico

1. Remover Id (no predictivo)
2. Transformar SalePrice (log-transform por distribución sesgada)
3. Imputar valores faltantes según tipo
4. Encoding de variables categóricas (one-hot, label)
5. Feature scaling
6. Detección y tratamiento de outliers
7. Feature engineering (edad de la casa, área total, etc.)

## Opciones de Target

### Para Regresión:
- `SalePrice` (continua)

### Para Clasificación:
- Binaria: `is_expensive` (SalePrice > mediana)
- Multiclase: Quartiles (Q1, Q2, Q3, Q4) o categorías (Bajo, Medio, Alto, Premium)
