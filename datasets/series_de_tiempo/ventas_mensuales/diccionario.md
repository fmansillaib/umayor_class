# Diccionario de Datos - Ventas Mensuales

## Descripción General

Dataset de series de tiempo con ventas mensuales de múltiples categorías de productos y regiones. Es un dataset sintético pero realista que muestra patrones típicos de series de tiempo comerciales: tendencia, estacionalidad y ciclos.

## Tipo de Target
- **Target:** `Sales` (ventas en USD) - Variable continua
- **Tipo:** Serie multivariada con múltiples series paralelas por categoría/región

## Variables

| Variable | Tipo | Descripción | Valores/Rango | Uso |
|----------|------|-------------|---------------|-----|
| Date | date | Mes de reporte | YYYY-MM | Índice temporal |
| Year | int | Año | 2015-2024 | Feature derivada/temporal |
| Month | int | Mes | 1-12 | Feature derivada/estacionalidad |
| Quarter | int | Trimestre | 1-4 | Feature derivada/ciclo |
| Product_Category | string | Categoría de producto | Electronics, Clothing, Home, Food, Beauty | Feature (categórica) |
| Region | string | Región de venta | North, South, East, West, Central | Feature (categórica) |
| Sales | float | Ventas en USD | 5,000-150,000 | **TARGET** |
| Units_Sold | int | Unidades vendidas | 100-3,000 | Feature (correlacionada) |
| Marketing_Spend | float | Gasto en marketing (USD) | 500-10,000 | Feature (explicativa) |
| Promotions | int | Número de promociones | 0-5 | Feature (actividad) |
| Price_Per_Unit | float | Precio unitario (USD) | 5-500 | Feature (dinámica) |
| Customer_Count | int | Cantidad de clientes nuevos | 10-500 | Feature (indicador) |
| Previous_Month_Sales | float | Ventas del mes anterior | Valores reales | Feature (autorregresiva) |

## Información del Dataset

- **Cantidad de registros:** 600 (10 años × 12 meses × 5 categorías)
- **Cantidad de variables:** 13
- **Períodos:** Enero 2015 - Diciembre 2024
- **Categorías:** 5 (Electronics, Clothing, Home, Food, Beauty)
- **Regiones:** 5 (North, South, East, West, Central)
- **Formato:** CSV
- **Fuente:** Dataset sintético para educación

## Características de las Series

1. **Tendencia:** Crecimiento general sobre el período
2. **Estacionalidad:** Patrones mensuales y trimestrales
   - Picos: Noviembre-Diciembre (holidays)
   - Valles: Enero-Febrero (post-holidays)
3. **Ciclos:** Patrones que se repiten cada 2-3 años
4. **Volatilidad:** Variación irregular aleatoria
5. **Múltiples series:** Una para cada categoría × región

## Estructura de Series

```
Univariada simple:
Fecha → Sales (1 serie)

Multivariada por categoría:
Fecha → Sales_Electronics, Sales_Clothing, Sales_Home, Sales_Food, Sales_Beauty
(5 series en paralelo)

Multivariada con exógenas:
Fecha → Sales, Marketing_Spend, Units_Sold, Promotions
(variables explicativas)
```

## Casos de Uso

1. **Pronóstico univariado:** Predecir ventas totales de los próximos 3-12 meses
2. **Pronóstico por categoría:** Proyecciones separadas por producto
3. **Pronóstico multivariado:** Usar Marketing_Spend y otras exógenas
4. **Descomposición:** Separar tendencia, estacionalidad y residuos
5. **Análisis de impacto:** Efecto de marketing en ventas
6. **Detección de anomalías:** Meses con ventas inusitadamente altas/bajas

## Técnicas Aplicables

| Técnica | Aplicación |
|---------|-----------|
| ARIMA | Capturar autocorrelación y diferenciación |
| SARIMA | Modelar estacionalidad mensual |
| Exponential Smoothing | Suavizamiento de tendencia y estacionalidad |
| Prophet | Pronóstico con cambios de tendencia y holidays |
| ARIMAX | Incluir variables exógenas (Marketing_Spend) |
| VAR/VARIMA | Correlaciones entre categorías |
| LSTM/GRU | Redes neuronales para secuencias |
| XGBoost Time Series | Features temporales con ML |

## Patrones Esperados

### Estacionalidad Mensual

| Mes | Patrón | Razón |
|-----|--------|-------|
| Enero-Febrero | Bajo | Post-holidays, presupuestos reducidos |
| Marzo-Abril | Medio | Recuperación gradual |
| Mayo-Octubre | Medio-Alto | Actividad de verano/actividad comercial |
| Noviembre-Diciembre | Muy Alto | Black Friday, Navidad, fin de año |

### Variación por Categoría

- **Electronics:** Muy estacional (altos en holidays)
- **Clothing:** Moderadamente estacional
- **Home:** Relativamente estable
- **Food:** Muy estable (menos sensible a temporada)
- **Beauty:** Moderadamente estacional

## Notas Importantes

- **No hay faltantes:** Datos completos por diseño
- **Estacionariedad:** Sales NO es estacionaria (tiene tendencia)
- **Diferenciar:** Sales[t] - Sales[t-1] o Sales[t] - Sales[t-12]
- **Múltiples series:** Permite análisis univariado o multivariado
- **Variables exógenas:** Marketing_Spend impacta Sales

## Preprocesamiento Típico

1. Agrupar por categoría o región según análisis
2. Crear features temporales (Year, Month, Quarter, DayOfWeek_equivalent)
3. Crear variables autorregresivas (Lag de Sales)
4. Diferenciación para estacionariedad
5. Log-transform si es necesario (para reducir heterocedasticidad)
6. Normalización si se usa redes neuronales
7. Train-test split respetando orden temporal

## Ventanas de Predicción Posibles

```
Período adelante:
- 1 mes adelante: Sales[t+1] dado datos hasta t
- 3 meses: Predecir próximo trimestre
- 12 meses: Pronóstico anual
- Multi-paso: Predecir secuencia de 12 meses

Lookback (ventana histórica):
- 3 meses: Usar últimos 3 meses para predecir
- 12 meses: Usar año completo (captura estacionalidad)
- 24 meses: Usar 2 años (captura ciclos)
```

## Análisis de Estacionariedad

- **Sales:** NO estacionaria (tiene tendencia creciente)
- **Sales - Lag1:** Más estacionaria
- **Sales - Lag12:** Remueve estacionalidad (mejor)
- **Diff Log Sales:** Similar al retorno relativo
- **YoY Growth:** Crecimiento año a año (más estacionario)

## Ejemplo de Estructura

| Date | Year | Month | Quarter | Product_Category | Region | Sales | Units_Sold | Marketing_Spend | Promotions | Price_Per_Unit | Customer_Count | Previous_Month_Sales |
|------|------|-------|---------|------------------|--------|-------|-----------|-----------------|-----------|----------------|----------------|----------------------|
| 2015-01 | 2015 | 1 | 1 | Electronics | North | 45000 | 250 | 3000 | 1 | 180 | 85 | 52000 |
| 2015-02 | 2015 | 2 | 1 | Electronics | North | 42000 | 230 | 2500 | 0 | 180 | 75 | 45000 |
| 2015-03 | 2015 | 3 | 1 | Electronics | North | 48000 | 270 | 3200 | 2 | 175 | 95 | 42000 |
| 2015-12 | 2015 | 12 | 4 | Electronics | North | 125000 | 800 | 8000 | 5 | 155 | 350 | 98000 |

## Integración con Otras Variables

- **Marketing_Spend:** Correlacionado positivamente con Sales
- **Promotions:** Aumenta Units_Sold y Sales
- **Price_Per_Unit:** Afecta negativa pero moderadamente
- **Customer_Count:** Indicador adelantado de Sales futura
- **Previous_Month_Sales:** Autorregresión clara (momentum)
