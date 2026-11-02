"""Genera las láminas BPMN del Leviatán.

    cd procesos && npm install && python3 generar.py

Por cada hoja escribe <nombre>.bpmn (BPMN 2.0, se abre en Bizagi Modeler, Camunda Modeler o
demo.bpmn.io) y ../figuras/<nombre>.svg (dibujado por bpmn-js con bpmn-to-image). Por cada
lámina con fuentes escribe además <lámina>-fuentes.md, con la fuente de cada actividad.
"""
import importlib
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).parent
FIGURAS = AQUI.parent / "figuras"
sys.path.insert(0, str(AQUI))
import bpmn  # noqa: E402

# (módulo, hojas, título del pool)
LAMINAS = [
    ("lamina_general", [("MODELO", "vista-general")], "Vista general tentativa de las rutas de acceso"),
    ("lamina_hipotesis", [("MODELO", "hipotesis")], "Hipótesis del equipo sobre el recorrido"),
    ("lamina_comisaria", [("HOJA_1", "comisaria-1"), ("HOJA_2", "comisaria-2"), ("HOJA_3", "comisaria-3")],
     "Comisaría de familia"),
    ("lamina_penal", [("HOJA_1", "proceso-penal-1"), ("HOJA_2", "proceso-penal-2")], "Proceso penal (Ley 906 de 2004)"),
    ("lamina_mediacion", [("MODELO", "mediacion-penal")], "Mediación penal (Resolución FGN 0383 de 2022)"),
]

for modulo, hojas, titulo in LAMINAS:
    mod = importlib.import_module(modulo)
    tablas = []
    for k, (attr, nombre) in enumerate(hojas, 1):
        m = getattr(mod, attr)
        pool = titulo if len(hojas) == 1 else f"{titulo}, hoja {k} de {len(hojas)}"
        bpmn.exportar(m, AQUI / f"{nombre}.bpmn", f"p_{nombre.replace('-', '_')}", pool)
        subprocess.run(["npx", "bpmn-to-image", "--no-footer", f"{nombre}.bpmn:{FIGURAS / nombre}.svg"],
                       cwd=AQUI, check=True, capture_output=True)
        if any(n[4] for n in m["nodos"].values()):
            tablas.append(bpmn.tabla_fuentes(m))
        print("ok", nombre)
    if tablas:
        cuerpo = tablas[0] + "".join("\n" + "\n".join(t.splitlines()[2:]) for t in tablas[1:])
        base = hojas[0][1].rsplit("-", 1)[0] if len(hojas) > 1 else hojas[0][1]
        (AQUI / f"{base}-fuentes.md").write_text(f"# {titulo}: fuente de cada actividad\n\n{cuerpo}\n", encoding="utf-8")
