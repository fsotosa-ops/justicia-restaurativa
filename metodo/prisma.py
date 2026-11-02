# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib>=3.8"]
# ///
"""Figura 1 del estado del arte: diagrama de flujo PRISMA 2020 de la búsqueda.

    uv run metodo/prisma.py

Sigue la plantilla PRISMA 2020 para revisiones con búsqueda en bases de datos y por otros
métodos (Page y colegas, 2021). Los conteos de Scopus salen de corpus.csv y de las revisiones
por título y resumen (datos/revision-e10.csv a revision-e12.csv). Los textos buscados, no
recuperados y leídos se registran a mano en LECTURA, a partir de evidencia/.
Escribe figuras/prisma.svg (vectorial).
"""
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

csv.field_size_limit(sys.maxsize)
AQUI = Path(__file__).parent
TINTA, TINTA_2, FASE = "#0b0b0b", "#52514e", "#dbe8f8"
plt.rcParams.update({"font.family": ["Avenir Next", "Helvetica Neue", "DejaVu Sans"], "svg.fonttype": "path"})

RESULTADOS_SCOPUS = 9268  # suma de las 13 ecuaciones en la segunda corrida (protocolo.md, Tabla 3)
corpus = list(csv.DictReader(open(AQUI / "corpus.csv", encoding="utf-8-sig")))
unicos = len(corpus)
cruces = [f for f in corpus if set(f["ecuaciones"].split()) & {"E10", "E11", "E12"}]

orden = {"incluye": 2, "conceptual": 1, "excluye": 0}
decision = {}
for nombre in ("revision-e10.csv", "revision-e11.csv", "revision-e12.csv"):
    for f in csv.DictReader(open(AQUI.parent / "datos" / nombre, encoding="utf-8")):
        k = f["titulo"].strip().lower()[:80]
        if k not in decision or orden[f["decision"]] > orden[decision[k]]:
            decision[k] = f["decision"]
con_sistema = sum(1 for d in decision.values() if d == "incluye")
conceptuales = sum(1 for d in decision.values() if d == "conceptual")
pertinentes = con_sistema + conceptuales
excluidos = len(cruces) - pertinentes

# Lectura en texto completo (fichas en evidencia/)
LECTURA = {
    "cruces_buscados": 23,      # 19 leídos y 4 no recuperados (Universidad Santo Tomás, Justice Buddy, Ali, Lu)
    "relevancia_buscados": 15,  # E6 a E9: 10 leídos y 5 no recuperados (Atkinson, recuperación jurídica, 2 revisiones RAG, grafos)
    "no_recuperados": 9,
    "otros_metodos": 22,        # búsqueda complementaria del 30 de octubre (evidencia/hipotesis.md)
}
buscados = LECTURA["cruces_buscados"] + LECTURA["relevancia_buscados"]
leidos = buscados - LECTURA["no_recuperados"]
incluidos = leidos + LECTURA["otros_metodos"]


def miles(n):
    return f"{n:,}".replace(",", ".")


fig, ax = plt.subplots(figsize=(11, 10.2))
ax.set_xlim(-0.5, 111)
ax.set_ylim(0, 102)
ax.axis("off")


def caja(x, y, w, h, texto, negrita=False, size=9.6):
    ax.add_patch(Rectangle((x, y), w, h, fc="white", ec=TINTA, lw=0.9))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=size, color=TINTA,
            linespacing=1.35, fontweight="bold" if negrita else "normal", wrap=True)


def flecha(x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=11, lw=0.9, color=TINTA))


def fase(y, h, texto):
    ax.add_patch(Rectangle((0, y), 4.5, h, fc=FASE, ec="none"))
    ax.text(2.25, y + h / 2, texto, rotation=90, ha="center", va="center", fontsize=10, fontweight="bold", color=TINTA)


# Encabezados de columna
ax.add_patch(Rectangle((6, 96), 66, 5, fc="#f3f2ee", ec="none"))
ax.text(39, 98.5, "Búsqueda en Scopus", ha="center", va="center", fontsize=10.5, fontweight="bold", color=TINTA)
ax.add_patch(Rectangle((76, 96), 34.5, 5, fc="#f3f2ee", ec="none"))
ax.text(93, 98.5, "Otros métodos", ha="center", va="center", fontsize=10.5, fontweight="bold", color=TINTA)

fase(78, 16, "Identificación")
fase(24, 52, "Revisión")
fase(4, 18, "Incluidos")

# Columna Scopus
caja(6, 82, 30, 12, f"Registros identificados\nen 13 ecuaciones\n(n = {miles(RESULTADOS_SCOPUS)})")
caja(42, 82, 30, 12, f"Registros eliminados\nantes de la revisión:\nduplicados (n = {miles(RESULTADOS_SCOPUS - unicos)})")
flecha(36, 88, 42, 88)

caja(6, 64, 30, 12, f"Registros únicos\n(n = {miles(unicos)})")
caja(42, 64, 30, 12, f"Sin revisión sistemática:\nliteraturas E1 a E9\n(n = {miles(unicos - len(cruces))})")
flecha(21, 82, 21, 76)
flecha(36, 70, 42, 70)

caja(6, 46, 30, 12, f"Registros revisados por\ntítulo y resumen:\ncruces E10 a E12\n(n = {len(cruces)})")
caja(42, 46, 30, 12, f"Registros excluidos:\nfuera del tema o con la\nIA tangencial (n = {excluidos})")
flecha(21, 64, 21, 58)
flecha(36, 52, 42, 52)

caja(6, 26, 30, 14, f"Textos completos buscados\n(n = {buscados}):\n{LECTURA['cruces_buscados']} priorizados entre {pertinentes}\npertinentes de los cruces y\n{LECTURA['relevancia_buscados']} elegidos en E6 a E9")
caja(42, 26, 30, 14, f"Textos no recuperados\n(n = {LECTURA['no_recuperados']}): ScienceDirect 3,\nIEEE 4, IOS Press 1 y\n1 sin ubicar")
flecha(21, 46, 21, 40)
flecha(36, 33, 42, 33)

caja(6, 8, 30, 12, f"Leídos en texto completo\ncon registro de páginas\n(n = {leidos})")
flecha(21, 26, 21, 20)

# Columna otros métodos
caja(78, 64, 30, 30, f"Textos identificados en\nuna búsqueda\ncomplementaria para\ncontrastar las hipótesis\ndel equipo (30 de\noctubre de 2026)")
caja(78, 26, 30, 14, f"Leídos en texto completo\ncon registro de páginas\n(n = {LECTURA['otros_metodos']})")
flecha(93, 64, 93, 40)

# Incluidos
caja(42, 8, 30, 12, f"Incluidos en el\nestado del arte\n(n = {incluidos})", negrita=True, size=10.5)
flecha(36, 14, 42, 14)
ax.add_patch(FancyArrowPatch((93, 26), (72, 14), arrowstyle="-|>", mutation_scale=11, lw=0.9, color=TINTA,
                             connectionstyle="angle,angleA=-90,angleB=180,rad=0"))

fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig(AQUI.parent / "figuras" / "prisma.svg", facecolor="white")
print(f"únicos {unicos} · cruces {len(cruces)} · pertinentes {pertinentes} ({con_sistema}+{conceptuales}) · "
      f"excluidos {excluidos} · buscados {buscados} · leídos {leidos} · incluidos {incluidos}")
