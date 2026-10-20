# Datos compartidos v3 — bases limpias para la N°38 en adelante (giro plug-and-play)

Versión de las bases del menú para la Clase 38 y las sesiones de proyecto. **Mismas filas, mismas columnas y mismos nombres que la v2**, pero:

1. Los números que venían escritos como texto (`"85,3"`, `"1.234.567"`, `"s/i"`) **ya vienen como número** (`85.3`, `1234567`, vacío).
2. Donde una columna escribía un número, un rango o una medida **con palabras**, se agregaron columnas numéricas **al lado**. La columna original se conserva.

Todas se abren igual, **sin parámetros**, y cada columna numérica ya es número (nada que limpiar):

```python
import pandas as pd
tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clase-38y38b/datos-compartidos-v3/<archivo>")
```

`guaguas` no se duplicó: sigue en `../../clases-octubre/datos-compartidos/bbdd_guaguas.csv` (su limpieza es parte del ICN de la N°37).

Las carpetas `clases-octubre/datos-compartidos/` (v1) y `clases-octubre/datos-compartidos-v2/` **no se tocaron**: quien ya tenga links de la v2 (por ejemplo, cuadernos de la 36b y la 37b) sigue funcionando.

## Columnas nuevas

| Base | Columna original (se conserva) | Columnas nuevas | Regla |
|---|---|---|---|
| `01_sies.csv` | `Ingreso Promedio al 4° año` | `Ingreso_min`, `Ingreso_max` | Extremos del rango, en pesos. `s/i` deja ambas vacías. `Sobre $3 millones 500 mil` deja solo el mínimo (3.500.000). `Ingreso_punto_medio` (ya existía) es el punto medio de ambas. |
| `01_sies.csv` | `Acreditación institución (al 31 de octubre 2025)` | `Acreditacion_anios` | `5 años` → 5. `No` (sin acreditación) → **0**. Ojo: ese 0 baja los promedios. |
| `08a_odepa_consumidor.csv` | `Unidad` | `Unidad_cantidad`, `Unidad_medida` | `$/bolsa 800 grs` → 800 gramos. Sin número es 1 (`$/kilo` → 1 kilos). **Lo que va entre paréntesis describe el envase, no la unidad del precio:** `$/kilo (en saco de 25 kilos)` → 1 kilos. Medidas: kilos, gramos, litros, ml, unidades. |
| `08b_odepa_mayorista.csv` | `Unidad de comercializacion` | `Envase`, `Unidad_cantidad`, `Unidad_medida` | `$/caja 18 kilos` → caja, 18, kilos. `$/bins (350 kilos)` → bins, 350, kilos. `$/kilo` y `$/unidad` no tienen envase (vacío). `$/docena de atados` → atado, 12, unidades. Atados y canastillos se cuentan como unidades. `$/paquete` no informa cuánto trae: cantidad y medida vacías. `empedrada`, `granel` y `embalada` quedan solo en la original. |
| `08b_odepa_mayorista.csv` | `Fecha` | `Mes_num` | Mes de la fecha (1-12), como en las demás bases. |

Cada separación se verifica contra una tabla de equivalencias que el script imprime (para SIES, las 23 filas de rango; para ODEPA, todas las unidades distintas).

## Cosas que conviene saber

- **El cambio es solo de escritura, nunca de valor.** El script lo comprueba: lo que no se convirtió queda idéntico a la v2, carácter por carácter, y lo convertido coincide con los valores verdaderos que calcula `preparar_bases.py`.
- **Una columna numérica no es siempre una cantidad.** Años, códigos (`cod_depe2`, `COD_DEPE`, `rbd`) y la fecha en milisegundos de CONASET (`FECHA`) son números que funcionan como etiquetas. Los significados de los códigos están en el *Diccionario de Columnas* (36b), en la tabla de códigos de cada base.
- **ODEPA mezcla unidades.** El precio puede ser por kilo, por unidad, por litro o por envase: un promedio que las junta no significa nada. Para promediar hay que filtrar una sola `Unidad_medida` (y, si se puede, una sola `Unidad_cantidad`). No se calculó un "precio por kilo" porque algunas etiquetas son ambiguas.
- **No se separó** `Producto` de ODEPA consumidor (`Palta|Hass|Primera`), `UBICACION` de CONASET (listas con `;`) ni `Calidad` de ODEPA mayorista, por decisión explícita.
- `Matrícula` y `CONASET` no tenían números como texto: son idénticas a la v2.
- `Subvenciones` es la más grande en columnas convertidas (24 montos con punto de miles → enteros).

## Qué trae cada una (filas × columnas)

| Archivo | Filas × cols | Columnas pasadas a número |
|---|---|---|
| `01_sies.csv` | 1.690 × 17 | 2 (`Retención 1er año`, `Duración Real (semestres)`) |
| `02_demre.csv` | 2.150 × 19 | 10 (`PROM_OBLIGATORIAS_*`) |
| `03_simce_establecimiento.csv` | 3.002 × 42 | 6 `palu_eda_*` |
| `04_simce_comuna.csv` | 346 × 24 | 6 `palu_eda_*` |
| `05_matricula.csv` | 16.768 × 71 | ninguna |
| `06_subvenciones.csv` | 123.361 × 44 | 23 montos |
| `07_conaset_rm.csv` | 123.343 × 37 | ninguna |
| `08a_odepa_consumidor.csv` | 67.453 × 17 | `Precio promedio` |
| `08b_odepa_mayorista.csv` | 78.218 × 18 | `Precio minimo`, `Precio maximo`, `Precio promedio` |
| `08c_odepa_catastro_fruticola.csv` | 14.471 × 14 | `Superficie (ha)` |
| `09a_hospitalarias_mensual.csv` | 13.668 × 21 | 5 indicadores |
| `09b_hospitalarias_anual.csv` | 1.139 × 17 | 5 indicadores |

(El script también pasa por la conversión columnas que ya eran número en la v2; el conteo de arriba son las que de verdad cambiaron de texto a número.)

## Cómo se regenera y verifica

```
python tools/datos_octubre/preparar_bases_v3.py
```

Lee `clases/clases-octubre/datos-compartidos-v2/` y escribe acá. Termina con código 1 si alguna verificación falla: reabre cada base sin parámetros, comprueba que cada columna convertida sea número y coincida con los valores verdaderos, que las columnas nuevas sean coherentes (por ejemplo, `Ingreso_max` > `Ingreso_min`) y que nada más haya cambiado.

> Estado: generadas y verificadas localmente (2026-10-20). **Pendiente subirlas a GitHub** antes de que los estudiantes usen los links.
