# Datos compartidos v2 — bases para N°37 en adelante (Calendario v3)

Versión de las bases del menú preparada para las clases N°37, 37b, 38 y 38b. **Desde el 2026-10-07 la Clase 36b también usa estas bases** (el cuaderno, el Solucionario y el Diccionario de Columnas se alinearon con v2). La carpeta `../datos-compartidos/` (versión 1) no se tocó y queda sin uso: si un estudiante tiene esos links, siguen funcionando.

Todas se abren igual, **sin parámetros** (UTF-8, coma, encabezado en la primera fila):

```python
import pandas as pd
tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos-v2/<archivo>")
```

`guaguas` no se duplicó: sigue en `../datos-compartidos/bbdd_guaguas.csv`.

## Qué trae cada una

La columna **Receta** es la línea de texto que va antes de `pd.to_numeric(..., errors="coerce")`. Siempre se mira primero el tipo (`.dtype`): si una columna ya es número, no hay nada que convertir.

| Archivo | Filas × cols | Números escritos como texto (el problema vivo) | Receta | Cambios respecto a v1 |
|---|---|---|---|---|
| `01_sies.csv` | 1.690 × 14 | `Retención 1er año`, `Duración Real (semestres)` (traen `s/i`). `Ingreso Promedio al 4° año` es un rango en texto | ninguna: el punto es **decimal**, no se quita | −3 filas basura (2 vacías y el pie "FUENTE"); "1er año" traía un espacio duro; **+`Ingreso_punto_medio`** (numérica) |
| `02_demre.csv` | 2.150 × 19 | 10 columnas `PROM_OBLIGATORIAS_*` con coma decimal (`807,13`) | `,` → `.` | sin `sep=";"`; 40 universidades con espacios sobrantes; **+`MARGEN_P25_MENOS_ULTIMO`** |
| `03_simce_establecimiento.csv` | 3.002 × 42 | 6 columnas `palu_eda_*` (% de logro) con coma decimal. Los promedios ya son números | `,` → `.` | sin `sep` ni `encoding="latin-1"` |
| `04_simce_comuna.csv` | 346 × 24 | 6 columnas `palu_eda_*` con coma decimal | `,` → `.` | ídem |
| `05_matricula.csv` | 16.768 × 71 | ninguna (solo vacíos: `SLEP` 10.281) | — | `"NULL"` pasa a vacío de verdad |
| `06_subvenciones.csv` | 123.361 × 44 | 23 columnas de monto con punto de miles (`253.447.695`) | `.` → nada | **sin `RUT_SOSTENEDOR`** |
| `07_conaset_rm.csv` | 123.343 × 37 | ninguna (vacíos: `Ruta` 118.077, `Calle_Dos` 35.367, `Calle_Uno` 5.941, `AM` 1.319) | — | celdas de solo espacios pasan a vacías; **+`Mes_num`** (1-12) |
| `08a_odepa_consumidor.csv` | 67.453 × 15 | `Precio promedio` con coma decimal | `,` → `.` | solo Región Metropolitana; sin BOM |
| `08b_odepa_mayorista.csv` | 78.218 × 14 | `Precio minimo`, `Precio maximo`, `Precio promedio` con coma decimal | `,` → `.` | ídem |
| `08c_odepa_catastro_fruticola.csv` | 14.471 × 14 | `Superficie (ha)` con coma decimal | `,` → `.` | ídem |
| `09a_hospitalarias_mensual.csv` | 13.668 × 21 | 5 indicadores con decimales (`Indice_Ocupacional`, `Indice_de_Rotacion`, `Letalidad`, `Promedio_Cama_Disponibles`, `Promedio_Dias_de_Estada`) | `,` → `.` | **reestructurada**: una fila por establecimiento, nivel y mes; sin `Glosa` (cada indicador es una columna), sin filas "Datos País/Servicio Salud/Establecimiento"; **+`Mes`, `Mes_num`, `Dias_mes`, `Egresos_por_dia`** |
| `09b_hospitalarias_anual.csv` | 1.139 × 17 | los mismos 5 indicadores | `,` → `.` | igual, con el acumulado del año |

## Qué se resolvió en silencio (lo que las clases no enseñan)

- Apertura sin parámetros: ya no hacen falta `sep`, `encoding` ni `header`.
- Espacios sobrantes, espacios duros (`\xa0`) y espacios repetidos dentro del texto (en ODEPA impedían filtrar por nombre exacto, por ejemplo `Pavo Pechuga s/hueso`).
- Celdas de solo espacios y textos `NULL` → vacías de verdad (pandas no cuenta `" "` como vacío).
- Filas basura o agregadas, y el pivote de Hospitalarias.
- Lo que no cabe en las operaciones enseñadas se entrega ya calculado: `Ingreso_punto_medio`, `MARGEN_P25_MENOS_ULTIMO`, `Mes_num`, `Egresos_por_dia`.

## Cosas que conviene saber

- **El maquillaje solo cambia el formato de escritura, nunca un valor.** Está verificado: la receta recupera exactamente los números originales.
- **Matrícula quedó sin problema de tipo a propósito.** Con punto de miles en celdas sueltas (`1.110`) pandas lee el decimal `1.11` sin avisar, y en una base real que se presenta ante dirección eso es peligroso. (En `guaguas`, la trampa existe y se resuelve con `dtype`, que es el Concepto 1 de N°37.)
- `Ingreso_punto_medio` usa el punto medio de cada rango; `Sobre $3 millones 500 mil` usa 3.500.000 (un solo extremo) y `s/i` queda vacío.
- `Diccionario de Columnas.pdf` (36b) se rehízo para v2 el 2026-10-07: columnas, tamaños y ejemplos de valor salen de estos mismos CSV y se verificaron uno a uno.
- ODEPA quedó recortada a la RM (las 3 tablas). SIMCE no tiene las glosas de `cod_depe1`/`cod_grupo` traducidas.

## Cómo se regenera y verifica

```
python tools/datos_octubre/preparar_bases.py
```

Lee `../datos-compartidos/` y escribe acá. Termina con código 1 si alguna base falla: la vuelve a abrir sin parámetros, comprueba que la receta recupere cada valor original y que no queden espacios sobrantes ni caracteres rotos.
