# Reclamos Call Center BancoAndes

## Descripción
Base de datos sintética de reclamos de clientes del call center de un banco ficticio (BancoAndes), pensada para practicar clasificación de texto (NLP) en español. Incluye dos archivos: `reclamos.csv` (etiquetado, para entrenar y evaluar un modelo) y `reclamos_sin_etiquetar.csv` (reclamos nuevos sin la columna `area`, para aplicar el modelo ya entrenado). El texto trae ruido de formato típico de datos reales de call center (mayúsculas inconsistentes, HTML, tildes faltantes, firmas, datos de contacto colados) pensado para practicar limpieza con expresiones regulares antes de modelar.

## Target
`area` - Clasificación multiclase (7 categorías: `cobranza`, `comercial`, `fraude_seguridad`, `post_venta`, `pre_venta`, `tecnologia`, `ventas`)

## Tamaño
- `reclamos.csv`: 3.914 registros, 5 variables
- `reclamos_sin_etiquetar.csv`: 150 registros, 4 variables (sin la columna `area`)

## Diccionario de Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| id_reclamo | int | Identificador único del reclamo |
| fecha | date (YYYY-MM-DD) | Fecha de registro del reclamo (18 meses: 2025-03-01 a 2026-08-31) |
| banco | string | Nombre del banco (`BancoAndes`; algunas filas tienen variantes de escritura a propósito, ej. `BANCOANDES`, `Banco Andes`) |
| area | string | Target: área a la que debería derivarse el reclamo (solo en `reclamos.csv`) |
| texto | string | Texto del reclamo redactado por el cliente, con ruido de formato incluido a propósito |

## Valores Faltantes
No tiene valores nulos. `reclamos_sin_etiquetar.csv` no incluye la columna `area` (a propósito, ya que es el conjunto sobre el que se aplica el modelo entrenado).

## Casos de Uso
Clasificación de texto (NLP), limpieza de texto con expresiones regulares, comparación de modelos (spaCy `TextCategorizer`, embeddings de palabras, embeddings de oraciones con `sentence-transformers`), análisis de series de tiempo (evolución mensual de reclamos), manejo de fuga de datos y de ruido de etiqueta.

## Cómo Usar

```python
import pandas as pd

df = pd.read_csv('reclamos.csv', parse_dates=['fecha'])
df.head()
df['area'].value_counts()
```

## Notas
- El texto está en español y contiene ruido intencional (mayúsculas, HTML, tildes faltantes, emojis, firmas, datos de contacto) para practicar limpieza con regex.
- Alrededor de un 5% de los reclamos de `reclamos.csv` tienen la etiqueta `area` intencionalmente incorrecta (ruido de etiqueta), simulando errores humanos de categorización en un call center real.
- Un pequeño grupo de reclamos ("ambiguos") mezcla a propósito vocabulario de dos áreas distintas, para que el problema de clasificación no sea trivial.
- No hay texto exactamente repetido entre registros.
- Ver el notebook [`nlp/Clase 4/clasificador_reclamos.ipynb`](../../../nlp/Clase%204/clasificador_reclamos.ipynb) para el flujo completo de análisis descriptivo, limpieza, modelado y evaluación.
