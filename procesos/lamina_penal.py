"""Proceso penal (Ley 906 de 2004) y los puntos donde se abre una salida restaurativa, en dos hojas.

Naranja: la vía restaurativa (conciliación preprocesal y mediación). El detalle de la mediación
está en su propia lámina.
"""
L906 = "Ley 906 de 2004"
VICTIMA = ("victima", "Víctima", "arriba")

HOJA_1 = {
    "carriles": [("rec", "Recepción de denuncias (SAU, URI)"), ("con", "Conciliador"), ("fis", "Fiscal delegado")],
    "externos": [VICTIMA],
    "nodos": {
        "inicio": ("start", "rec", 0, "Denuncia o\nquerella", ""),
        "t1": ("task", "rec", 1, "Recibir la denuncia o querella", f"{L906}, arts. 67 a 69"),
        "g1": ("gateway", "fis", 2, "¿Delito\nquerellable?", ""),
        "t3": ("task", "con", 3, "Citar a conciliación preprocesal", f"{L906}, art. 522"),
        "g2": ("gateway", "con", 4, "¿Hay acuerdo?", ""),
        "fin_conc": ("end", "con", 5, "Se archiva por conciliación", ""),
        "t4": ("task", "fis", 5, "Adelantar la indagación", f"{L906}, art. 200"),
        "g3": ("gateway", "fis", 6, "¿Hay mérito?", ""),
        "fin_arch": ("end", "fis", 6, "Archivo de las diligencias", ""),
        "a_hoja2": ("link_out", "fis", 7, "Continúa en\nla hoja 2", ""),
    },
    "flujos": [
        ("victima", "inicio", "Denuncia o querella", "msg"),
        ("inicio", "t1"), ("t1", "g1"),
        ("g1", "t3", "Querellable"), ("t3", "g2"),
        ("g2", "fin_conc", "Sí"), ("g2", "t4", "No"),
        ("g1", "t4", "De oficio"),
        ("t4", "g3"), ("g3", "fin_arch", "No"), ("g3", "a_hoja2", "Sí"),
    ],
    "rutas": {("g2", "t4"): "hv"},
    "ajuste_y": {"fin_conc": -52, "fin_arch": 56},
    "etiqueta_derecha": {"fin_conc", "fin_arch"},
    "restaurativos": {"t3", "g2", "fin_conc"},
    "enlace": {"a_hoja2": "Imputación"},
}

HOJA_2 = {
    "num_inicio": 4,
    "carriles": [("con", "Mediador"), ("fis", "Fiscal delegado"), ("jue", "Juez de garantías o de conocimiento")],
    "externos": [VICTIMA],
    "nodos": {
        "de_hoja1": ("link_in", "fis", 0, "Viene de\nla hoja 1", ""),
        "t5": ("task", "fis", 1, "Formular la imputación ante el juez de garantías", f"{L906}, arts. 286 a 288 (abreviado: art. 536)"),
        "g4": ("gateway", "fis", 2, "¿Qué salida\naplica?", ""),
        "cm": ("subprocess", "con", 3, "Mediación penal", f"{L906}, arts. 523 a 527; Resolución FGN 0383 de 2022"),
        "g5": ("gateway", "con", 4, "¿Hay acuerdo?", ""),
        "t6": ("task", "con", 5, "Remitir el acta al fiscal, que la lleva al juez", "Resolución FGN 0383 de 2022, arts. 19 y 22"),
        "fin_med": ("end", "con", 6, "Acta ante el juez", ""),
        "t7": ("task", "jue", 3, "Control de legalidad del principio de oportunidad", f"{L906}, arts. 323 a 327"),
        "fin_op": ("end", "jue", 4, "Se suspende o extingue la acción", ""),
        "gm": ("gateway", "fis", 4, "", ""),
        "t8": ("task", "fis", 5, "Formular la acusación", f"{L906}, art. 336"),
        "t9": ("task", "jue", 5, "Juicio oral y sentencia", f"{L906}, libro III"),
        "t10": ("task", "jue", 6, "Incidente de reparación integral", f"{L906}, arts. 102 a 108"),
        "fin": ("end", "jue", 7, "Proceso terminado", ""),
        "n_med": ("note", "jue", 1, "Mediación: en el ordinario, desde la imputación hasta antes del juicio, con pena mínima de hasta 5 años, bien jurídico personal y aceptación expresa de ambas partes; en el abreviado, hasta antes del fallo (arts. 524 y 547)", ""),
    },
    "flujos": [
        ("de_hoja1", "t5"), ("t5", "g4"),
        ("g4", "cm", "Mediación", "restaurativo"),
        ("g4", "t7", "Oportunidad"), ("t7", "fin_op"),
        ("g4", "gm", "Ninguna"),
        ("cm", "g5"), ("g5", "t6", "Sí"), ("t6", "fin_med"),
        ("g5", "gm", "No"),
        ("gm", "t8"), ("t8", "t9"), ("t9", "t10"), ("t10", "fin"),
        ("victima", "cm", "Solicita la mediación", "msg"),
        ("t5", "n_med"),
    ],
    "restaurativos": {"cm", "g5", "t6", "fin_med"},
    "responsable": {"t5": "Fiscal delegado, ante el juez de control de garantías", "t7": "Juez de control de garantías",
                    "t9": "Juez de conocimiento", "t10": "Juez de conocimiento"},
    "enlace": {"de_hoja1": "Imputación"},
}
