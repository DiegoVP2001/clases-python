"""
Lee revision/puntajes.json y genera:
  - revision/resumen.csv   (para Excel / Google Sheets)
  - revision/resumen.md    (tabla legible en Markdown)

Uso: python tools/review_eval/calcular_notas.py

Solo procesa estudiantes con revisado=true.
"""

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
REVISION_DIR = BASE_DIR / "clases" / "reforzamiento-evaluacion" / "revision"

NOTA_MIN = 2.0
NOTA_APROBACION = 4.0
NOTA_MAX = 7.0


def calcular_nota(puntaje: float, exigencia: float, puntaje_max: float = 100.0) -> float:
    """
    Escala chilena lineal a tramos.
      exigencia=0.5 → 50 pts = nota 4.0
      exigencia=0.6 → 60 pts = nota 4.0
    """
    if puntaje_max == 0:
        return NOTA_MIN
    corte = exigencia * puntaje_max
    if puntaje <= corte:
        nota = NOTA_MIN + (NOTA_APROBACION - NOTA_MIN) * (puntaje / corte) if corte else NOTA_MIN
    else:
        nota = NOTA_APROBACION + (NOTA_MAX - NOTA_APROBACION) * (
            (puntaje - corte) / (puntaje_max - corte)
        )
    return round(min(max(nota, NOTA_MIN), NOTA_MAX), 1)


def generar_resumen() -> None:
    puntajes_path = REVISION_DIR / "puntajes.json"
    if not puntajes_path.exists():
        print("ERROR: revision/puntajes.json no encontrado. Ejecuta preparar_submissions.py primero.")
        return

    data = json.loads(puntajes_path.read_text(encoding="utf-8"))
    meta = data["metadata"]
    ej_keys = list(meta["ejercicios"].keys())
    puntaje_max = meta["puntaje_maximo"]

    rows = []
    pendientes = []

    for nombre, info in data["estudiantes"].items():
        if not info.get("revisado"):
            pendientes.append(nombre)
            continue
        row: dict = {"Nombre": nombre}
        total = 0
        for ej in ej_keys:
            obtenido = info["puntajes"].get(ej, {}).get("obtenido") or 0
            row[ej.upper()] = obtenido
            total += obtenido
        row["Total"] = total
        row["Nota 50%"] = calcular_nota(total, 0.50, puntaje_max)
        row["Nota 60%"] = calcular_nota(total, 0.60, puntaje_max)
        rows.append(row)

    if not rows:
        print("No hay estudiantes revisados aún.")
        if pendientes:
            print(f"Pendientes ({len(pendientes)}): {', '.join(pendientes[:5])}...")
        return

    rows.sort(key=lambda r: r["Total"], reverse=True)

    col_names = ["Nombre"] + [k.upper() for k in ej_keys] + ["Total", "Nota 50%", "Nota 60%"]

    # --- CSV ---
    csv_path = REVISION_DIR / "resumen.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(rows)

    # --- Markdown ---
    ejercicios_meta = meta["ejercicios"]
    header_labels = (
        ["Nombre"]
        + [f"Ej{i+1} ({ejercicios_meta[k]['maximo']}p)" for i, k in enumerate(ej_keys)]
        + ["Total", "Nota 50%", "Nota 60%"]
    )

    lines = [
        f"# Resumen — {meta['nombre']}",
        "",
        f"Revisados: {len(rows)}  |  Pendientes: {len(pendientes)}",
        "",
        "## Tabla de puntajes",
        "",
        "| " + " | ".join(header_labels) + " |",
        "| " + " | ".join(["---"] * len(header_labels)) + " |",
    ]
    for row in rows:
        vals = (
            [row["Nombre"]]
            + [str(row[k.upper()]) for k in ej_keys]
            + [str(row["Total"]), str(row["Nota 50%"]), str(row["Nota 60%"])]
        )
        lines.append("| " + " | ".join(vals) + " |")

    # Stats
    totales = [r["Total"] for r in rows]
    notas_50 = [r["Nota 50%"] for r in rows]
    notas_60 = [r["Nota 60%"] for r in rows]
    n = len(rows)
    aprobados_50 = sum(1 for x in notas_50 if x >= 4.0)
    aprobados_60 = sum(1 for x in notas_60 if x >= 4.0)

    lines += [
        "",
        "## Estadisticas del curso",
        "",
        "| Metrica | Valor |",
        "| --- | --- |",
        f"| Revisados | {n} |",
        f"| Promedio puntaje | {sum(totales)/n:.1f} pts |",
        f"| Maximo | {max(totales)} pts |",
        f"| Minimo | {min(totales)} pts |",
        f"| Aprobados con exigencia 50% | {aprobados_50} / {n} |",
        f"| Aprobados con exigencia 60% | {aprobados_60} / {n} |",
        f"| Promedio nota (50%) | {sum(notas_50)/n:.2f} |",
        f"| Promedio nota (60%) | {sum(notas_60)/n:.2f} |",
    ]

    if pendientes:
        lines += ["", "## Pendientes de revision", ""]
        for p in pendientes:
            lines.append(f"- {p}")

    (REVISION_DIR / "resumen.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Resumen generado ({n} estudiantes revisados):")
    print(f"  CSV : revision/resumen.csv")
    print(f"  MD  : revision/resumen.md")
    print(f"  Promedio: {sum(totales)/n:.1f} pts")
    print(f"  Aprobados (60%): {aprobados_60}/{n}")
    if pendientes:
        print(f"  Pendientes: {len(pendientes)}")


if __name__ == "__main__":
    generar_resumen()
