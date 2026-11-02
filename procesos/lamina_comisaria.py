"""Recepción de un caso de violencia en el contexto familiar en una comisaría de familia, en tres hojas.

Fuente: Ministerio de Justicia y del Derecho y PNUD (2022). Modelos de justicia local y rural, Tomo V:
Lineamientos para el servicio de atención en comisarías de familia. Fase 1 (Tabla 2, pp. 17-22) y
fase 2 (pp. 23-26). Las actividades 9 a 19 de la fase 2 y las fases 3 a 8 quedan colapsadas como una actividad de llamada.
"""
T5 = "MinJusticia y PNUD (2022), Tomo V"
PERSONA = ("persona", "Persona usuaria", "arriba")

HOJA_1 = {
    "carriles": [("com", "Comisario(a) y sustanciador"), ("seg", "Personal de seguridad"), ("pro", "Profesional de recepción")],
    "externos": [PERSONA],
    "nodos": {
        "inicio": ("start", "seg", 0, "Llega una persona\na la comisaría", ""),
        "t1": ("task", "seg", 1, "Registrar el ingreso", f"{T5}, fase 1, act. 1, p. 17"),
        "t2": ("task", "pro", 2, "Registrar la información básica", f"{T5}, fase 1, act. 2, p. 18"),
        "t3": ("task", "pro", 3, "Indagar el motivo de consulta", f"{T5}, fase 1, act. 3, p. 18"),
        "g1": ("gateway", "pro", 4, "¿Es competencia\nde la comisaría?", ""),
        "t4": ("task", "com", 5, "Remitir por oficio a la entidad competente", f"{T5}, fase 1, act. 4, pp. 18-19"),
        "fin_remitido": ("end", "com", 6, "Caso remitido", ""),
        "a_hoja2": ("link_out", "pro", 5, "Continúa en\nla hoja 2", ""),
    },
    "flujos": [
        ("persona", "inicio", "Solicita atención", "msg"),
        ("inicio", "t1"), ("t1", "t2"), ("t2", "t3"), ("t3", "g1"),
        ("g1", "t4", "No"), ("t4", "fin_remitido"),
        ("t4", "persona", "Oficio remisorio", "msg"),
        ("g1", "a_hoja2", "Sí"),
    ],
    "enlace": {"a_hoja2": "Valoración"},
    "responsable": {"t4": "Sustanciador (abogado) o comisario(a)"},
}

HOJA_2 = {
    "num_inicio": 5,
    "carriles": [("pro", "Profesional de recepción")],
    "nodos": {
        "de_hoja1": ("link_in", "pro", 0, "Viene de\nla hoja 1", ""),
        "t5": ("task", "pro", 1, "Valoración inicial psicológica y emocional", f"{T5}, fase 1, act. 5, p. 19"),
        "t6": ("task", "pro", 2, "Identificar el riesgo", f"{T5}, fase 1, act. 6, p. 19"),
        "t7": ("task", "pro", 3, "Iniciar la solicitud de medida de protección", f"{T5}, fase 1, act. 7, pp. 19-20"),
        "t8": ("task", "pro", 4, "Abrir el trámite en el sistema", f"{T5}, fase 1, act. 10, p. 21"),
        "t9": ("task", "pro", 5, "Verificar el nivel del riesgo", f"{T5}, fase 1, act. 13, p. 22"),
        "t10": ("task", "pro", 6, "Elaborar el informe de la entrevista", f"{T5}, fase 1, act. 14, p. 22"),
        "a_hoja3": ("link_out", "pro", 7, "Continúa en\nla hoja 3", ""),
    },
    "flujos": [("de_hoja1", "t5"), ("t5", "t6"), ("t6", "t7"), ("t7", "t8"), ("t8", "t9"), ("t9", "t10"), ("t10", "a_hoja3")],
    "enlace": {"de_hoja1": "Valoración", "a_hoja3": "Medidas provisionales"},
    "responsable": {"t8": "Profesional de recepción o secretario(a) del despacho"},
}

HOJA_3 = {
    "num_inicio": 11,
    "carriles": [("com", "Comisario(a) de familia"), ("sec", "Secretaría del despacho")],
    "externos": [PERSONA, ("entidades", "Entidades de la ruta (Fiscalía, Policía, Medicina Legal, Secretaría de la Mujer)", "abajo")],
    "nodos": {
        "de_hoja2": ("link_in", "sec", 0, "Viene de\nla hoja 2", ""),
        "t11": ("task", "sec", 1, "Proyectar auto que avoca conocimiento y decreta medidas provisionales", f"{T5}, fase 2, act. 1, p. 23"),
        "g2": ("gateway", "com", 2, "¿El auto está\nconforme?", ""),
        "t12": ("task", "sec", 3, "Diligenciar el formato de denuncia", f"{T5}, fase 2, act. 4, p. 24"),
        "t13": ("task", "sec", 4, "Elaborar los oficios de la medida", f"{T5}, fase 2, act. 5, p. 24"),
        "t14": ("task", "sec", 5, "Elaborar las notificaciones", f"{T5}, fase 2, act. 7, p. 24"),
        "sp": ("subprocess", "com", 6, "Pruebas, audiencia, medida definitiva y seguimiento",
               f"{T5}, fase 2 (acts. 9 a 19) y fases 3 a 8, desde p. 24"),
        "fin": ("end", "com", 7, "Medida cerrada", ""),
        "n_med": ("note", "sec", 6.6, "La comisaría no remite a mediación penal: solo el fiscal o el juez (Res. 0383 de 2022, art. 14)", ""),
    },
    "flujos": [
        ("de_hoja2", "t11"), ("t11", "g2"),
        ("g2", "t11", "No"), ("g2", "t12", "Sí"), ("t12", "t13"), ("t13", "t14"),
        ("t12", "entidades", "Denuncia", "msg"), ("t13", "entidades", "Oficios", "msg"),
        ("t14", "persona", "Notificación (act. 8)", "msg", -30),
        ("t14", "sp"), ("sp", "fin"),
        ("n_med", "entidades"),
    ],
    "rutas": {("t11", "g2"): "hv", ("g2", "t11"): "hv", ("g2", "t12"): "hv"},
    "enlace": {"de_hoja2": "Medidas provisionales"},
    "responsable": {"t11": "Secretario(a) del despacho (abogado)"},
}
