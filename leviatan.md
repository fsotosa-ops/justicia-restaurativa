# El Leviatán: hoja de ruta para mapear el ecosistema de justicia

**Origen:** reunión del 28-oct-2026 con Jorge Salcedo. El equipo acordó dibujar el mapa completo del ecosistema de justicia en Colombia, porque sin él no se ven las bifurcaciones donde la vía restaurativa aparece o desaparece. El mapa queda a cargo de Luis Gabriel, Felipe y Efraín, y sirve además para retomar la conversación con Jorge sobre algo concreto.

**Estado al 30-oct-2026:** las seis capas ya tienen contenido, sacado de las investigaciones del cuaderno [Leviatán · justicia restaurativa Bogotá](https://notebook.google.com/notebook/0d8f078d-4f14-43cc-9d68-d1d4487e226d) (178 fuentes). El 2-nov se dibujó una primera versión: el recorrido por las seis capas está en el [README](README.md#7-el-mapa-del-leviatán) y las redes de remisiones en [`mapa/grafos/`](mapa/grafos/). Falta el mapa completo con el equipo.

**Cómo leer el grado de verificación** (marca al final de cada dato):
- **[abierto]**: abrí la fuente oficial y la leí.
- **[cita]**: Gemini devolvió el texto literal de una fuente oficial que está en el cuaderno.
- **[sin cita]**: Gemini lo afirma sin citar. Hay que verificarlo antes de usarlo.

## Cómo se lee el Leviatán

La analogía del 28-oct es el sistema de salud, que tiene puertas de entrada, triaje, niveles de atención y salidas. Llevada a la justicia, una persona con un conflicto entra por alguna puerta, alguien clasifica su caso y esa clasificación abre o cierra rutas. La pregunta que ordena el mapa es **en qué punto de cada recorrido se ofrece la vía restaurativa, quién decide ofrecerla y qué pasa cuando no se ofrece**. Esos puntos son los que la PoC podría orientar, y los que no tienen una fuente oficial que los describa se convierten en brechas para E2.

## Dónde se prueba cada hipótesis

El [contraste del 30-oct](estado-del-arte/contraste-hipotesis.md) amarra cada hipótesis del Doc a una capa del mapa. Esta tabla muestra qué tiene que dibujar cada capa para que la hipótesis se pueda poner a prueba.

| Capa | Hipótesis | Qué tiene que mostrar el mapa |
|---|---|---|
| 1. Puertas | H1, H2 | Qué mecanismo restaurativo se ofrece en cada puerta y quién orienta ahí. La gente conoce las puertas pero no los mecanismos |
| 2. Triaje | H3 | Las reglas de elegibilidad (arts. 74, 524 y 534) como árbol de decisión, sin modelo predictivo |
| 4. Quiebres | H3, H4 | Dónde decide el operador si ofrece la vía, y cuántos casos salen por cada mecanismo (la conciliación es el 1,37% de las salidas) |
| 5. Referentes | H2 | El CRI de las casas de justicia y LegalApp, como las dos formas de orientar que ya existen |
| 6. Recorridos | H5 | El filtro de riesgo antes de mediar en VIF |
| Transversal | H6 | El agente informa sobre la ruta, no dice cómo se resolvería un caso (T-323 de 2024) |

## Las seis capas

### 1. Puertas de entrada

| Puerta | Qué atiende | Norma | ¿Ofrece o deriva a lo restaurativo? |
|---|---|---|---|
| Casa de justicia | Centro multiagencial: el CRI recibe al usuario, analiza su necesidad y lo remite a la entidad competente | Decreto Distrital 563 de 2007 [cita]; procedimiento PD-AJ-10 de la SDSCJ [cita] | Sí: dentro funcionan las Unidades de Mediación y Conciliación, el centro de conciliación de la Personería y la SAU de la Fiscalía [cita] |
| Comisaría de familia | Violencia en el contexto familiar; medidas de protección | [Ley 2126 de 2021](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=168066) [abierto] | Según el lineamiento de MinJusticia, la Ley 2126 eliminó la conciliación directa [sin abrir] |
| Fiscalía SAU / URI | Denuncia; la URI recibe flagrancias y actos urgentes las 24 horas | Ley 906 de 2004 | Sí: en querellables orienta a la conciliación preprocesal [cita] |
| Consultorio jurídico | Asesoría, conciliación y representación para quien no puede pagar | Ley 2113 de 2021, art. 6 (lo autoriza a mediar) [cita] | Sí, como mediador penal por convenio con la Fiscalía (Res. 0383/2022, art. 6) [cita] |
| Inspección de policía | Convivencia, querellas policivas | Ley 1801 de 2016 | Mediación policial, fuera de lo penal [sin abrir] |
| Defensoría / Personería | Defensa pública, Ministerio Público | Ley 941 de 2005 | Mediación penal: la Defensoría empezó un piloto en Bogotá en 2023 [sin abrir] |
| CAVIF / CAIVAS / CAPIV (Fiscalía) | VIF, delitos sexuales, atención integral a víctimas | Ley 906 de 2004 | La violencia sexual no se concilia; en el resto se deriva [sin cita] |

**Cambios recientes en Bogotá que el equipo no tenía:**
- **Corregido el 30-oct:** las comisarías de familia **siguen en Integración Social**. El traslado a la Secretaría de Seguridad, anunciado en mayo de 2024 y reglamentado en el D. 644 de 2025 (arts. 175–177), se revirtió el 4 de abril de 2026 ([bogota.gov.co](https://bogota.gov.co/mi-ciudad/integracion-social/comisarias-de-familia-de-bogota-continuaran-en-integracion-social)). Detalle en [`leviatan-estructura.md`](leviatan-estructura.md).
- **[Decreto 225 de 2026](https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=193449)** (12-jun-2026), que reglamenta el **Sistema Distrital de Justicia** [abierto]:
  - Integra la justicia formal, la no formal y la comunitaria, con la justicia restaurativa como principio (art. 174.4) y como enfoque (art. 174.5).
  - Crea un Comité Distrital de Justicia y un Comité Local por localidad. En los locales se sientan la comisaría, la Personería, los jueces de pequeñas causas y la URI.
  - Ordena un esquema de interoperabilidad de los sistemas de información (art. 174.10).
  - **Es el marco institucional distrital al que se conectaría la PoC, y nadie lo mencionó en las reuniones.**
- El número de casas de justicia no cuadra entre fuentes: el Decreto 563 de 2007 proyectó 19, las notas oficiales dicen 12, 13 o 16, y las que tienen ruta integral para mujeres son 5, 7 o 9. La cifra vigente hay que pedírsela a la SDSCJ.

### 2. Clasificación del caso (el triaje)

Las preguntas, en el orden en que deciden la ruta:

1. ¿La víctima es menor de edad o inimputable, hay violencia contra la mujer o hubo flagrancia? Entonces el delito se persigue de oficio, aunque esté en la lista de querellables (art. 74, parágrafo) [cita].
2. ¿El delito está en el art. 74? Si no está, se persigue de oficio. Si está, es querellable: lesiones leves, injuria, calumnia, hurto simple o estafa de hasta 150 SMLMV, abuso de confianza, daño en bien ajeno, entre otros [cita].
3. ¿Pasaron más de 6 meses desde el hecho? La querella caduca (art. 73) [cita].
4. En querellables la **conciliación preprocesal es obligatoria** y requisito para que exista acción penal (art. 522). La pueden hacer el fiscal, un centro de conciliación o un conciliador reconocido [cita: texto del art. 522, Secretaría del Senado]. Si concilian, la acción se extingue. Si fracasa, el caso sigue por el procedimiento abreviado de la Ley 1826 de 2017 [cita].

**Corrección a las notas del 7-oct:** la defensoría pública **no exige estrato 3 o menos**. La Ley 941 de 2005 pide imposibilidad económica o social, y el criterio de estrato es de los reglamentos de los consultorios jurídicos [cita, falta abrir el artículo]. El agente que propuso Juan, que pregunta el estrato, tendría que diferenciar a qué servicio aplica.

La [Ley 1542 de 2012](https://urosario.edu.co/sites/default/files/2022-10/ley_1542_2012.pdf) volvió de oficio la violencia intrafamiliar y la inasistencia alimentaria, y la C-022 de 2015 la declaró exequible [cita].

### 3. Rutas restaurativas en la justicia penal ordinaria

| Mecanismo | Norma | Cuándo | A qué delitos | Quién | Efecto del acuerdo |
|---|---|---|---|---|---|
| Conciliación preprocesal | Art. 522 | Antes del proceso | Querellables | Fiscal, centro de conciliación, consultorio | Archivo o preclusión [cita] |
| Mediación | Arts. 523–527 | De la imputación hasta antes del juicio oral | De oficio, con **pena mínima de hasta 5 años** y bien jurídico personal (art. 524) | La piden la víctima o el imputado ante el fiscal o el juez; el mediador lo designa la Fiscalía | Si la pena mínima es de hasta 5 años, se extingue la acción. Si es mayor, solo da beneficios (C-979/05) [cita] |
| Restaurativos en el abreviado | Art. 547 (Ley 1826/2017) | En cualquier momento antes del fallo de primera instancia | Los del art. 534 | | Extinción de la acción [cita] |
| Conciliación en el incidente de reparación | Arts. 102–108 | Después de la condena | Cualquier delito con víctima | Juez | Solo efectos civiles [cita] |
| Principio de oportunidad con suspensión a prueba | Arts. 323–325 | De la indagación hasta antes del juicio | Pena máxima de hasta 6 años (art. 324, que según una compilación del CPP fue modificado por la Ley 2477 de 2025 [por verificar]) | Fiscalía, con control del juez de garantías | Extinción tras cumplir el plan de reparación [cita] |

- El **Manual de JR** (Res. 0383 de 2022) habilita como mediadores a abogados, consultorios, personeros y centros autorizados, siempre por convenio con la Fiscalía. La 0447 de 2023 cubre los lugares donde no hay convenios [cita].
- La **Resolución 0-0211 de 2025** crea la Unidad de Justicia Restaurativa con rutas nacional, seccionales y para investigados [cita: Diario Oficial]. Según su art. 10 deroga «las disposiciones que le sean contrarias», y una fuente secundaria se pregunta si el manual y los convenios de mediación siguen vigentes. **Esto queda abierto y conviene preguntárselo a Lorena.**
- Dato de la **SU-122 de 2022**: el principio de oportunidad explica solo el 1,8% de las salidas del sistema penal acusatorio [cita]. Es la cifra de subuso mejor sustentada que hay en el cuaderno.

### 4. Bifurcaciones y salidas

En estos puntos se pierde la opción restaurativa, según las fuentes:
1. **El archivo en la indagación:** el caso no avanza y nunca llega al momento en que se podría ofrecer la mediación. Según la CEJ, el 93% de las denuncias no pasa de la indagación (informe sobre el SPOA de 2025) y en 2024 se archivó el 81,9% de lo que evacuó la Fiscalía [sin cita; hay notas de prensa en el cuaderno].
2. **Una parte no comparece** a la citación de conciliación o mediación [sin cita].
3. **El operador no la ofrece:** la mediación depende de que la pidan las partes ante el fiscal o el juez (art. 525), y la literatura atribuye su bajo uso a la cultura punitiva de los operadores [cita]. Es lo mismo que muestran los estudios de Dinamarca y Países Bajos que trajo Consensus.
4. **La querella caduca** a los 6 meses (art. 73) [cita].

Cifras para verificar en la fuente primaria antes de usarlas:
- **Encuesta de Necesidades Jurídicas 2022 (DNP):** 12,4% de las personas con un problema justiciable, 37% atendido por una ruta institucional, 32,7% resuelto. Bogotá tendría el mayor conocimiento de los mecanismos alternativos (60%) [sin cita; el documento del DNP está en el cuaderno].
- **Piloto de mediación de la Fiscalía 2022–2024:** 1.888 casos en 17 seccionales, con acuerdo en el 35% [sin cita].

### 5. Operadores y referentes

- **LegalApp** (MinJusticia): orienta sobre rutas de justicia con un directorio de más de 20.000 autoridades. Desde 2021 permite agendar citas con consultorios jurídicos, y tiene una versión sin internet, «LegalApp Rural», distribuida a casas de justicia y comisarías [cita: MinJusticia]. **No tiene un módulo de mediación penal** [cita]. Es el antecedente directo de la PoC, que tendría que explicar qué agrega respecto de LegalApp.
- **Casas de justicia:** el procedimiento PD-AJ-10 de la SDSCJ ya es un triaje. El CRI analiza la necesidad, registra datos y remite, y si hace falta el usuario vuelve al CRI para otra remisión [cita]. **Es el flujo humano que un agente replicaría**, así que conviene conseguir el documento completo.
- **Rama Judicial, Justicia Restaurativa y Terapéutica:** en Bogotá opera en adolescentes (SRPA, tribunales de tratamiento de drogas), no en la justicia ordinaria de adultos [cita parcial].
- **SIDIJUS:** la SDSCJ diseña un sistema de información distrital de justicia, con un módulo para las mediaciones de las Unidades de Mediación y Conciliación [cita]. Es una fuente de datos posible para medir.
- **JEP / LEIRA** (28-oct) y **T-025 de 2004** como modelos de orientación a víctimas.

### 6. Recorridos de los delitos priorizados

**Violencia intrafamiliar (art. 229 CP; pena de 4 a 8 años según la Ley 1959 de 2019)**
Comisaría o Línea Púrpura (medidas de protección) → la comisaría remite a la Fiscalía → procedimiento abreviado → mediación, principio de oportunidad o juicio.

**Inasistencia alimentaria (art. 233 CP)**
Comisaría, ICBF o consultorio (fijación de la cuota) → mora → REDAM o denuncia → procedimiento abreviado → acuerdo o sentencia. Según una fuente, sigue siendo conciliable aunque sea de oficio [sin cita; hay que verificarlo].

**Cómo se resuelve la tensión del equipo** (de oficio pero «el delito más mediado»): la VIF no admite conciliación preprocesal, porque dejó de ser querellable. Sí entra a la **mediación** por dos vías:
- El art. 524: es de oficio y su pena mínima, 4 años, no pasa de 5.
- El art. 547: se tramita por el procedimiento abreviado, donde los mecanismos restaurativos extinguen la acción.

La mediación la hacen los consultorios por convenio con la Fiscalía (Res. 0383). **El límite** es el enfoque de género: según Gemini, la Ley 1257 de 2008 y la Ley 2126 de 2021 impiden conciliar o mediar cuando la víctima es mujer y hay desequilibrio de poder [sin cita]. Esta lectura es mía, armada sobre artículos con cita, y hay que validarla con Lorena antes de dibujarla, porque define si la primera iteración puede ofrecer mediación en VIF.

## Flujo de búsqueda

1. **Gemini Notebook busca y lee.** Seis investigaciones `deep`, una por capa (30-oct). Solo se importaron las fuentes que citan los informes: 167 de unas 250 encontradas.
2. **Aquí se procesa.** Una pregunta por capa, con salida corta y citas. Las respuestas de las capas 4 y 6 volvieron sin citas.
3. **Consensus contrasta** (pendiente). Las hipótesis H1–H6 del [Doc de estado del arte](https://docs.google.com/document/d/1rVOEqIFU9WSb554K3JUJLBeF2PCU98-E6-1-WaPMuyE) se reescriben sobre los cuatro puntos de quiebre de la capa 4 y sobre el CRI de las casas de justicia.

| Capa | Consulta lanzada en Gemini Notebook |
|---|---|
| 1 | Puertas de entrada al sistema de justicia en Bogotá para víctimas de delitos: comisarías de familia, casas de justicia, inspecciones de policía, Fiscalía SAU y URI, consultorios jurídicos, Defensoría del Pueblo, Personería; competencias de cada una |
| 2 | Clasificación de casos penales en Colombia: delitos querellables art. 74 Ley 906 de 2004, conciliación preprocesal como requisito de procedibilidad, delitos de oficio, requisitos de acceso a defensoría pública |
| 3 | Mecanismos de justicia restaurativa en la justicia penal ordinaria colombiana: Libro VI Ley 906 de 2004, Manual de Justicia Restaurativa Fiscalía 2022, Resolución 0211 de 2025 Unidad de Justicia Restaurativa, mediación penal, principio de oportunidad |
| 4 | Barreras de acceso a la justicia restaurativa en Colombia: denuncias inadmitidas, bajo uso de la mediación penal, necesidades jurídicas insatisfechas, encuesta de necesidades jurídicas DNP DANE |
| 5 | Casas de justicia de Bogotá servicios y rutas; programa justicia restaurativa y terapéutica Rama Judicial; LegalApp Ministerio de Justicia rutas de justicia; ruta de atención a víctimas sentencia T-025 de 2004 |
| 6 | Ruta de atención de violencia intrafamiliar e inasistencia alimentaria en Bogotá: denuncia, comisaría de familia, Fiscalía, mediación y conciliación, Ley 1542 de 2012, Ley 1959 de 2019 |

**Consultas para Consensus** (en inglés, como máximo 3 por tanda):

| Fecha | Consulta | Resultado o para qué |
|---|---|---|
| 30-oct | mapping legal problem pathways and justice journeys of citizens: legal needs surveys and access to justice | Marco OCDE/Open Society de *legal needs surveys* (2019) |
| 30-oct | referral and gatekeeping to restorative justice programs in criminal justice: who decides eligibility and at what stage | El operador que deriva decide quién accede (Dinamarca, Países Bajos, Australia). Sirve para el punto de quiebre 3 |
| pendiente | triage and first point of contact in access to justice systems, one-stop justice centres | Para comparar con el CRI |
| pendiente | restorative justice domestic violence mediation safety concerns | Para el límite de género en VIF |
| pendiente | AI legal information chatbots citizens access to justice evaluation abstention | Puente hacia E4 y E5 |

Lo que devuelve Consensus es el abstract: sirve para ubicar el artículo, pero no se cita como hallazgo hasta leerlo.

## Fuentes y criterio de consulta

| Fuente | Para qué | Acceso | Nota |
|---|---|---|---|
| Secretaría del Senado | Normas vigentes con notas de vigencia | Descarga | Gemini la usó para la Ley 906 |
| Función Pública, Gestor Normativo | Normas nacionales | Descarga | Alternativa estable al Senado |
| Régimen Legal de Bogotá (alcaldiabogota.gov.co/sisjur) | Decretos y acuerdos distritales | Público | Ahí están los decretos 563/2007, 644/2025 y 225/2026 |
| Corte Constitucional | Exequibilidad (C-979/05, C-060/08, C-022/15, SU-122/22) | Público | Faltaba en los links originales |
| Corte Suprema (relatoría) | Jurisprudencia penal | Por revisar | Exige manejar descriptores |
| Fiscalía | Manual, resoluciones 0383, 0447 y 0211 | Público | |
| Portal MIPG de la SDSCJ | Procedimientos de las casas de justicia (PD-AJ-10, PD-AJ-24) | Descarga | Aquí está el flujo del CRI |
| Diario Oficial | Detectar cambios normativos | Por revisar | Propuesto como monitor (23-sep) |
| Biblioteca Javeriana | Académico | Requiere usuario | Pendiente con Juan |

## Próximos pasos

| Qué | Quién | Para cuándo |
|---|---|---|
| Verificar las cifras marcadas [sin cita] (ENJ 2022, CEJ 93%, piloto de la Fiscalía) en la fuente primaria | Felipe | antes de la próxima sesión |
| Validar con Lorena la vía de la mediación en VIF y el límite de género | Felipe | próxima sesión |
| Preguntar si la Res. 0211 de 2025 dejó sin efecto el manual y los convenios de mediación | Felipe | próxima sesión |
| Llevar como hallazgos LegalApp, el Decreto 225 de 2026 y el CRI de las casas de justicia | Felipe | próxima sesión |
| Conseguir el PD-AJ-10 completo y la cifra vigente de casas de justicia (SDSCJ) | sin dueño | |
| Lanzar las 3 consultas pendientes en Consensus y reescribir H1–H6 | Felipe | después de validar |
| Dibujar el mapa (capas 1–6) | Luis Gabriel, Felipe, Efraín | sin fecha (28-oct) |
| Nueva reunión con Jorge, ya con el mapa | sin dueño | después del mapa |
