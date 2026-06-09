# Diccionario de Datos - Ventas de Empresas

## Descripción General

Dataset sintético con información sobre empresas, características de operación y múltiples variables objetivo. Es un dataset versátil que permite trabajar con **targets continuos, categóricos y dicotómicos** simultáneamente.

## Tipos de Targets Disponibles

| Target | Tipo | Descripción | Valores |
|--------|------|-------------|---------|
| Revenue | Continua | Ingresos anuales en USD | 100,000-10,000,000 |
| Revenue_Category | Categórica | Categoría de ingresos | Bajo, Medio, Alto, Premium |
| Is_Profitable | Dicotómica | ¿Es rentable? | 0 = No, 1 = Sí |

## Variables

| Variable | Tipo | Descripción | Valores/Rango | Uso |
|----------|------|-------------|---------------|-----|
| Company_ID | int | Identificador de la empresa | 1-500 | ID |
| Company_Name | string | Nombre de la empresa | Texto | ID |
| Industry | string | Sector industrial | Tech, Finance, Retail, Manufacturing, Healthcare | Feature (categórica) |
| Years_Operating | int | Años en operación | 1-50 | Feature (continua) |
| Employees | int | Número de empleados | 10-5,000 | Feature (continua) |
| R&D_Investment | float | Inversión en I+D (USD) | 0-2,000,000 | Feature (continua) |
| Marketing_Spend | float | Gasto en marketing (USD) | 10,000-500,000 | Feature (continua) |
| Operating_Costs | float | Costos operativos (USD) | 50,000-8,000,000 | Feature (continua) |
| Revenue | float | Ingresos anuales (USD) | 100,000-10,000,000 | **TARGET 1 (Regresión)** |
| Revenue_Category | string | Categoría de ingresos | Bajo, Medio, Alto, Premium | **TARGET 2 (Clasificación)** |
| Is_Profitable | int | ¿Es rentable? | 0, 1 | **TARGET 3 (Dicotómica)** |
| Market_Share | float | Participación de mercado (%) | 0.1-15.0 | Feature (continua) |
| Customer_Satisfaction | float | Satisfacción del cliente (0-100) | 20-95 | Feature (continua) |
| Export_Percentage | float | % de ventas al extranjero | 0-100 | Feature (continua) |
| Has_Patents | int | ¿Tiene patentes? | 0, 1 | Feature (dicotómica) |
| Region | string | Región geográfica | North, South, East, West, Central | Feature (categórica) |

## Información del Dataset

- **Cantidad de registros:** 500
- **Cantidad de variables:** 16
- **Variables sin faltantes:** Diseñado sin valores faltantes (control)
- **Formato:** CSV
- **Fuente:** Dataset sintético para educación
- **Tipo:** Panel de empresas (sección transversal)

## Estructura de Targets

### 1. Target Continuo: Revenue
- **Rango:** 100,000 - 10,000,000 USD
- **Distribución:** Log-normal
- **Caso de uso:** Regresión
- **Métrica:** MAE, RMSE, R²

### 2. Target Categórico Multiclase: Revenue_Category
- **Categorías:** 
  - Bajo (< percentil 25)
  - Medio (percentil 25-50)
  - Alto (percentil 50-75)
  - Premium (> percentil 75)
- **Caso de uso:** Clasificación multiclase
- **Métrica:** Accuracy, F1-weighted, Confusion Matrix

### 3. Target Dicotómico: Is_Profitable
- **Valores:** 0 (No rentable), 1 (Rentable)
- **Definición:** Revenue > Operating_Costs
- **Caso de uso:** Clasificación binaria
- **Métrica:** Accuracy, Precision, Recall, F1, AUC-ROC

## Casos de Uso

1. **Regresión:** Predecir `Revenue` basado en características operativas
2. **Clasificación Multiclase:** Categorizar empresas por nivel de ingresos
3. **Clasificación Binaria:** Predecir rentabilidad
4. **Análisis Multitarget:** Comparar desempeño entre modelos con diferentes targets
5. **Feature Importance:** Identificar qué variables afectan más cada target
6. **Correlación:** Analizar relación entre targets

## Características Especiales

- **Múltiples targets:** Permite comparar modelos regresivos vs clasificadores
- **Variables categóricas y continuas:** Mix realista de tipos de datos
- **Sin faltantes:** Facilita enfoque en modelado sin preprocesamiento
- **Sintético pero realista:** Relaciones lógicas entre variables
- **Variables dicotómicas:** Incluye features binarias

## Relaciones entre Variables

- **Revenue** está correlacionado con: Employees, R&D_Investment, Marketing_Spend
- **Is_Profitable** depende de: Revenue vs Operating_Costs
- **Revenue_Category** es discretización de Revenue
- **Industry** afecta: Márgenes, tipo de inversión esperada

## Preprocesamiento Típico

1. Remover Company_ID, Company_Name (ID)
2. Encoding: Industry, Region (categóricas nominales)
3. No requiere imputación (diseño sin faltantes)
4. Feature scaling (si se usa KNN, SVM, etc.)
5. Análisis de colinealidad

## Posibles Análisis

1. Comparar tres modelos diferentes (uno para cada target)
2. Validar si modelo de regresión coincide con clasificación
3. Feature importance comparativo entre targets
4. Análisis de industria vs rentabilidad
5. Impacto de I+D y Marketing en ingresos
