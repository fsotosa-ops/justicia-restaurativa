# ¿Existe ya un mapa de procesos del sistema de justicia colombiano?

2 de noviembre de 2026. Antes de dibujar el Leviatán se buscó si ya existe un mapa de procesos del sistema de justicia colombiano, en tres frentes: fuentes oficiales, literatura académica y una ecuación en Scopus.

## Fuentes oficiales

Se hicieron dos búsquedas a fondo en la web, una por ruta.

- **Fiscalía y proceso penal.** De 52 fuentes, ninguna es un procedimiento vigente de la Fiscalía: el manual de gestión integral es de 2012 (FGN-14100-M-01, versión 07, Resolución 0-1834) y su mapa está como imagen; el «instructivo de la bandeja fiscal» es del Ministerio Público del Perú; el resto son caracterizaciones de otras entidades o fuentes secundarias. Los procedimientos de la Sala de Atención al Usuario y de justicia restaurativa no están publicados.
- **Comisarías, violencia intrafamiliar y alimentos.** De 47 fuentes, la oficial que sirve es el Tomo V de los lineamientos del Ministerio de Justicia para comisarías de familia (2022, 68 páginas), que describe la ruta en ocho fases (recepción y entrevista, medidas provisionales, medidas de atención, audiencia, medidas definitivas, seguimiento, incidente de incumplimiento y levantamiento de medidas) con tablas de actividades y responsables, sin flujograma. También hay procedimientos del sistema de gestión de la Secretaría de Integración Social, por leer.

## Literatura académica

No hay publicaciones que mapeen como proceso el sistema de justicia colombiano. Lo más cercano estudia rutas sin dibujarlas: la Ruta Única de Atención para mujeres víctimas de violencia en Bogotá (Sprague y colegas, 2025), la evaluación de las comisarías que originó la Ley 2126 (Friedemann-Sánchez y colegas, 2026) y las fases de atención en comisarías de Boyacá (Coronado y colegas, 2024). El proceso penal se describe en texto (Bayona Aristizábal y colegas, 2017; Jiménez Sánchez y colegas, 2026).

En cambio, sí hay método: BPMN aplicado a tribunales en Italia (Ambrisi y colegas, 2023), al procedimiento penal polaco (Antkiewicz y colegas, 2013) y a un procedimiento brasileño validado con abogados (Zorzanelli Costa y colegas, 2025); mapas de vías de reclamo co-diseñados con expertos (Roberts y colegas, 2021); y, sobre todo, el Sequential Intercept Model (Munetz y Griffin, 2006), el marco estándar para mapear el sistema penal como puntos de intercepción donde un caso puede desviarse del proceso ordinario, usado en talleres de mapeo por condado y adaptado a la justicia juvenil (Heilbrun y colegas, 2017).

## Scopus

Ecuación: `TITLE-ABS-KEY(BPMN OR "business process model*" OR "process model*" OR "process map*" OR "process mining" OR flowchart* OR "journey map*" OR "legal journey*" OR "justice journey*" OR "paths of redress") AND TITLE-ABS-KEY("justice system" OR court* OR judicial OR "criminal procedure" OR "criminal justice" OR prosecutor* OR "access to justice" OR "restorative justice" OR "domestic violence")`, sin filtro de años, 2 de noviembre de 2026.

| Alcance | Documentos |
|---|---:|
| Mundo | 329 |
| América Latina | 24 |
| Colombia | 2 |

Los 2 documentos de Colombia son el mismo registro de las actas de un congreso de modelado conceptual (ER 2023) y no mapean el sistema colombiano. En América Latina, los trabajos pertinentes son de Brasil (minería de procesos sobre expedientes judiciales) y de Argentina (modelado BPMN en una fiscalía de investigaciones administrativas de La Pampa). La ecuación global trae ruido, porque «court*» captura «courtship» y «process model» se usa en muchas áreas.

## Conclusión

No existe un mapa de procesos publicado del sistema de justicia colombiano, ni oficial ni académico. Por eso el mapa del proyecto se construye desde las fuentes oficiales disponibles, con el Sequential Intercept Model como marco conceptual y BPMN 2.0 para cada proceso, y se valida con el equipo jurídico, como hacen Zorzanelli Costa y colegas (2025).
