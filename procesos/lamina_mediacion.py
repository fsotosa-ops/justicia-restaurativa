"""Mediación penal según la Resolución FGN 0383 de 2022 y la Ley 906 de 2004."""
R = "Resolución FGN 0383 de 2022"

MODELO = {
    "carriles": [("pro", "Programa de mediación con convenio"), ("fis", "Fiscal o juez")],
    "externos": [("partes", "Víctima e imputado o acusado", "arriba")],
    "nodos": {
        "inicio": ("start", "fis", 0, "Solicitud de\nmediación", ""),
        "t1": ("task", "fis", 1, "Evaluar si procede la mediación", f"{R}, art. 12; Ley 906 de 2004, arts. 524 y 525"),
        "g1": ("gateway", "fis", 2, "¿Procede?", ""),
        "fin_no": ("end", "fis", 2, "El proceso sigue", ""),
        "t2": ("task", "fis", 3, "Remitir el caso al programa por comunicación", f"{R}, art. 14"),
        "t3": ("task", "pro", 3, "Reuniones previas por separado (hasta 15 días)", f"{R}, art. 16, inc. 1"),
        "t4": ("task", "pro", 4, "Audiencia de mediación (hasta 7 días hábiles después)", f"{R}, art. 16"),
        "g2": ("gateway", "pro", 5, "¿Hay acuerdo?", ""),
        "fin_fr": ("end", "pro", 5, "Informe de fracaso al fiscal", ""),
        "t5": ("task", "pro", 6, "Remitir el acta al fiscal", f"{R}, art. 19"),
        "t6": ("task", "fis", 6, "Remitir el acta al juez", f"{R}, art. 22"),
        "fin": ("end", "fis", 7, "Acta ante el juez", ""),
        "n_vif": ("note", "pro", 1.6, "Violencia de género: no procede si el riesgo es grave o extremo (art. 12). Las reuniones previas van por separado en todos los casos (art. 16)", ""),
    },
    "flujos": [
        ("partes", "inicio", "Solicita (víctima o imputado)", "msg"),
        ("inicio", "t1"), ("t1", "g1"),
        ("g1", "fin_no", "No"), ("g1", "t2", "Sí"),
        ("t2", "t3"), ("t3", "t4"), ("t4", "g2"),
        ("g2", "t5", "Sí"), ("g2", "fin_fr", "No"),
        ("t5", "t6"), ("t6", "fin"),
        ("t3", "partes", "Citación", "msg"),
        ("t4", "partes", "Citación", "msg"),
        ("g1", "n_vif"),
    ],
    "ajuste_y": {"fin_no": 56, "fin_fr": 56},
    "etiqueta_derecha": {"fin_no", "fin_fr"},
    "restaurativos": {"t2", "t3", "t4", "g2", "t5", "t6", "fin"},
}
