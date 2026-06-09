# Diccionario de Datos - Registro Centralizado

## Descripción General

Este documento mantiene un registro centralizado de todas las bases de datos disponibles en el repositorio, organizadas por tipo (transversales/paneles y series de tiempo).

---

## DATOS TRANSVERSALES Y PANELES

### 1. Titanic - Clasificación Binaria Dicotómica
**Ubicación:** `datasets/datos_transversales_paneles/titanic/`

**Descripción:** Dataset histórico del naufragio del RMS Titanic con información sobre pasajeros y supervivencia.

**Target:** 
- Variable: `Survived` (0 = No, 1 = Sí)
- Tipo: **Clasificación Binaria Dicotómica**

**Características principales:**
- 891 registros
- 12 variables (ID, features categóricas y continuas)
- Desbalanceo: ~62% no sobrevivió, ~38% sobrevivió
- Valores faltantes: Age, Cabin, Embarked

**Casos de uso:**
- Aprender clasificación binaria
- Feature engineering
- Manejo de valores faltantes
- Desbalanceo de clases

**Archivo:** `diccionario.md` (detalles completos)

---

### 2. Precios de Casas - Regresión Continua y Clasificación
**Ubicación:** `datasets/datos_transversales_paneles/precios_casas/`

**Descripción:** Dataset con características de casas y precios de venta. Permite trabajar con regresión continua o clasificación de rangos.

**Targets disponibles:**
- **Regresión:** `SalePrice` (continua, rango: $34,900-$755,000)
- **Clasificación:** Categorías de precio (Bajo, Medio, Alto, Premium)

**Características principales:**
- 1,460 registros de entrenamiento
- 81 variables (área, año, características estructurales, etc.)
- Múltiples tipos: continuas, discretas, ordinales, nominales
- Valores faltantes en LotFrontage, Alley, Cabin, etc.

**Casos de uso:**
- Regresión continua
- Clasificación multiclase
- Feature engineering (edad, área total)
- Manejo de outliers y valores faltantes
- Detección de multicolinealidad

**Archivo:** `diccionario.md` (detalles completos)

---

### 3. Ventas de Empresas - Targets Múltiples (Continuo, Categórico, Dicotómico)
**Ubicación:** `datasets/datos_transversales_paneles/ventas_empresas/`

**Descripción:** Dataset sintético con información de 500 empresas y múltiples variables objetivo, permitiendo comparar diferentes tipos de targets.

**Targets disponibles:**
- **Continuo:** `Revenue` (ingresos en USD, rango: $100k-$10M)
- **Categórico:** `Revenue_Category` (Bajo, Medio, Alto, Premium)
- **Dicotómico:** `Is_Profitable` (0 = No rentable, 1 = Rentable)

**Características principales:**
- 500 registros
- 16 variables (industria, empleados, inversión, gastos, etc.)
- Mix de variables categóricas y continuas
- **Sin valores faltantes** (diseño controlado)
- Múltiples targets para análisis comparativo

**Casos de uso:**
- Comparar regresión vs clasificación
- Análisis multitarget
- Feature importance comparativo
- Análisis de rentabilidad
- Impacto de I+D y marketing

**Archivo:** `diccionario.md` (detalles completos)

---

## SERIES DE TIEMPO

### 4. Precios de Acciones
**Ubicación:** `datasets/series_de_tiempo/precios_acciones/`

**Descripción:** Series de tiempo diarias de precios de acciones de 5 empresas tecnológicas (AAPL, GOOGL, MSFT, AMZN, TSLA) durante ~20 años.

**Target:**
- Variable: `Close` (precio de cierre)
- Tipo: **Pronóstico de Series de Tiempo**

**Características principales:**
- ~5,000 registros (diarios, ~20 años)
- Variables OHLCV (Open, High, Low, Close, Volume)
- Múltiples series paralelas (5 acciones)
- Período: Aproximadamente 2003-2023
- **Sin valores faltantes** (solo días de bolsa)

**Patrones:**
- Tendencia creciente a largo plazo
- Volatilidad e impactos de noticias
- Autocorrelación fuerte
- Correlaciones entre stocks

**Casos de uso:**
- Pronóstico de precios
- Análisis de volatilidad
- Detección de tendencias
- Modelos ARIMA, SARIMA
- Redes neuronales (LSTM)
- Análisis multiseries

**Archivo:** `diccionario.md` (detalles completos)

---

### 5. Ventas Mensuales
**Ubicación:** `datasets/series_de_tiempo/ventas_mensuales/`

**Descripción:** Series de tiempo mensual de ventas de 5 categorías de productos en 5 regiones durante 10 años (2015-2024).

**Target:**
- Variable: `Sales` (ventas en USD)
- Tipo: **Pronóstico de Series de Tiempo con Componentes Estacionales**

**Características principales:**
- 600 registros (10 años × 12 meses, con 5 categorías)
- Variables temporales y exógenas
- Período: Enero 2015 - Diciembre 2024
- Frecuencia: Mensual
- **Sin valores faltantes**

**Patrones:**
- **Tendencia:** Crecimiento general
- **Estacionalidad:** Fuerte (picos nov-dic, valles ene-feb)
- **Ciclos:** 2-3 años
- **Variación por categoría:** Diferentes patrones estacionales
- **Variables exógenas:** Marketing_Spend impacta ventas

**Casos de uso:**
- Pronóstico mensual/trimestral/anual
- Descomposición STL
- Análisis de estacionalidad
- Modelos SARIMA, Prophet
- Impacto de marketing
- Análisis por categoría/región
- Redes neuronales (LSTM/GRU)

**Archivo:** `diccionario.md` (detalles completos)

---

## COMPARATIVA RÁPIDA

| Dataset | Tipo | Categoría | Target | Observaciones | Complejidad |
|---------|------|-----------|--------|---------------|-------------|
| Titanic | Transversal | Clasificación | Binaria Dicotómica | 891 | Baja-Media |
| Precios Casas | Transversal | Regresión/Clasificación | Continua/Multiclase | 1,460 | Media-Alta |
| Ventas Empresas | Transversal | Multi-target | 3 tipos diferentes | 500 | Media |
| Precios Acciones | Serie Temporal | Pronóstico | Continua univariada | 5,000 | Media-Alta |
| Ventas Mensuales | Serie Temporal | Pronóstico | Continua multiseries | 600 | Media-Alta |

---

## CÓMO USAR ESTE DICCIONARIO

1. **Para elegir un dataset:** Busca por tipo de problema (clasificación, regresión, pronóstico)
2. **Para entender variables:** Lee el `diccionario.md` específico de cada dataset
3. **Para preprocesamiento:** Consulta la sección "Preprocesamiento típico" en cada diccionario
4. **Para modelos:** Revisa "Técnicas aplicables" según el tipo de datos

---

## NOTAS IMPORTANTES

- **Datos transversales:** Sin dependencia temporal entre observaciones
- **Series de tiempo:** Orden cronológico es crítico para modelado y validación
- **Targets múltiples:** Los datasets de empresas y casas permiten análisis comparativo
- **Síntéticos vs Reales:** Titanic y Precios de Casas son reales; Empresas es sintética pero realista

---

**Última actualización:** Junio 2024

