# Datasets

Este directorio contiene las bases de datos y sus diccionarios de datos utilizados en los proyectos de la clase. Los datasets están organizados por tipo: **datos transversales/paneles** y **series de tiempo**.

## Estructura

```
datasets/
├── README.md                                    # Este archivo
├── diccionario_datos.md                        # Registro centralizado de todas las BD
│
├── datos_transversales_paneles/                # Datos transversales y paneles
│   ├── README.md                               # Guía de esta subcategoría
│   ├── titanic/                                # Dataset Titanic (clasificación binaria)
│   │   ├── datos.csv
│   │   └── diccionario.md
│   ├── precios_casas/                          # Precios de casas (regresión continua)
│   │   ├── datos.csv
│   │   └── diccionario.md
│   └── ventas_empresas/                        # Ventas de empresas (regresión + categorización)
│       ├── datos.csv
│       └── diccionario.md
│
└── series_de_tiempo/                           # Series de tiempo
    ├── README.md                               # Guía de esta subcategoría
    ├── precios_acciones/                       # Precios de acciones
    │   ├── datos.csv
    │   └── diccionario.md
    └── ventas_mensuales/                       # Ventas mensuales
        ├── datos.csv
        └── diccionario.md
```

## Categorías de Datasets

### 1. Datos Transversales y Paneles
Conjuntos de datos con observaciones independientes, ideales para:
- **Clasificación binaria:** Titanic (¿Sobrevivió?)
- **Clasificación multiclase:** Precios de casas (categorización)
- **Regresión continua:** Precios de casas (predicción de precios)
- **Targets categóricos y dicotómicos**

### 2. Series de Tiempo
Datos ordenados temporalmente para:
- Análisis de tendencias
- Predicción de valores futuros
- Detección de patrones estacionales

## Cómo usar

1. Cada dataset está en su propia subcarpeta con `datos.csv` y `diccionario.md`
2. Lee el `diccionario.md` de cada dataset para entender sus variables
3. Consulta `diccionario_datos.md` para una descripción general de todos los datasets
4. Para agregar nuevos datasets, sigue la estructura existente

## Diccionarios de datos

Ver [diccionario_datos.md](./diccionario_datos.md) para la descripción completa de todas las bases de datos.
