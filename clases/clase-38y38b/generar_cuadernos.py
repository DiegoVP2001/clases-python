"""Genera Clase 38y38b - Responder con Datos: cuaderno de Código, cuaderno de Texto y Solucionario.

Fuente de verdad de los tres cuadernos: no editar los .ipynb a mano, editar acá y regenerar.
Al generar, cada ejemplo de la galería y cada solución se EJECUTA contra las bases v3 locales, y los resultados
que se muestran en el Solucionario y en la galería salen de esa ejecución (nada escrito a mano).

Uso:  python generar_cuadernos.py
"""
import base64
import contextlib
import io
import re
import sys
import warnings
from pathlib import Path
from urllib.parse import quote

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import nbformat
import pandas as pd
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

CARPETA = Path(__file__).resolve().parent
CLASES = CARPETA.parent
NOMBRE = "Clase 38y38b - Responder con Datos"
SAL_CODIGO = CARPETA / f"{NOMBRE} - Código.ipynb"
SAL_TEXTO = CARPETA / f"{NOMBRE} - Texto.ipynb"
SAL_SOL = CARPETA / f"{NOMBRE} - Solucionario.ipynb"
FOTO = CLASES / "clase-35-listas" / "foto_lun.png"
LOCAL_V3 = CARPETA / "datos-compartidos-v3"
LOCAL_GUAGUAS = CLASES / "clases-octubre" / "datos-compartidos" / "bbdd_guaguas.csv"

REPO = "https://raw.githubusercontent.com/DiegoVP2001/clases-python/master/clases/"
RAW = REPO + "clase-38y38b/datos-compartidos-v3/"
URL_GUAGUAS = REPO + "clases-octubre/datos-compartidos/bbdd_guaguas.csv"
GH = "https://github.com/DiegoVP2001/clases-python/blob/master/clases/"
LINK_DICCIONARIO = GH + "clase-38y38b/" + quote("Clase 38y38b - Diccionario de Columnas.pdf")
LINK_MUESTRA = GH + "clase-38y38b/" + quote("Clase 38y38b - Muestra de las Bases.pdf")
LINK_RUBRICA = ("https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-38y38b/"
                + quote("Clase 38y38b - Criterios de Evaluación del Proyecto.ipynb"))


# ───────────────────────── utilidades ─────────────────────────
def escapar_pesos(texto: str) -> str:
    """El signo peso suelto en markdown activa MathJax en Colab: se escapa fuera de bloques y de `código`."""
    salida, en_bloque = [], False
    for linea in texto.split("\n"):
        if linea.lstrip().startswith("```"):
            en_bloque = not en_bloque
            salida.append(linea)
        elif en_bloque:
            salida.append(linea)
        else:
            trozos = re.split(r"(`[^`]*`)", linea)
            salida.append("".join(t if t.startswith("`") else re.sub(r"(?<!\\)\$", r"\\$", t) for t in trozos))
    return "\n".join(salida)


class Cuaderno:
    def __init__(self):
        self.celdas = []

    def md(self, texto):
        self.celdas.append(new_markdown_cell(escapar_pesos(texto.strip("\n"))))

    def code(self, texto):
        self.celdas.append(new_code_cell(texto.strip("\n") + "\n" if texto.strip() else ""))

    def guardar(self, ruta):
        nb = new_notebook(cells=self.celdas)
        nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
        nb.metadata["language_info"] = {"name": "python"}
        nbformat.validate(nb)
        nbformat.write(nb, ruta)
        return nb


def correr(codigo: str, ns: dict) -> str:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), warnings.catch_warnings():
        warnings.simplefilter("ignore")           # plt.show() con el backend Agg avisa que no puede mostrar nada
        exec(codigo, ns)
    plt.close("all")
    return buf.getvalue()


def cl(v) -> str:
    """Número en formato chileno: miles con punto, decimales con coma."""
    if isinstance(v, (int,)) or float(v).is_integer():
        return f"{int(v):,}".replace(",", ".")
    return f"{v:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")


def lit(v) -> str:
    """Valor como se escribe en el curso: texto con comillas dobles, número y None tal cual."""
    return '"' + v.replace('"', '\\"') + '"' if isinstance(v, str) else repr(v)


# ───────────────────────── la receta ─────────────────────────
def espacios_codigo(esp: dict | None, titulo_ejemplo: bool = False) -> str:
    """Las líneas que se cambian. Con esp=None quedan en blanco (_____) para que el estudiante las llene."""
    v = (lambda k: lit(esp[k])) if esp else (lambda k: "_____")
    return (
        "# ── Lo único que cambias (tu pregunta, traducida) ──\n"
        f"COL_FILTRO = {v('COL_FILTRO'):<30} # 🔎 ¿en qué columna miro?\n"
        f"VALOR      = {v('VALOR'):<30} # 🔎 ¿con qué valor me quedo?  (texto con comillas, número sin comillas; None = no filtrar)\n"
        f"COL_GRUPO  = {v('COL_GRUPO'):<30} # 🧺 ¿qué junto?\n"
        f"COL_NUMERO = {v('COL_NUMERO'):<30} # 🔢 ¿qué cifra resumo?\n"
        f"RESUMEN    = {v('RESUMEN'):<30} # \"sum\" total · \"mean\" promedio · \"count\" cuántas filas\n"
        f"N          = {v('N'):<30} # ¿cuántos muestro?\n"
        f"TITULO     = {lit(esp.get('TITULO', '')) if esp else chr(34) * 2:<30} # opcional: tu propio título (vacío = se arma solo)\n"
    )


RECETA = '''# ── La receta (no la cambies) ──
if VALOR == None:
    filtrada = tabla
else:
    filtrada = tabla[tabla[COL_FILTRO] == VALOR]

usadas = filtrada[COL_NUMERO].notna().sum()
perdidas = filtrada[COL_NUMERO].isna().sum()
print("Filas que dejó el filtro:", len(filtrada))
print("Con dato en", COL_NUMERO, ":", usadas, "| sin dato (se pierden):", perdidas)

if len(filtrada) == 0:
    print("⚠️ El filtro dejó 0 filas: revisa cómo escribiste VALOR (mayúsculas, tildes, comillas).")
else:
    resumen = filtrada.groupby(COL_GRUPO)[COL_NUMERO].agg(RESUMEN)
    top = resumen.sort_values(ascending=False).head(N)

    print("Cifras del top:")
    print(top.round(2))
    if RESUMEN != "mean":
        print("% del total:")
        print((top / resumen.sum() * 100).round(1))
    print("Mayor:", top.index[0], "→", round(top.iloc[0], 2))
    print("Menor del top:", top.index[-1], "→", round(top.iloc[-1], 2))
    print("Promedio de los", len(resumen), "grupos:", round(resumen.mean(), 2))

    if TITULO == "":
        TITULO = RESUMEN + " de " + COL_NUMERO + " por " + COL_GRUPO
    top.sort_values().plot(kind="barh", title=TITULO, xlabel=COL_NUMERO, ylabel=COL_GRUPO)
    plt.show()
'''


def receta_completa(esp: dict | None) -> str:
    return espacios_codigo(esp) + "\n" + RECETA


# ───────────────────────── las bases ─────────────────────────
# cols: las 5 columnas sugeridas, con su rol. ejemplo: una receta ya llena, que se ejecuta al generar.
BASES = [
    dict(n="1", icono="💼", nombre="Empleabilidad e ingresos por carrera (SIES)", archivo="01_sies.csv", peso="",
         cols=[("🔎", "Área"), ("🔎", "Nombre carrera genérica"), ("🧺", "Nombre de institución"),
               ("🔢", "Empleabilidad 1er año"), ("🔢", "Ingreso_punto_medio")],
         ej=dict(pregunta="¿Cuánto ganan, en promedio, los ingenieros civiles industriales según su universidad?",
                 COL_FILTRO="Nombre carrera genérica", VALOR="Ingeniería Civil Industrial", COL_GRUPO="Nombre de institución",
                 COL_NUMERO="Ingreso_punto_medio", RESUMEN="mean", N=5,
                 nota="Hay 34 filas, pero solo 29 con dato de ingreso: las otras 5 se pierden, y eso va en tus límites.",
                 check=lambda ns: ns["perdidas"] == 5 and len(ns["filtrada"]) == 34)),
    dict(n="2", icono="🎓", nombre="Puntajes de corte por carrera — Admisión 2026 (DEMRE)", archivo="02_demre.csv", peso="",
         cols=[("🔎", "NOMBRE_CARRERA"), ("🔎", "AREA_CONOCIMIENTO_SIES"), ("🧺", "NOMBRE_UNIVERSIDAD"),
               ("🔢", "PROM_OBLIGATORIAS_ULTIMO_SELEC"), ("🔢", "VACANTES_REG")],
         ej=dict(pregunta="¿Cuántas vacantes ofrecen, en total y por área, las carreras que no completaron sus cupos?",
                 COL_FILTRO="COMPLETA_VACANTES_REG", VALOR=0, COL_GRUPO="AREA_CONOCIMIENTO_SIES",
                 COL_NUMERO="VACANTES_REG", RESUMEN="sum", N=5,
                 nota="`COMPLETA_VACANTES_REG` es 0 o 1: son etiquetas (0 = no completó, 1 = sí), no cantidades. Va sin comillas porque es número.",
                 check=lambda ns: ns["perdidas"] == 0)),
    dict(n="3", icono="📝", nombre="SIMCE 2° medio 2025, por establecimiento", archivo="03_simce_establecimiento.csv", peso="",
         cols=[("🔎", "nom_reg_rbd"), ("🔎", "nom_pro_rbd"), ("🧺", "nom_com_rbd"),
               ("🔢", "prom_lect2m_rbd"), ("🔢", "prom_mate2m_rbd")],
         ej=dict(pregunta="¿Cómo les fue en Matemática a las comunas de la provincia de Talagante?",
                 COL_FILTRO="nom_pro_rbd", VALOR="TALAGANTE", COL_GRUPO="nom_com_rbd",
                 COL_NUMERO="prom_mate2m_rbd", RESUMEN="mean", N=5,
                 nota="Es un promedio de promedios: un colegio con 20 estudiantes pesa igual que uno con 300. Dilo en tus límites.",
                 check=lambda ns: len(ns["filtrada"]) == 66)),
    dict(n="4", icono="🗺️", nombre="SIMCE 2° medio 2025, por comuna", archivo="04_simce_comuna.csv", peso="",
         cols=[("🔎", "nom_reg"), ("🔎", "nom_pro"), ("🧺", "nom_com"),
               ("🔢", "prom_lect2m_com"), ("🔢", "prom_mate2m_com")],
         ej=dict(pregunta="¿Qué comunas de la Región de Los Lagos tuvieron mejor puntaje en Lectura?",
                 COL_FILTRO="nom_reg", VALOR="Región de Los Lagos", COL_GRUPO="nom_com",
                 COL_NUMERO="prom_lect2m_com", RESUMEN="mean", N=5,
                 nota="Las regiones están escritas distinto en esta base (`Región de Los Lagos`, `Región de los ríos`): copia el valor tal cual de la tabla.",
                 check=lambda ns: len(ns["filtrada"]) == 30)),
    dict(n="5", icono="🏫", nombre="Matrícula de estudiantes por establecimiento 2025 (Mineduc)", archivo="05_matricula.csv", peso="",
         cols=[("🔎", "NOM_REG_RBD_A"), ("🔎", "NOM_COM_RBD"), ("🧺", "NOM_RBD"), ("🔢", "MAT_TOTAL"), ("🔢", "MAT_EXT")],
         ej=dict(pregunta="¿Qué colegios de Isla de Maipo tienen más estudiantes matriculados?",
                 COL_FILTRO="NOM_COM_RBD", VALOR="ISLA DE MAIPO", COL_GRUPO="NOM_RBD",
                 COL_NUMERO="MAT_TOTAL", RESUMEN="sum", N=5,
                 nota="`NOM_REG_RBD_A` usa siglas (por ejemplo `AYP`); para filtrar por lugar es más fácil `NOM_COM_RBD`.",
                 check=lambda ns: len(ns["filtrada"]) == 25)),
    dict(n="6", icono="💰", nombre="Subvenciones a establecimientos 2025", archivo="06_subvenciones.csv", peso="⏳ pesada (~29 MB)",
         cols=[("🔎", "NOM_REG_RBD_A"), ("🔎", "NOM_COM_RBD"), ("🧺", "NOMBRERBD"), ("🔢", "SEP_PRIO"), ("🔢", "MATRICULA")],
         ej=dict(pregunta="¿Qué colegios de Peñaflor recibieron más subvención SEP prioritaria en el año?",
                 COL_FILTRO="NOM_COM_RBD", VALOR="PEÑAFLOR", COL_GRUPO="NOMBRERBD",
                 COL_NUMERO="SEP_PRIO", RESUMEN="sum", N=5,
                 nota="Cada colegio aparece hasta 12 veces (una por mes): al sumar queda el total del año.",
                 check=lambda ns: len(ns["filtrada"]) == 624)),
    dict(n="7", icono="🚗", nombre="Siniestros de tránsito 2020-2025 (CONASET), Región Metropolitana", archivo="07_conaset_rm.csv", peso="⏳ pesada (~44 MB)",
         cols=[("🔎", "AÑO"), ("🔎", "CAUSA_NUEV"), ("🧺", "COMUNA"), ("🔢", "FALLECIDOS"), ("🔢", "TOTAL_LESI")],
         ej=dict(pregunta="¿Qué comunas de la Región Metropolitana tuvieron más fallecidos en siniestros de tránsito en 2025?",
                 COL_FILTRO="AÑO", VALOR=2025, COL_GRUPO="COMUNA",
                 COL_NUMERO="FALLECIDOS", RESUMEN="sum", N=5,
                 nota="`AÑO` es un número: va sin comillas.",
                 check=lambda ns: len(ns["filtrada"]) == 19198 and ns["top"].iloc[0] == 21)),
    dict(n="8", icono="🛒", nombre="Precios de alimentos al consumidor 2025 (ODEPA), Región Metropolitana", archivo="08a_odepa_consumidor.csv", peso="⏳ pesada (~11 MB)",
         cols=[("🔎", "Grupo"), ("🔎", "Unidad"), ("🧺", "Producto"), ("🧺", "Sector"), ("🔢", "Precio promedio")],
         ej=dict(pregunta="¿Qué familias de productos son más caras cuando el precio es por kilo?",
                 COL_FILTRO="Unidad", VALOR="$/kilo", COL_GRUPO="Grupo",
                 COL_NUMERO="Precio promedio", RESUMEN="mean", N=5,
                 nota="Filtramos una sola `Unidad` (`$/kilo`): promediar precios por kilo con precios por unidad o por litro no significa nada.",
                 check=lambda ns: len(ns["filtrada"]) == 47027)),
    dict(n="8b", icono="🚚", nombre="Precios mayoristas de frutas y hortalizas 2025 (ODEPA) — fuera del menú", archivo="08b_odepa_mayorista.csv", peso="⏳ pesada (~17 MB)",
         cols=[("🔎", "Subsector"), ("🔎", "Unidad de comercializacion"), ("🧺", "Producto"), ("🧺", "Mercado"), ("🔢", "Precio promedio")],
         ej=dict(pregunta="¿Qué productos son más caros por caja de 18 kilos en el mercado mayorista?",
                 COL_FILTRO="Unidad de comercializacion", VALOR="$/caja 18 kilos", COL_GRUPO="Producto",
                 COL_NUMERO="Precio promedio", RESUMEN="mean", N=5,
                 nota="De nuevo una sola unidad. Para filtrar por tipo de envase y cantidad usa `Envase`, `Unidad_cantidad` y `Unidad_medida`.",
                 check=lambda ns: ns["perdidas"] == 0 and len(ns["filtrada"]) > 0)),
    dict(n="8c", icono="🌳", nombre="Catastro frutícola (ODEPA-CIREN) — fuera del menú", archivo="08c_odepa_catastro_fruticola.csv", peso="",
         cols=[("🔎", "Especie"), ("🔎", "Tipo productor"), ("🧺", "Comuna"), ("🔢", "Superficie (ha)"), ("🔢", "Numero de arboles")],
         ej=dict(pregunta="¿En qué comunas de la región hay más hectáreas de paltos?",
                 COL_FILTRO="Especie", VALOR="Palto", COL_GRUPO="Comuna",
                 COL_NUMERO="Superficie (ha)", RESUMEN="sum", N=5,
                 nota="La superficie está en hectáreas.",
                 check=lambda ns: len(ns["filtrada"]) == 1463)),
    dict(n="9a", icono="🏥", nombre="Estadísticas hospitalarias 2024 — mensual (si quieres ver mes a mes)", archivo="09a_hospitalarias_mensual.csv", peso="",
         cols=[("🔎", "Establecimiento"), ("🧺", "Mes"), ("🧺", "Nivel_Cuidado"), ("🔢", "Numero_de_Egresos"), ("🔢", "Egresos_Fallecidos")],
         ej=dict(pregunta="¿En qué meses tuvo más egresos el Hospital Félix Bulnes?",
                 COL_FILTRO="Establecimiento", VALOR="Hospital Félix Bulnes Cerda", COL_GRUPO="Mes",
                 COL_NUMERO="Numero_de_Egresos", RESUMEN="sum", N=5,
                 nota="Los meses salen ordenados por valor, no por calendario: para un ranking está bien.",
                 check=lambda ns: len(ns["filtrada"]) == 180)),
    dict(n="9b", icono="🏥", nombre="Estadísticas hospitalarias 2024 — anual (si quieres comparar hospitales)", archivo="09b_hospitalarias_anual.csv", peso="",
         cols=[("🔎", "Servicio_Salud"), ("🧺", "Establecimiento"), ("🧺", "Nivel_Cuidado"), ("🔢", "Numero_de_Egresos"), ("🔢", "Egresos_Fallecidos")],
         ej=dict(pregunta="¿Qué hospitales del Servicio de Salud Metropolitano Occidente tuvieron más egresos fallecidos?",
                 COL_FILTRO="Servicio_Salud", VALOR="Metropolitano Occidente", COL_GRUPO="Establecimiento",
                 COL_NUMERO="Egresos_Fallecidos", RESUMEN="sum", N=5,
                 nota="Usa el nombre exacto del Servicio de Salud: con `\"Occidente\"` solo, el filtro deja 0 filas.",
                 check=lambda ns: len(ns["filtrada"]) == 53)),
]

# Base elegida → equipos. Estado según la nómina del 2026-10-19 (Calendario v4).
EQUIPOS = [
    ("🚗 Siniestros de tránsito (CONASET)", "Santino García y Tomás Díaz · Benjamín Mejías · Felipe Román"),
    ("🎓 Puntajes de corte (DEMRE)", "Maura Muñoz y Simón Abrahams · Eduardo Pacco y Damián Flores · Diego Peña y Felipe Aravena · Vicente Benítez y Vicente Narváez · Martín Sánchez"),
    ("💼 Empleabilidad e ingresos (SIES)", "Francisca Parra y Julián Sandoval · Sebastián Ulloa"),
    ("🏥 Estadísticas hospitalarias", "Francisco Vega y Héctor Vergara · Alex Saravia y Diego Donoso"),
    ("📝 SIMCE 2° medio por establecimiento", "Cristóbal Muñoz y Luckas Letelier"),
    ("🏫 Matrícula por establecimiento", "Diego Vargas y Benjamín Díaz"),
]


def cargar_base(archivo: str) -> pd.DataFrame:
    return pd.read_csv(LOCAL_V3 / archivo, low_memory=False)


def ejecutar_ejemplo(b: dict) -> dict:
    """Corre la receta del ejemplo de una base contra la v3 local y devuelve el resultado real."""
    esp = {k: b["ej"][k] for k in ("COL_FILTRO", "VALOR", "COL_GRUPO", "COL_NUMERO", "RESUMEN", "N")}
    ns = {"pd": pd, "plt": plt, "tabla": cargar_base(b["archivo"])}
    salida = correr(receta_completa(esp), ns)
    assert b["ej"]["check"](ns), f"{b['archivo']}: el resultado ya no coincide con lo verificado"
    top = ns["top"]
    ranking = " · ".join(f"{i} {cl(v)}" for i, v in top.items())
    return dict(salida=salida, ranking=ranking, ns=ns, esp=esp)


# ───────────────────────── guaguas (ICN) ─────────────────────────
INICIO = f'''import pandas as pd
import matplotlib.pyplot as plt

URL = "{URL_GUAGUAS}"

tabla = pd.read_csv(URL, dtype={{"n": "str"}})
tabla["cantidad_guaguas"] = pd.to_numeric(
    tabla["n"].str.strip().str.replace(".", "", regex=False), errors="coerce"
)
tabla = tabla[tabla["cantidad_guaguas"].notna()]
print("Tabla lista. Filas:", len(tabla))
'''

ICN = [
    dict(
        titulo="Filtrar por un valor", pregunta="1. ¿Con qué parte de la tabla me quedo?",
        definicion=("Casi siempre una pregunta es sobre una parte de la tabla. Llenas dos espacios: **en qué columna miras** (`COL_FILTRO`) y **con qué valor te quedas** (`VALOR`). La tabla original no cambia: obtienes una nueva, solo con las filas que cumplen."),
        idea="`tabla[tabla[\"columna\"] == valor]` deja solo las filas donde la columna vale ese valor.",
        instruccion="Quédate solo con las filas donde `nombre` sea `\"Antonia\"`, guardadas en `filtrada`, e imprime cuántas filas quedaron.",
        partida="# La tabla ya está lista (celda de inicio).",
        solucion='filtrada = tabla[tabla["nombre"] == "Antonia"]\nprint("Filas de Antonia:", len(filtrada))',
    ),
    dict(
        titulo="Agrupar y resumir", pregunta="2. ¿Qué junto y qué cifra resumo?",
        definicion=("Para saber cuántas Antonias hay por año hay que juntar las filas del mismo año y sumarlas. Llenas dos espacios: **qué junto** (`COL_GRUPO`) y **qué cifra resumo** (`COL_NUMERO`). El resultado es un total por grupo."),
        idea="`tabla.groupby(\"grupo\")[\"número\"].sum()` junta las filas por grupo y entrega un total por grupo.",
        instruccion="Junta `filtrada` por `anio` y suma `cantidad_guaguas`, guardado en `resumen`, e imprime cuántos años hay.",
        partida='filtrada = tabla[tabla["nombre"] == "Antonia"]',
        solucion='filtrada = tabla[tabla["nombre"] == "Antonia"]\nresumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()\nprint("Años con datos:", len(resumen))',
    ),
    dict(
        titulo="Ordenar y quedarse con los primeros", pregunta="3. ¿En qué orden lo pongo y cuántos muestro?",
        definicion=("Cien años son demasiados para leerlos o graficarlos. Ordenamos de mayor a menor y mostramos solo los primeros: ese es el espacio `N`. El resultado es un «top»."),
        idea="`.sort_values(ascending=False).head(n)` ordena de mayor a menor y deja solo los primeros `n`.",
        instruccion="Ordena `resumen` de mayor a menor y quédate con los 10 primeros, guardados en `top`, e imprime cuántos quedaron.",
        partida='filtrada = tabla[tabla["nombre"] == "Antonia"]\nresumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()',
        solucion=('filtrada = tabla[tabla["nombre"] == "Antonia"]\nresumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()\n'
                  'top = resumen.sort_values(ascending=False).head(10)\nprint("Años en el top:", len(top))'),
    ),
    dict(
        titulo="Graficar en barras", pregunta="4. ¿Cómo lo muestro para compararlo?",
        definicion=("Un gráfico se entiende de un vistazo: `.plot(kind=\"bar\")` hace una barra por categoría. "
                    "`title`, `xlabel` e `ylabel` le ponen título y nombres a los ejes, y `plt.show()` lo muestra."),
        idea="`.plot(kind=\"bar\", title=..., xlabel=..., ylabel=...)` convierte el resultado en un gráfico de barras para comparar categorías.",
        instruccion="Grafica `top` en barras, con un título y nombres para ambos ejes, y muéstralo.",
        partida=('filtrada = tabla[tabla["nombre"] == "Antonia"]\nresumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()\n'
                 'top = resumen.sort_values(ascending=False).head(10)'),
        solucion=('filtrada = tabla[tabla["nombre"] == "Antonia"]\nresumen = filtrada.groupby("anio")["cantidad_guaguas"].sum()\n'
                  'top = resumen.sort_values(ascending=False).head(10)\n'
                  'top.plot(kind="bar", title="Años con más Antonias", xlabel="Año", ylabel="Cantidad de guaguas")\nplt.show()'),
    ),
]

ESPACIOS_GUAGUAS = dict(COL_FILTRO="nombre", VALOR="Antonia", COL_GRUPO="anio", COL_NUMERO="cantidad_guaguas", RESUMEN="sum", N=10)
ESPACIOS_CONASET = dict(COL_FILTRO="AÑO", VALOR=2025, COL_GRUPO="COMUNA", COL_NUMERO="FALLECIDOS", RESUMEN="sum", N=5)

HAZ_AHORA = """\
La periodista de las clases pasadas ya tiene la tabla de nombres limpia, y ahora quiere escribir sobre un nombre en particular: "Antonia". Quiere saber en qué años nacieron más Antonias, pero la tabla tiene cientos de miles de filas con todos los nombres de todos los años. La periodista, sabiendo de sus habilidades de programación, les pide ayuda para automatizar esto — pero antes, quiere que tengan clara la lógica:

1. De cientos de miles de filas con todos los nombres, ¿qué haces para trabajar solo con las de "Antonia"?
2. Si quieres el total de Antonias de cada año, ¿qué haces con las filas que comparten el mismo año?
3. Para ver cuáles son los años con más Antonias, ¿cómo acomodas los totales y con cuántos te quedas para que quepan en un gráfico?
4. Para comparar un año contra otro, ¿qué tipo de gráfico te sirve: de barras o de torta?"""

HAZ_AHORA_RESP = """\
1. Quedarme solo con las filas donde el nombre sea "Antonia" y descartar el resto.
2. Juntarlas por año y sumar sus cantidades, para tener un solo total por año.
3. Ordenarlos del mayor al menor y quedarme con los primeros (por ejemplo, 10).
4. De barras: cada año es una barra y se comparan por altura."""

TEXTO_BASES_LINK = "\n".join(
    f"# {b['n']} · {b['nombre']}" + (f"   {b['peso']}" if b["peso"] else "") + f'\n# "{RAW}{quote(b["archivo"])}"\n'
    for b in BASES
)


def tabla_columnas_sugeridas() -> str:
    filas = ["| Base | 🔎 Para filtrar · 🧺 Para agrupar · 🔢 Cantidad a resumir (5 columnas sugeridas) |", "|---|---|"]
    for b in BASES:
        cols = " · ".join(f"{r} `{c}`" for r, c in b["cols"])
        filas.append(f"| {b['icono']} **{b['n']}** · {b['nombre'].split(' (')[0].split(' —')[0]} | {cols} |")
    return "\n".join(filas)


NOTA_CODIGOS = """\
> 🔢 **Códigos que verás en varias bases** (números que representan categorías: **no se suman ni se promedian**, se usan para filtrar o agrupar). La lista completa está en el [Diccionario de Columnas](%s).
>
> | Código | Qué significa |
> |---|---|
> | Dependencia (`cod_depe2` en SIMCE) | 1 Municipal · 2 Particular subvencionado · 3 Particular pagado · 4 Servicio Local de Educación |
> | Dependencia (`COD_DEPE2` en Matrícula y Subvenciones) | 1 Municipal · 2 Particular subvencionado · 3 Particular pagado · 4 Corp. de Administración Delegada · 5 Servicio Local de Educación |
> | Grupo socioeconómico (`cod_grupo`, SIMCE) | 1 Bajo · 2 Medio bajo · 3 Medio · 4 Medio alto · 5 Alto |
> | Rural (SIMCE: `cod_rural_rbd`) | 1 Urbano · 2 Rural |
> | Rural (Matrícula y Subvenciones: `RURAL_RBD`) | **0** Urbano · **1** Rural (¡distinto que en SIMCE!) |
""" % LINK_DICCIONARIO


# ───────────────────────── Cuaderno de CÓDIGO ─────────────────────────
def cuaderno_codigo() -> Cuaderno:
    c = Cuaderno()
    c.md("""
# 🐍 Clase 38 y 38b — Responder con datos · cuaderno de Código

**Curso:** 3ro y 4to medio  |  **Duración:** 2 sesiones (mar 20 y jue 22-oct, ~77 min cada una)  |  **Plataforma:** Google Colab

---
""")
    c.md("""
## 👤 ¿Quién soy?

Escribe estos datos para que podamos unir tu trabajo con el de tu pareja.

- **Mi nombre:**
- **Mi pareja** *(si trabajo solo, lo dejo vacío)*:
- **Mi base:**
""")
    c.md("""
> 🧭 **Este proyecto se trabaja con dos cuadernos que van juntos:** 🧑‍💻 **Código** (este) y ✍️ **Texto**.
> En este escribimos código. Cuando aparezca el cuadro **✍️ Responde ahora en el cuaderno de Texto, sección N**, pasamos al otro.
> Si trabajamos en pareja, uno puede llevar este cuaderno y el otro el de Texto; si trabajamos solos, usamos los dos.
>
> 📌 **Lo que dejemos hoy es lo que seguimos usando hasta el lunes 26: no hay cuaderno nuevo el jueves.**

| Sesión | Qué hacemos |
|---|---|
| **Mar 20-oct** (Clase 38) | Aprendemos la receta con un ejemplo → la usamos en un ejemplo guiado → abrimos nuestra base y corremos nuestra primera pregunta (Pasos 1 y 2). |
| **Jue 22-oct** (Clase 38b) | Revisamos lo que salió (Paso 3), hacemos una pregunta distinta (Paso 4) y completamos el cuaderno de Texto. |
| **Lun 26-oct** | Terminamos. **Entrega del Colab final: 23:59.** |
""")
    foto_b64 = base64.b64encode(FOTO.read_bytes()).decode("ascii")
    portada = new_markdown_cell(
        "## 📰 De dónde partimos\n\n"
        "Con datos públicos como los de nuestra base se armó una noticia de circulación nacional: "
        "*cuánto ganan los ingenieros civiles industriales según su universidad de egreso*.\n\n"
        "![La nota del LUN — Cuánto ganan los ingenieros civiles industriales según su universidad de egreso](attachment:foto_lun.png)\n\n"
        "Un titular así es creíble por dos cosas: **la evidencia** (una cifra o un gráfico que responde una pregunta clara) y "
        "**la honestidad sobre sus límites** (qué no se puede afirmar con esos datos). En estas dos sesiones producimos las dos para nuestra propia pregunta."
    )
    portada["attachments"] = {"foto_lun.png": {"image/png": foto_b64}}
    c.celdas.append(portada)
    c.md("""
## 🎯 Objetivo

Construir una secuencia ordenada de pasos que responda una pregunta con una tabla de datos —quedarse con lo que interesa, resumirlo, ordenarlo y graficarlo—, con método.

## 🔎 ¿Para qué sirve?

> En estas dos sesiones armamos la evidencia de nuestro proyecto: un gráfico y una tabla que responden una pregunta con datos reales. Es la misma secuencia que hay detrás de cualquier ranking de una noticia, como los nombres más usados o las comunas con más matrícula.
""")
    c.md(f"""
---

## 📋 Cómo se evalúa (recordatorio)

El proyecto de cierre se traduce en **una sola nota** (vale doble en el promedio semestral), armada con 4 partes:

| Parte | Peso | Qué mide |
|---|---|---|
| 📓 Producto — Colab narrado | **35%** | Análisis correcto y razonamiento explicado en texto, de corrido |
| 🎤 Presentación | 20% | Claridad del hallazgo, evidencia y qué NO se puede concluir |
| 🔍 Defensa técnica — código intervenido | 30% | Explicar nuestro propio código y corregir errores metidos a propósito |
| 📒 Proceso — bitácora e hitos | **15%** | Avance real clase a clase, con evidencia |

📖 **La rúbrica completa, con equipos y bases, está en el cuaderno [Criterios de Evaluación del Proyecto]({LINK_RUBRICA}).**

> 🚫 **Sobre la IA:** el código y los textos de estos cuadernos se escriben sin IA. Es el código que vamos a tener que explicar en la Defensa técnica.
""")
    filas_equipos = "\n".join(f"| {b} | {e} |" for b, e in EQUIPOS)
    c.md(f"""
---

## 👥 Equipos y bases

| Base elegida | Equipos |
|---|---|
{filas_equipos}

¿Tu nombre no aparece? Elige del menú de abajo la base que más te interese y avísale al profe cuál elegiste.
""")
    c.md("---\n\n## 🔗 Links de las bases\n\nCopia el link de **tu** base —con sus comillas— para el Paso 1. Están en la celda de abajo, comentados, así que ejecutarla no hace nada. Las bases ya vienen limpias: los números ya son números.")
    c.code(TEXTO_BASES_LINK)
    c.md(f"""
📖 **Diccionario de Columnas** (qué significa cada columna): [abrir el PDF]({LINK_DICCIONARIO})
👀 **Muestra de las bases** (6 filas reales de cada una): [abrir el PDF]({LINK_MUESTRA})
""")
    c.md("---\n\n### 🔧 Preparación\n\nEjecuta esta celda antes de empezar: instala pandas en tu sesión de Colab, por si acaso.")
    c.code("!pip install pandas")

    # ── Haz Ahora ──
    c.md("---\n\n## 1️⃣ Haz Ahora (6 min)\n\n" + HAZ_AHORA)
    c.md("**Mis respuestas:**\n\n1. \n2. \n3. \n4. ")

    # ── ICN ──
    c.md("---\n\n## 2️⃣ Introducción al Contenido Nuevo (22 min)\n\nEstudia cada concepto y escribe tú el código que falta en cada celda, siguiendo la instrucción:")
    c.md("### ▶️ Celda de inicio\n\nEjecútala una sola vez: lee la tabla de nombres de guaguas y la deja lista en `tabla`. Todos los conceptos de hoy parten de ahí.")
    c.code(INICIO)
    for k in ICN:
        c.md(f"### 💡 {k['titulo']}\n\n#### ❓ {k['pregunta']}\n\n{k['definicion']}\n\n> **Idea clave:** {k['idea']}\n\n✍️ **Escríbelo tú:** {k['instruccion']}")
        c.code(k["partida"])

    # ── Concepto 5 ──
    c.md("""
### 💡 Qué columna va en cada espacio, y qué salió

#### ❓ 5. ¿Qué columna pongo en cada espacio y cómo leo el resultado?

Cada espacio pide un **tipo** de columna. Con la tabla de guaguas:

| Columna | Qué guarda | Es una… | Va en… |
|---|---|---|---|
| `nombre` | Un nombre (`"Antonia"`) | etiqueta | 🔎 `COL_FILTRO` o 🧺 `COL_GRUPO` |
| `anio` | Un año (`1920`, `1921`…) | etiqueta, **¡aunque sea número!** | 🧺 `COL_GRUPO` |
| `sexo` | `"F"`, `"M"`… | etiqueta | 🔎 `COL_FILTRO` |
| `cantidad_guaguas` | Cuántas guaguas hubo | cantidad | 🔢 `COL_NUMERO` |

> **Idea clave:** las **etiquetas** (nombres, categorías, años, códigos) sirven para filtrar y agrupar; solo las **cantidades** se suman o se promedian. Sumar años no significa nada.

Para decidir con tu base, esta **ficha** muestra de cada columna su tipo, cuántos valores distintos tiene, ejemplos y vacíos. Ejecútala (ya está escrita):
""")
    c.code('''columnas = ["nombre", "anio", "sexo", "cantidad_guaguas"]   # en tu base, aquí van tus 5 columnas

for columna in columnas:
    print("Columna:", columna)
    print("  tipo:", tabla[columna].dtype)
    print("  valores distintos:", tabla[columna].nunique())
    print("  ejemplos:", list(tabla[columna].dropna().unique()[:3]))
    print("  vacíos:", tabla[columna].isna().sum())
''')
    c.md("Ahora las cuatro preguntas juntas en una sola celda: **arriba los espacios, que es lo único que cambias**; abajo la receta, que no se toca. Ejecútala:")
    c.code(receta_completa(ESPACIOS_GUAGUAS))
    c.md("""
**Cómo se lee lo que salió:**

- **Filas que dejó el filtro y filas sin dato** → tus **límites** («perdimos ___ de ___ filas»).
- **Cifras del top y % del total** → tu **evidencia**: las cifras que citas.
- **Mayor, menor y promedio** → tu **hallazgo** y tu **conclusión**.
- **El gráfico** → la **diapositiva** de evidencia. `kind="barh"` son barras horizontales: se leen mejor con nombres largos.

> `.agg(RESUMEN)` hace lo mismo que `.sum()`, pero se elige con un texto: `"sum"` suma, `"mean"` promedia, `"count"` cuenta filas. Con `VALOR = None` no se filtra.
""")
    c.md("""
### 📌 Entonces, ¿qué debe quedar claro en tu cuaderno?

| Pregunta | Espacios que llenas | Tipo de columna | Línea |
|---|---|---|---|
| 1. ¿Con qué parte de la tabla me quedo? | `COL_FILTRO`, `VALOR` | 🔎 etiqueta | `tabla[tabla[COL_FILTRO] == VALOR]` |
| 2. ¿Qué junto y qué cifra resumo? | `COL_GRUPO`, `COL_NUMERO`, `RESUMEN` | 🧺 etiqueta · 🔢 cantidad | `.groupby(COL_GRUPO)[COL_NUMERO].agg(RESUMEN)` |
| 3. ¿En qué orden lo pongo y cuántos muestro? | `N` | — | `.sort_values(ascending=False).head(N)` |
| 4. ¿Cómo lo muestro para compararlo? | `TITULO` (opcional) | — | `.plot(kind="barh", ...)` |

### 🚀 Otras preguntas con la misma receta

| Si mi pregunta es… | Cambio… |
|---|---|
| El **promedio**, no el total | `RESUMEN = "mean"` |
| **Cuántas filas** hay por grupo | `RESUMEN = "count"` |
| Sobre **toda la tabla**, sin filtrar | `VALOR = None` |
| Una **comparación entre años o categorías** | `COL_GRUPO` = esa columna |

### 🧗 Para ir más allá (opcional)

> **¿Mi pregunta necesita dos condiciones a la vez?** Une cada condición con `&` ("y"), escribiendo cada una **entre paréntesis**. Para "una **o** la otra" se usa `|`. No uses la palabra `and`: con tablas da error.
""")
    c.code('''# Dos condiciones a la vez: el nombre Antonia Y años desde el 2000
filtrada = tabla[(tabla["nombre"] == "Antonia") & (tabla["anio"] >= 2000)]
print("Filas de Antonia desde el 2000:", len(filtrada))
''')
    c.md("""
#### ⚠️ Errores típicos a evitar

| Error | Qué ocurre | Cómo corregirlo |
|---|---|---|
| Usar `=` en vez de `==` al filtrar | `SyntaxError`: `=` guarda un valor, `==` compara | Usar `==` para comparar la columna con el valor |
| Escribir el valor con otra mayúscula o tilde (`"antonia"`) | El filtro deja 0 filas, sin ningún error (la receta avisa) | Copiar el valor tal cual está en la tabla |
| Poner un texto en `COL_NUMERO` | Error al sumar o promediar | Elegir una columna de **cantidad** (mira la ficha) |
| Escribir un número entre comillas (`"2025"`) | El filtro deja 0 filas | Los números van sin comillas |
""")

    # ── Guiada ──
    c.md(f"""
---

## 3️⃣ Práctica Guiada (8 min) — la receta sobre otra tabla

Un equipo del curso trabaja con los siniestros de tránsito de la Región Metropolitana y quiere saber qué comunas tuvieron más fallecidos en 2025, para armar una nota sobre dónde conviene reforzar la seguridad vial. La tabla trae un registro por siniestro, de varios años, y nos dicen que la columna del año se llama `AÑO`, la de la comuna `COMUNA` y la de fallecidos `FALLECIDOS`.

**El programa debe:**
- Quedarse con los siniestros del **año 2025**.
- Juntarlos por **comuna** y **sumar** los fallecidos de cada una.
- Mostrar las **5 comunas** con más fallecidos, con su cifra y su porcentaje del total.

📤 <em>El programa imprime:</em>
<pre>Filas que dejó el filtro: 19198
Con dato en FALLECIDOS : 19198 | sin dato (se pierden): 0
Cifras del top:   (las 5 comunas, cada una con su total)
% del total:      (lo que pesa cada una)
Mayor: Pudahuel → 21
Menor del top: Maipú → 13
Promedio de los 50 grupos: 6.1</pre>
Y debajo, un gráfico de 5 barras horizontales, con Pudahuel como la más larga.

▶️ **Ejecuta primero esta celda** (ya está escrita): abre la tabla de siniestros en `tabla`.
""")
    c.code(f'tabla = pd.read_csv("{RAW}07_conaset_rm.csv")\nprint("Filas:", tabla.shape[0], "| Columnas:", tabla.shape[1])')
    c.md("✍️ **Llena los espacios `_____`** con la pregunta de arriba traducida (las columnas sugeridas de la base están en la tabla de más abajo) y ejecuta:")
    c.code(receta_completa(None))

    # ── Galería ──
    c.md("---\n\n## 📚 Galería de ejemplos: una receta ya llena por cada base\n\nAsí se ve la receta llena con una pregunta real de cada base. **Son para entender cómo se traduce una pregunta, no para copiarlos**: si usamos el mismo ejemplo sin cambiarlo, no cuenta como una pregunta nuestra. Los resultados se verificaron ejecutando cada ejemplo.")
    ejemplos = {}
    for b in BASES:
        r = ejecutar_ejemplo(b)
        ejemplos[b["n"]] = r
        e, esp = b["ej"], r["esp"]
        lineas_esp = "\n".join(f"{k:<10} = {lit(esp[k])}" for k in ("COL_FILTRO", "VALOR", "COL_GRUPO", "COL_NUMERO", "RESUMEN", "N"))
        c.md(f"""
### {b['icono']} {b['n']} · {b['nombre']}

**Pregunta:** {e['pregunta']}

```python
{lineas_esp}
```

**Resultado:** {r['ranking']}

> 💡 {e['nota']}
""")

    # ── Mi base ──
    c.md("""
---

## 🔍 Mi base

Desde aquí trabajamos con **nuestra** base. En cada paso encontrarás primero **lo que necesitas saber** y luego **lo que debes hacer**.
""")
    c.md("### 🗂️ Mis 5 columnas sugeridas\n\nCada base trae 5 columnas que sirven bien para armar una pregunta. Busca la tuya:\n\n" + tabla_columnas_sugeridas()
         + "\n\n> 🌟 **Explorar más allá de las 5 sugeridas se premia** (la rúbrica lo premia): con `list(tabla.columns)` ves todas las columnas de tu base, y la ficha del Paso 1 sirve para cualquiera.")
    c.md(NOTA_CODIGOS)

    c.md("""
### Paso 1 · Abro mi base y miro mis columnas

**Lo que necesitas saber:** nuestra base ya viene limpia, así que lo primero es abrirla y entender qué hay en ella: qué representa una fila, cuántas filas y columnas tiene, y de qué tipo es cada una de nuestras 5 columnas.

**Lo que debes hacer:**
1. Pega el link de tu base (de la celda de links de arriba, **con las comillas**) y ejecuta.
2. Escribe en la lista `columnas` los nombres de tus 5 columnas, copiados tal cual, y ejecuta la ficha.
3. Mira las columnas con `list(tabla.columns)`: ¿hay alguna que te interese fuera de las 5?
""")
    c.code('''import pandas as pd
import matplotlib.pyplot as plt

LINK = "pega aquí el link de tu base"   # ← lo único que cambias (con comillas)

tabla = pd.read_csv(LINK)
print("Filas:", tabla.shape[0], "| Columnas:", tabla.shape[1])
tabla.head()
''')
    c.code('''columnas = ["", "", "", "", ""]   # ← tus 5 columnas, entre comillas y separadas por coma

for columna in columnas:
    print("Columna:", columna)
    print("  tipo:", tabla[columna].dtype)
    print("  valores distintos:", tabla[columna].nunique())
    print("  ejemplos:", list(tabla[columna].dropna().unique()[:3]))
    print("  vacíos:", tabla[columna].isna().sum())
''')
    c.code("list(tabla.columns)")
    c.md("> ✍️ **Responde ahora en el cuaderno de Texto, secciones 1 y 2** (contexto, pregunta e hipótesis · conoce tu base).")

    c.md("""
### Paso 2 · Traduzco mi pregunta y corro la receta

**Lo que necesitas saber:** nuestra pregunta se traduce llenando los espacios de la receta. Antes, tres decisiones:

- **¿Con qué parte me quedo?** Es una columna 🔎 y un valor. Un texto va con comillas y **escrito exacto**; un número, sin comillas. Si la pregunta es sobre toda la tabla, `VALOR = None`.
- **¿Qué junto y qué cifra resumo?** Una columna 🧺 para agrupar y una 🔢 para resumir. Elige `"sum"` si preguntas «¿cuánto hay en total?», `"mean"` para «¿cómo es lo típico?» y `"count"` para «¿cuántas filas hay?».
- **¿Cuántos muestro?** Entre 5 y 10 se lee bien en un gráfico.

**Lo que debes hacer:** llena los espacios `_____` con **tu** pregunta y ejecuta. Si el filtro deja 0 filas, la receta te lo avisa: revisa cómo escribiste `VALOR`.
""")
    c.code(receta_completa(None))
    c.md("> ✍️ **Responde ahora en el cuaderno de Texto, secciones 3 y 4** (cómo lo investigamos · hallazgo y evidencia).")

    c.md("""
### Paso 3 · Miro lo que salió

**Lo que necesitas saber:** un resultado que «salió» no es un resultado correcto. Antes de creerle, revisa:

- **¿Responde mi pregunta?** El gráfico muestra lo que preguntamos, no algo parecido.
- **¿Las cifras tienen sentido?** Compáralas con la escala de la columna.
- **¿Cuántas filas hay detrás de cada barra?** Un promedio calculado con 3 filas pesa lo mismo en el gráfico que uno calculado con 300.
- **¿Cuántas filas se perdieron?** Las que no tenían dato: nuestro análisis no dice nada de ellas.

**Lo que debes hacer:** ejecuta esta celda (ya está escrita) y anota lo que veas.
""")
    c.code('''# Paso 3 — Revisa tu resultado (solo ejecuta)
print("¿Cuántas filas hay detrás de cada barra?")
print(filtrada.groupby(COL_GRUPO)[COL_NUMERO].count().loc[top.index])
print()
print("Resumen de la columna que sumaste o promediaste:")
print(filtrada[COL_NUMERO].describe().round(2))
''')
    c.md("> ✍️ **Responde ahora en el cuaderno de Texto, sección 5** (límites).")

    c.md("""
### Paso 4 · Una pregunta distinta

**Lo que necesitas saber:** una segunda pregunta cambia **al menos un espacio**: otro valor, otra columna para agrupar, otro resumen, o una columna que **no esté entre las 5 sugeridas**. Es lo que más se premia en la rúbrica.

**Lo que debes hacer:** llena los espacios de nuevo con la pregunta distinta y ejecuta. Anota qué cambiaste respecto de la primera.
""")
    c.code(receta_completa(None))
    c.md("> ✍️ **Responde ahora en el cuaderno de Texto, secciones 6, 7 y 8** (pregunta distinta · conclusión · nota de prensa).")

    c.md("""
---

## 📤 Entrega

El **Colab final se entrega el lunes 26-oct hasta las 23:59** en Classroom. Antes de entregar:

1. Ejecuta todo de arriba hacia abajo: menú **Entorno de ejecución → Ejecutar todo**. Revisa que no quede ningún error en rojo (las celdas de la Galería no se ejecutan: son texto).
2. Escribe tu nombre y el de tu pareja al inicio (**¿Quién soy?**).
3. Si trabajamos en pareja, **cada uno entrega su cuaderno** (el de Código y el de Texto); después los unimos.
4. Completa la **Bitácora** del cuaderno de Texto.
""")
    return c, ejemplos


# ───────────────────────── Cuaderno de TEXTO ─────────────────────────
def cuaderno_texto() -> Cuaderno:
    t = Cuaderno()
    t.md("""
# ⚠️ Antes de partir

> 📒 **Al final de este cuaderno hay una Bitácora.** La respondemos **cada día que trabajemos** en el proyecto: **mar 20-oct, jue 22-oct y lun 26-oct**. Cuenta para la nota de Proceso.
""")
    t.md("""
# ✍️ Clase 38 y 38b — Responder con datos · cuaderno de Texto

**Curso:** 3ro y 4to medio  |  **Plataforma:** Google Colab

Este cuaderno es la **parte escrita de nuestro proyecto**. Cada sección es una diapositiva de la presentación, así que lo que escribimos aquí es lo que después presentamos. Se completa a medida que avanzamos en el cuaderno de 🧑‍💻 **Código**: cada vez que allá aparezca **✍️ Responde ahora en el cuaderno de Texto, sección N**, volvemos acá.

Cada sección trae **frases para completar**. Haz doble clic en la celda de respuesta y reemplaza los `___` con tus palabras.
""")
    t.md("""
## 👤 ¿Quién soy?

- **Mi nombre:**
- **Mi pareja** *(si trabajo solo, lo dejo vacío)*:
- **Mi base:**
""")
    t.md("""
## 🔁 Mis espacios y mi tabla (copiados del cuaderno de Código)

Para escribir las secciones 3, 4 y 5 necesitamos las cifras. **Pega aquí** los seis espacios de tu receta y las cifras del top, tal como salieron en el cuaderno de Código. Así puedes escribir aunque tu pareja tenga el otro cuaderno abierto.
""")
    t.md("""
**Mis espacios:**

```
COL_FILTRO =
VALOR      =
COL_GRUPO  =
COL_NUMERO =
RESUMEN    =
N          =
```

**Mis cifras** (el top, el % del total, y filas usadas y perdidas):

```
(pega aquí lo que imprimió la receta)
```
""")

    t.md("""
---

## 1️⃣ Contexto, pregunta e hipótesis · 📽️ diapositiva 1

**Lo que necesitas saber:** una buena pregunta es **concreta**, se puede **responder con tu tabla** y no se contesta con un sí o un no. La hipótesis es lo que **esperas encontrar antes de mirar el resultado**.

**Completa:**
""")
    t.md("""
**Mi respuesta:**

- Nuestra base trata de ___ y la elegimos porque ___.
- Nuestra pregunta es: ¿___?
- Creemos que vamos a encontrar que ___ porque ___. *(Esa es nuestra hipótesis.)*
- Esta pregunta importa porque ___.
""")

    t.md("""
---

## 2️⃣ Conoce tu base · 📽️ diapositiva 2

**Lo que necesitas saber:** aquí describes tu base como si se la explicaras a alguien que no la conoce. Las fuentes y los significados de cada columna están en el [Diccionario de Columnas](%s). Explorar más allá de las columnas sugeridas (sección 6) es lo que más se premia en la rúbrica.

**Completa:**
""" % LINK_DICCIONARIO)
    t.md("""
**Mi respuesta:**

- Cada fila de nuestra base es ___ (un colegio, una carrera, un siniestro…).
- Tiene ___ filas y ___ columnas. Los datos vienen de ___.
- Usamos estas columnas: ___ *(para cada una: qué es y si la usamos para 🔎 filtrar, 🧺 agrupar o 🔢 resumir)*.
- 🌟 *Columna fuera de las 5 sugeridas:* usamos ___ porque ___. *(Si no usamos ninguna, lo dejamos escrito: «no usamos ninguna».)*
""")

    t.md("""
---

## 3️⃣ Cómo lo investigamos · 📽️ diapositiva 3

**Lo que necesitas saber:** cuentas tus pasos **en palabras, sin pegar código**, y cada uno con su **porqué**. Mira tus espacios de arriba: cada uno es una respuesta.

**Completa:**
""")
    t.md("""
**Mi respuesta:**

- **Paso 1.** Nos quedamos con las filas donde ___ es ___, porque ___.
- **Paso 2.** Juntamos por ___ y calculamos el/la *(total · promedio · cantidad)* de ___, porque ___.
- **Paso 3.** Ordenamos de mayor a menor y mostramos los primeros ___, porque ___.
- **Paso 4.** Lo graficamos en barras porque ___.
""")

    t.md("""
---

## 4️⃣ Hallazgo y evidencia · 📽️ diapositiva 4

**Lo que necesitas saber:** el hallazgo es **la frase que responde tu pregunta**, sin términos técnicos que tu audiencia no entienda, y se apoya en **cifras de tu tabla**. El gráfico está en el cuaderno de Código (Paso 2); en la presentación lo pegamos como imagen.

**Completa:**
""")
    t.md("""
**Mi respuesta:**

- **Nuestro hallazgo, en una frase:** ___.
- El valor más alto es ___ con ___; el más bajo de los que mostramos es ___ con ___.
- Lo vemos en el gráfico porque ___.
""")

    t.md("""
---

## 5️⃣ Límites · 📽️ diapositiva 5

**Lo que necesitas saber:** todo resultado tiene límites, y decirlos es lo que lo hace creíble. Un límite real es **concreto de tus datos**, no una frase de relleno como «faltan más datos». Los más comunes:

| Tipo de límite | Ejemplo |
|---|---|
| Filas descartadas | «Perdimos 5 filas sin ingreso»: nuestro análisis no dice nada de ellas |
| Pocas filas detrás | Una barra se apoya en 3 filas y otra en 300 *(Paso 3 del cuaderno de Código)* |
| Promedio de promedios | Cada colegio pesa igual en el promedio aunque tenga 20 o 300 estudiantes |
| La columna no mide lo que creíamos | «Empleabilidad» mide haber trabajado, no cuánto se gana |
| Alcance | Es una región o un año, no todo Chile ni todos los años |
| Asociación no es causa | Dos cosas que suben juntas no prueban que una cause la otra |

**Completa:**
""")
    t.md("""
**Mi respuesta:**

- Se perdieron ___ de ___ filas porque ___.
- Con estos datos **NO** podemos concluir que ___ porque ___ *(una cifra o un dato de nuestra tabla)*.
- Una barra se apoya en ___ filas y otra en ___ filas.
- Si alguien olvidara este límite, sacaría la conclusión equivocada de que ___.
""")

    t.md("""
---

## 6️⃣ Una pregunta distinta · 🌟

**Lo que necesitas saber:** una segunda pregunta, o una pregunta que use una columna **fuera de las 5 sugeridas**. Es lo que más se premia en la rúbrica.

**Completa:**
""")
    t.md("""
**Mi respuesta:**

- Nuestra pregunta distinta es: ¿___?
- Lo que cambiamos en los espacios respecto de la primera fue ___.
- Lo que encontramos: ___ *(con una cifra)*.
- Se diferencia de la primera en que ___.
""")

    t.md("""
---

## 7️⃣ Conclusión y próximo paso · 📽️ diapositiva 6

**Lo que necesitas saber:** una conclusión no repite el gráfico: **responde la pregunta**, se apoya en la evidencia, reconoce su límite y **descarta al menos una explicación alternativa**.

**Completa:**
""")
    t.md("""
**Mi respuesta:**

- Respondiendo nuestra pregunta: ___ *(con una cifra)*.
- Volviendo a nuestra hipótesis: se cumplió / no se cumplió porque ___.
- Una explicación alternativa que descartamos (o que no pudimos descartar): ___ porque ___.
- Nuestro próximo paso sería ___.
""")

    t.md("""
---

## 8️⃣ Nota de prensa

**Lo que necesitas saber:** traduces el hallazgo a lenguaje de noticia, para quien no sabe nada de datos. Tiene un **titular** y un **cuerpo de 3 o 4 líneas**. La política de IA aplica solo aquí: el **borrador es nuestro**, y si después lo corregimos con IA, anotamos **qué le pedimos y qué nos respondió**.

**Completa:**
""")
    t.md("""
**Borrador propio (sin corregir):**

- **Titular** *(máx. 12 palabras)*: ___
- **Cuerpo** *(3 o 4 líneas)*: ___

**Versión corregida** *(si usamos IA)*:

- Qué le pedimos: ___
- Qué respondió: ___
- Versión final: ___
""")

    t.md("""
---

## 📒 Bitácora

> Se completa **al cerrar cada sesión**. Es lo que la rúbrica de Proceso revisa: avance real, clase a clase.

**Sesión mar 20-oct — Clase 38**
- Qué avanzamos hoy:
- Qué nos costó o qué dudas tuvimos:
- Qué pensamos hacer el jueves 22:

**Sesión jue 22-oct — Clase 38b**
- Qué avanzamos hoy:
- Qué nos costó o qué dudas tuvimos:
- Qué nos falta para terminar el Colab final:

**Sesión lun 26-oct — cierre**
- Qué dejamos terminado:
- Qué cambiamos desde la última vez, y por qué:
- Qué haríamos distinto si tuviéramos una clase más:
""")
    t.md("""
---

## 📤 Entrega

El **Colab final se entrega el lunes 26-oct hasta las 23:59** en Classroom. Antes de entregar:

1. Revisa que todas las secciones tengan su respuesta y que no queden `___` sin completar.
2. Escribe tu nombre y el de tu pareja al inicio (**¿Quién soy?**).
3. Si trabajamos en pareja, **cada uno entrega su cuaderno**; después los unimos.
4. Completa la **Bitácora** de cada sesión.
""")
    return t


# ───────────────────────── SOLUCIONARIO ─────────────────────────
def solucionario(ejemplos: dict) -> Cuaderno:
    s = Cuaderno()
    s.md("""
# 🔐 Solucionario — Clase 38 y 38b · Responder con datos

**Solo para el profesor.** No se sube a Classroom hasta después de la entrega del 26-oct. Todos los resultados de este cuaderno salen de ejecutar el código contra las bases v3.

Contiene: respuestas del Haz Ahora, código del ICN, la Guiada resuelta, los 12 ejemplos de la galería con su salida real, y un **modelo de las secciones del cuaderno de Texto** para corregir.
""")
    s.md("---\n\n## 1️⃣ Haz Ahora — respuestas esperadas\n\n" + HAZ_AHORA_RESP)

    s.md("---\n\n## 2️⃣ ICN — código completo\n\n**Celda de inicio:**")
    ns = {}
    out = correr(INICIO.replace(URL_GUAGUAS, LOCAL_GUAGUAS.as_posix()), ns)
    s.code(INICIO)
    s.md(f"Salida: `{out.strip()}`")
    for k in ICN:
        salida = correr(k["solucion"], ns)
        s.md(f"### {k['pregunta']}\n\n✍️ {k['instruccion']}")
        s.code(k["solucion"])
        if salida.strip():
            s.md("Salida:\n```\n" + salida.strip() + "\n```")
    s.md("### 5. La receta completa con guaguas")
    s.code(receta_completa(ESPACIOS_GUAGUAS))
    salida = correr(receta_completa(ESPACIOS_GUAGUAS), ns)
    s.md("Salida:\n```\n" + salida.strip() + "\n```")

    s.md("---\n\n## 3️⃣ Práctica Guiada — CONASET, comunas con más fallecidos en 2025")
    conaset = next(b for b in BASES if b["n"] == "7")
    r = ejemplos["7"]
    s.code(receta_completa(ESPACIOS_CONASET))
    s.md("Salida:\n```\n" + r["salida"].strip() + "\n```")
    s.md("Gráfico: 5 barras horizontales, Pudahuel la más larga (21 fallecidos).")

    s.md("---\n\n## 📚 Galería — los 12 ejemplos con su salida real")
    filas = ["| Base | Pregunta | Espacios | Resultado |", "|---|---|---|---|"]
    for b in BASES:
        e, r = b["ej"], ejemplos[b["n"]]
        esp = f"`{e['COL_FILTRO']}` = `{e['VALOR']}` → `{e['COL_GRUPO']}` · `{e['COL_NUMERO']}` · `{e['RESUMEN']}`"
        filas.append(f"| {b['icono']} {b['n']} | {e['pregunta']} | {esp} | {r['ranking']} |")
    s.md("\n".join(filas))
    for b in BASES:
        s.md(f"### {b['icono']} {b['n']} · {b['nombre']}\n\nSalida completa:\n```\n{ejemplos[b['n']]['salida'].strip()}\n```")

    s.md("""
---

## ✍️ Modelo del cuaderno de Texto (CONASET, para corregir)

Un ejemplo de cómo se ve una buena respuesta en cada sección, sobre la pregunta de la Guiada. **No es la única forma correcta**: se califica lo que dicen y que se apoye en las cifras de su tabla.

**1 · Contexto, pregunta e hipótesis.** Nuestra base trata de los siniestros de tránsito en la Región Metropolitana y la elegimos porque queremos saber dónde ocurren más accidentes graves. Nuestra pregunta es: ¿qué comunas tuvieron más fallecidos en siniestros de tránsito el 2025? Creemos que serán las comunas con más población, como Santiago o Maipú. Importa porque ayudaría a decidir dónde reforzar la seguridad vial.

**2 · Conoce tu base.** Cada fila es un siniestro de tránsito. Tiene 123.343 filas y 37 columnas; los datos vienen de CONASET. Usamos `AÑO` (🔎 filtrar), `COMUNA` (🧺 agrupar) y `FALLECIDOS` (🔢 resumir). 🌟 Usamos además `Bicicleta`, que no está entre las sugeridas, para la segunda pregunta.

**3 · Cómo lo investigamos.** Paso 1: nos quedamos con las filas donde `AÑO` es 2025, porque la pregunta es sobre ese año. Paso 2: juntamos por `COMUNA` y sumamos `FALLECIDOS`, porque queremos el total de cada comuna. Paso 3: ordenamos de mayor a menor y mostramos las 5 primeras, para que quepan en el gráfico. Paso 4: lo graficamos en barras para comparar.

**4 · Hallazgo y evidencia.** Las comunas con más fallecidos el 2025 no son las más pobladas: Pudahuel tuvo 21, Santiago 19 y Quilicura 17. El valor más bajo del top es Maipú, con 13. Lo vemos en el gráfico porque Pudahuel es la barra más larga.

**5 · Límites.** No se perdió ninguna fila (todas tenían dato en `FALLECIDOS`). Con estos datos **no** podemos concluir que Pudahuel sea la comuna más peligrosa: no sabemos cuánta gente circula ahí; 21 fallecidos en una comuna con mucho tránsito pesado no significa lo mismo que en una pequeña. Si alguien olvidara esto, concluiría que vivir en Pudahuel es más riesgoso que en Maipú.

**6 · Una pregunta distinta.** ¿En qué comunas hubo más siniestros con bicicletas el 2025? Cambiamos `COL_NUMERO` a `Bicicleta` (una columna fuera de las sugeridas, de 0 y 1) y `RESUMEN` a `"sum"`.

**7 · Conclusión.** Respondiendo nuestra pregunta: Pudahuel tuvo más fallecidos el 2025 (21). Nuestra hipótesis no se cumplió: las comunas más pobladas no encabezan el ranking. No pudimos descartar que influya el tránsito pesado de las rutas que cruzan la comuna. Nuestro próximo paso sería comparar con la cantidad de habitantes.

**8 · Nota de prensa.** *Titular:* «Pudahuel lidera las muertes en siniestros de tránsito de la Región Metropolitana en 2025». *Cuerpo:* Con 21 fallecidos, Pudahuel superó a Santiago (19) y a Quilicura (17), según los registros de CONASET. Sin embargo, los datos no dicen cuánta gente circula por cada comuna…
""")
    return s


def revisar_pesos(nb, nombre: str):
    """Ningún $ suelto fuera de bloques y de `código` en las celdas markdown."""
    malos = []
    for i, celda in enumerate(nb.cells):
        if celda.cell_type != "markdown":
            continue
        en_bloque = False
        for linea in celda.source.split("\n"):
            if linea.lstrip().startswith("```"):
                en_bloque = not en_bloque
                continue
            if en_bloque:
                continue
            fuera = "".join(t for j, t in enumerate(re.split(r"(`[^`]*`)", linea)) if not t.startswith("`"))
            if re.search(r"(?<!\\)\$", fuera):
                malos.append((i, linea[:80]))
    assert not malos, f"{nombre}: $ sin escapar: {malos[:3]}"


def main():
    codigo, ejemplos = cuaderno_codigo()
    texto = cuaderno_texto()
    sol = solucionario(ejemplos)
    nbs = {}
    for nombre, cuad, ruta in (("Código", codigo, SAL_CODIGO), ("Texto", texto, SAL_TEXTO), ("Solucionario", sol, SAL_SOL)):
        nb = cuad.guardar(ruta)
        revisar_pesos(nb, nombre)
        nbs[nombre] = nb
        print(f"{ruta.name}: {len(nb.cells)} celdas")
    # Comprobaciones de contenido
    cod = "\n".join(c.source for c in nbs["Código"].cells)
    tex = "\n".join(c.source for c in nbs["Texto"].cells)
    for prohibido in ("Diego trae", "Diego les", "le pide Diego", "**Curso:** 4to medio"):
        assert prohibido not in cod and prohibido not in tex, f"texto prohibido: {prohibido}"
    assert "3ro y 4to medio" in cod and "3ro y 4to medio" in tex
    assert "Bitácora" in tex.split("# ✍️")[0], "el aviso de la Bitácora debe abrir el cuaderno de Texto"
    print("OK")


if __name__ == "__main__":
    sys.exit(main())
