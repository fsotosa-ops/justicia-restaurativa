"""Genera archivos BPMN 2.0 (XML con diagrama) a partir de un modelo escrito como datos.

El dibujo no se hace aquí: el .bpmn se convierte a SVG con bpmn-to-image, que usa bpmn-js,
el mismo motor de Camunda Modeler y bpmn.io (ver generar.py). Así la lámina del README es
idéntica a la que se ve al abrir el archivo en Bizagi Modeler, Camunda Modeler o demo.bpmn.io.

Modelo:
  carriles: [(id, nombre)]                 un carril por actor, de arriba hacia abajo
  nodos:    {id: (tipo, carril, columna, texto, fuente)}
            tipo: start, end, task, subprocess, gateway, note
            las actividades (task, subprocess) se numeran en el orden en que aparecen
  flujos:   [(origen, destino, etiqueta)]  flujo de secuencia; si el destino es una nota,
            se dibuja como asociación
            (origen, destino, etiqueta, "msg", dx) es un flujo de mensaje hacia o desde un
            participante externo; dx desplaza la flecha en horizontal
  externos: [(id, nombre, "arriba"|"abajo")]  participantes externos como pools colapsados
  rutas:    {(origen, destino): "hv"}      la flecha sale por el costado y entra por arriba o abajo
  restaurativos: {ids}                     se pintan en naranja (vía restaurativa)
  pendientes:    {ids}                     se pintan en gris punteado (sin fuente oficial)
"""
from xml.sax.saxutils import escape

COL = 170          # ancho de columna
LANE_H = 160       # alto de carril
POOL_LABEL = 30    # franja del nombre del pool
LANE_X = POOL_LABEL
X0 = POOL_LABEL + 90
TASK_W, TASK_H = 120, 80
GW = 50
EV = 36
NOTE_W, NOTE_H = 190, 74

EXT_H, EXT_GAP = 60, 50  # pools externos colapsados

NARANJA, NARANJA_CLARO = "#c4501c", "#fde6dc"
GRIS, GRIS_CLARO = "#8a8984", "#f1f0ec"


def numerar(m):
    """Devuelve {id: n} para actividades, en el orden del modelo."""
    n, out = 0, {}
    for nid, nodo in m["nodos"].items():
        if nodo[0] in ("task", "subprocess"):
            n += 1
            out[nid] = n
    return out


def _tam(tipo):
    return {"task": (TASK_W, TASK_H), "subprocess": (TASK_W, TASK_H), "gateway": (GW, GW),
            "note": (NOTE_W, NOTE_H)}.get(tipo, (EV, EV))


def _y0(m):
    return sum(EXT_H + EXT_GAP for e in m.get("externos", []) if e[2] == "arriba")


def _centro(m, nid):
    tipo, carril, col = m["nodos"][nid][:3]
    i = [c for c, _ in m["carriles"]].index(carril)
    dy = m.get("ajuste_y", {}).get(nid, 0)
    return X0 + col * COL, _y0(m) + i * LANE_H + LANE_H / 2 + dy, tipo


def _ext_y(m, eid):
    """Borde superior e inferior del pool externo."""
    arriba = [e for e in m.get("externos", []) if e[2] == "arriba"]
    abajo = [e for e in m.get("externos", []) if e[2] == "abajo"]
    H = len(m["carriles"]) * LANE_H
    for k, e in enumerate(arriba):
        if e[0] == eid:
            top = k * (EXT_H + EXT_GAP)
            return top, top + EXT_H, "arriba"
    for k, e in enumerate(abajo):
        if e[0] == eid:
            top = _y0(m) + H + EXT_GAP + k * (EXT_H + EXT_GAP)
            return top, top + EXT_H, "abajo"
    raise KeyError(eid)


def _ruta_msg(m, a, b, dx=0):
    ext = {e[0] for e in m.get("externos", [])}
    nodo, pool = (b, a) if a in ext else (a, b)
    top, bot, lado = _ext_y(m, pool)
    x, y, tipo = _centro(m, nodo)
    w, h = _tam(tipo)
    if lado == "arriba":
        pn, pp = (x + dx, y - h / 2), (x + dx, bot)
    else:
        pn, pp = (x + dx, y + h / 2), (x + dx, top)
    return [pp, pn] if a in ext else [pn, pp]


def _borde(m, nid, dx, dy):
    x, y, tipo = _centro(m, nid)
    w, h = _tam(tipo)
    return (x + dx * w / 2, y) if dx else (x, y + dy * h / 2)


def _ruta(m, a, b):
    """Ruta ortogonal entre dos nodos."""
    ax, ay, _ = _centro(m, a)
    bx, by, tb = _centro(m, b)
    if tb == "note":
        if abs(ay - by) < 1:  # misma altura: asociación horizontal
            d = 1 if bx > ax else -1
            return [_borde(m, a, d, 0), _borde(m, b, -d, 0)]
        return [_borde(m, a, 0, -1 if by < ay else 1), _borde(m, b, 0, 1 if by < ay else -1)]
    if m.get("rutas", {}).get((a, b)) == "hv":
        p0 = _borde(m, a, 1 if bx > ax else -1, 0)
        p2 = _borde(m, b, 0, 1 if ay > by else -1)
        return [p0, (p2[0], p0[1]), p2]
    if abs(ay - by) < 1:
        if bx > ax:
            return [_borde(m, a, 1, 0), _borde(m, b, -1, 0)]
        # vuelta atrás en el mismo carril: por debajo de los nodos
        p0, p3 = _borde(m, a, 0, 1), _borde(m, b, 0, 1)
        yb = ay + LANE_H * 0.40
        return [p0, (p0[0], yb), (p3[0], yb), p3]
    s = 1 if by > ay else -1
    if abs(bx - ax) < 1:
        return [_borde(m, a, 0, s), _borde(m, b, 0, -s)]
    if bx < ax:
        # vuelve hacia la izquierda en otro carril: sale vertical y entra por arriba o abajo
        p0, p2 = _borde(m, a, 0, s), _borde(m, b, 0, -s)
        ym = (p0[1] + p2[1]) / 2
        return [p0, (p0[0], ym), (p2[0], ym), p2]
    p0, p2 = _borde(m, a, 0, s), _borde(m, b, -1, 0)
    return [p0, (p0[0], p2[1]), p2]


def exportar(m, ruta, pid, nombre):
    tags = {"start": "startEvent", "end": "endEvent", "task": "task", "gateway": "exclusiveGateway",
            "subprocess": "callActivity"}
    num = numerar(m)
    carriles = m["carriles"]
    ncol = max(n[2] for n in m["nodos"].values()) + 1
    W = X0 + (ncol - 1) * COL + max(TASK_W, NOTE_W) / 2 + 50
    H = len(carriles) * LANE_H
    Y0 = _y0(m)
    notas = {k for k, n in m["nodos"].items() if n[0] == "note"}
    mensajes = [f for f in m["flujos"] if len(f) > 3 and f[3] == "msg"]
    secuencia = [f for f in m["flujos"] if f[1] not in notas and f not in mensajes]
    asociaciones = [f for f in m["flujos"] if f[1] in notas]
    ent, sal = {}, {}
    for k, f in enumerate(secuencia):
        sal.setdefault(f[0], []).append(f"f{k}")
        ent.setdefault(f[1], []).append(f"f{k}")

    def nombre_de(nid):
        tipo, _, _, texto, _ = m["nodos"][nid]
        texto = texto.replace("\n", " ")
        return f"{num[nid]}. {texto}" if nid in num else texto

    L = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
         'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
         'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
         'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
         'xmlns:bioc="http://bpmn.io/schema/bpmn/biocolor/1.0" '
         'xmlns:color="http://www.omg.org/spec/BPMN/non-normative/color/1.0" '
         f'id="def_{pid}" targetNamespace="https://github.com/fsotosa-ops/justicia-restaurativa" '
         'exporter="justicia-restaurativa/mapa/procesos/bpmn.py" exporterVersion="1">',
         f'  <bpmn:collaboration id="col_{pid}">',
         f'    <bpmn:participant id="pool_{pid}" name="{escape(nombre)}" processRef="{pid}"/>']
    for eid, en, _ in m.get("externos", []):
        L.append(f'    <bpmn:participant id="{eid}" name="{escape(en)}"/>')
    for k, f in enumerate(mensajes):
        nm = f' name="{escape(f[2])}"' if f[2] else ""
        L.append(f'    <bpmn:messageFlow id="mf{k}" sourceRef="{f[0]}" targetRef="{f[1]}"{nm}/>')
    L += ['  </bpmn:collaboration>',
          f'  <bpmn:process id="{pid}" name="{escape(nombre)}" isExecutable="false">',
          f'    <bpmn:laneSet id="ls_{pid}">']
    for cid, cn in carriles:
        L.append(f'      <bpmn:lane id="lane_{cid}" name="{escape(cn)}">')
        L += [f'        <bpmn:flowNodeRef>{nid}</bpmn:flowNodeRef>'
              for nid, n in m["nodos"].items() if n[1] == cid and n[0] != "note"]
        L.append('      </bpmn:lane>')
    L.append('    </bpmn:laneSet>')
    for nid, (tipo, carril, col, texto, fuente) in m["nodos"].items():
        if tipo == "note":
            L.append(f'    <bpmn:textAnnotation id="{nid}"><bpmn:text>{escape(texto.replace(chr(10), " "))}</bpmn:text></bpmn:textAnnotation>')
            continue
        t = tags[tipo]
        L.append(f'    <bpmn:{t} id="{nid}" name="{escape(nombre_de(nid))}">')
        if fuente:
            L.append(f'      <bpmn:documentation>Fuente: {escape(fuente)}</bpmn:documentation>')
        if tipo == "start" and any(f[1] == nid for f in mensajes):
            L.append(f'      <bpmn:messageEventDefinition id="med_{nid}"/>')
        L += [f'      <bpmn:incoming>{e}</bpmn:incoming>' for e in ent.get(nid, [])]
        L += [f'      <bpmn:outgoing>{s}</bpmn:outgoing>' for s in sal.get(nid, [])]
        L.append(f'    </bpmn:{t}>')
    for k, f in enumerate(secuencia):
        nm = f' name="{escape(f[2])}"' if len(f) > 2 and f[2] else ""
        L.append(f'    <bpmn:sequenceFlow id="f{k}" sourceRef="{f[0]}" targetRef="{f[1]}"{nm}/>')
    for k, f in enumerate(asociaciones):
        L.append(f'    <bpmn:association id="asoc{k}" sourceRef="{f[0]}" targetRef="{f[1]}"/>')
    L.append('  </bpmn:process>')

    # Diagrama
    L.append(f'  <bpmndi:BPMNDiagram id="dia_{pid}">')
    L.append(f'    <bpmndi:BPMNPlane id="pl_{pid}" bpmnElement="col_{pid}">')
    L.append(f'      <bpmndi:BPMNShape id="s_pool" bpmnElement="pool_{pid}" isHorizontal="true">'
             f'<dc:Bounds x="0" y="{Y0}" width="{W:.0f}" height="{H}"/></bpmndi:BPMNShape>')
    for eid, _, _ in m.get("externos", []):
        top, _, _ = _ext_y(m, eid)
        L.append(f'      <bpmndi:BPMNShape id="s_{eid}" bpmnElement="{eid}" isHorizontal="true">'
                 f'<dc:Bounds x="0" y="{top:.0f}" width="{W:.0f}" height="{EXT_H}"/></bpmndi:BPMNShape>')
    for i, (cid, _) in enumerate(carriles):
        L.append(f'      <bpmndi:BPMNShape id="s_lane_{cid}" bpmnElement="lane_{cid}" isHorizontal="true">'
                 f'<dc:Bounds x="{LANE_X}" y="{Y0 + i * LANE_H}" width="{W - LANE_X:.0f}" height="{LANE_H}"/></bpmndi:BPMNShape>')
    for nid, n in m["nodos"].items():
        x, y, tipo = _centro(m, nid)
        w, h = _tam(tipo)
        color = ""
        if nid in m.get("restaurativos", ()):
            color = f' bioc:stroke="{NARANJA}" bioc:fill="{NARANJA_CLARO}" color:border-color="{NARANJA}" color:background-color="{NARANJA_CLARO}"'
        elif nid in m.get("pendientes", ()):
            color = f' bioc:stroke="{GRIS}" bioc:fill="{GRIS_CLARO}" color:border-color="{GRIS}" color:background-color="{GRIS_CLARO}"'
        extra = ""
        L.append(f'      <bpmndi:BPMNShape id="s_{nid}" bpmnElement="{nid}"{extra}{color}>'
                 f'<dc:Bounds x="{x - w / 2:.0f}" y="{y - h / 2:.0f}" width="{w}" height="{h}"/>')
        if tipo in ("start", "end", "gateway"):
            # etiqueta externa: bajo los eventos, sobre las compuertas
            lw = 110
            if nid in m.get("etiqueta_arriba", ()):
                L.append(f'        <bpmndi:BPMNLabel><dc:Bounds x="{x - lw / 2:.0f}" y="{y - h / 2 - 42:.0f}" width="{lw}" height="28"/></bpmndi:BPMNLabel>')
                L.append('      </bpmndi:BPMNShape>')
                continue
            if nid in m.get("etiqueta_derecha", ()):
                L.append(f'        <bpmndi:BPMNLabel><dc:Bounds x="{x + w / 2 + 6:.0f}" y="{y - 14:.0f}" width="90" height="28"/></bpmndi:BPMNLabel>')
                L.append('      </bpmndi:BPMNShape>')
                continue
            extremos = [p for f in secuencia + asociaciones for p in (_ruta(m, f[0], f[1])[0], _ruta(m, f[0], f[1])[-1])]
            usa_arriba = any(abs(px - x) < 1 and abs(py - (y - h / 2)) < 1 for px, py in extremos)
            usa_abajo = any(abs(px - x) < 1 and abs(py - (y + h / 2)) < 1 for px, py in extremos)
            if tipo == "gateway" and usa_arriba and usa_abajo:
                # ambos lados ocupados: etiqueta arriba a la izquierda
                L.append(f'        <bpmndi:BPMNLabel><dc:Bounds x="{x - lw - 4:.0f}" y="{y - h / 2 - 30:.0f}" width="{lw}" height="28"/></bpmndi:BPMNLabel>')
                L.append('      </bpmndi:BPMNShape>')
                continue
            ly = y - h / 2 - 34 if tipo == "gateway" and not usa_arriba else y + h / 2 + 6
            L.append(f'        <bpmndi:BPMNLabel><dc:Bounds x="{x - lw / 2:.0f}" y="{ly:.0f}" width="{lw}" height="28"/></bpmndi:BPMNLabel>')
        L.append('      </bpmndi:BPMNShape>')
    for k, f in enumerate(secuencia):
        pts = _ruta(m, f[0], f[1])
        wp = "".join(f'<di:waypoint x="{px:.0f}" y="{py:.0f}"/>' for px, py in pts)
        color = ""
        if f[0] in m.get("restaurativos", ()) and f[1] in m.get("restaurativos", ()) or (len(f) > 3 and f[3] == "restaurativo"):
            color = f' bioc:stroke="{NARANJA}" color:border-color="{NARANJA}"'
        lab = ""
        if len(f) > 2 and f[2]:
            (xa, ya), (xb, yb) = pts[0], pts[1]
            lx, ly = (xa + xb) / 2, (ya + yb) / 2
            if abs(xa - xb) < 1:   # tramo vertical: etiqueta a la derecha
                lab = f'<bpmndi:BPMNLabel><dc:Bounds x="{lx + 5:.0f}" y="{ly - 8:.0f}" width="70" height="14"/></bpmndi:BPMNLabel>'
            else:                  # tramo horizontal: etiqueta encima
                lab = f'<bpmndi:BPMNLabel><dc:Bounds x="{lx - 30:.0f}" y="{ly - 18:.0f}" width="60" height="14"/></bpmndi:BPMNLabel>'
        L.append(f'      <bpmndi:BPMNEdge id="e_f{k}" bpmnElement="f{k}"{color}>{wp}{lab}</bpmndi:BPMNEdge>')
    for k, f in enumerate(mensajes):
        pts = _ruta_msg(m, f[0], f[1], f[4] if len(f) > 4 else 0)
        wp = "".join(f'<di:waypoint x="{px:.0f}" y="{py:.0f}"/>' for px, py in pts)
        lab = ""
        if f[2]:
            (xa, ya), (xb, yb) = pts
            lab = f'<bpmndi:BPMNLabel><dc:Bounds x="{xa + 6:.0f}" y="{(ya + yb) / 2 - 7:.0f}" width="90" height="14"/></bpmndi:BPMNLabel>'
        L.append(f'      <bpmndi:BPMNEdge id="e_mf{k}" bpmnElement="mf{k}">{wp}{lab}</bpmndi:BPMNEdge>')
    for k, f in enumerate(asociaciones):
        wp = "".join(f'<di:waypoint x="{px:.0f}" y="{py:.0f}"/>' for px, py in _ruta(m, f[0], f[1]))
        L.append(f'      <bpmndi:BPMNEdge id="e_asoc{k}" bpmnElement="asoc{k}">{wp}</bpmndi:BPMNEdge>')
    L.append('    </bpmndi:BPMNPlane>')
    L.append('  </bpmndi:BPMNDiagram>')
    L.append('</bpmn:definitions>')
    open(ruta, "w", encoding="utf-8").write("\n".join(L) + "\n")


def tabla_fuentes(m):
    """Tabla en Markdown: número, actividad, responsable y fuente."""
    num = numerar(m)
    carril = dict(m["carriles"])
    filas = ["| N.º | Actividad | Responsable | Fuente |", "|---|---|---|---|"]
    for nid, n in m["nodos"].items():
        if nid in num:
            fuente = n[4] or "Sin fuente oficial; pendiente de validar"
            filas.append(f"| {num[nid]} | {n[3].replace(chr(10), ' ')} | {carril[n[1]]} | {fuente} |")
    return "\n".join(filas)
