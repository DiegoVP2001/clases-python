# -*- coding: utf-8 -*-
"""
Gate de consolidacion para calificacion masiva con subagentes en paralelo.

Contexto: cuando varios subagentes califican batches distintos al mismo tiempo,
cada uno ve solo su parte. El riesgo no es que uno se equivoque -- es que dos
califiquen el mismo patron de codigo distinto sin que nadie lo note. Este script
corre las verificaciones que la sesion principal DEBE pasar antes de escribir
nada a puntajes.json.

Entrada: los JSON que devuelven los subagentes (esquema de PROMPT_BATCH), mas el
codigo extraido programaticamente. Los subagentes no escriben archivos: devuelven
JSON, se consolida aca, y recien despues se escribe.

Uso:
    python tools/review_eval/gate_consolidacion.py \
        --codigo ruta/codigo_extraido_evaluacion2.json \
        --batches b1.json b2.json b3.json b4.json \
        --items-programa 2.1 2.2 2.3 2.4

Que verifica:
  1. Aritmetica    -- componentes suman el total del item; items suman el total
                      del estudiante; ningun componente excede su maximo.
  2. Estructura    -- todos traen los mismos items y el mismo numero de
                      componentes por item (se infiere la forma mayoritaria).
  3. Portazo       -- en los items "arregla el bug", si el primer componente es
                      0, ningun otro puede sumar.
  4. Cobertura     -- celda vacia => 0; celda con codigo => se reporta si quedo
                      en 0, para revisarlo a mano.
  5. Consistencia  -- LO IMPORTANTE: agrupa el codigo real normalizado (sin
                      comentarios, sin nombres de variable, sin el texto de los
                      mensajes) y avisa si dos estudiantes con codigo equivalente
                      recibieron puntajes distintos.
  6. Sintaxis      -- que items de programa completo no compilan (util para
                      aplicar un descuento parejo, y para no confiar en el output
                      pegado en la celda).
  7. Patrones      -- junta el campo patrones_nuevos de todos los batches.

OJO con el limite del metodo: la verificacion 5 detecta cuando dos agentes se
contradicen, NO cuando los cuatro se equivocan igual. Sigue siendo obligatorio
verificar a mano un par de casos ejecutando el codigo.
"""

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def celda_vacia(codigo) -> bool:
    """Vacia = sin ninguna linea util (los comentarios del enunciado no cuentan)."""
    if not codigo:
        return True
    return not [l for l in codigo.splitlines()
                if l.strip() and not l.strip().startswith("#")]


def normalizar(codigo: str) -> str:
    """Deja el ESQUELETO del codigo: estructura + indentacion + operadores.

    Se borra todo lo que la rubrica declara irrelevante -- comentarios, mayusculas,
    tildes, espacios, y el texto de los mensajes (que por politica no se exige
    literal). Lo que queda es comparable entre estudiantes.

    Cuidado al leer los resultados: al borrar los strings tambien se borra QUE
    mensaje quedo en cada rama. Dos codigos con el mismo esqueleto pueden merecer
    puntajes distintos si el componente que falla es justamente "cada mensaje en
    su franja". Por eso la salida dice "revisar", no "error".
    """
    salida = []
    for linea in codigo.splitlines():
        linea = re.sub(r"#.*$", "", linea)
        if not linea.strip():
            continue
        indent = len(linea) - len(linea.lstrip())
        cuerpo = re.sub(r"\s+", "", linea.strip()).replace("'", '"')
        cuerpo = unicodedata.normalize("NFKD", cuerpo)
        cuerpo = "".join(c for c in cuerpo if not unicodedata.combining(c)).lower()
        cuerpo = re.sub(r'"[^"]*"', '"S"', cuerpo)
        salida.append(f"{indent // 4}|{cuerpo}")
    return "\n".join(salida)


def cargar_batches(rutas):
    """[(nombre_batch, {estudiante: registro})], mas los patrones nuevos."""
    estudiantes, patrones, de_que_batch = {}, [], {}
    for ruta in rutas:
        data = json.loads(Path(ruta).read_text(encoding="utf-8"))
        etiqueta = str(data.get("batch", Path(ruta).stem))
        for nombre, registro in data["estudiantes"].items():
            assert nombre not in estudiantes, f"{nombre} aparece en dos batches"
            estudiantes[nombre] = registro
            de_que_batch[nombre] = etiqueta
        for p in data.get("patrones_nuevos", []):
            patrones.append(dict(p, batch=etiqueta))
    return estudiantes, de_que_batch, patrones


# --------------------------------------------------------------------------
# Verificaciones
# --------------------------------------------------------------------------

def verificar_aritmetica(estudiantes):
    problemas = []
    for nombre, reg in estudiantes.items():
        suma_items = 0
        for item_id, info in reg["items"].items():
            comps = info["componentes"]
            suma = sum(c["obtenido"] for c in comps)
            pen = info.get("penalizacion", {}).get("puntos", 0)
            esperado = max(0, suma - pen)
            if info["total"] != esperado:
                problemas.append(
                    f"{nombre} / {item_id}: los componentes dan {esperado} y el total dice {info['total']}")
            if info["total"] > info["maximo"]:
                problemas.append(f"{nombre} / {item_id}: {info['total']} supera el máximo {info['maximo']}")
            for c in comps:
                if not (0 <= c["obtenido"] <= c["maximo"]):
                    problemas.append(f"{nombre} / {item_id} / {c['nombre']}: fuera de rango")
            suma_items += info["total"]
        if reg.get("total_estudiante") not in (None, suma_items):
            problemas.append(
                f"{nombre}: los ítems suman {suma_items} y el total dice {reg['total_estudiante']}")
    return problemas


def verificar_estructura(estudiantes):
    """La forma mayoritaria es la referencia; se reporta quien se desvía."""
    problemas = []
    items_por_est = {n: set(r["items"]) for n, r in estudiantes.items()}
    forma = Counter(frozenset(v) for v in items_por_est.values()).most_common(1)[0][0]
    for nombre, items in items_por_est.items():
        if items != set(forma):
            faltan, sobran = set(forma) - items, items - set(forma)
            problemas.append(f"{nombre}: ítems distintos (faltan {sorted(faltan)}, sobran {sorted(sobran)})")

    n_comp = defaultdict(Counter)
    for reg in estudiantes.values():
        for item_id, info in reg["items"].items():
            n_comp[item_id][len(info["componentes"])] += 1
    esperado = {i: c.most_common(1)[0][0] for i, c in n_comp.items()}
    for nombre, reg in estudiantes.items():
        for item_id, info in reg["items"].items():
            if len(info["componentes"]) != esperado[item_id]:
                problemas.append(
                    f"{nombre} / {item_id}: {len(info['componentes'])} componentes "
                    f"(el resto del curso trae {esperado[item_id]})")
    return problemas, esperado


def verificar_portazo(estudiantes, items_bug):
    problemas = []
    for nombre, reg in estudiantes.items():
        for item_id in items_bug:
            info = reg["items"].get(item_id)
            if not info:
                continue
            comps = info["componentes"]
            if comps[0]["obtenido"] == 0 and any(c["obtenido"] > 0 for c in comps[1:]):
                problemas.append(f"{nombre} / {item_id}: viola la regla de portazo")
    return problemas


def verificar_cobertura(estudiantes, codigo):
    vacios_con_puntaje, con_codigo_en_cero = [], []
    for nombre, reg in estudiantes.items():
        items_codigo = codigo["estudiantes"][nombre]["items"]
        for item_id, info in reg["items"].items():
            crudo = items_codigo.get(item_id, {}).get("codigo")
            if celda_vacia(crudo):
                if info["total"] != 0:
                    vacios_con_puntaje.append(f"{nombre} / {item_id}: celda vacía con {info['total']} pts")
            elif info["total"] == 0:
                con_codigo_en_cero.append(f"{nombre} / {item_id} ({len(crudo.strip())} chars)")
    return vacios_con_puntaje, con_codigo_en_cero


def verificar_consistencia(estudiantes, codigo, de_que_batch):
    """El corazon del gate: mismo esqueleto de codigo -> mismo puntaje."""
    grupos = defaultdict(lambda: defaultdict(list))
    for nombre, reg in estudiantes.items():
        items_codigo = codigo["estudiantes"][nombre]["items"]
        for item_id in reg["items"]:
            crudo = items_codigo.get(item_id, {}).get("codigo")
            if celda_vacia(crudo):
                continue
            grupos[item_id][normalizar(crudo)].append(nombre)

    hallazgos = []
    for item_id in sorted(grupos):
        for nombres in grupos[item_id].values():
            if len(nombres) < 2:
                continue
            puntajes = {n: estudiantes[n]["items"][item_id]["total"] for n in nombres}
            if len(set(puntajes.values())) > 1:
                detalle = ", ".join(f"{n}(b{de_que_batch[n]})={p}" for n, p in puntajes.items())
                hallazgos.append(f"{item_id}: código equivalente con puntajes distintos -> {detalle}")
    return hallazgos


def escanear_sintaxis(estudiantes, codigo, items_programa):
    """Items de programa completo que no compilan. Solo SyntaxError: los errores
    de ejecucion normalmente ya los cubre algun componente de la rubrica, y
    descontarlos aparte seria penalizar el mismo error dos veces."""
    hallazgos = []
    for nombre in sorted(estudiantes):
        items_codigo = codigo["estudiantes"][nombre]["items"]
        for item_id in items_programa:
            crudo = items_codigo.get(item_id, {}).get("codigo")
            if celda_vacia(crudo):
                continue
            try:
                compile(crudo, "<entrega>", "exec")
            except SyntaxError as e:
                total = estudiantes[nombre]["items"][item_id]["total"]
                hallazgos.append(f"{nombre} / {item_id}: {e.msg}  (hoy vale {total} pts)")
            except Exception:
                pass
    return hallazgos


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Gate de consolidación de batches paralelos")
    ap.add_argument("--codigo", required=True, help="codigo_extraido_<evaluacion>.json")
    ap.add_argument("--batches", required=True, nargs="+", help="JSON devuelto por cada subagente")
    ap.add_argument("--items-bug", nargs="*", default=[],
                    help='Ítems "arregla el bug" donde rige la regla de portazo')
    ap.add_argument("--items-programa", nargs="*", default=[],
                    help="Ítems de programa completo, para el escaneo de sintaxis")
    args = ap.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    codigo = json.loads(Path(args.codigo).read_text(encoding="utf-8"))
    estudiantes, de_que_batch, patrones = cargar_batches(args.batches)

    def seccion(titulo):
        print("\n" + "=" * 78 + f"\n{titulo}\n" + "=" * 78)

    def listar(items, ok):
        print("\n".join(f"  {x}" for x in items) if items else f"  {ok}")

    bloqueantes = 0

    seccion(f"1) ARITMÉTICA  ({len(estudiantes)} estudiantes)")
    p = verificar_aritmetica(estudiantes)
    bloqueantes += len(p)
    listar(p, "OK: sumas y rangos cuadran.")

    seccion("2) ESTRUCTURA")
    p, esperado = verificar_estructura(estudiantes)
    bloqueantes += len(p)
    listar(p, f"OK: todos con los mismos ítems y componentes ({esperado}).")

    if args.items_bug:
        seccion("3) REGLA DE PORTAZO")
        p = verificar_portazo(estudiantes, args.items_bug)
        bloqueantes += len(p)
        listar(p, "OK: se respeta en todos.")

    seccion("4) COBERTURA")
    vacios, en_cero = verificar_cobertura(estudiantes, codigo)
    bloqueantes += len(vacios)
    print("  Celdas vacías con puntaje (BLOQUEANTE):")
    listar(vacios, "ninguna")
    print("  Con código pero en 0 (revisar a mano, puede ser correcto):")
    listar(en_cero, "ninguno")

    seccion("5) CONSISTENCIA ENTRE BATCHES")
    h = verificar_consistencia(estudiantes, codigo, de_que_batch)
    listar(h, "OK: ningún código equivalente recibió puntajes distintos.")
    if h:
        print("\n  Revisa el código crudo de cada grupo antes de concluir: el normalizador")
        print("  borra el texto de los mensajes, así que un ítem donde lo que falla es")
        print("  QUÉ mensaje quedó en cada rama aparece acá siendo correcto.")

    if args.items_programa:
        seccion("6) SINTAXIS (ítems de programa completo)")
        h = escanear_sintaxis(estudiantes, codigo, args.items_programa)
        listar(h, "OK: todos compilan.")

    seccion(f"7) PATRONES NUEVOS REPORTADOS  ({len(patrones)})")
    if patrones:
        for pat in patrones:
            print(f"  [b{pat['batch']}] {pat.get('estudiante','?')} / {pat.get('item','?')}")
            print(f"      patrón : {pat.get('patron','')}")
            print(f"      no calza: {pat.get('por_que_no_calza','')}")
            print(f"      usó    : {pat.get('nivel_usado','')}")
    else:
        print("  ninguno")
    print("\n  Los patrones se resuelven SUBIÉNDOLOS A LA RÚBRICA (aplican a todos),")
    print("  nunca parchando el puntaje de un estudiante.")

    seccion("RESULTADO")
    if bloqueantes:
        print(f"  ❌ {bloqueantes} problema(s) bloqueante(s). NO escribas puntajes todavía.")
    else:
        print("  ✅ Sin bloqueantes. Falta lo que ningún script puede hacer por ti:")
        print("     verificar a mano un par de casos ejecutando el código, y resolver")
        print("     los patrones nuevos con Diego. El cruce entre agentes detecta")
        print("     cuando dos se contradicen, no cuando todos se equivocan igual.")
    return 1 if bloqueantes else 0


if __name__ == "__main__":
    raise SystemExit(main())
