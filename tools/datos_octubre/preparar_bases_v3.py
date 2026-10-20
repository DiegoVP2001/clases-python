"""
Prepara la versión 3 de las bases del Proyecto Cierre Octubre (N°38 en adelante, giro plug-and-play).

Parte de `clases/clases-octubre/datos-compartidos-v2/` (que NO se toca) y escribe `clases/clase-38y38b/datos-compartidos-v3/`:
mismas filas, mismas columnas y mismos nombres, pero con los números que venían escritos como texto
("85,3", "1.234.567", "s/i") ya escritos como número ("85.3", "1234567", vacío). Así `pd.read_csv(url)` los
abre sin parámetros y cada columna numérica ya es número, sin limpiar nada.

El cambio es solo de escritura, nunca de valor: el script lo comprueba contra los valores verdaderos
que calcula `preparar_bases.py` (la misma lista de columnas) y contra la v2.

Uso: python tools/datos_octubre/preparar_bases_v3.py
Termina con código 1 si alguna verificación falla.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import preparar_bases as v2mod  # noqa: E402  (misma carpeta)

V2 = v2mod.V2
V3 = v2mod.RAIZ / "clases" / "clase-38y38b" / "datos-compartidos-v3"

# Columnas que preparar_bases.py no marca como "sucias" pero igual vienen como texto numérico.
#   "punto": ya trae punto decimal; solo hay que dejar vacío el "s/i".
#   "coma" : trae coma decimal.
EXTRAS = {
    "01_sies.csv": {"Retención 1er año": "punto", "Duración Real (semestres)": "punto"},
    "08a_odepa_consumidor.csv": {"Precio promedio": "coma"},
    "08b_odepa_mayorista.csv": {"Precio minimo": "coma", "Precio maximo": "coma", "Precio promedio": "coma"},
    "08c_odepa_catastro_fruticola.csv": {"Superficie (ha)": "coma"},
}


MEDIDAS = {"kilo": "kilos", "kilos": "kilos", "grs": "gramos", "gramos": "gramos", "litro": "litros", "litros": "litros",
           "ml": "ml", "unidad": "unidades", "unidades": "unidades"}


# Unidades de ODEPA mayorista que no siguen el patrón "$/envase cantidad medida": (envase, cantidad, medida)
UNIDADES_ESPECIALES = {
    "$/docena de atados": ("atado", 12, "unidades"),
    "$/docena de matas": ("mata", 12, "unidades"),
    "$/docena de paquetes": ("paquete", 12, "unidades"),
    "$/cien unidades (volumen en unidades)": (None, 100, "unidades"),
    "$/paquete": ("paquete", None, None),
    "$/caja 36 atados": ("caja", 36, "unidades"),                       # los atados se cuentan como unidades
    "$/bandeja 12 canastillos 125 gramos": ("bandeja", 12, "unidades"),  # los canastillos se cuentan; el peso queda en la original
}


def monto(parte: str) -> int:
    """'$1 millón 100 mil' -> 1100000; '$800 mil' -> 800000; '$2 millones' -> 2000000."""
    mill = re.search(r"(\d+)\s+mill", parte)
    mil = re.search(r"(\d+)\s+mil\b", parte)
    return (int(mill.group(1)) * 1_000_000 if mill else 0) + (int(mil.group(1)) * 1_000 if mil else 0)


def rango_ingreso(texto: str):
    """(mínimo, máximo) en pesos. 's/i' -> sin dato; 'Sobre $3 millones 500 mil' -> solo mínimo."""
    if texto in ("", "s/i"):
        return None, None
    if texto.startswith("Sobre"):
        return monto(texto), None
    desde, hasta = re.split(r"\s+a\s+", texto)
    return monto(desde), monto(hasta)


def anios_acreditacion(texto: str):
    """'5 años' -> 5; 'No' (sin acreditación) -> 0."""
    if texto == "No":
        return 0
    return int(re.fullmatch(r"(\d+) años", texto).group(1))


def unidad_consumidor(texto: str):
    """(cantidad, medida) de la unidad en que se expresa el precio. Lo que va entre paréntesis ('en saco de 25 kilos')
    describe el envase, no la unidad del precio: '$/kilo (en saco de 25 kilos)' es 1 kilo."""
    base = re.sub(r"\s*\(en .*\)$", "", texto)
    m = re.fullmatch(r"\$/(?:[A-Za-záéíóú]+\s+(?:de\s+)?)?(?:(\d+(?:[.,]\d+)?)\s+)?(kilos?|grs|gramos|litros?|ml|unidades|unidad)",
                     base, re.I)
    return int(m.group(1)) if m.group(1) else 1, MEDIDAS[m.group(2).lower()]


def unidad_mayorista(texto: str):
    """(envase, cantidad, medida). '$/caja 18 kilos' -> (caja, 18, kilos); '$/bins (350 kilos)' -> (bins, 350, kilos);
    '$/kilo' y '$/unidad' se venden sin envase: (vacío, 1, kilos|unidades). 'empedrada' / 'granel' quedan solo en la original.
    La nota '(volumen en unidades)' dice en qué se reporta el volumen, no la unidad del precio: '$/kilo (volumen en unidades)' es 1 kilo.
    '$/paquete' no informa cuánto trae: cantidad y medida quedan vacías."""
    texto = re.sub(r"\s*\(volumen en unidades\)$", "", texto) if texto != "$/cien unidades (volumen en unidades)" else texto
    if texto in UNIDADES_ESPECIALES:
        return UNIDADES_ESPECIALES[texto]
    m = re.fullmatch(r"\$/(?P<envase>[a-záéíóú]+)(?:\s+\(?(?P<cant>\d+)\s+(?P<med>kilos?|unidades|gramos|litros?)\)?)?(?:\s+.+)?",
                     texto, re.I)
    envase, cant, med = m.group("envase").lower(), m.group("cant"), m.group("med")
    if cant is None:
        if envase not in ("kilo", "unidad"):
            raise ValueError(f"unidad sin cantidad: {texto}")
        return None, 1, MEDIDAS[envase]
    return envase, int(cant), MEDIDAS[med.lower()]


def a_texto(valor):
    """Número entero -> texto; sin dato -> vacío."""
    return "" if valor is None or (isinstance(valor, float) and np.isnan(valor)) else str(valor)


def insertar(t: pd.DataFrame, despues_de: str, nuevas: dict) -> pd.DataFrame:
    pos = t.columns.get_loc(despues_de) + 1
    for i, (nombre, serie) in enumerate(nuevas.items()):
        t.insert(pos + i, nombre, serie)
    return t


def derivar(archivo: str, t: pd.DataFrame):
    """Agrega, junto a la columna original (que se conserva), las columnas numéricas o separadas que salen de un número
    escrito con palabras. Devuelve la tabla y {columna_nueva: columna_original} para la verificación."""
    origen = {}
    if archivo == "01_sies.csv":
        col = "Ingreso Promedio al 4° año"
        pares = t[col].map(rango_ingreso)
        t = insertar(t, col, {"Ingreso_min": pares.map(lambda p: a_texto(p[0])), "Ingreso_max": pares.map(lambda p: a_texto(p[1]))})
        origen.update({"Ingreso_min": col, "Ingreso_max": col})
        col = "Acreditación institución (al 31 de octubre 2025)"
        t = insertar(t, col, {"Acreditacion_anios": t[col].map(lambda s: a_texto(anios_acreditacion(s)) if s else "")})
        origen["Acreditacion_anios"] = col
    elif archivo == "08a_odepa_consumidor.csv":
        pares = t["Unidad"].map(unidad_consumidor)
        t = insertar(t, "Unidad", {"Unidad_cantidad": pares.map(lambda p: a_texto(p[0])), "Unidad_medida": pares.map(lambda p: p[1])})
        origen.update({"Unidad_cantidad": "Unidad", "Unidad_medida": "Unidad"})
    elif archivo == "08b_odepa_mayorista.csv":
        col = "Unidad de comercializacion"
        trio = t[col].map(unidad_mayorista)
        t = insertar(t, col, {"Envase": trio.map(lambda p: a_texto(p[0])), "Unidad_cantidad": trio.map(lambda p: a_texto(p[1])),
                              "Unidad_medida": trio.map(lambda p: p[2])})
        origen.update({"Envase": col, "Unidad_cantidad": col, "Unidad_medida": col})
        t = insertar(t, "Fecha", {"Mes_num": t["Fecha"].map(lambda s: a_texto(int(s[5:7])) if s else "")})
        origen["Mes_num"] = "Fecha"
    return t, origen


def leer_texto(ruta: Path) -> pd.DataFrame:
    """Lee todo como texto, sin convertir nada (ni "NA" ni vacíos): el texto vuelve a escribirse idéntico."""
    return pd.read_csv(ruta, dtype=str, keep_default_na=False, low_memory=False)


def transformar(serie: pd.Series, tipo: str) -> pd.Series:
    if tipo == "coma":
        return serie.str.replace(",", ".", regex=False)
    if tipo == "miles":
        return serie.str.replace(".", "", regex=False)
    if tipo == "punto":
        return serie.replace({"s/i": ""})
    raise ValueError(tipo)


def verificar_derivadas(archivo: str, texto: pd.DataFrame, leida: pd.DataFrame, derivadas: dict) -> list:
    """Cada columna nueva: tipo correcto, ningún valor perdido donde la original tenía dato, y coherencia interna."""
    problemas = []
    for nueva, original in derivadas.items():
        if nueva in ("Envase", "Unidad_medida"):
            continue
        if not pd.api.types.is_numeric_dtype(leida[nueva]):
            problemas.append(f"{nueva}: no quedó como número (dtype {leida[nueva].dtype})")
    if problemas:
        return problemas
    if archivo == "01_sies.csv":
        orig = texto["Ingreso Promedio al 4° año"]
        mn, mx, pm = leida["Ingreso_min"], leida["Ingreso_max"], leida["Ingreso_punto_medio"]
        if not (mn.isna() == orig.isin(["s/i", ""])).all():
            problemas.append("Ingreso_min: vacío donde no debía (o con dato donde la original era s/i)")
        if not (mx.isna() == (orig.isin(["s/i", ""]) | orig.str.startswith("Sobre"))).all():
            problemas.append("Ingreso_max: debe quedar vacío solo en 's/i' y en 'Sobre ...'")
        ambos = mn.notna() & mx.notna()
        if not (mx[ambos] > mn[ambos]).all():
            problemas.append("Ingreso_max no es mayor que Ingreso_min en algún rango")
        if not np.allclose(pm[ambos], (mn[ambos] + mx[ambos]) / 2):
            problemas.append("Ingreso_punto_medio no es el punto medio de min y max")
        sobre = orig.str.startswith("Sobre")
        if not (mn[sobre] == pm[sobre]).all():
            problemas.append("En 'Sobre ...' el mínimo debe coincidir con el punto medio ya publicado (3.500.000)")
        acre = texto["Acreditación institución (al 31 de octubre 2025)"]
        a = leida["Acreditacion_anios"]
        if a.isna().any() or not (a[acre == "No"] == 0).all() or sorted(a.unique()) != [0, 3, 4, 5, 6, 7]:
            problemas.append("Acreditacion_anios: valores inesperados")
        tabla = pd.DataFrame({"original": orig, "min": mn, "max": mx}).drop_duplicates().sort_values("min", na_position="first")
        print("        · tabla de equivalencias (Ingreso):"); print(tabla.to_string(index=False))
    elif archivo in ("08a_odepa_consumidor.csv", "08b_odepa_mayorista.csv"):
        col = "Unidad" if archivo.startswith("08a") else "Unidad de comercializacion"
        sin_cantidad = leida[col] == "$/paquete"                      # el único caso que no informa cuánto trae
        if (leida["Unidad_cantidad"].isna() != sin_cantidad).any() or (leida["Unidad_cantidad"].dropna() <= 0).any():
            problemas.append("Unidad_cantidad: vacía donde no debía, o no positiva")
        if (leida["Unidad_medida"].isna() != sin_cantidad).any() or not leida["Unidad_medida"].dropna().isin(
                ["kilos", "gramos", "litros", "ml", "unidades"]).all():
            problemas.append("Unidad_medida: valor fuera de la lista")
        cols = [col, "Unidad_cantidad", "Unidad_medida"] + (["Envase"] if archivo.startswith("08b") else [])
        tabla = leida[cols].drop_duplicates().sort_values(col)
        print(f"        · tabla de equivalencias ({col}):"); print(tabla.to_string(index=False))
        if archivo.startswith("08b"):
            sin_envase = leida[col].str.startswith(("$/kilo", "$/unidad", "$/cien unidades"))   # precio por kilo o por unidad suelta
            if not (leida["Envase"].isna() == sin_envase).all():
                problemas.append("Envase: debe quedar vacío solo cuando el precio es por kilo o por unidad suelta")
            mes = pd.to_datetime(leida["Fecha"]).dt.month
            if not (mes == leida["Mes_num"]).all():
                problemas.append("Mes_num no coincide con el mes de Fecha")
    return problemas


def main():
    V3.mkdir(exist_ok=True)
    trabajos = [
        ("01_sies.csv", v2mod.sies), ("02_demre.csv", v2mod.demre), ("03_simce_establecimiento.csv", v2mod.simce_rbd),
        ("04_simce_comuna.csv", v2mod.simce_comuna), ("05_matricula.csv", v2mod.matricula),
        ("06_subvenciones.csv", v2mod.subvenciones), ("07_conaset_rm.csv", v2mod.conaset),
        ("08a_odepa_consumidor.csv", v2mod.odepa_consumidor), ("08b_odepa_mayorista.csv", v2mod.odepa_mayorista),
        ("08c_odepa_catastro_fruticola.csv", v2mod.odepa_catastro), ("09_hospitalarias", v2mod.hospitalarias),
    ]
    hubo_error = False
    for nombre, funcion in trabajos:
        verdad, sucias, _ = funcion()
        tablas = verdad if isinstance(verdad, dict) else {nombre: verdad}
        for archivo, tabla in tablas.items():
            tabla = v2mod.enteros_donde_corresponda(tabla.reset_index(drop=True), excepto=sucias.keys())
            texto = leer_texto(V2 / archivo)
            conversiones = {c: t for c, t in sucias.items() if c in texto.columns}
            conversiones.update(EXTRAS.get(archivo, {}))
            nuevo = texto.copy()
            for col, tipo in conversiones.items():
                nuevo[col] = transformar(texto[col], tipo)
            nuevo, derivadas = derivar(archivo, nuevo)
            ruta = V3 / archivo
            nuevo.to_csv(ruta, index=False, encoding="utf-8", lineterminator="\n")

            # ── verificación ──
            problemas = []
            leida = pd.read_csv(ruta, low_memory=False)  # SIN parámetros: así la abrirá el estudiante
            if leida.shape != nuevo.shape or list(leida.columns) != list(nuevo.columns):
                problemas.append(f"forma o columnas distintas a lo esperado: {leida.shape} vs {nuevo.shape}")
            else:
                problemas += verificar_derivadas(archivo, texto, leida, derivadas)
                for col, tipo in conversiones.items():
                    if not pd.api.types.is_numeric_dtype(leida[col]):
                        problemas.append(f"{col}: no quedó como número (dtype {leida[col].dtype})")
                    elif col in tabla.columns and pd.api.types.is_numeric_dtype(tabla[col]):
                        if not np.array_equal(leida[col].to_numpy(float), tabla[col].to_numpy(float), equal_nan=True):
                            problemas.append(f"{col}: los valores no coinciden con los verdaderos")
                    elif tipo == "punto":
                        esperado = pd.to_numeric(texto[col].replace({"s/i": ""}), errors="coerce")
                        if not np.array_equal(leida[col].to_numpy(float), esperado.to_numpy(float), equal_nan=True):
                            problemas.append(f"{col}: valores distintos al texto de la v2")
                    else:
                        esperado = pd.to_numeric(transformar(texto[col], tipo), errors="coerce")
                        if not np.array_equal(leida[col].to_numpy(float), esperado.to_numpy(float), equal_nan=True):
                            problemas.append(f"{col}: valores distintos al texto de la v2")
                otras = [c for c in texto.columns if c not in conversiones]
                v3_texto = leer_texto(ruta)
                for col in otras:                                   # lo que no se tocó queda idéntico, carácter por carácter
                    if not (v3_texto[col] == texto[col]).all():
                        problemas.append(f"{col}: cambió y no debía")
            mb = ruta.stat().st_size / 1024 / 1024
            estado = "OK " if not problemas else "ERR"
            print(f"[{estado}] {archivo:34} {leida.shape[0]:>7} filas x {leida.shape[1]:>2} cols  {mb:5.1f} MB  "
                  f"columnas pasadas a número: {len(conversiones)}")
            for p in problemas:
                print("        ✗", p)
                hubo_error = True
    sys.exit(1 if hubo_error else 0)


if __name__ == "__main__":
    main()
