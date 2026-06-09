# Datasets

Colección de bases de datos para proyectos de Machine Learning e IA. Los datasets están organizados por tipo: **datos transversales/paneles** y **series de tiempo**.

## Datos Transversales y Paneles

| Dataset | Registros | Tipo | Descripción |
|---------|-----------|------|-------------|
| **titanic** | 891 | Clasificación binaria | Supervivencia en el Titanic |
| **precios_casas** | 1,460 | Regresión / Clasificación | Predicción de precios inmobiliarios |
| **ventas_empresas** | 500 | Multi-target | Ventas, categorización y rentabilidad |
| **iris** | 150 | Clasificación multiclase | Clasificación de especies de flores |
| **wine** | 178 | Clasificación multiclase | Clasificación de cultivares de vino |
| **breast_cancer** | 569 | Clasificación binaria | Diagnóstico de tumores |
| **adult_income** | 32,561 | Clasificación binaria | Predicción de ingresos |
| **mushroom** | 8,124 | Clasificación binaria | Identificación comestible/venenoso |
| **diabetes** | 768 | Clasificación binaria | Predicción de diabetes |
| **insurance_charges** | 1,338 | Regresión | Predicción de costos de seguros |
| **penguin** | 344 | Clasificación multiclase | Clasificación de especies de pingüinos |

## Series de Tiempo

| Dataset | Registros | Tipo | Descripción |
|---------|-----------|------|-------------|
| **precios_acciones** | 27,385 | Pronóstico | Precios históricos de 5 stocks (20 años) |
| **ventas_mensuales** | 3,000 | Pronóstico estacional | Ventas mensuales con estacionalidad (10 años) |

## Estructura

```
datasets/
├── README.md (este archivo)
├── datos_transversales_paneles/
│   ├── titanic/datos.csv
│   ├── precios_casas/datos.csv
│   ├── ventas_empresas/datos.csv
│   ├── iris/datos.csv
│   ├── wine/datos.csv
│   ├── breast_cancer/datos.csv
│   ├── adult_income/datos.csv
│   ├── mushroom/datos.csv
│   ├── diabetes/datos.csv
│   ├── insurance_charges/datos.csv
│   └── penguin/datos.csv
└── series_de_tiempo/
    ├── precios_acciones/datos.csv
    └── ventas_mensuales/datos.csv
```

## Fuentes

- Datasets sintéticos propios (Titanic, Precios de Casas, Ventas de Empresas, Ventas Mensuales)
- Kaggle - Datasets públicos clásicos (Iris, Wine, Breast Cancer, Adult Income, Mushroom, Diabetes, Insurance, Penguin, Stock Prices)
