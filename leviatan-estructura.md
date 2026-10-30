# El Leviatán, bajado a la estructura jurídica real

**Fecha:** 30-oct-2026. Es la bajada de [`leviatan.md`](leviatan.md) a instituciones, entidades, normas y procesos. Sale del cuaderno [Leviatán · estructura jurídica e institucional](https://notebook.google.com/notebook/9f63dd7b-6e37-44f5-a196-ff573f9f00a1), que tiene 6 investigaciones, 152 fuentes y el prompt de [`estado-del-arte/prompt-lectura-gemini.md`](estado-del-arte/prompt-lectura-gemini.md). Los datos tabulados están en [`mapa/entidades.csv`](mapa/entidades.csv) y [`mapa/etapas.csv`](mapa/etapas.csv), para dibujar el mapa.

**Verificación:**
- **[verificado]**: lo abrí en el texto oficial.
- **[cita]**: texto literal de una fuente oficial, tal como lo devolvió Gemini.
- **[secundaria]**: viene de prensa o de un blog jurídico.
- **[sin cita]**: sin respaldo.

## 1. Los cinco bloques del Leviatán

Antes de entrar a la ruta penal, las entidades se ordenan por su lugar en el Estado:

```
RAMA JUDICIAL ─────────── jueces (garantías, conocimiento, ejecución), tribunales, Corte Suprema,
  │                        Consejo Superior de la Judicatura, Comisión de Disciplina, jueces de paz
  └─ FISCALÍA ─────────── (parte de la Rama, con autonomía) investiga y acusa
       ├─ puertas: SAU, URI, CAVIF, CAIVAS, CAPIV
       ├─ policía judicial: CTI (propio) + Policía Nacional (SIJIN/DIJIN, depende funcionalmente)
       ├─ Medicina Legal (adscrita)
       └─ Unidad de Justicia Restaurativa (Res. 0-0211 de 2025)
MINISTERIO PÚBLICO ────── Procuraduría (procuradores judiciales penales), Defensoría del Pueblo
                           (defensa pública, Ley 941/2005), Personería de Bogotá
EJECUTIVO NACIONAL ────── MinJusticia (Dirección de MASC, Casas de Justicia, SICAAC, Sistemas Locales
                           de Justicia), ICBF y defensorías de familia, INPEC
DISTRITO DE BOGOTÁ ────── Sec. de Seguridad, Convivencia y Justicia (casas de justicia, UMC,
                           Sistema Distrital de Justicia), Sec. de Integración Social (comisarías),
                           Sec. de la Mujer (CIOM, Línea Púrpura), alcaldías locales, inspecciones
NO FORMAL Y COMUNITARIO ─ conciliadores en equidad, centros de conciliación, consultorios jurídicos
```

## 2. Entidades y su papel en la ruta

Esta tabla es la versión corta; la completa, con norma, presencia en Bogotá y fuente, está en el CSV.

| Entidad | Bloque | Norma clave | Qué hace en la ruta | ¿Lo restaurativo pasa por aquí? |
|---|---|---|---|---|
| **Sala de Atención al Usuario (SAU), Fiscalía** | Fiscalía | D. Ley 016/2014, modificado por el 898/2017; Res. 2638/2016, art. 3 | Recibe denuncias y las **clasifica, filtra y asigna**. Informa sobre conciliación [verificado, Res. 2638/2016; la dependencia se llama hoy «Dirección Nacional de Atención al Usuario, Intervención Temprana y Asignaciones», según el manual de la Fiscalía] | Sí: es el primer filtro y ahí se informa la conciliación |
| URI, Fiscalía | Fiscalía | Ley 906/2004 | Flagrancias, actos urgentes y denuncias las 24 horas. En Bogotá hay sedes en Engativá, Bosa y Kennedy, entre otras [cita] | No está en las fuentes |
| CAVIF / CAIVAS / CAPIV, Fiscalía | Fiscalía | Res. FGN 1948/2014 (CAPIV) [secundaria] | Atención especializada: violencia intrafamiliar, delitos sexuales, atención integral. CAIVAS tiene 6 sedes en Bogotá [cita] | CAVIF: principio de oportunidad con suspensión a prueba [cita] |
| Fiscal delegado | Fiscalía | Ley 906/2004 | Dirige la indagación y la investigación y acusa. Ofrece o pide principio de oportunidad, conciliación y mediación | **Sí: es el principal operador de lo restaurativo** |
| Unidad de Justicia Restaurativa | Fiscalía | Res. 0-0211/2025, art. 5 [verificado] | Define rutas restaurativas y coordina programas | Sí, en todas las etapas |
| CTI y Policía Nacional (SIJIN/DIJIN) | Fiscalía / Ejecutivo | Ley 906/2004, arts. 200–201 [cita] | Policía judicial: actos urgentes, evidencia y recepción de denuncias | No está en las fuentes |
| Medicina Legal | Fiscalía (adscrita) | Ley 270/1996, art. 31; Ley 938/2004 [cita] | Dictámenes periciales; acredita lesiones e incapacidad, que definen el tipo y la pena | No |
| Juez de control de garantías | Rama Judicial | Ley 906/2004, art. 39 [cita] | Controla la legalidad: capturas, medidas de aseguramiento, principio de oportunidad | Sí: avala el principio de oportunidad y recibe solicitudes de mediación |
| Juez de conocimiento (municipal o de circuito) | Rama Judicial | Ley 906/2004, arts. 36–37 [cita] | Acusación, juicio y sentencia. Los municipales llevan los querellables | Sí: mediación y conciliación en el incidente de reparación |
| Juez de ejecución de penas | Rama Judicial | Ley 906/2004, art. 38 [cita] | Vigila el cumplimiento de la pena | No está en las fuentes |
| Procuraduría (procuradores judiciales penales) | Ministerio Público | Ley 906/2004, arts. 109–112 [cita] | Interviene en defensa del orden jurídico y de los derechos | Interviene en el principio de oportunidad |
| Defensoría del Pueblo, defensa pública | Ministerio Público | Ley 941/2005, art. 1 [cita] | Defensa técnica de quien no puede pagarla | Orienta sobre mediación [cita] |
| Personería de Bogotá | Ministerio Público | D. Ley 1421/1993, art. 99 [cita] | Ministerio Público distrital. Está en las URI y en las casas de justicia | Concilia en asuntos conciliables [cita] |
| Consultorios jurídicos | No formal | Ley 2113/2021, art. 6 [cita] | Asesoría y representación gratuita, también como apoderados de víctimas | Sí: pueden tener centro de conciliación, mediación y justicia restaurativa (art. 6, par. 3) [cita] |
| Centros de conciliación y conciliadores en equidad | No formal | Ley 2220/2022, arts. 17 y 139 [cita] | Conciliación extrajudicial y en equidad | Sí |
| MinJusticia: Dirección de MASC, Casas de Justicia, SICAAC | Ejecutivo nacional | D. 2897/2011, art. 13; Ley 2220/2022, art. 133 [cita] | Rector de la política de MASC y de las casas de justicia; registro SICAAC | Diseña la política de conciliación |
| ICBF y defensorías de familia | Ejecutivo nacional | Ley 1098/2006; Ley 2126/2021 [cita] | Restablecimiento de derechos de niños y niñas; concilia en familia | Concilia en familia (Ley 2220, art. 12) |
| **Comisarías de familia** | Distrito (**Integración Social**) | Ley 2126/2021, art. 2 [cita] | «Puerta de acceso a la justicia» en violencia familiar: medidas de protección y remisión a la Fiscalía | Concilia en familia, pero no en violencia contra la mujer |
| Casas de justicia (16 localidades) | Distrito (SDSCJ) + Nación | D. 2897/2011; D. Distrital 644/2025 [cita] | Ventanilla multiagencial. El CRI recibe, clasifica y remite (PD-AJ-10) | Sí: allí funcionan las UMC, la Fiscalía y la Personería |
| Unidades de Mediación y Conciliación (UMC) | Distrito (SDSCJ) | D. Distrital 485/1996; D. 413/2016, art. 18 [cita] | Mediación y conciliación en equidad gratuitas | Sí, en lo comunitario y preprocesal |
| Inspecciones de policía | Distrito | Ley 1801/2016, arts. 231–234A [cita] | Convivencia y trámite policivo; hacen cumplir actas de conciliación. La Ley 2492/2025 las rebautizó «Inspecciones de Convivencia y Paz» [cita, sin verificar] | Concilia en convivencia, no en lo penal |
| Sec. de la Mujer: CIOM y Línea Púrpura | Distrito | Acuerdo 490/2012; Convenio 1864/2024 con la Fiscalía [cita] | Orientación y representación jurídica para mujeres; está en 5 URI y en Paloquemao | Deriva; en violencia contra la mujer prima la protección |
| **Sistema Distrital de Justicia** | Distrito | D. 225/2026, arts. 174.3–174.26 [verificado] | Articula lo formal, lo no formal y lo comunitario con comités distrital y locales; enfoque restaurativo; interoperabilidad (174.10) | Sí, como principio y como enfoque |

## 3. El proceso penal y dónde se abre lo restaurativo

| Etapa | Ordinario (Ley 906) | Abreviado (Ley 1826) | Quién dirige | Salidas restaurativas |
|---|---|---|---|---|
| 1. Noticia criminal e indagación | Denuncia, querella o de oficio. Hasta 2 años para imputar o archivar (art. 175) | Igual. La víctima puede pedir que la acción pase a ser privada (art. 553) | Fiscal + policía judicial | **Conciliación preprocesal** (querellables, art. 522), mediación, principio de oportunidad. Archivo (art. 79) |
| 2. Imputación | Audiencia ante el juez de garantías (art. 286) | **No existe**: el traslado del escrito de acusación equivale a la imputación (art. 536) | Garantías / fiscal | Mediación (art. 524 y ss.), principio de oportunidad, allanamiento |
| 3. Investigación | 90 a 120 días para acusar o pedir la preclusión | 60 días para preparar la defensa (art. 541) | Fiscal | Igual que la etapa 2 |
| 4. Acusación y preparatoria | Dos audiencias (arts. 338 y 355 y ss.) | **Audiencia concentrada**, una sola (art. 542) | Juez de conocimiento | Preacuerdos; en el abreviado, **mecanismos restaurativos en cualquier momento antes del fallo** (art. 547) |
| 5. Juicio y sentencia | Juicio oral; sentencia en 15 días (art. 447) | Juicio en 30 días; sentencia en 10 (art. 545) | Juez de conocimiento | Allanamiento con rebaja |
| 6. Reparación | Incidente de reparación: caduca a los 30 días del fallo (art. 106) | El acusador privado la incluye en la acusación (art. 564) | Juez de conocimiento | **Conciliación en el incidente** (arts. 103 y 521) |
| 7. Ejecución | Juez de ejecución de penas | Igual | Juez de ejecución + INPEC | No está en las fuentes |

Fuente de la tabla: Ley 906/2004 y Ley 1826/2017 [cita; la respuesta de Gemini no trajo identificadores de fuente, pero los artículos se pueden revisar uno a uno].

**Qué va por el abreviado (art. 534):** los querellables y una lista cerrada de delitos de oficio, entre ellos lesiones personales, hurto, estafa, **inasistencia alimentaria** y **violencia intrafamiliar**. La VIF entró por la **Ley 1959 de 2019, art. 4** [verificado], y esa misma ley, en su **art. 5, prohíbe convertir la VIF en acción privada** [verificado]. En VIF, entonces, no hay acusador privado: el caso queda siempre en manos de la Fiscalía.

## 4. Correcciones a lo que teníamos

1. **Las comisarías de familia siguen en Integración Social.** El traslado a la Secretaría de Seguridad, anunciado en 2024 y reglamentado en los arts. 175–177 del D. 644 de 2025, **se revirtió el 4 de abril de 2026**: el Distrito decidió no gastar unos $16.000 millones en la transición ([bogota.gov.co](https://bogota.gov.co/mi-ciudad/integracion-social/comisarias-de-familia-de-bogota-continuaran-en-integracion-social)) [verificado por búsqueda]. `leviatan.md` decía lo contrario y quedó corregido.
2. **Comisarías las 24 horas:** la Ley 2126 de 2021, art. 30, obliga a que haya atención los 7 días de la semana y las 24 horas [cita]. Según RCN (1-oct-2026), de más de 35 comisarías en Bogotá **solo una atiende las 24 horas** [secundaria]. Es una brecha concreta en la puerta principal de la VIF.
3. **El primer filtro de la Fiscalía tiene nombre y norma:** la SAU clasifica, filtra y asigna las denuncias (Res. 2638/2016, art. 3). Es el punto del Leviatán donde se decide la ruta de un caso, igual que el CRI en las casas de justicia.
4. **VIF y prueba anticipada:** la Ley 1959 de 2019, art. 3, permite la prueba anticipada en VIF y que **no se repita en el juicio** si hay revictimización, riesgo, afectación emocional o dependencia económica [verificado]. Es un criterio legal de riesgo que se puede llevar al filtro de seguridad de la capa 6.

## 5. Lo que falta bajar

- **El número de despachos en Bogotá:** juzgados de garantías y de conocimiento, SAU, URI y CAVIF. Ninguna fuente lo trae; la estadística está en el Consejo Superior de la Judicatura y en la Fiscalía.
- **El texto vigente de la Res. 0-0211 de 2025** y si dejó sin efecto la Res. 0383 de 2022 (pendiente con Lorena).
- **El PD-AJ-10 completo** (flujo del CRI) y el manual MA-AJ-08 de las UMC. Los dos están en el portal MIPG de la SDSCJ.
- **Las relaciones entre entidades como grafo** (quién remite a quién). El CSV tiene las entidades y las etapas; las remisiones todavía hay que levantarlas.
- **La Ley 2492 de 2025** (nombre de las inspecciones), sin verificar.
