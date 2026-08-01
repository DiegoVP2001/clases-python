# -*- coding: utf-8 -*-
"""
Motor generico de Colabs personalizados de devolucion (rubrica parcelada por
componentes). Extraido de la Evaluacion 2 (Clase 19, Condicionales) el
2026-07-30 para poder reutilizarlo en las evaluaciones de Ciclos y de
Funciones+Strings+Listas.

Reparto de responsabilidades:

  - ESTE MODULO (generico): el formato del cuaderno. Como se renderiza la tabla
    de componentes, el bloque "Lo que escribiste" vs "Como debia quedar", el
    cierre "En simple", el mensaje de apertura, el calculo de totales y las
    validaciones que impiden que los datos violen la rubrica en silencio.

  - EL SCRIPT DE CADA EVALUACION (especifico): que items existen, cuanto vale
    cada componente, la solucion de referencia de cada item, y los puntajes y
    razones de cada estudiante. Ese script arma un `Devolucion` y llama a
    `generar_colabs()`.

Convenciones de fondo (ver la skill `revisar-evaluacion`):
  - El codigo del estudiante SIEMPRE viene del JSON del extractor programatico,
    nunca transcrito a mano.
  - Todo item se parcela por componentes independientes.
  - En items "arregla el bug" rige la regla de portazo: si el primer componente
    (Diagnostico) es 0, ningun otro componente del item puede sumar.
  - Mostrar o no la nota es configurable (`mostrar_nota`). Por defecto NO se
    muestra -- ese era el acuerdo original. Diego lo activo para la Evaluacion 2
    el 2026-08-01, junto con las decimas de bono y el reparto en carpetas por
    tramo de logro.
"""

import json
import textwrap
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple


# --------------------------------------------------------------------------
# Helpers de texto y celdas
# --------------------------------------------------------------------------

def bloque_cierre(texto: str, ancho: int = 92) -> str:
    """Convierte un texto narrativo en un bloque de comentarios '# ...' envuelto
    a `ancho` columnas. Los parrafos se separan con una linea en blanco."""
    lineas_salida = []
    for parrafo in texto.strip("\n").split("\n"):
        if not parrafo.strip():
            lineas_salida.append("#")
            continue
        for linea in textwrap.wrap(parrafo.strip(), ancho):
            lineas_salida.append(f"# {linea}")
    return "\n".join(lineas_salida)


def md_cell(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def code_cell(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def item_obtenido(info: dict) -> Optional[int]:
    """Puntaje de un item = suma de sus componentes, menos la penalizacion del
    item si la hay (None si algun componente esta pendiente).

    La penalizacion es un descuento que NO pertenece a ningun componente -- por
    ejemplo, que el programa no alcance a ejecutar. Se modela aparte justamente
    para no repartir a la fuerza un castigo transversal dentro de componentes
    que miden decisiones de logica. Nunca baja el item de 0.
    """
    obtenidos = [c["obtenido"] for c in info["componentes"]]
    if any(o is None for o in obtenidos):
        return None
    return max(0, sum(obtenidos) - (info.get("penalizacion") or {}).get("puntos", 0))


# --------------------------------------------------------------------------
# Nota (escala chilena) y decimas de bono
# --------------------------------------------------------------------------

def _redondear(valor: float, decimales: int = 1) -> float:
    """Redondeo half-up, como se calcula una nota a mano. `round()` de Python usa
    redondeo bancario (round(4.25, 1) -> 4.2), que no es lo esperado aca."""
    cuant = Decimal(1).scaleb(-decimales)
    return float(Decimal(str(valor)).quantize(cuant, rounding=ROUND_HALF_UP))


def calcular_nota(puntaje: int, maximo: int, exigencia: float = 0.5,
                  nota_min: float = 2.0, nota_aprob: float = 4.0,
                  nota_max: float = 7.0) -> float:
    """Escala chilena de dos tramos lineales. Con exigencia 0.5 sobre 100 pts:
    0 -> nota_min, 50 -> nota_aprob, 100 -> nota_max."""
    corte = maximo * exigencia
    if puntaje < corte:
        nota = nota_min + (nota_aprob - nota_min) * (puntaje / corte)
    else:
        nota = nota_aprob + (nota_max - nota_aprob) * ((puntaje - corte) / (maximo - corte))
    return _redondear(nota)


def _coma(valor: float) -> str:
    """5.6 -> '5,6' (separador decimal chileno)."""
    return f"{valor:.1f}".replace(".", ",")


def bloque_nota(dev: "Devolucion", nombre: str, puntaje: int) -> str:
    """Tabla de nota al pie del encabezado: puntaje -> nota base -> decimas -> final."""
    nota_base = calcular_nota(puntaje, dev.maximo_total, dev.exigencia,
                              dev.nota_min, dev.nota_aprob, dev.nota_max)
    decimas = (dev.decimas or {}).get(nombre, 0)
    nota_final = min(dev.nota_max, _redondear(nota_base + decimas / 10))

    filas = [
        "| | |",
        "|---|---|",
        f"| Puntaje | {puntaje} / {dev.maximo_total} |",
        f"| Nota de la evaluación (exigencia {int(dev.exigencia * 100)}%) | {_coma(nota_base)} |",
        f"| {dev.etiqueta_decimas} | +{_coma(decimas / 10)} |",
        f"| **Nota final** | **{_coma(nota_final)}** |",
    ]
    pie = dev.nota_pie_decimas.format(decimas=decimas)
    if decimas == 0:
        pie = dev.nota_pie_sin_decimas
    return "### 🧮 Tu nota\n\n" + "\n".join(filas) + f"\n\n{pie}"


def tramo_de(puntaje: int, maximo: int, tramos: Sequence[Tuple[str, int, int]]) -> Optional[str]:
    """Etiqueta del tramo de logro (carpeta destino) segun el % obtenido."""
    if not tramos:
        return None
    pct = 100 * puntaje / maximo
    for etiqueta, desde, hasta in tramos:
        if desde <= pct <= hasta:
            return etiqueta
    return None


# --------------------------------------------------------------------------
# Configuracion de una evaluacion
# --------------------------------------------------------------------------

@dataclass
class Devolucion:
    """Todo lo especifico de una evaluacion. Lo arma su propio script."""

    subtitulo: str                                  # ej. "Evaluación 2 — Clase 19 (Condicionales)"
    item_titulos: Dict[str, str]                    # item_id -> titulo legible
    item_maximos: Dict[str, int]                    # item_id -> puntaje maximo
    componentes_item: Dict[str, List[Tuple[str, int]]]   # item_id -> [(nombre_componente, pts), ...]
    soluciones_base: Dict[str, str]                 # item_id -> solucion de referencia sin anotar
    mensajes_apertura: Dict[str, str]               # estudiante -> mensaje macro de apertura
    estudiantes: Dict[str, dict]                    # estudiante -> {item_id: {componentes, solucion}}
    codigo_path: Path                               # JSON del extractor programatico
    out_dir: Path                                   # carpeta destino de los .ipynb
    items_bug: Sequence[str] = ()                   # items "arregla el bug" (rige la regla de portazo)
    sufijo_archivo: str = " - Revisión Detallada"
    nota_metodo: Optional[str] = None               # parrafo extra en el encabezado (ver texto_metodo_por_defecto)

    # --- Nota (opt-in: por defecto el cuaderno solo muestra puntajes) ---
    mostrar_nota: bool = False
    exigencia: float = 0.5
    nota_min: float = 2.0
    nota_aprob: float = 4.0
    nota_max: float = 7.0
    decimas: Dict[str, int] = field(default_factory=dict)   # estudiante -> decimas de bono (1 decima = 0,1)
    etiqueta_decimas: str = "Décimas de bono"
    nota_pie_decimas: str = "Las décimas ya vienen sumadas en la nota final."
    nota_pie_sin_decimas: str = "En esta evaluación no se sumaron décimas de bono a tu nota."

    # --- Reparto en carpetas por tramo de logro: [(etiqueta, %desde, %hasta)] ---
    tramos_logro: Sequence[Tuple[str, int, int]] = ()

    @property
    def item_orden(self) -> List[str]:
        return list(self.item_titulos.keys())

    @property
    def maximo_total(self) -> int:
        return sum(self.item_maximos.values())


def texto_metodo_por_defecto(con_items_bug: bool) -> str:
    """Parrafo del encabezado que le explica al estudiante como se corrigio.
    Incluye el criterio permanente de Diego sobre no evaluar eficiencia."""
    base = (
        "Cada ítem muestra tu código tal cual lo entregaste (\"📝 Lo que escribiste\") y la solución de "
        "referencia (\"✅ Cómo debía quedar\"), con comentarios en las líneas donde algo faltó, más una "
        "explicación breve al final del código (\"💬 En simple\"). Todo se revisó **ejecutando el código**, "
        "no solo leyéndolo, y el puntaje de cada ítem se desglosa **por componente**: puedes fallar una "
        "parte y aun así recibir el puntaje completo de las demás.\n\n"
        "Algo importante sobre cómo se corrigió: **no se evalúa la elegancia ni la eficiencia del código** "
        "— si tu programa hace lo que pide el enunciado, no importa que sea más largo o distinto a la "
        "solución."
    )
    if con_items_bug:
        base += (
            " Y en los ítems de \"arregla el bug\" el puntaje mira tres cosas: 🔎 **Diagnóstico** "
            "(encontrar dónde estaba el error), 🔧 **Corrección** (que el arreglo deje la lógica bien) y "
            "🛡️ **Sin daños** (que el resto siga funcionando)."
        )
    return base


# --------------------------------------------------------------------------
# Validaciones: los datos no pueden violar la rubrica en silencio
# --------------------------------------------------------------------------

def validar(dev: Devolucion) -> None:
    for item_id, componentes in dev.componentes_item.items():
        assert sum(pts for _, pts in componentes) == dev.item_maximos[item_id], (
            f"Los componentes de {item_id} no suman el máximo declarado en item_maximos"
        )

    for nombre, items in dev.estudiantes.items():
        assert nombre in dev.mensajes_apertura, f"{nombre}: falta su mensaje de apertura"
        for item_id in dev.item_orden:
            info = items[item_id]
            assert "componentes" in info, f"{nombre} / {item_id}: falta el desglose por componentes"
            assert len(info["componentes"]) == len(dev.componentes_item[item_id]), (
                f"{nombre} / {item_id}: el desglose no coincide con componentes_item"
            )
            for (nombre_comp, max_comp), comp in zip(dev.componentes_item[item_id], info["componentes"]):
                obt = comp["obtenido"]
                assert obt is None or 0 <= obt <= max_comp, (
                    f"{nombre} / {item_id} / {nombre_comp}: puntaje fuera de rango (0-{max_comp})"
                )
            pen = info.get("penalizacion")
            if pen:
                assert {"nombre", "puntos", "razon"} <= set(pen), (
                    f"{nombre} / {item_id}: la penalización necesita nombre, puntos y razón"
                )
                assert pen["puntos"] > 0, f"{nombre} / {item_id}: penalización sin puntos"
        for item_id in dev.items_bug:
            comps = items[item_id]["componentes"]
            if comps[0]["obtenido"] == 0:
                assert all(c["obtenido"] == 0 for c in comps[1:]), (
                    f"{nombre} / {item_id}: viola la regla de portazo "
                    f"(Diagnóstico en 0 pero otros componentes suman)"
                )

    # Si se muestra la nota con decimas, nadie puede quedar fuera del registro
    # por omision: un estudiante ausente del dict sumaria 0 en silencio.
    if dev.mostrar_nota and dev.decimas:
        faltan = sorted(set(dev.estudiantes) - set(dev.decimas))
        assert not faltan, f"Sin décimas registradas: {', '.join(faltan)}"


# --------------------------------------------------------------------------
# Construccion del cuaderno
# --------------------------------------------------------------------------

def construir_notebook(dev: Devolucion, nombre: str, codigo_estudiante: dict) -> Tuple[dict, Optional[int]]:
    info_items = dev.estudiantes[nombre]
    obtenidos = [item_obtenido(info_items[i]) for i in dev.item_orden]
    hay_pendientes = any(o is None for o in obtenidos)
    subtotal = sum(o for o in obtenidos if o is not None)
    maximo_confirmado = sum(
        dev.item_maximos[i] for i, o in zip(dev.item_orden, obtenidos) if o is not None
    )

    resumen_total = (
        f"**Subtotal confirmado: {subtotal} / {maximo_confirmado}** "
        f"(quedan {dev.maximo_total - maximo_confirmado} pts pendientes — ver más abajo)"
        if hay_pendientes else
        f"**Puntaje total: {subtotal} / {dev.maximo_total}**"
    )

    metodo = dev.nota_metodo or texto_metodo_por_defecto(bool(dev.items_bug))

    # La nota solo se calcula si el puntaje esta cerrado: con items pendientes
    # seria una nota provisoria y confundiria mas de lo que informa.
    tabla_nota = ""
    if dev.mostrar_nota and not hay_pendientes:
        tabla_nota = bloque_nota(dev, nombre, subtotal) + "\n\n"

    cells = [md_cell(
        f"# 🔎 Revisión detallada — {nombre}\n\n"
        f"**{dev.subtitulo}**\n\n"
        f"{dev.mensajes_apertura[nombre]}\n\n"
        f"---\n\n"
        f"{resumen_total}\n\n"
        f"{tabla_nota}"
        f"{metodo}"
    )]

    for item_id in dev.item_orden:
        info = info_items[item_id]
        obtenido = item_obtenido(info)
        maximo = dev.item_maximos[item_id]

        if obtenido is None:
            emoji, puntaje_txt = "❓", f"PENDIENTE / {maximo}"
        else:
            emoji = "✅" if obtenido == maximo else ("⚠️" if obtenido > 0 else "❌")
            puntaje_txt = f"{obtenido} / {maximo}"

        filas = ["| Componente | Puntaje | Comentario |", "|---|---|---|"]
        for (nombre_comp, max_comp), comp in zip(dev.componentes_item[item_id], info["componentes"]):
            obt_comp = comp["obtenido"]
            if obt_comp is None:
                celda_pts = f"❓ PENDIENTE / {max_comp}"
            else:
                emoji_comp = "✅" if obt_comp == max_comp else ("⚠️" if obt_comp > 0 else "❌")
                celda_pts = f"{obt_comp}/{max_comp} {emoji_comp}"
            filas.append(f"| {nombre_comp} | {celda_pts} | {comp['razon']} |")

        pen = info.get("penalizacion")
        if pen:
            filas.append(f"| {pen['nombre']} | −{pen['puntos']} | {pen['razon']} |")

        cells.append(md_cell(
            f"---\n### {emoji} Ítem {item_id} — {dev.item_titulos[item_id]}\n\n"
            f"**Puntaje: {puntaje_txt}**\n\n"
            f"**Desglose por componente** (✅ completo · ⚠️ parcial · ❌ cero):\n\n"
            + "\n".join(filas)
        ))

        codigo_real = codigo_estudiante[item_id]["codigo"]
        cells.append(md_cell("📝 **Lo que escribiste:**"))
        cells.append(code_cell(
            codigo_real if codigo_real and codigo_real.strip()
            else "# (celda vacía en la entrega original)"
        ))

        cells.append(md_cell("✅ **Cómo debía quedar:**"))
        cells.append(code_cell(
            info["solucion"] if info["solucion"] is not None else dev.soluciones_base[item_id]
        ))

    cells.append(md_cell(f"---\n## 🏁 {resumen_total}\n\n{tabla_nota}".rstrip() + "\n"))

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    return notebook, (None if hay_pendientes else subtotal)


def generar_colabs(dev: Devolucion, log: Callable[[str], None] = print) -> List[Tuple[str, int]]:
    """Valida, construye y escribe un .ipynb por estudiante. Devuelve [(nombre, total)].
    Si hay `tramos_logro`, cada cuaderno se escribe en la subcarpeta de su tramo."""
    validar(dev)
    codigo_data = json.loads(Path(dev.codigo_path).read_text(encoding="utf-8"))
    dev.out_dir.mkdir(parents=True, exist_ok=True)

    resultados = []
    for nombre in dev.estudiantes:
        codigo_estudiante = codigo_data["estudiantes"][nombre]["items"]
        nb, total = construir_notebook(dev, nombre, codigo_estudiante)

        destino = dev.out_dir
        if total is not None:
            tramo = tramo_de(total, dev.maximo_total, dev.tramos_logro)
            if tramo:
                destino = dev.out_dir / tramo
                destino.mkdir(parents=True, exist_ok=True)

        out_path = destino / f"{nombre}{dev.sufijo_archivo}.ipynb"
        out_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")

        etiqueta = "PENDIENTE" if total is None else f"{total}/{dev.maximo_total}"
        if dev.mostrar_nota and total is not None:
            nota = calcular_nota(total, dev.maximo_total, dev.exigencia,
                                 dev.nota_min, dev.nota_aprob, dev.nota_max)
            final = min(dev.nota_max, _redondear(nota + dev.decimas.get(nombre, 0) / 10))
            etiqueta += f"  nota {_coma(nota)} +{dev.decimas.get(nombre, 0)}d -> {_coma(final)}"
        rel = out_path.relative_to(dev.out_dir)
        log(f"  -> {rel}  ({etiqueta})")
        resultados.append((nombre, total))
    return resultados


# --------------------------------------------------------------------------
# Volcado a puntajes.json
# --------------------------------------------------------------------------

def _comentario_item(dev: Devolucion, item_id: str, info: dict) -> str:
    """Comentario corto para puntajes.json: solo lo que costó puntos."""
    partes = []
    for (nombre_comp, max_comp), comp in zip(dev.componentes_item[item_id], info["componentes"]):
        if comp["obtenido"] is not None and comp["obtenido"] < max_comp:
            partes.append(f"[{nombre_comp} {comp['obtenido']}/{max_comp}] {comp['razon']}")
    pen = info.get("penalizacion")
    if pen:
        partes.append(f"[{pen['nombre']} −{pen['puntos']}] {pen['razon']}")
    return " ".join(partes) if partes else "Correcto en todos los componentes."


def escribir_puntajes(dev: Devolucion, puntajes_path: Path, fecha: Optional[str] = None,
                      log: Callable[[str], None] = print) -> dict:
    """Vuelca los puntajes de `dev` al puntajes.json de la evaluacion.

    La gracia de derivarlo de `dev` y no de una tabla aparte: los Colabs que ve
    el estudiante y el JSON que alimenta el resumen final salen de la MISMA
    estructura, asi que no pueden divergir. Es el mismo principio que hace que
    el codigo venga siempre del extractor y nunca de una transcripcion.

    Solo toca a los estudiantes presentes en `dev.estudiantes`; los demas
    (ausentes, no gradables) quedan intactos.
    """
    validar(dev)
    puntajes_path = Path(puntajes_path)
    data = json.loads(puntajes_path.read_text(encoding="utf-8"))

    faltan = sorted(set(dev.estudiantes) - set(data["estudiantes"]))
    assert not faltan, f"No están en {puntajes_path.name}: {', '.join(faltan)}"

    escritos = 0
    for nombre, items in dev.estudiantes.items():
        registro = data["estudiantes"][nombre]
        total = 0
        completo = True
        for item_id in dev.item_orden:
            info = items[item_id]
            obtenido = item_obtenido(info)
            registro["puntajes"][item_id]["obtenido"] = obtenido
            registro["puntajes"][item_id]["comentario"] = _comentario_item(dev, item_id, info)
            if obtenido is None:
                completo = False
            else:
                total += obtenido
        registro["revisado"] = completo
        if completo:
            registro["total"] = total
            escritos += 1

    if fecha:
        data.setdefault("metadata", {})["fecha_revision"] = fecha

    puntajes_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    log(f"  {escritos}/{len(dev.estudiantes)} estudiantes escritos en {puntajes_path.name}")
    return data
