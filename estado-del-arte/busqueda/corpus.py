"""Une las exportaciones de Scopus y mide cuánto se leen entre sí las literaturas.

    python3 estado-del-arte/busqueda/corpus.py

Lee scopus/E*.csv (una exportación por ecuación, con referencias) y escribe:
  corpus.csv      un documento por fila, primera aparición por EID, con la columna «ecuaciones»
                  (todas las ecuaciones que lo trajeron) y «literatura»
  conexion.txt    la fracción de pares de documentos que comparten al menos una referencia citada,
                  dentro de cada literatura y entre literaturas

La literatura de cada documento sale de la ecuación que lo trajo, en este orden excluyente:
  cruce          E10 a E13
  acceso         E1 o E2
  restaurativa   E3 a E5
  ia             E6 a E8
  lenguaje       E9 (lenguaje judicial sobre víctimas; no exige IA)
Es la misma medida del mapa del campo de la tesis (conexion_impulso_u.py).
"""
import csv
import re
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

csv.field_size_limit(sys.maxsize)
AQUI = Path(__file__).parent
ORDEN = [("cruce", {"E10", "E11", "E12", "E13"}), ("acceso", {"E1", "E2"}),
         ("restaurativa", {"E3", "E4", "E5"}), ("ia", {"E6", "E7", "E8"}), ("lenguaje", {"E9"})]


def literatura(ecuaciones):
    for nombre, grupo in ORDEN:
        if ecuaciones & grupo:
            return nombre
    return "otra"


def referencias(fila):
    salida = set()
    for ref in fila.get("References", "").split("; "):
        clave = re.sub(r"[^a-z0-9]", "", ref.lower())[:60]
        if len(clave) >= 25:
            salida.add(clave)
    return salida


def tasa(a, b=None):
    pares = combinations(a, 2) if b is None else ((x, y) for x in a for y in b)
    total = unidos = 0
    for x, y in pares:
        total += 1
        unidos += bool(x & y)
    return unidos, total


def unir():
    filas, por_eid, columnas = [], {}, []
    for ruta in sorted(AQUI.glob("scopus/E*.csv"), key=lambda p: int(re.search(r"E(\d+)", p.name).group(1))):
        ecuacion = re.search(r"(E\d+)", ruta.name).group(1)
        for f in csv.DictReader(open(ruta, encoding="utf-8-sig")):
            for c in f:
                if c not in columnas:
                    columnas.append(c)
            if f["EID"] in por_eid:
                por_eid[f["EID"]]["ecuaciones"].add(ecuacion)
            else:
                f["ecuaciones"] = {ecuacion}
                por_eid[f["EID"]] = f
                filas.append(f)
    for f in filas:
        f["literatura"] = literatura(f["ecuaciones"])
        f["ecuaciones"] = " ".join(sorted(f["ecuaciones"], key=lambda e: int(e[1:])))
    return filas, columnas + ["ecuaciones", "literatura"]


if __name__ == "__main__":
    filas, columnas = unir()
    with open(AQUI / "corpus.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columnas, quoting=csv.QUOTE_ALL, restval="")
        w.writeheader()
        w.writerows(filas)

    G = {nombre: [referencias(f) for f in filas if f["literatura"] == nombre] for nombre, _ in ORDEN}
    lineas = [f"corpus: {len(filas)} documentos únicos",
              " · ".join(f"{k} {len(v)}" for k, v in G.items()),
              f"sin referencias: {sum(1 for f in filas if not f.get('References', '').strip())}", ""]
    ac, jr, ia, cr, le = G["acceso"], G["restaurativa"], G["ia"], G["cruce"], G["lenguaje"]
    for nombre, (u, t) in [
        ("dentro de acceso", tasa(ac)), ("dentro de restaurativa", tasa(jr)), ("dentro de ia", tasa(ia)), ("dentro de lenguaje", tasa(le)),
        ("acceso × restaurativa", tasa(ac, jr)), ("acceso × ia", tasa(ac, ia)), ("restaurativa × ia", tasa(jr, ia)), ("lenguaje × ia", tasa(le, ia)), ("lenguaje × restaurativa", tasa(le, jr)),
        ("cruce × acceso", tasa(cr, ac)), ("cruce × restaurativa", tasa(cr, jr)), ("cruce × ia", tasa(cr, ia)),
    ]:
        lineas.append(f"{nombre:24} {u:>9,} de {t:>11,} pares  {100 * u / t if t else 0:6.2f} %")
    cj, ci = Counter(r for s in jr for r in s), Counter(r for s in ia for r in s)
    lineas += ["", "referencias citadas a la vez por restaurativa e ia:"]
    for r in sorted(set(cj) & set(ci), key=lambda r: -(cj[r] * ci[r]))[:15]:
        lineas.append(f"  {cj[r]:>3} {ci[r]:>3}  {r}")
    texto = "\n".join(lineas)
    (AQUI / "conexion.txt").write_text(texto + "\n", encoding="utf-8")
    print(texto)
