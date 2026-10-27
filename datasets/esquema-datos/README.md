# Esquema de datos: bases relacionales

Tres bases de datos **sintéticas** con modelo dimensional (esquema estrella), pensadas para practicar **SQL**, **Power BI** y análisis con **pandas**. Todas siguen las mismas convenciones, así que lo que se aprende en una sirve para las otras.

| Base | Dominio | Período | Tablas | Filas | Hechos | Preguntas típicas |
|---|---|---|---:|---:|---|---|
| [**compras**](compras/) | Retail omnicanal | 2024–2025 | 6 | 40.497 | `orden`, `detalle_orden` | ventas, margen, ticket promedio, YoY, canales |
| [**tarjetas_credito**](tarjetas_credito/) | Emisor de tarjetas de crédito | 2025 | 6 | 407.066 | `transaccion`, `estado_cuenta` | mora, roll rates, utilización de cupo, fraude |
| [**taxis**](taxis/) | Transporte de pasajeros en Santiago | 2025 | 6 | 196.569 | `viaje` | demanda por hora, precio dinámico, cancelaciones, rutas |

## Cómo se organizan los datos

![Esquema unificado](diagramas/esquema_unificado.png)

Cada base es una estrella: las **tablas de hechos** (en azul oscuro) guardan eventos medibles, y las **dimensiones** (en celeste) los describen. Las tres bases comparten **`dim_fecha`**, con la misma estructura y llave, así que se pueden comparar en una misma línea de tiempo.

### Convenciones comunes

| Convención | Regla |
|---|---|
| Prefijos | `dim_` para dimensiones. Los hechos van sin prefijo |
| Llaves primarias | `id_<entidad>`, entero correlativo desde 1 |
| Llaves foráneas | mismo nombre que la PK a la que apuntan, con dos excepciones: `id_zona_origen`/`id_zona_destino` e `id_fecha_cierre` |
| Llave de fecha | `id_fecha` entero con formato `AAAAMMDD`, por ejemplo `20251225` |
| Montos | pesos chilenos (CLP) enteros, sin decimales |
| Banderas | enteros 0/1 (`es_fin_semana`, `es_fraude`, `con_lluvia`, …) |
| Textos | en español. Los nombres de personas son ficticios |
| Vistas | `v_ventas`, `v_transacciones` y `v_viajes` dejan cada estrella aplanada para consultar rápido |

### Estructura de carpetas

```
esquema-datos/
├── README.md                    ← este archivo
├── diagramas/
│   ├── esquema_unificado.png
│   └── esquema_unificado.mmd    ← fuente Mermaid del diagrama
├── compras/
│   ├── README.md                ← diccionario, diagrama ER y consultas
│   ├── compras.db.zip           ← base SQLite (descomprimir)
│   ├── esquema.sql              ← DDL (CREATE TABLE + vista)
│   ├── generar.py               ← script que regenera los datos
│   └── csv/                     ← una tabla por archivo (UTF-8 con BOM)
├── tarjetas_credito/            ← misma estructura (tarjetas.db.zip)
└── taxis/                       ← misma estructura (taxis.db.zip)
```

## Cómo usarlas

**SQL (SQLite):** descomprime el `.db.zip` y ábrelo con [DB Browser for SQLite](https://sqlitebrowser.org/) o DBeaver. Para PostgreSQL o SQL Server, ejecuta `esquema.sql` y carga los CSV.

**Power BI:** usa *Obtener datos → Texto/CSV* con cada archivo de `csv/`, o *Carpeta* para cargarlos todos a la vez. Luego crea las relaciones que muestra el diagrama ER de cada README y marca `dim_fecha` como tabla de fechas.

**Python:**

```python
import pandas as pd, sqlite3

# Directo desde GitHub
base = "https://raw.githubusercontent.com/fmansillaib/umayor_class/main/datasets/esquema-datos"
viajes = pd.read_csv(f"{base}/taxis/csv/viaje.csv")

# Con SQL sobre la base local
con = sqlite3.connect("compras.db")
pd.read_sql("SELECT anio, SUM(monto_neto) AS ventas FROM v_ventas GROUP BY anio", con)
```

**Regenerar o ampliar:** cada `generar.py` usa una semilla fija, así que produce siempre los mismos datos. Para crear más volumen, cambia los parámetros del script (número de clientes, órdenes, etc.) y ejecútalo con `python generar.py` dentro de la carpeta.

## Nota

Todos los datos son **sintéticos**: se generaron con reglas de negocio simplificadas y no corresponden a personas, empresas ni transacciones reales. Los patrones de cada README (estacionalidad, mora por segmento, precio dinámico) son intencionales, para que el análisis encuentre algo.
