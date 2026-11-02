"""Lámina 2. Recepción de un caso de violencia en el contexto familiar en una comisaría de familia.

Fuente: Ministerio de Justicia y del Derecho (2022). Modelos de justicia local y rural, Tomo V:
Lineamientos para el servicio de atención en comisarías de familia. Fase 1 (Tabla 2, pp. 17-22) y
Fase 2 (pp. 23-24). Las fases 3 a 8 quedan colapsadas como subprocesos.
"""
T5 = "MinJusticia (2022), Tomo V"

MODELO = {
    "carriles": [
        ("com", "Comisario(a) de familia"),
        ("seg", "Personal de seguridad"),
        ("pro", "Profesional de recepción"),
        ("sec", "Secretaría del despacho"),
    ],
    "externos": [
        ("persona", "Persona usuaria", "arriba"),
        ("entidades", "Entidades de la ruta (Fiscalía, Policía, Medicina Legal, Secretaría de la Mujer)", "abajo"),
    ],
    "nodos": {
        "inicio": ("start", "seg", 0, "Llega una persona\na la comisaría", ""),
        "t1": ("task", "seg", 1, "Registrar el ingreso", f"{T5}, fase 1, act. 1, p. 17"),
        "t2": ("task", "pro", 2, "Registrar la información básica", f"{T5}, fase 1, act. 2, p. 18"),
        "t3": ("task", "pro", 3, "Indagar el motivo de consulta", f"{T5}, fase 1, act. 3, p. 18"),
        "g1": ("gateway", "pro", 4, "¿Es competencia\nde la comisaría?", ""),
        "t4": ("task", "com", 5, "Remitir por oficio a la entidad competente", f"{T5}, fase 1, act. 4, pp. 18-19"),
        "fin_remitido": ("end", "com", 6, "Caso remitido", ""),
        "t5": ("task", "pro", 5, "Valoración inicial psicológica y emocional", f"{T5}, fase 1, act. 5, p. 19"),
        "t6": ("task", "pro", 6, "Identificar el riesgo", f"{T5}, fase 1, act. 6, p. 19"),
        "t7": ("task", "pro", 7, "Iniciar la solicitud de medida de protección", f"{T5}, fase 1, act. 7, p. 19"),
        "t8": ("task", "pro", 8, "Abrir el trámite en el sistema", f"{T5}, fase 1, act. 10, p. 21"),
        "t9": ("task", "pro", 9, "Verificar el nivel del riesgo", f"{T5}, fase 1, act. 13, p. 22"),
        "t10": ("task", "pro", 10, "Elaborar el informe de la entrevista", f"{T5}, fase 1, act. 14, p. 22"),
        "t11": ("task", "sec", 11, "Proyectar auto que avoca conocimiento y decreta medidas provisionales",
                f"{T5}, fase 2, act. 1, p. 23"),
        "g2": ("gateway", "com", 12, "¿El auto está\nconforme?", ""),
        "t12": ("task", "sec", 13, "Diligenciar el formato de denuncia", f"{T5}, fase 2, act. 4, p. 24"),
        "t13": ("task", "sec", 14, "Elaborar los oficios de la medida", f"{T5}, fase 2, act. 5, p. 24"),
        "t14": ("task", "sec", 15, "Notificar a las partes", f"{T5}, fase 2, act. 7 y 8, p. 24"),
        "sp1": ("subprocess", "com", 16, "Medidas de atención, audiencia y medida definitiva",
                f"{T5}, fases 3 a 5, pp. 26-43"),
        "sp2": ("subprocess", "com", 17, "Seguimiento, incumplimiento y levantamiento", f"{T5}, fases 6 a 8, desde p. 44"),
        "fin": ("end", "com", 18, "Medida cerrada", ""),
        "n_nna": ("note", "seg", 8, "Con niños, niñas o adolescentes: verificar sus derechos y pedir consentimiento (act. 8, 9, 11 y 12)", ""),
        "n_med": ("note", "pro", 14, "La comisaría no remite a mediación penal: solo el fiscal o el juez (Res. 0383 de 2022, art. 14)", ""),
    },
    "flujos": [
        ("persona", "inicio", "Solicita atención", "msg"),
        ("inicio", "t1"), ("t1", "t2"), ("t2", "t3"), ("t3", "g1"),
        ("g1", "t4", "No"), ("t4", "fin_remitido"),
        ("t4", "persona", "Oficio remisorio", "msg"),
        ("g1", "t5", "Sí"), ("t5", "t6"), ("t6", "t7"), ("t7", "t8"), ("t8", "t9"), ("t9", "t10"),
        ("t10", "t11"), ("t11", "g2"),
        ("g2", "t11", "No"),
        ("g2", "t12", "Sí"), ("t12", "t13"), ("t13", "t14"),
        ("t12", "entidades", "Denuncia", "msg"),
        ("t13", "entidades", "Oficios", "msg"),
        ("t14", "persona", "Notificación", "msg", -40),
        ("t14", "sp1"), ("sp1", "sp2"), ("sp2", "fin"),
        ("t8", "n_nna"), ("t12", "n_med"),
    ],
    "rutas": {("t11", "g2"): "hv", ("g2", "t11"): "hv", ("g2", "t12"): "hv"},
}
