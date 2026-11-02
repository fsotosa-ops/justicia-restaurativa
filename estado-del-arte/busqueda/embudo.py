# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib>=3.8"]
# ///
"""Figura 1 del README: recorrido de la búsqueda y lo que quedó en cada literatura.

    uv run estado-del-arte/busqueda/embudo.py

Lee corpus.csv y tamizaje-e10.csv, y escribe grafos/00-recorrido.png. Los textos leídos en
texto completo se cuentan a mano a partir de estado-del-arte/contraste-hipotesis.md.
"""
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

csv.field_size_limit(sys.maxsize)
AQUI = Path(__file__).parent
AZUL, TINTA, TINTA_2, BORDE, FONDO = "#2a78d6", "#0b0b0b", "#52514e", "#d9d8d2", "#f3f6fb"
plt.rcParams.update({"font.family": ["Avenir Next", "Helvetica Neue", "DejaVu Sans"]})

corpus = list(csv.DictReader(open(AQUI / "corpus.csv", encoding="utf-8-sig")))
n = {k: sum(1 for f in corpus if f["literatura"] == k) for k in ("acceso", "restaurativa", "ia", "lenguaje", "cruce")}
tam = list(csv.DictReader(open(AQUI / "tamizaje-e10.csv", encoding="utf-8")))
inc_e10 = sum(1 for f in tam if f["decision"] == "incluye")
cruce_tamizados = len(tam) + sum(1 for f in corpus if "E13" in f["ecuaciones"].split())

# Textos leídos en texto completo el 30 de octubre, por literatura (contraste-hipotesis.md)
LEIDOS = {"acceso": 7, "restaurativa": 15, "ia": 0, "lenguaje": 0}

PASOS = [
    ("1 · Hipótesis", "Consensus para contrastar\nH1 a H6 con la literatura"),
    ("2 · Búsqueda", "13 ecuaciones en Scopus,\ndos corridas con prueba\nde sensibilidad"),
    ("3 · Tamizaje", "Título y resumen de los\ncruces E10 y E13"),
    ("4 · Texto completo", "22 textos con registro\nde páginas, cotejados\nen el PDF"),
]
FILAS = [
    ("E1 y E2", "Acceso a la justicia", n["acceso"], f"{LEIDOS['acceso']}", "leídos"),
    ("E3 a E5", "Justicia restaurativa en lo penal", n["restaurativa"], f"{LEIDOS['restaurativa']}", "leídos"),
    ("E6 a E8", "IA y derecho", n["ia"], "0", "leídos"),
    ("E9", "Lenguaje judicial sobre las víctimas", n["lenguaje"], "0", "leídos"),
    ("E10 a E13", "Cruces entre las literaturas", n["cruce"], f"{inc_e10} de {cruce_tamizados}",
     "aplican IA a lo restaurativo"),
]


def caja(ax, x, y, w, h, fc="white", ec=BORDE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12", fc=fc, ec=ec, lw=1))


fig, ax = plt.subplots(figsize=(11, 7.4))
ax.set_xlim(0, 11); ax.set_ylim(0, 7.4); ax.axis("off")

w, gap = 2.56, 0.17
for i, (t, d) in enumerate(PASOS):
    x = i * (w + gap)
    caja(ax, x, 5.75, w, 1.5)
    ax.text(x + 0.18, 7.02, t.upper(), fontsize=9, color=AZUL, fontweight="bold", va="top")
    ax.text(x + 0.18, 6.6, d, fontsize=9.5, color=TINTA, va="top", linespacing=1.3)
    if i < len(PASOS) - 1:
        ax.text(x + w + gap / 2, 6.5, "›", fontsize=16, color=TINTA_2, ha="center", va="center")

for j, (eqs, nombre, docs, leidos, et) in enumerate(FILAS):
    y = 4.75 - j * 1.08
    caja(ax, 0, y, 11, 0.92, fc=FONDO, ec=FONDO)
    ax.text(0.25, y + 0.62, eqs.upper(), fontsize=8.5, color=AZUL, fontweight="bold", va="center")
    ax.text(0.25, y + 0.3, nombre, fontsize=11, color=TINTA, fontweight="bold", va="center")
    ax.text(6.6, y + 0.56, f"{docs:,}".replace(",", "."), fontsize=19, color=AZUL, fontweight="bold", va="center")
    ax.text(6.6, y + 0.18, "documentos", fontsize=8.5, color=TINTA_2, va="center")
    ax.text(8.55, y + 0.56, leidos, fontsize=19 if " de " not in leidos else 15, color=TINTA, fontweight="bold", va="center")
    ax.text(8.55, y + 0.18, et, fontsize=8.5, color=TINTA_2, va="center")

fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
(AQUI / "grafos").mkdir(exist_ok=True)
fig.savefig(AQUI / "grafos" / "00-recorrido.png", dpi=200, facecolor="white")
print("listo:", n, "e10 incluidos", inc_e10, "tamizados", cruce_tamizados)
