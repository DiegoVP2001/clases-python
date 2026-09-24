# Datos compartidos — Proyecto Cierre Octubre

Copias públicas, listas para leer directo desde un Colab de estudiante sin subir nada a mano:

```python
import pandas as pd
tabla = pd.read_csv("https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/clases-octubre/datos-compartidos/<ruta del archivo>")
```

No requiere autenticación ni montar Google Drive — funciona igual de rápido que un archivo local. Patrón usado desde la Clase 36 (Pandas 1) para `bbdd_guaguas.csv`, reutilizable tal cual en N°37-N°40 y en las sesiones de proyecto (N°42+) para cualquiera de las 9 bases del menú.

## Contenido

| Archivo | Origen | Notas |
|---|---|---|
| `bbdd_guaguas.csv` | `clases-octubre/entregas-ideales/datos/guaguas_maquillada.csv` | Hilo conductor N°35-N°40, con nulos reales maquillados |
| `01_sies_empleabilidad/Buscador_Empleabilidad_ingresos_2025_2026_SIES.csv` | menú de 9 bases, #1 | |
| `02_demre_admision/ADM2026_INDICADORES_POR_CARRERA_PROMEDIO_OBLIGATORIAS_20260116.csv` | menú de 9 bases, #2 | `sep=";"`, UTF-8 |
| `03_simce_2m/simce2m2025_rbd_final.csv` | menú de 9 bases, #3 | `sep=";"`, `encoding="latin-1"` |
| `03_simce_2m/simce2m2025_comuna_final.csv` | menú de 9 bases, #4 | versión liviana por comuna |
| `05_mineduc_matricula/20251029_Resumen_Matricula_EE_Oficial_2025_20250430.csv` | menú de 9 bases, #5 | `sep=","`, `encoding="latin-1"` |
| `06_subvenciones/20260421_Detalle Subvenciones 2025_20240520.csv` | menú de 9 bases, #6 | UTF-8, coma |
| `08_odepa/ODEPA_precios-consumidor_2025.csv` | menú de 9 bases, #8a | `encoding="utf-8-sig"` |
| `08_odepa/ODEPA_precios-mayoristas-fruta-hortaliza_2025.csv` | menú de 9 bases, #8b | `encoding="utf-8-sig"` |
| `08_odepa/ODEPA-CIREN_catastro-fruticola_2025.csv` | menú de 9 bases, #8c | `encoding="utf-8-sig"` |
| `09_salud/Estadísticas Hospitalarias Año 2024.csv` | menú de 9 bases, #9 | `pd.read_csv(f, header=2)` |

## Pendiente

**`07_conaset` (CONASET — Siniestros de tránsito 2020-2025) no está acá.** El original pesa ~143 MB — supera el límite duro de GitHub (100 MB), no se puede subir tal cual. El propio `Catastro de Bases y Banco de Preguntas - Proyecto Octubre.md` ya anotaba "recorte a RM obligatorio antes de entregar" para esta base — falta que Diego confirme el criterio exacto (qué comunas cuentan como RM, qué ~12 columnas conservar) antes de generar y subir la versión recortada.

Las versiones `.xlsx`/`.pdf` de diccionarios y glosarios (Libro de Códigos DEMRE, Glosas SIMCE, Diccionario/Glosario de Subvenciones, etc.) no se copiaron acá — solo los `.csv` de datos. Si algún equipo necesita el diccionario de su base, se comparte aparte.
