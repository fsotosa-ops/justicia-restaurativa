# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib>=3.8"]
# ///
"""Grafos del Leviatán a partir de los CSV de esta carpeta.

    uv run mapa/grafos.py

Escribe en mapa/grafos/:
  remisiones.png            quién manda el caso a quién, por bloque del Estado
  remisiones-por-ruta.png   la misma red, una ruta por panel
  etapas.png                en qué etapa del proceso penal se abre cada salida restaurativa

Antes de dibujar valida los ids: si una remisión o una dependencia apunta a una
entidad que no está en entidades.csv, se detiene y dice cuál.
"""

import csv
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "grafos"

# Paleta de referencia (skill dataviz). En una red todos los pares de color se
# ven juntos, así que se usan solo dos tonos con significado; el bloque del
# Estado lo dice la franja, no el color.
AZUL = "#2a78d6"        # en esta entidad opera un mecanismo restaurativo
AZUL_CLARO = "#e3edf9"
NARANJA = "#eb6834"     # la bifurcación restaurativa: fiscal o juez -> mediación
TINTA = "#0b0b0b"
TINTA_2 = "#52514e"
TENUE = "#d9d8d2"
SUPERFICIE = "#fcfcfb"
FRANJA = "#f3f2ee"

plt.rcParams.update({
    "font.family": ["Avenir Next", "Helvetica Neue", "DejaVu Sans"],
    "font.size": 10,
    "figure.facecolor": SUPERFICIE,
    "savefig.facecolor": SUPERFICIE,
})


def leer(nombre):
    with open(AQUI / nombre, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ids(campo):
    return [x.strip() for x in campo.split("|") if x.strip()]


entidades = {e["id"]: e for e in leer("entidades.csv")}
remisiones = leer("remisiones.csv")
etapas = leer("etapas.csv")

# Validación
huerfanos = []
for r in remisiones:
    for x in ids(r["origen"]) + ids(r["destino"]):
        if x not in entidades:
            huerfanos.append(f"{r['id']}: {x}")
for e in entidades.values():
    if e["depende_de"] and e["depende_de"] not in entidades:
        huerfanos.append(f"depende_de de {e['id']}: {e['depende_de']}")
if huerfanos:
    sys.exit("ids sin entidad en entidades.csv:\n  " + "\n  ".join(huerfanos))

# Aristas: cada fila con varios ids se expande. r13 (casa de justicia a sí
# misma: el CRI clasifica internamente) no se dibuja como arista.
aristas = []
for r in remisiones:
    for o in ids(r["origen"]):
        for d in ids(r["destino"]):
            if o != d:
                aristas.append({**r, "o": o, "d": d})



def fusionar(lista):
    """Una ida y vuelta del mismo tipo se dibuja como una flecha de doble punta."""
    vistas, out = {}, []
    for a in lista:
        inversa = vistas.get((a["d"], a["o"]))
        if inversa is not None and obligatoria(inversa) == obligatoria(a) and not bifurcacion(a):
            inversa["doble"] = True
            continue
        a = dict(a)
        vistas[(a["o"], a["d"])] = a
        out.append(a)
    return out


# Disposición por franjas: una fila por bloque del Estado.
FRANJAS = [
    ("Distrito", 5),
    ("Ejecutivo nacional", 4),
    ("Ministerio Público", 3),
    ("No formal", 2),
    ("Fiscalía", 1),
    ("Rama Judicial", 0),
]
POS = {
    "sdmujer_casas_refugio": (0.6, 5), "sdmujer": (2.6, 5), "comisarias": (4.8, 5),
    "casas_justicia": (7.2, 5), "umc": (9.4, 5), "inspecciones": (11.4, 5),
    "pon_cai": (0.6, 4), "salud_ips": (2.6, 4), "icbf": (5.8, 4), "redam": (11.4, 4),
    "personeria_bogota": (9.4, 3), "dp_defensa": (11.4, 3),
    "programa_mediacion": (3.4, 2), "centros_conciliacion": (7.2, 2), "consultorios": (9.4, 2),
    "fgn_uri": (0.6, 1), "fgn_sau": (2.4, 1), "fgn_seccional_bogota": (4.8, 1),
    "fgn_grupo_apoyo_jr": (7.2, 1), "inmlcf": (11.4, 1),
    "rj_garantias": (2.4, 0), "rj_conocimiento": (4.8, 0), "rj_juez_familia": (7.2, 0),
}
ETIQUETA = {
    "sdmujer_casas_refugio": "Casa refugio", "sdmujer": "Sec. de la Mujer\nCIOM · Línea Púrpura",
    "comisarias": "Comisaría\nde familia", "casas_justicia": "Casa de justicia\n(CRI)",
    "umc": "UMC", "inspecciones": "Inspección\nde policía", "pon_cai": "Policía · CAI",
    "salud_ips": "Salud · IPS", "icbf": "ICBF", "redam": "REDAM",
    "personeria_bogota": "Personería", "dp_defensa": "Defensoría\n(defensa pública)",
    "programa_mediacion": "Programa de mediación\ncon convenio",
    "centros_conciliacion": "Centro de\nconciliación", "consultorios": "Consultorio\njurídico",
    "fgn_uri": "URI", "fgn_sau": "SAU", "fgn_seccional_bogota": "Fiscal delegado\n(Seccional Bogotá)",
    "fgn_grupo_apoyo_jr": "Grupo de apoyo JR\n(Res. 0383)", "inmlcf": "Medicina Legal",
    "rj_garantias": "Juez de garantías", "rj_conocimiento": "Juez de\nconocimiento",
    "rj_juez_familia": "Juez de familia",
}
faltan = {x for a in aristas for x in (a["o"], a["d"])} - POS.keys()
if faltan:
    sys.exit(f"entidades con remisión pero sin posición en POS: {sorted(faltan)}")

NO_RESTAURATIVO = {"", "no", "no está en las fuentes", "no aplica"}


def restaurativa(i):
    return entidades[i]["restaurativo"].strip() not in NO_RESTAURATIVO


def obligatoria(a):
    t = a["tipo"]
    return t.startswith("obligatoria") and "opcional" not in t


def bifurcacion(a):
    return a["d"] == "programa_mediacion"


def fondo(ax, x0=-0.6, x1=12.6):
    for k, (nombre, y) in enumerate(FRANJAS):
        if k % 2 == 0:
            ax.add_patch(plt.Rectangle((x0, y - 0.5), x1 - x0, 1, color=FRANJA, lw=0, zorder=0))
        ax.text(x0 + 0.1, y + 0.42, nombre.upper(), fontsize=7.5, color=TINTA_2,
                va="top", ha="left", fontweight="bold", zorder=1)
    ax.set_xlim(x0, x1)
    ax.set_ylim(-0.6, 5.6)
    ax.axis("off")


CAJAS = {}


def nodo(ax, i, activo=True, escala=1.0, fuente=7.6):
    x, y = POS[i]
    rest = restaurativa(i)
    borde = AZUL if rest else TINTA_2
    relleno = AZUL_CLARO if rest else "white"
    if i == "programa_mediacion":
        borde, relleno = NARANJA, "#fde6dc"
    alfa = 1 if activo else 0.25
    w, h = 1.62 * escala, 0.5 * escala
    caja = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                          boxstyle="round,pad=0.02,rounding_size=0.08",
                          fc=relleno, ec=borde, lw=1.2, alpha=alfa, zorder=4)
    ax.add_patch(caja)
    CAJAS[(id(ax), i)] = caja
    ax.text(x, y, ETIQUETA[i], ha="center", va="center", fontsize=fuente,
            color=TINTA, alpha=alfa, zorder=5, linespacing=1.05)


def flecha(ax, a, color=None, lw=None, alfa=1.0):
    (x0, y0), (x1, y1) = POS[a["o"]], POS[a["d"]]
    # Las recíprocas (ida y vuelta) se curvan en sentidos opuestos para que no se tapen.
    rad = 0.12 if (a["o"] < a["d"]) else -0.12
    if bifurcacion(a):
        color, lw = NARANJA, 2.6
    if a.get("doble"):
        rad = 0.0
    ax.add_patch(FancyArrowPatch(
        (x0, y0), (x1, y1), connectionstyle=f"arc3,rad={rad}",
        arrowstyle="<|-|>" if a.get("doble") else "-|>", mutation_scale=10,
        patchA=CAJAS.get((id(ax), a["o"])), patchB=CAJAS.get((id(ax), a["d"])),
        lw=lw or (1.5 if obligatoria(a) else 1.1),
        ls="-" if obligatoria(a) else (0, (3, 2)),
        color=color or TINTA_2, alpha=alfa,
        shrinkA=1, shrinkB=1, zorder=3 if not bifurcacion(a) else 3.5))


def leyenda(ax, loc="lower right", bbox=None):
    elems = [
        Line2D([], [], color=TINTA_2, lw=1.5, label="Remisión obligatoria"),
        Line2D([], [], color=TINTA_2, lw=1.1, ls=(0, (3, 2)), label="Opcional, orientativa o con voluntad"),
        Line2D([], [], color=NARANJA, lw=2.6, ls=(0, (3, 2)), label="Fiscal o juez → mediación (Res. 0383, art. 14)"),
        Patch(fc=AZUL_CLARO, ec=AZUL, label="Ofrece conciliación, mediación u otra vía alterna"),
        Patch(fc="white", ec=TINTA_2, label="Sin vía alterna en las fuentes"),
    ]
    ax.legend(handles=elems, loc=loc, bbox_to_anchor=bbox, frameon=False, fontsize=8.5,
              handlelength=2.6)


def figura_remisiones():
    fig, ax = plt.subplots(figsize=(13, 7.2))
    fondo(ax)
    for i in POS:
        nodo(ax, i)
    for a in fusionar(aristas):
        flecha(ax, a)
    fig.suptitle("Remisiones en el Leviatán: quién manda el caso a quién",
                 x=0.02, ha="left", fontsize=14, fontweight="bold", color=TINTA)
    fig.text(0.02, 0.915,
             f"{len(remisiones)} remisiones de mapa/remisiones.csv ({len(aristas)} flechas al separar "
             "los destinos múltiples). Toda la violencia intrafamiliar termina en el fiscal, "
             "y solo el fiscal o el juez abren la mediación.",
             fontsize=9, color=TINTA_2)
    leyenda(ax, loc="lower right", bbox=(1.0, -0.02))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.01)
    fig.savefig(SALIDA / "remisiones.png", dpi=200)
    plt.close(fig)


RUTAS = [
    ("vif", "Violencia intrafamiliar"),
    ("mujeres", "Violencia contra la mujer"),
    ("casas_justicia", "Casas de justicia"),
    ("alimentos", "Inasistencia alimentaria"),
    ("fiscalia", "Dentro de la Fiscalía"),
]


def figura_por_ruta():
    fig, axs = plt.subplots(3, 2, figsize=(14, 13.5))
    for ax, (ruta, titulo) in zip(axs.flat, RUTAS):
        fondo(ax)
        propias = [a for a in aristas if a["ruta"] == ruta]
        tocados = {x for a in propias for x in (a["o"], a["d"])}
        for i in POS:
            nodo(ax, i, activo=i in tocados, escala=1.0, fuente=6.3)
        for a in fusionar([a for a in aristas if a["ruta"] != ruta and not bifurcacion(a)]):
            flecha(ax, a, color=TENUE, lw=0.8, alfa=0.6)
        for a in fusionar(propias):
            flecha(ax, a)
        n = len({a["id"] for a in propias})
        ax.set_title(f"{titulo} · {n} remisiones", loc="left", fontsize=11.5,
                     fontweight="bold", color=TINTA, pad=4)
    ult = axs.flat[-1]
    ult.axis("off")
    leyenda(ult, loc="center")
    fig.suptitle("La misma red, una ruta por panel", x=0.02, ha="left", fontsize=14,
                 fontweight="bold", color=TINTA)
    fig.text(0.02, 0.955, "En gris claro, las remisiones de las otras rutas; atenuadas, las entidades que la ruta no toca.",
             fontsize=9, color=TINTA_2)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.93, bottom=0.01, hspace=0.12, wspace=0.03)
    fig.savefig(SALIDA / "remisiones-por-ruta.png", dpi=170)
    plt.close(fig)


MECANISMOS = [
    ("conciliacion_preprocesal", "Conciliación\npreprocesal"),
    ("mediacion", "Mediación"),
    ("principio_oportunidad", "Principio de\noportunidad"),
    ("conciliacion_reparacion", "Conciliación en\nla reparación"),
]


def mecanismos_de(e):
    """Lee la columna restaurativo de etapas.csv: devuelve {mecanismo: nota}."""
    out = {}
    for parte in e["restaurativo"].split("|"):
        parte = parte.strip()
        clave, _, nota = parte.partition(" ")
        nota = nota.strip(" ()")
        if clave == "conciliacion_preprocesal":
            out["conciliacion_preprocesal"] = nota
        elif clave == "mediacion":
            out["mediacion"] = nota
        elif clave == "principio_oportunidad":
            out["principio_oportunidad"] = nota
        elif clave in ("conciliacion_incidente", "conciliacion"):
            out["conciliacion_reparacion"] = nota
    return out


def figura_etapas():
    filas = [e for e in etapas if e["procedimiento"] == "ordinario"] + \
            [e for e in etapas if e["procedimiento"] == "abreviado"]
    n = len(filas)
    fig, ax = plt.subplots(figsize=(11.5, 9.4))
    ys = []
    y = 0
    for k, e in enumerate(filas):
        if k and e["procedimiento"] != filas[k - 1]["procedimiento"]:
            y += 0.9
        ys.append(y)
        y += 1
    for (e, yy) in zip(filas, ys):
        ax.text(-0.15, yy, f"{e['orden']}. {e['etapa']}", ha="right", va="center", fontsize=9, color=TINTA)
        ax.plot([0, len(MECANISMOS) - 1], [yy, yy], color=TENUE, lw=0.6, zorder=1)
        m = mecanismos_de(e)
        for j, (clave, _) in enumerate(MECANISMOS):
            if clave in m:
                ax.scatter(j, yy, s=150, color=AZUL, zorder=3, edgecolor=SUPERFICIE, linewidth=2)
                if m[clave]:
                    nota = textwrap.fill(m[clave].replace("<=", "≤"), 34)
                    ax.text(j, yy + 0.22, nota, fontsize=6.8, color=TINTA_2, va="top", ha="center",
                            linespacing=1.0)
    # Etiquetas de procedimiento
    corte = next(k for k, e in enumerate(filas) if e["procedimiento"] == "abreviado")
    ax.text(-4.3, ys[0] - 0.9, "ORDINARIO · Ley 906 de 2004", fontsize=8.5, fontweight="bold", color=TINTA_2)
    ax.text(-4.3, ys[corte] - 0.9, "ABREVIADO · Ley 1826 de 2017 (incluye la VIF desde la Ley 1959 de 2019)",
            fontsize=8.5, fontweight="bold", color=TINTA_2)
    for j, (_, nombre) in enumerate(MECANISMOS):
        ax.text(j, -1.6, nombre, ha="center", va="bottom", fontsize=9, color=TINTA, fontweight="bold")
    ax.set_xlim(-4.4, len(MECANISMOS) - 0.2)
    ax.set_ylim(ys[-1] + 0.9, -2.3)
    ax.axis("off")
    fig.suptitle("Dónde se abre la vía restaurativa en el proceso penal", x=0.02, ha="left",
                 fontsize=14, fontweight="bold", color=TINTA)
    fig.text(0.02, 0.935, "Cada punto es una salida restaurativa que la ley admite en esa etapa (mapa/etapas.csv). "
             "En el abreviado la mediación cabe hasta antes del fallo (art. 547).", fontsize=9, color=TINTA_2)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.02)
    fig.savefig(SALIDA / "etapas.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    figura_remisiones()
    figura_por_ruta()
    figura_etapas()
    print(f"{len(entidades)} entidades, {len(remisiones)} remisiones ({len(aristas)} flechas), "
          f"{len(etapas)} etapas -> {SALIDA.relative_to(AQUI.parent)}/")
