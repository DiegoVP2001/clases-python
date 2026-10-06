"""Recorta CONASET (siniestros de tránsito 2020-2025) a la Región Metropolitana.

El original pesa ~149 MB y supera el límite de GitHub (100 MB). Se conservan las 36
columnas tal cual; solo se filtran las filas con REGION == "Metropolitana de Santiago".
Se lee todo como texto (dtype=str, sin NaN automáticos) para no alterar ningún valor.
"""
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2] / "clases" / "clases-octubre"
ORIGEN = RAIZ / "bbdd-seleccionadas" / "raw" / "07_conaset" / "CONASET_siniestros-transito-nacional_2020-2025.csv"
DESTINO = RAIZ / "datos-compartidos" / "07_conaset" / "CONASET_siniestros-transito-RM_2020-2025.csv"
LIMITE_MB = 50

tabla = pd.read_csv(ORIGEN, encoding="utf-8-sig", dtype=str, keep_default_na=False)
print("Original:", tabla.shape)

recorte = tabla[tabla["REGION"] == "Metropolitana de Santiago"]
print("Recorte RM:", recorte.shape)

DESTINO.parent.mkdir(parents=True, exist_ok=True)
recorte.to_csv(DESTINO, index=False, encoding="utf-8")

peso_mb = DESTINO.stat().st_size / 1_000_000
print(f"Peso del archivo: {peso_mb:.1f} MB")
if peso_mb >= LIMITE_MB:
    raise SystemExit(f"El recorte pesa {peso_mb:.1f} MB (límite {LIMITE_MB} MB)")
