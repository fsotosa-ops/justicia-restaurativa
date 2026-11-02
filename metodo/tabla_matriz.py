"""Escribe evidencia/matriz.md: la matriz de extracción como tablas legibles, una por literatura.

    python3 metodo/tabla_matriz.py

La fuente es evidencia/matriz.csv (una fila por estudio o norma). Este archivo solo la presenta.
"""
import csv
from pathlib import Path

RAIZ = Path(__file__).parent.parent
ORDEN = ["Acceso a la justicia", "Justicia restaurativa en lo penal", "IA y derecho", "Lenguaje judicial",
         "Normas colombianas", "Método"]

filas = list(csv.DictReader(open(RAIZ / "evidencia" / "matriz.csv", encoding="utf-8")))


def celda(t):
    return t.replace("|", "/").replace("\n", " ").strip()


def aportes(a):
    if a in ("", "ninguna"):
        return "ninguna"
    return ", ".join(f"{h} {d}" for h, d in (x.split(":") for x in a.split("|")))


L = ["# Matriz de extracción", "",
     "Una fila por estudio o norma citado en los documentos. Las columnas completas, con el resultado medido y el nivel de evidencia, están en [`matriz.csv`](matriz.csv). «Aporta a» dice a qué hipótesis de trabajo aporta cada texto y en qué dirección respecto de la hipótesis tal como está formulada: *respalda*, *matiza*, *contradice* o *contexto* (da el marco sin probar ni refutar). Los textos marcados con † solo se conocen por su resumen.",
     ""]
n = 0
for lit in ORDEN:
    grupo = [f for f in filas if f["literatura"] == lit]
    if not grupo:
        continue
    n += 1
    L += [f"**Tabla {n}.** {lit} ({len(grupo)})", ""]
    if lit == "Normas colombianas":
        L += ["| Norma | Qué dice, con su ubicación | Aporta a |", "|---|---|---|"]
        for f in grupo:
            L.append(f"| {celda(f['autor_ano'])} | {celda(f['hallazgo_principal'])} ({celda(f['pagina'])}) | {aportes(f['aportes'])} |")
    else:
        L += ["| Estudio | País | Diseño y muestra | Hallazgo principal | Páginas | Aporta a |", "|---|---|---|---|---|---|"]
        for f in grupo:
            marca = " †" if f["leido_completo"] == "solo_resumen" else ""
            L.append(f"| {celda(f['autor_ano'])}{marca} | {celda(f['pais'])} | {celda(f['diseno'])}; {celda(f['muestra'])} | "
                     f"{celda(f['hallazgo_principal'])} | {celda(f['pagina'])} | {aportes(f['aportes'])} |")
    L += ["", "*Fuente:* Elaboración propia.", ""]
(RAIZ / "evidencia" / "matriz.md").write_text("\n".join(L), encoding="utf-8")
print("tablas", n, "filas", len(filas))
