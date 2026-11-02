"""Hipótesis del equipo sobre el recorrido de la vista general.

Cada anotación ubica una hipótesis (H1 a H6, documento de estado del arte del equipo, sección 4)
en el paso del recorrido donde actúa, con su veredicto tras la lectura completa (docs/01-estado-del-arte.md, Tabla 3).
"""
MODELO = {
    "carriles": [
        ("pue", "Puerta de entrada"),
        ("age", "Agente de orientación (propuesta)"),
        ("com", "Comisaría de familia"),
        ("fis", "Fiscalía y jueces"),
        ("con", "Conciliación y mediación"),
    ],
    "nodos": {
        "inicio": ("start", "pue", 0, "Consulta en consultorio\njurídico o casa de justicia", ""),
        "a1": ("task", "age", 1, "Preguntar por el conflicto, el rol y si hay un proceso abierto", ""),
        "gB": ("gateway", "age", 2.4, "¿Violencia\nintrafamiliar?", ""),
        "gC": ("gateway", "age", 3.6, "¿Es un delito?", ""),
        "fin_o": ("end", "age", 4.8, "Orientado a otra entidad", ""),
        "cC": ("subprocess", "com", 2.4, "Comisaría de familia", ""),
        "cP": ("subprocess", "fis", 4.8, "Proceso penal", ""),
        "fin_p": ("end", "fis", 6.6, "Sentencia o archivo", ""),
        "cM": ("subprocess", "con", 6.2, "Mediación penal", ""),
        "fin_m": ("end", "con", 7.4, "Acuerdo restaurativo", ""),
        "h1": ("note", "pue", 1.3, "H1 Comprensión: reformular. En los delitos, solo el 4% no actuó por no saber a dónde ir", ""),
        "h2": ("note", "pue", 2.6, "H2 Orientación: reformular. Con acompañamiento, el 80% recibió la ayuda que necesitaba; sin él, el 17%", ""),
        "h3": ("note", "pue", 3.9, "H3 Derivación: reformular. Triaje con las reglas de la Ley 906, no un modelo predictivo", ""),
        "h6": ("note", "com", 1, "H6 Gobernanza: se sostiene. El agente informa; deciden las personas", ""),
        "h4": ("note", "fis", 5.8, "H4 Eficiencia: se sostiene, pero el estudio casi no incluyó violencia intrafamiliar", ""),
        "h5": ("note", "fis", 7.6, "H5 Resultados: reformular. Satisfacción robusta; la reincidencia baja poco", ""),
    },
    "flujos": [
        ("inicio", "a1"), ("a1", "gB"),
        ("gB", "cC", "Sí"), ("gB", "gC", "No"),
        ("gC", "fin_o", "No"), ("gC", "cP", "Sí"),
        ("cC", "cP", "Denuncia"),
        ("cP", "cM", "Remisión del fiscal o el juez", "restaurativo"),
        ("cP", "fin_p"), ("cM", "fin_m"),
        ("inicio", "h1"), ("a1", "h2"), ("gB", "h3"), ("a1", "h6"), ("cM", "h4"), ("fin_m", "h5"),
    ],
    "rutas": {("gC", "cP"): "hv"},
    "ajuste_y": {"fin_o": -52, "inicio": 12, "h1": 12, "h4": -42},
    "etiqueta_derecha": {"fin_o"},
    "etiqueta_arriba": {"inicio"},
    "restaurativos": {"cM", "fin_m"},
    "pendientes": {"a1", "gB", "gC", "fin_o"},
}
