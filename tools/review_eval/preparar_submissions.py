"""
Prepara las submissions de Google Classroom para revision.
Copia cada notebook (con o sin extension .ipynb) a revision/notebooks/
con nombre limpio. Genera manifest.json y el skeleton de puntajes.json.

Uso (desde la raiz del proyecto):
    python tools/review_eval/preparar_submissions.py
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
SUBMISSIONS_DIR = BASE_DIR / "clases" / "reforzamiento-evaluacion" / "cuadernos_ev_estudiantes"
REVISION_DIR = BASE_DIR / "clases" / "reforzamiento-evaluacion" / "revision"

EVALUACION_META = {
    "nombre": "Evaluacion 1 — Clases 1 a 7",
    "puntaje_maximo": 100,
    "ejercicios": {
        "ej1": {"nombre": "Promedio de notas",           "maximo": 10},
        "ej2": {"nombre": "Reporte feria escolar",       "maximo": 10},
        "ej3": {"nombre": "Simulador ahorro mensual",    "maximo": 15},
        "ej4": {"nombre": "Calculadora de descuento",    "maximo": 15},
        "ej5": {"nombre": "Reparto ganancias dulces",    "maximo": 15},
        "ej6": {"nombre": "Depuracion 5 errores",        "maximo": 15},
        "ej7": {"nombre": "Registro semanal de gastos",  "maximo": 20},
    },
}

SUFFIX_RE = re.compile(
    r"\s*-\s*Evaluaci[oó]n(\s+1\s+de\s+python)?(\s*\(\d+\))?$",
    re.IGNORECASE,
)


def clean_name(raw: str) -> str:
    return SUFFIX_RE.sub("", raw).strip() or raw.strip()


def preparar() -> None:
    notebooks_dir = REVISION_DIR / "notebooks"
    (REVISION_DIR / "feedback").mkdir(parents=True, exist_ok=True)
    notebooks_dir.mkdir(parents=True, exist_ok=True)

    # Group items by normalized (lowercase) student name to detect duplicates
    groups: dict[str, list[dict]] = {}
    advertencias: list[str] = []

    for item in sorted(SUBMISSIONS_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not item.is_file():
            continue

        ext = item.suffix.lower()

        # --- archivo con extension .ipynb ---
        if ext == ".ipynb":
            nombre = clean_name(item.stem)
            source_file = item
            tipo = "ipynb_con_extension"

        # --- notebook sin extension (formato Google Classroom) ---
        elif ext == "":
            nombre = clean_name(item.name)
            source_file = item
            tipo = "notebook_sin_extension"

        else:
            continue  # ignorar otros tipos de archivo

        key = nombre.lower()
        groups.setdefault(key, [])
        idx = len(groups[key]) + 1  # 1-based submission number

        display = nombre if idx == 1 else f"{nombre} (entrega {idx})"
        dest_stem = nombre if idx == 1 else f"{nombre} (entrega {idx})"
        dest = notebooks_dir / f"{dest_stem}.ipynb"

        shutil.copy2(source_file, dest)

        groups[key].append({
            "nombre": display,
            "nombre_base": nombre,
            "tipo_fuente": tipo,
            "archivo_fuente": str(item),
            "archivo_revision": str(dest.relative_to(BASE_DIR)),
            "estado": "ok" if idx == 1 else "duplicado",
        })

    # Flatten
    flat = [entry for entries in groups.values() for entry in entries]

    # --- manifest.json ---
    manifest = {
        "evaluacion": EVALUACION_META["nombre"],
        "fecha_preparacion": datetime.now().strftime("%Y-%m-%d"),
        "total": len(flat),
        "ok": sum(1 for e in flat if e["estado"] == "ok"),
        "vacios": sum(1 for e in flat if e["estado"] == "vacio"),
        "duplicados": sum(1 for e in flat if e["estado"] == "duplicado"),
        "advertencias": advertencias,
        "estudiantes": flat,
    }
    (REVISION_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # --- puntajes.json skeleton ---
    puntajes: dict = {
        "metadata": {
            **EVALUACION_META,
            "fecha_revision": None,
            "criterios_calibracion": {},
        },
        "estudiantes": {},
    }
    for entry in flat:
        if entry["estado"] not in ("ok", "duplicado"):
            continue
        puntajes["estudiantes"][entry["nombre"]] = {
            "archivo": entry["archivo_revision"],
            "revisado": False,
            "puntajes": {
                ej: {"obtenido": None, "maximo": meta["maximo"], "comentario": ""}
                for ej, meta in EVALUACION_META["ejercicios"].items()
            },
            "total": None,
        }
    (REVISION_DIR / "puntajes.json").write_text(
        json.dumps(puntajes, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # --- Print summary ---
    w = 52
    print("=" * w)
    print("  PREPARACION COMPLETADA")
    print("=" * w)
    print(f"  Total      : {manifest['total']}")
    print(f"  Con notebook : {manifest['ok']}")
    print(f"  Vacios       : {manifest['vacios']}")
    print(f"  Duplicados   : {manifest['duplicados']}")
    if advertencias:
        print("\n  Advertencias:")
        for a in advertencias:
            print(f"    * {a}")
    print(f"\n  -> revision/notebooks/  ({manifest['ok'] + manifest['duplicados']} archivos)")
    print(f"  -> revision/manifest.json")
    print(f"  -> revision/puntajes.json  (skeleton)")
    print("=" * w)


if __name__ == "__main__":
    preparar()
