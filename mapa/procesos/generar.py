"""Genera las láminas BPMN del Leviatán.

    python3 mapa/procesos/generar.py

Por cada lámina escribe <nombre>.bpmn (BPMN 2.0, se abre en Bizagi Modeler, Camunda Modeler
o demo.bpmn.io), <nombre>.svg (dibujado por bpmn-js con bpmn-to-image) y <nombre>-fuentes.md
(tabla de actividades con su fuente). Requiere `npm install` en esta carpeta.
"""
import importlib
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI))
import bpmn  # noqa: E402

LAMINAS = [
    ("lamina_general", "vista-general", "Leviatán: vista general tentativa de las rutas de acceso"),
    ("lamina_hipotesis", "hipotesis", "Hipótesis del equipo sobre el recorrido"),
    ("lamina_comisaria", "comisaria", "Comisaría de familia: recepción de un caso de violencia en el contexto familiar"),
    ("lamina_penal", "proceso-penal", "Proceso penal (Ley 906 de 2004) y salidas restaurativas"),
    ("lamina_mediacion", "mediacion-penal", "Mediación penal (Resolución FGN 0383 de 2022)"),
]

for modulo, nombre, titulo in LAMINAS:
    m = importlib.import_module(modulo).MODELO
    destino = AQUI / nombre
    bpmn.exportar(m, f"{destino}.bpmn", f"p_{nombre}", titulo)
    (AQUI / f"{nombre}-fuentes.md").write_text(bpmn.tabla_fuentes(m) + "\n", encoding="utf-8")
    subprocess.run(["npx", "bpmn-to-image", "--no-footer", f"{destino}.bpmn:{destino}.svg"],
                   cwd=AQUI, check=True)
    print("ok", nombre)
