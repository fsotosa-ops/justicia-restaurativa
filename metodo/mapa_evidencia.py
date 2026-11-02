# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib>=3.8"]
# ///
"""Mapa de evidencia: cuántos estudios aportan a cada hipótesis, según su diseño y su dirección.

    uv run metodo/mapa_evidencia.py

Lee evidencia/matriz.csv (una fila por estudio o norma; la columna aportes dice a qué hipótesis
aporta cada uno y en qué dirección, por ejemplo «H2:respalda|H4:matiza») y escribe figuras/mapa-evidencia.svg.
Filas: hipótesis H1 a H6. Columnas: nivel de la evidencia. En cada celda, un círculo por dirección
(respalda, matiza, contradice) cuyo tamaño es el número de estudios. Sigue la forma de los mapas
de brechas de evidencia (evidence gap maps) de Campbell y 3ie.
"""
import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAIZ = Path(__file__).parent.parent
TINTA, TINTA_2, LINEA = "#0b0b0b", "#52514e", "#dcdad4"
COLOR = {"respalda": "#2a78d6", "matiza": "#1baf7a", "contradice": "#eb6834"}
plt.rcParams.update({"font.family": ["Avenir Next", "Helvetica Neue", "DejaVu Sans"], "svg.fonttype": "path"})

HIPOTESIS = [("H1", "H1. Comprensión"), ("H2", "H2. Orientación"), ("H3", "H3. Derivación"),
             ("H4", "H4. Eficiencia"), ("H5", "H5. Resultados"), ("H6", "H6. Gobernanza")]
NIVELES = [("alto", "Alto\n(ensayo aleatorio\no metaanálisis)"), ("medio", "Medio\n(cuasiexperimental u\nobservacional con datos)"),
           ("bajo", "Bajo\n(cualitativo, caso o\nevaluación técnica)"), ("normativo", "Normativo\n(norma o\nsentencia)")]
DIRECCIONES = ["respalda", "matiza", "contradice"]

filas = list(csv.DictReader(open(RAIZ / "evidencia" / "matriz.csv", encoding="utf-8")))
cuenta = Counter()
for f in filas:
    for aporte in f["aportes"].split("|"):
        if ":" not in aporte:
            continue
        h, d = aporte.split(":", 1)
        if h in dict(HIPOTESIS) and d in DIRECCIONES:
            cuenta[(h, f["nivel_evidencia"], d)] += 1

fig, ax = plt.subplots(figsize=(10, 6.4))
ax.set_xlim(-0.5, len(NIVELES) - 0.5)
ax.set_ylim(len(HIPOTESIS) - 0.5, -0.5)
for i in range(len(HIPOTESIS) + 1):
    ax.axhline(i - 0.5, color=LINEA, lw=0.8)
for j in range(len(NIVELES) + 1):
    ax.axvline(j - 0.5, color=LINEA, lw=0.8)
desplaz = {"respalda": -0.27, "matiza": 0, "contradice": 0.27}
for i, (h, _) in enumerate(HIPOTESIS):
    for j, (nivel, _) in enumerate(NIVELES):
        for d in DIRECCIONES:
            n = cuenta[(h, nivel, d)]
            if not n:
                continue
            x = j + desplaz[d]
            ax.scatter(x, i, s=170 * n ** 0.9 + 60, color=COLOR[d], edgecolor="white", linewidth=2, zorder=3)
            ax.text(x, i, str(n), ha="center", va="center", fontsize=9, color="white", fontweight="bold", zorder=4)
ax.set_xticks(range(len(NIVELES)), [n for _, n in NIVELES], fontsize=9.5, color=TINTA)
ax.set_yticks(range(len(HIPOTESIS)), [n for _, n in HIPOTESIS], fontsize=10.5, color=TINTA)
ax.xaxis.tick_top()
ax.tick_params(length=0)
for s in ax.spines.values():
    s.set_visible(False)
manejadores = [plt.scatter([], [], s=150, color=COLOR[d], label=d.capitalize()) for d in DIRECCIONES]
ax.legend(handles=manejadores, loc="upper center", bbox_to_anchor=(0.5, -0.03), ncol=3, frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(RAIZ / "figuras" / "mapa-evidencia.svg", facecolor="white")
print({h: sum(v for k, v in cuenta.items() if k[0] == h) for h, _ in HIPOTESIS})
