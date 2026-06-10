# Datasets

Colección de bases de datos para proyectos de Machine Learning e IA. Los datasets están organizados por tipo: **datos transversales/paneles** y **series de tiempo**.

## Datos Transversales y Paneles

### Clasificación

| Dataset | Registros | Tipo | Descripción |
|---------|-----------|------|-------------|
| **titanic** | 891 | Binaria | Supervivencia en el Titanic |
| **iris** | 150 | Multiclase | Clasificación de especies de flores |
| **wine** | 178 | Multiclase | Clasificación de cultivares de vino |
| **breast_cancer** | 569 | Binaria | Diagnóstico de tumores |
| **adult_income** | 32,561 | Binaria | Predicción de ingresos |
| **mushroom** | 8,124 | Binaria | Identificación comestible/venenoso |
| **diabetes** | 768 | Binaria | Predicción de diabetes |
| **penguin** | 344 | Multiclase | Clasificación de especies de pingüinos |

### Regresión (Target Continuo)

| Dataset | Registros | Target | Descripción |
|---------|-----------|--------|-------------|
| **precios_casas** | 1,460 | MEDV | Predicción de precios inmobiliarios |
| **insurance_charges** | 1,338 | Charges | Predicción de costos de seguros |
| **boston_housing** | 506 | MEDV | Predicción de precios en Boston |
| **student_performance** | 649 | FinalGrade | Predicción de calificaciones |
| **air_quality** | 1,320 | PM2.5 | Predicción de contaminación del aire |
| **energy_efficiency** | 768 | Y1, Y2 | Predicción de carga térmica/refrigeración |
| **concrete_strength** | 1,030 | Strength | Predicción de resistencia del concreto |
| **car_prices** | 1,000 | Price | Predicción de precios de autos |
| **california_housing** | 20,640 | MedianHouseValue | Predicción de precios en California |
| **salary_prediction** | 1,000 | Salary | Predicción de salarios |
| **determinantes_salario** | 525 | salario | Determinantes del salario (educación, experiencia) |

### Multi-target

| Dataset | Registros | Targets | Descripción |
|---------|-----------|---------|-------------|
| **ventas_empresas** | 500 | 3 targets | Ventas, categorización y rentabilidad |

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
│   ├── Clasificación:
│   │   ├── titanic/datos.csv
│   │   ├── iris/datos.csv
│   │   ├── wine/datos.csv
│   │   ├── breast_cancer/datos.csv
│   │   ├── adult_income/datos.csv
│   │   ├── mushroom/datos.csv
│   │   ├── diabetes/datos.csv
│   │   └── penguin/datos.csv
│   ├── Regresión:
│   │   ├── precios_casas/datos.csv
│   │   ├── insurance_charges/datos.csv
│   │   ├── boston_housing/datos.csv
│   │   ├── student_performance/datos.csv
│   │   ├── air_quality/datos.csv
│   │   ├── energy_efficiency/datos.csv
│   │   ├── concrete_strength/datos.csv
│   │   ├── car_prices/datos.csv
│   │   ├── california_housing/datos.csv
│   │   ├── salary_prediction/datos.csv
│   │   └── determinantes_salario/datos.csv
│   └── Multi-target:
│       └── ventas_empresas/datos.csv
└── series_de_tiempo/
    ├── precios_acciones/datos.csv
    └── ventas_mensuales/datos.csv
```

## Fuentes

- Datasets sintéticos propios: Titanic, Precios de Casas, Ventas de Empresas, Ventas Mensuales
- Kaggle - Datasets clásicos: 
  - Clasificación: Iris, Wine, Breast Cancer, Adult Income, Mushroom, Diabetes, Penguin
  - Regresión: Boston Housing, California Housing, Insurance Charges, Car Prices
  - Educacional: Student Performance, Air Quality, Energy Efficiency, Concrete Strength, Salary Prediction

## Resumen Estadístico

### Datasets Transversales
- **Total datasets**: 20
- **Total registros**: ~79,500+
- **Clasificación binaria**: 6 datasets
- **Clasificación multiclase**: 3 datasets
- **Regresión (targets continuos)**: 11 datasets
- **Multi-target**: 1 dataset

### Series de Tiempo
- **Total datasets**: 2
- **Total registros**: ~30,300
