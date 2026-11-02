"""Lámina 1. Vista general tentativa: por dónde entra una persona y dónde se abre la vía restaurativa.

Es la lámina base para validar con el equipo. En gris va lo que propone el proyecto (el agente y
sus preguntas, tomadas de las reuniones de octubre de 2026); en naranja, la vía restaurativa.
Cada actividad con el marcador de llamada se detalla en su propia lámina.
"""
PROPUESTA = "Propuesta del equipo, por validar"

MODELO = {
    "carriles": [
        ("pue", "Puerta de entrada"),
        ("age", "Agente de orientación (propuesta)"),
        ("com", "Comisaría de familia"),
        ("fis", "Fiscalía y jueces"),
        ("con", "Conciliación y mediación"),
    ],
    "externos": [("persona", "Persona con un conflicto", "arriba")],
    "nodos": {
        "inicio": ("start", "pue", 0, "Consulta en consultorio\njurídico o casa de justicia", ""),
        "a1": ("task", "age", 1, "Preguntar por el conflicto, el rol y si hay un proceso abierto", PROPUESTA),
        "gB": ("gateway", "age", 2, "¿Violencia\nintrafamiliar?", ""),
        "gC": ("gateway", "age", 3, "¿Es un delito?", ""),
        "fin_o": ("end", "age", 4, "Orientado a otra entidad", ""),
        "cC": ("subprocess", "com", 2, "Comisaría de familia (lámina 2)", "MinJusticia (2022), Tomo V"),
        "cP": ("subprocess", "fis", 4, "Proceso penal (lámina 3)", "Ley 906 de 2004"),
        "cM": ("subprocess", "con", 5, "Mediación penal (lámina 4)", "Resolución FGN 0383 de 2022"),
        "fin_p": ("end", "fis", 6, "Sentencia o archivo", ""),
        "fin_m": ("end", "con", 6, "Acuerdo restaurativo", ""),
        "n_q": ("note", "con", 3, "En delitos querellables, el proceso penal empieza por la conciliación preprocesal (Ley 906, art. 522)", ""),
        "n_a": ("note", "pue", 2, "Preguntas de las reuniones del equipo: tipo de conflicto, si ya hay proceso y si la persona es víctima o señalada", ""),
    },
    "flujos": [
        ("persona", "inicio", "Consulta", "msg"),
        ("inicio", "a1"), ("a1", "gB"),
        ("gB", "cC", "Sí"), ("gB", "gC", "No"),
        ("gC", "fin_o", "No"), ("gC", "cP", "Sí"),
        ("cC", "cP", "Denuncia"),
        ("cP", "cM", "Remisión del fiscal o el juez", "restaurativo"),
        ("cP", "fin_p"), ("cM", "fin_m"),
        ("cP", "n_q"), ("a1", "n_a"),
    ],
    "rutas": {("gC", "cP"): "hv"},
    "ajuste_y": {"fin_o": -52},
    "etiqueta_derecha": {"fin_o", "inicio"},
    "restaurativos": {"cM", "fin_m"},
    "pendientes": {"a1", "gB", "gC", "fin_o"},
}
