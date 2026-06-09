# Diccionario de Datos - Precios de Acciones

## Descripción General

Dataset de series de tiempo con datos históricos de precios de acciones de empresas tecnológicas. Contiene precios diarios de cierre y volumen de transacciones, ideal para aprender técnicas de análisis de series de tiempo.

## Tipo de Target
- **Target:** `Close` (precio de cierre) - Variable continua para predicción de próximo valor
- **Tipo:** Serie de tiempo univariada o multivariada (usando OHLCV)

## Variables

| Variable | Tipo | Descripción | Valores/Rango | Uso |
|----------|------|-------------|---------------|-----|
| Date | date | Fecha de transacción | YYYY-MM-DD | Índice temporal |
| Stock_Symbol | string | Símbolo del ticker | AAPL, GOOGL, MSFT, AMZN, TSLA | Feature (identificador) |
| Open | float | Precio de apertura | Valores reales | Feature (OHLC) |
| High | float | Precio máximo del día | Valores reales | Feature (OHLC) |
| Low | float | Precio mínimo del día | Valores reales | Feature (OHLC) |
| Close | float | Precio de cierre | Valores reales | **TARGET** (próximo valor) |
| Volume | int | Volumen de acciones transadas | Números enteros | Feature (momentum) |
| Adj_Close | float | Precio de cierre ajustado | Valores reales | Feature (alternativa) |
| Daily_Return | float | Retorno porcentual diario | -10% a +10% | Feature derivada |
| MA_5 | float | Media móvil 5 días | Valores reales | Feature derivada |
| MA_20 | float | Media móvil 20 días | Valores reales | Feature derivada |

## Información del Dataset

- **Cantidad de registros:** ~5,000 (aprox. 20 años de datos diarios)
- **Cantidad de variables:** 11
- **Empresas incluidas:** 5 (Apple, Google, Microsoft, Amazon, Tesla)
- **Período:** Aproximadamente 2003-2023
- **Frecuencia:** Diaria (solo días de bolsa)
- **Formato:** CSV
- **Fuente:** Datos históricos públicos (Yahoo Finance simulado)

## Estructura de Series de Tiempo

```
Índice temporal (Date) → Observaciones ordenadas cronológicamente
Cada observación = Precios OHLC + Volumen
```

## Características de las Series

1. **Tendencia:** Crecimiento general a largo plazo
2. **Estacionalidad:** Patrones según temporada (ej: caídas por crisis, crecimientos post-pandemia)
3. **Volatilidad:** Cambios abruptos en precios (ej: anuncios de noticias)
4. **Autocorrelación:** Dependencia con valores pasados
5. **Correlación cruzada:** Posible correlación entre stocks

## Casos de Uso

1. **Pronóstico univariado:** Predecir Close del día siguiente para una acción
2. **Pronóstico multivariado:** Usar OHLC para mejor predicción
3. **Detección de tendencias:** Identificar tendencias alcistas/bajistas
4. **Detección de volatilidad:** Identificar períodos de alta incertidumbre
5. **Análisis de retornos:** Analizar returns en lugar de precios
6. **Comparación de series:** Correlaciones entre diferentes stocks

## Técnicas Aplicables

| Técnica | Aplicación |
|---------|-----------|
| ARIMA | Modelado de autocorrelación |
| Exponential Smoothing | Pronóstico con diferentes pesos |
| SARIMA | Con componente estacional |
| Prophet | Pronóstico robusto con tendencias |
| LSTM/RNN | Redes neuronales para secuencias |
| VAR | Modelos vectoriales autorregresivos |
| Rolling Windows | Validación de series de tiempo |

## Notas Importantes

- **No hay faltantes:** Datos limpios de bolsa (solo días de transacción)
- **Estacionariedad:** Close NO es estacionaria (tiene tendencia)
- **Transformación necesaria:** Daily_Return es más estacionaria que Close
- **Múltiples series:** Permite análisis de múltiples acciones simultáneamente
- **Autocorrelación:** Fuerte dependencia con valores pasados

## Preprocesamiento Típico

1. Extraer una acción o trabajar con todas según el análisis
2. Crear features derivadas (MA, volatilidad, retorno)
3. Diferenciación para hacerla estacionaria (Close[t] - Close[t-1])
4. Log-returns para mejor modelado de volatilidad
5. Normalización/escalado si se usa redes neuronales
6. Train-test split respetando orden temporal

## Análisis de Estacionariedad

- **Close:** NO estacionaria (rechaza ADF test)
- **Daily_Return:** Estacionaria (acepta ADF test)
- **Log-Close:** NO estacionaria
- **Log-Daily_Return:** Estacionaria

## Ventanas de Predicción Posibles

```
Univariada: Close[t] → Close[t+1]
Multivariada: [Open, High, Low, Close, Volume][t] → Close[t+1]
Multi-paso: Predecir próximos 5, 10, 30 días
```

## Ejemplo de Estructura

| Date | Stock_Symbol | Open | High | Low | Close | Volume | Adj_Close | Daily_Return | MA_5 | MA_20 |
|------|-------------|------|------|-----|-------|--------|-----------|---------------|------|-------|
| 2003-01-02 | AAPL | 10.50 | 10.75 | 10.32 | 10.65 | 50000000 | 10.65 | NaN | NaN | NaN |
| 2003-01-03 | AAPL | 10.70 | 11.00 | 10.50 | 10.85 | 48000000 | 10.85 | 1.88% | NaN | NaN |
| 2003-01-06 | AAPL | 10.80 | 11.20 | 10.75 | 11.10 | 52000000 | 11.10 | 2.30% | NaN | NaN |
