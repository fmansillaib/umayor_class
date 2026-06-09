# Resumen de Datasets Generados

## Estructura Completa

```
datasets/
├── README.md
├── diccionario_datos.md
├── DATASETS_SUMMARY.md (este archivo)
│
├── datos_transversales_paneles/
│   ├── README.md
│   ├── titanic/
│   │   ├── datos.csv (891 registros)
│   │   └── diccionario.md
│   ├── precios_casas/
│   │   ├── datos.csv (1,460 registros)
│   │   └── diccionario.md
│   └── ventas_empresas/
│       ├── datos.csv (500 registros)
│       └── diccionario.md
│
└── series_de_tiempo/
    ├── README.md
    ├── precios_acciones/
    │   ├── datos.csv (~27,385 registros)
    │   └── diccionario.md
    └── ventas_mensuales/
        ├── datos.csv (3,000 registros)
        └── diccionario.md
```

## Estadísticas de Datasets

| Dataset | Categoría | Registros | Target | Tipo Target | Características |
|---------|-----------|-----------|--------|-------------|-----------------|
| **Titanic** | Transversal | 891 | Survived | Binaria Dicotómica | Clasificación clásica |
| **Precios Casas** | Transversal | 1,460 | SalePrice | Continua/Multiclase | Regresión inmobiliaria |
| **Ventas Empresas** | Transversal | 500 | Revenue, Revenue_Category, Is_Profitable | 3 tipos diferentes | Multi-target |
| **Precios Acciones** | Serie Temporal | 27,385 | Close | Continua univariada | 5 stocks × ~20 años |
| **Ventas Mensuales** | Serie Temporal | 3,000 | Sales | Continua multiseries | 5 categorías × 5 regiones × 10 años |

## Cómo Usar los Datasets

### 1. Leer en Python
```python
import pandas as pd

# Transversales
df_titanic = pd.read_csv('datasets/datos_transversales_paneles/titanic/datos.csv')
df_casas = pd.read_csv('datasets/datos_transversales_paneles/precios_casas/datos.csv')
df_empresas = pd.read_csv('datasets/datos_transversales_paneles/ventas_empresas/datos.csv')

# Series de Tiempo
df_acciones = pd.read_csv('datasets/series_de_tiempo/precios_acciones/datos.csv')
df_ventas = pd.read_csv('datasets/series_de_tiempo/ventas_mensuales/datos.csv')
```

### 2. Leer en R
```r
df_titanic <- read.csv('datasets/datos_transversales_paneles/titanic/datos.csv')
df_casas <- read.csv('datasets/datos_transversales_paneles/precios_casas/datos.csv')
```

### 3. Exploración Rápida
```python
# Info del dataset
df.info()
df.describe()
df.head()

# Verificar datos faltantes
df.isnull().sum()

# Distribución del target
df['target'].value_counts()  # Para clasificación
df['target'].describe()      # Para regresión
```

## Características Especiales por Dataset

### Titanic
- ✓ Desbalanceo de clases (~62-38%)
- ✓ Valores faltantes en Age y Cabin
- ✓ Variables categóricas y continuas
- ✓ Excelente para aprender clasificación binaria

### Precios de Casas
- ✓ 20 variables (numéricas y categóricas)
- ✓ Precios distribuidos log-normalmente
- ✓ Múltiples opciones de target
- ✓ Ideal para feature engineering y regresión

### Ventas de Empresas
- ✓ 3 targets simultáneamente
- ✓ Sin valores faltantes (datos limpios)
- ✓ Múltiples tipos de variables
- ✓ Perfecto para análisis comparativo

### Precios de Acciones
- ✓ 5 series paralelas (stocks)
- ✓ ~20 años de datos diarios
- ✓ OHLCV completo
- ✓ Media móviles incluidas
- ✓ Excelente para series de tiempo y pronóstico

### Ventas Mensuales
- ✓ Estacionalidad clara
- ✓ Múltiples categorías y regiones
- ✓ Variables exógenas (Marketing_Spend)
- ✓ 10 años de datos mensuales
- ✓ Ideal para SARIMA, Prophet, LSTM

## Próximos Pasos

1. **Exploración:** Lee cada diccionario.md para entender las variables
2. **Preprocesamiento:** Sigue las recomendaciones de cada dataset
3. **Modelado:** Aplica técnicas según el tipo de target
4. **Validación:** Usa las técnicas de validación apropias para cada tipo

## Notas Importantes

- Todos los datos son sintéticos o públicos educacionales
- Los datos están limpios pero con características realistas
- Los diccionarios incluyen información detallada sobre preprocesamiento
- Cada dataset tiene un propósito pedagógico específico

---

**Generado:** Junio 2024
**Total de registros:** 33,236 observaciones
**Total de datasets:** 5
