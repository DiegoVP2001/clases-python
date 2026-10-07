"""
Prepara las bases del menú del Proyecto Cierre Octubre para las clases N°37-N°38b (Calendario v3).

Lee las copias de `clases/clases-octubre/datos-compartidos/` (versión 1, que usó la Clase 36b y NO se toca)
y escribe la versión 2 en `clases/clases-octubre/datos-compartidos-v2/`.

Criterio (ver Catastro §6): lo que las clases no enseñan lo resuelve este script en silencio;
lo que sí enseñan (limpiar a número, descartar vacíos) se deja vivo en UN problema por base, sin alterar
ningún valor — solo el formato de escritura, de modo que la receta de la clase lo revierte exactamente.

  En silencio : apertura sin parámetros (UTF-8, coma, encabezado en la 1ª fila), filas basura/agregadas,
                espacios en los bordes del texto, celdas de solo espacios (→ vacías), pivote de Hospitalarias,
                diccionario de rangos de ingreso (SIES), columnas derivadas que las clases no enseñan.
  Queda vivo  : número escrito como texto — con coma decimal ("85,3"), con punto de miles ("1.234") o con
                "s/i" — más los vacíos naturales de cada base.

Uso: python tools/datos_octubre/preparar_bases.py
Termina con código 1 si alguna verificación falla.
"""
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
V1 = RAIZ / "clases" / "clases-octubre" / "datos-compartidos"
V2 = RAIZ / "clases" / "clases-octubre" / "datos-compartidos-v2"

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ABREV = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
DIAS_2024 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
RM = "Región Metropolitana de Santiago"


# ───────────────────────── utilidades ─────────────────────────
def limpiar_texto(t: pd.DataFrame) -> pd.DataFrame:
    """Quita espacios en los bordes y deja vacías las celdas de solo espacios y las que dicen "NULL"
    (pandas ya lee "NULL" como vacío, pero no cuando trae espacios alrededor). Los espacios duros (\\xa0) y los
    espacios repetidos dentro del texto pasan a un solo espacio normal: con ellos, filtrar por nombre exacto falla
    aunque se vea igual (ej. "Pavo Pechuga\\xa0s/hueso" en ODEPA). Solo columnas de texto."""
    t = t.copy()
    for c in t.columns:
        if not pd.api.types.is_numeric_dtype(t[c]):
            t[c] = t[c].str.replace(r"\s+", " ", regex=True).str.strip().replace({"": np.nan, "NULL": np.nan})
    return t


def enteros_donde_corresponda(t: pd.DataFrame, excepto=()) -> pd.DataFrame:
    """Columnas float cuyos valores son todos enteros (ej. 3.0) pasan a Int64, para no escribir '3.0'."""
    t = t.copy()
    for c in t.columns:
        if c in excepto or not pd.api.types.is_float_dtype(t[c]):
            continue
        v = t[c].dropna()
        if len(v) and (v == v.round()).all():
            t[c] = t[c].astype("Int64")
    return t


def a_miles(serie: pd.Series) -> pd.Series:
    """1234567 -> '1.234.567' (como se escribe en Chile). Vacíos quedan vacíos."""
    def f(v):
        if pd.isna(v):
            return np.nan
        n = int(v)
        return f"{n:,}".replace(",", ".")
    return serie.map(f)


def a_coma(serie: pd.Series) -> pd.Series:
    """85.3 -> '85,3'; 792776.0 -> '792776'. Vacíos quedan vacíos."""
    def f(v):
        if pd.isna(v):
            return np.nan
        if float(v) == int(v):
            return str(int(v))
        return repr(float(v)).replace(".", ",")
    return serie.map(f)


def sin_tildes(texto: str) -> str:
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().replace(" ", "_")


# ───────────────────────── una función por base ─────────────────────────
# Cada una devuelve: (tabla_limpia_numerica, {columna: "miles"|"coma"}, notas)

def sies():
    t = pd.read_csv(V1 / "01_sies_empleabilidad/Buscador_Empleabilidad_ingresos_2025_2026_SIES.csv")
    t = t[t["Código"].notna()].copy()                                     # 3 filas basura (2 vacías + pie "FUENTE: ...")
    t = t.rename(columns=lambda c: c.replace("\xa0", " "))                # "Retención 1er año" traía un espacio duro (no se podía tipear)
    t = limpiar_texto(t)
    t["Código"] = t["Código"].astype("Int64")

    def monto(parte: str) -> float:
        mill = re.search(r"(\d+)\s+mill", parte)
        mil = re.search(r"(\d+)\s+mil\b", parte)
        return (int(mill.group(1)) * 1_000_000 if mill else 0) + (int(mil.group(1)) * 1_000 if mil else 0)

    def punto_medio(texto):
        if pd.isna(texto) or texto == "s/i":
            return np.nan
        partes = [monto(p) for p in re.split(r"\s+a\s+", texto)]
        return float(np.mean(partes))                                    # "Sobre $3 millones 500 mil" -> usa ese piso (un solo extremo)

    t["Ingreso_punto_medio"] = t["Ingreso Promedio al 4° año"].map(punto_medio)
    notas = ["Vivo: 's/i' en Retención 1er año, Duración Real e Ingreso (texto) → to_numeric(errors=\"coerce\") los deja vacíos.",
             "Nueva columna Ingreso_punto_medio (numérica): punto medio de cada rango; 'Sobre $3 millones 500 mil' usa 3.500.000; 's/i' queda vacío."]
    return t, {}, notas


def demre():
    t = pd.read_csv(V1 / "02_demre_admision/ADM2026_INDICADORES_POR_CARRERA_PROMEDIO_OBLIGATORIAS_20260116.csv", sep=";")
    t = limpiar_texto(t)                                                 # 40 NOMBRE_UNIVERSIDAD con espacios en los bordes
    t["MARGEN_P25_MENOS_ULTIMO"] = (t["PROM_OBLIGATORIAS_P25"] - t["PROM_OBLIGATORIAS_ULTIMO_SELEC"]).round(2)
    sucias = {c: "coma" for c in t.columns if c.startswith("PROM_OBLIGATORIAS_")}
    notas = ["Vivo: bloque PROM_OBLIGATORIAS_* escrito con coma decimal ('807,13'); 3-6 vacíos naturales.",
             "Nueva columna MARGEN_P25_MENOS_ULTIMO (numérica): P25 − último seleccionado."]
    return t, sucias, notas


def simce_rbd():
    t = pd.read_csv(V1 / "03_simce_2m/simce2m2025_rbd_final.csv", sep=";", encoding="latin-1")
    t = limpiar_texto(t)
    sucias = {c: "coma" for c in t.columns if c.startswith(("prom_", "dif_", "difgru_", "palu_eda"))}
    return t, sucias, ["Vivo: promedios, diferencias y % de logro con coma decimal; vacíos naturales en varias columnas."]


def simce_comuna():
    t = pd.read_csv(V1 / "03_simce_2m/simce2m2025_comuna_final.csv", sep=";", encoding="latin-1")
    t = limpiar_texto(t)
    sucias = {c: "coma" for c in t.columns if c.startswith(("prom_", "dif_", "palu_eda"))}
    return t, sucias, ["Vivo: promedios, diferencias y % de logro con coma decimal; 11-16 vacíos naturales por columna."]


def matricula():
    t = pd.read_csv(V1 / "05_mineduc_matricula/20251029_Resumen_Matricula_EE_Oficial_2025_20250430.csv")
    t = limpiar_texto(t)                                                 # textos con espacios al final y "NULL" como nombre de colegio
    # Sin número-como-texto a propósito: con punto de miles en celdas sueltas ("1.110") pandas lee el decimal 1.11
    # SIN avisar, en una base real que se presenta ante dirección. Verificado: 10.253 filas mal en MAT_TOTAL.
    return t, {}, ["Vivo: solo vacíos naturales (SLEP vacío en 10.281 filas; algunos nombres de colegio 'NULL' ahora vacíos de verdad).",
                   "Sin números escritos como texto (como CONASET): un equipo la revisa y reporta 'nada que arreglar'."]


def subvenciones():
    t = pd.read_csv(V1 / "06_subvenciones/20260421_Detalle Subvenciones 2025_20240520.csv")
    t = t.drop(columns=["RUT_SOSTENEDOR"])                               # dato de identificación: no se publica (Catastro §6)
    t = limpiar_texto(t)
    montos = ["MONTO_ASIG_ZONA", "DESCUENTO_FICOM", "APORTE_ESTADO_FICOM", "DISCREPANCIA", "DONACIONAPLICADA", "REINTEGROS",
              "RETENCIONES", "MULTAS", "DESEMPEÑO_DIFICIL", "DESEMPEÑO_DIFICIL_NODOC", "SUBV_ADICIONAL_ESPECIAL",
              "SUBV_ASISTENTES_EDUCACION", "PROFESOR_ENCARGADO", "RELIQUIDACION", "APOR_GRATUIDAD", "SUB_NORMAL", "SEP_PRIO",
              "SEP_PREF", "MANTENIMIENTO", "SNED", "PRORETENCION", "REFORZAMIENTO", "RURALIDAD", "PISO_RURAL"]
    sucias = {c: "miles" for c in montos}
    return t, sucias, ["Vivo: columnas de monto con punto de miles ('1.234.567'). Se eliminó RUT_SOSTENEDOR."]


def conaset():
    t = pd.read_csv(V1 / "07_conaset/CONASET_siniestros-transito-RM_2020-2025.csv", low_memory=False)
    t = limpiar_texto(t)                                                 # Ruta/Calle_Uno/Calle_Dos traían ' ' en vez de vacío
    t.insert(t.columns.get_loc("Mes") + 1, "Mes_num", t["Mes"].map({m: i + 1 for i, m in enumerate(MESES)}).astype("Int64"))
    t = enteros_donde_corresponda(t)
    notas = ["Vivo: vacíos naturales — Ruta 96 %, Calle_Dos 29 %, Calle_Uno 5 %, AM 1 % (antes escondidos como ' ', que pandas no cuenta como vacío).",
             "Sin números escritos como texto: es la única base sin problema de tipo (un equipo la revisa y reporta 'nada que arreglar').",
             "Nueva columna Mes_num (1-12) para ordenar los meses en orden de calendario."]
    return t, {}, notas


def odepa(archivo, destino_nombre):
    t = pd.read_csv(V1 / "08_odepa" / archivo, encoding="utf-8-sig", dtype=str, low_memory=False)
    t = t[t["Region"] == RM].copy()                                      # recorte a la RM (Catastro §6)
    t = limpiar_texto(t)
    for c in t.columns:                                                  # se leyó todo como texto para no tocar las comas:
        v = t[c].dropna()                                                # lo que es entero de verdad vuelve a ser entero
        if len(v) and v.str.fullmatch(r"-?\d+").all():
            t[c] = t[c].astype("Int64")
    return t


def odepa_consumidor():
    return odepa("ODEPA_precios-consumidor_2025.csv", "08a"), {}, ["Vivo (natural): Precio minimo/maximo/promedio con coma decimal en texto. Recortada a la RM."]


def odepa_mayorista():
    return odepa("ODEPA_precios-mayoristas-fruta-hortaliza_2025.csv", "08b"), {}, ["Vivo (natural): volumen y precios con coma decimal en texto. Recortada a la RM."]


def odepa_catastro():
    return odepa("ODEPA-CIREN_catastro-fruticola_2025.csv", "08c"), {}, ["Vivo (natural): Superficie (ha) con coma decimal en texto. Recortada a la RM."]


def hospitalarias():
    crudo = pd.read_csv(V1 / "09_salud/Estadísticas Hospitalarias Año 2024.csv", header=2)
    crudo = limpiar_texto(crudo)
    agregada = (crudo["Nombre SS/SEREMI"].str.startswith("Datos") | crudo["Nombre Establecimiento"].str.startswith("Datos")
                | crudo["Nombre Nivel Cuidado"].str.startswith("Datos"))
    crudo = crudo[~agregada].copy()                                      # Datos País / Datos Servicio Salud / Datos Establecimiento
    codigo_nombre = crudo["Nombre Nivel Cuidado"].str.extract(r"^(\d+)\s*-\s*(.+)$")
    crudo["Cod_Nivel"] = codigo_nombre[0].astype(int)
    crudo["Nivel_Cuidado"] = codigo_nombre[1].str.strip()
    crudo["Glosa"] = crudo["Glosa"].map(sin_tildes)
    llaves = ["Cód. SS/SEREMI", "Nombre SS/SEREMI", "Cód. Estab.", "Nombre Establecimiento", "Cod_Nivel", "Nivel_Cuidado"]
    nombres = {"Cód. SS/SEREMI": "Cod_SS", "Nombre SS/SEREMI": "Servicio_Salud", "Cód. Estab.": "Cod_Estab",
               "Nombre Establecimiento": "Establecimiento", "Cod_Nivel": "Cod_Nivel", "Nivel_Cuidado": "Nivel_Cuidado"}

    # Anual: una fila por (establecimiento, nivel de cuidado), una columna por glosa
    anual = crudo.pivot(index=llaves, columns="Glosa", values="Acum").reset_index().rename(columns=nombres)
    anual.columns.name = None

    # Mensual: una fila por (establecimiento, nivel de cuidado, mes)
    largo = crudo.melt(id_vars=llaves + ["Glosa"], value_vars=ABREV, var_name="Mes_abrev", value_name="valor")
    mensual = largo.pivot(index=llaves + ["Mes_abrev"], columns="Glosa", values="valor").reset_index().rename(columns=nombres)
    mensual.columns.name = None
    num = {a: i + 1 for i, a in enumerate(ABREV)}
    mensual.insert(6, "Mes_num", mensual["Mes_abrev"].map(num).astype(int))
    mensual.insert(6, "Mes", mensual["Mes_num"].map(lambda n: MESES[n - 1]))
    mensual.insert(8, "Dias_mes", mensual["Mes_num"].map(lambda n: DIAS_2024[n - 1]))
    mensual = mensual.drop(columns="Mes_abrev").sort_values(["Cod_Estab", "Cod_Nivel", "Mes_num"]).reset_index(drop=True)
    mensual["Egresos_por_dia"] = (mensual["Numero_de_Egresos"] / mensual["Dias_mes"]).round(3)
    anual = anual.sort_values(["Cod_Estab", "Cod_Nivel"]).reset_index(drop=True)

    glosas = [c for c in anual.columns if c not in nombres.values()]
    sucias = {c: "coma" for c in glosas}
    notas = ["Vivo: los 11 indicadores con coma decimal ('85,3').",
             "Pivotada: ya no hay columna Glosa, cada indicador es una columna. Sin filas agregadas (Datos País / Servicio Salud / Establecimiento).",
             "09a mensual: filas por mes, con Mes, Mes_num, Dias_mes y Egresos_por_dia (egresos del mes ÷ días del mes). 09b anual: el acumulado del año."]
    return {"09a_hospitalarias_mensual.csv": mensual, "09b_hospitalarias_anual.csv": anual}, sucias, notas


# ───────────────────────── escritura y verificación ─────────────────────────
def ensuciar(t: pd.DataFrame, sucias: dict) -> pd.DataFrame:
    s = t.copy()
    for col, tipo in sucias.items():
        if tipo == "coma":
            s[col] = a_coma(t[col])
        elif tipo == "miles":
            s[col] = a_miles(t[col])
    return s


def receta(serie: pd.Series, tipo: str) -> pd.Series:
    """La línea de texto de la clase para cada caso, seguida de to_numeric(errors='coerce')."""
    if tipo == "coma":
        serie = serie.str.replace(",", ".", regex=False)
    elif tipo == "miles":
        serie = serie.str.replace(".", "", regex=False)
    return pd.to_numeric(serie, errors="coerce")


def verificar(nombre: str, verdad: pd.DataFrame, sucias: dict, ruta: Path) -> list:
    problemas = []
    plana = pd.read_csv(ruta, low_memory=False)                          # SIN parámetros: así la abrirá el estudiante
    # Como la leerá la clase (Concepto 1 de N°37): columnas con punto de miles como texto, con dtype
    como_texto = {c: "str" for c, tipo in sucias.items() if tipo == "miles"}
    leida = pd.read_csv(ruta, low_memory=False, dtype=como_texto) if como_texto else plana
    mal_leidas = [c for c in como_texto if pd.api.types.is_numeric_dtype(plana[c])
                  and not np.array_equal(plana[c].to_numpy(float), verdad[c].to_numpy(float), equal_nan=True)]
    if mal_leidas:                                                       # aviso, no error: es la trampa que enseña el Concepto 1
        print(f"        ⚠ sin dtype se leen MAL en silencio: {mal_leidas}")
    if leida.shape != verdad.shape:
        problemas.append(f"forma {leida.shape} ≠ {verdad.shape}")
        return problemas
    if list(leida.columns) != list(verdad.columns):
        problemas.append("las columnas no coinciden con las esperadas")
    for col, tipo in sucias.items():                                     # la receta revierte el formato EXACTAMENTE
        if pd.api.types.is_numeric_dtype(leida[col]):
            recuperada = leida[col].astype(float)                        # columna sin celdas que ensuciar (p. ej. todas < 1000)
        else:
            recuperada = receta(leida[col], tipo)
        if not np.array_equal(recuperada.to_numpy(float), verdad[col].to_numpy(float), equal_nan=True):
            problemas.append(f"{col}: la receta '{tipo}' NO recupera el valor original")
    for col in verdad.columns:
        if col in sucias:
            continue
        a, b = leida[col], verdad[col]
        if pd.api.types.is_numeric_dtype(b):
            if not np.array_equal(pd.to_numeric(a, errors="coerce").to_numpy(float), b.to_numpy(float), equal_nan=True):
                problemas.append(f"{col}: valores distintos")
        elif not (a.fillna("§") == b.fillna("§")).all():
            problemas.append(f"{col}: textos distintos")
    for col in leida.columns:                                            # texto: sin bordes sucios ni mojibake
        if not pd.api.types.is_numeric_dtype(leida[col]):
            v = leida[col].dropna().astype(str)
            if (v.str.strip() != v).any() or v.str.contains("Ã|�|\xa0").any():
                problemas.append(f"{col}: espacios en bordes o caracteres rotos")
    return problemas


def main():
    V2.mkdir(exist_ok=True)
    trabajos = [
        ("01_sies.csv", sies), ("02_demre.csv", demre), ("03_simce_establecimiento.csv", simce_rbd), ("04_simce_comuna.csv", simce_comuna),
        ("05_matricula.csv", matricula), ("06_subvenciones.csv", subvenciones), ("07_conaset_rm.csv", conaset),
        ("08a_odepa_consumidor.csv", odepa_consumidor), ("08b_odepa_mayorista.csv", odepa_mayorista),
        ("08c_odepa_catastro_fruticola.csv", odepa_catastro), ("09_hospitalarias", hospitalarias),
    ]
    hubo_error = False
    for nombre, funcion in trabajos:
        verdad, sucias, notas = funcion()
        tablas = verdad if isinstance(verdad, dict) else {nombre: verdad}
        for archivo, tabla in tablas.items():
            tabla = enteros_donde_corresponda(tabla.reset_index(drop=True), excepto=sucias.keys())
            salida = ensuciar(tabla, sucias)
            ruta = V2 / archivo
            salida.to_csv(ruta, index=False, encoding="utf-8", lineterminator="\n")
            problemas = verificar(archivo, tabla, sucias, ruta)
            mb = ruta.stat().st_size / 1024 / 1024
            estado = "OK " if not problemas else "ERR"
            print(f"[{estado}] {archivo:34} {tabla.shape[0]:>7} filas x {tabla.shape[1]:>2} cols  {mb:5.1f} MB  columnas ensuciadas: {len(sucias) if sucias else 0}")
            for p in problemas:
                print("        ✗", p)
                hubo_error = True
        for n in notas:
            print("        ·", n)
    sys.exit(1 if hubo_error else 0)


if __name__ == "__main__":
    main()
