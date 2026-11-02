# El Leviatán: el mapa del sistema de justicia

[Inicio](../README.md) · [Estado del arte](01-estado-del-arte.md) · [El Leviatán](02-leviatan.md) · [Validación](03-validacion.md)

> Versión 1, en proceso de validación con el equipo del proyecto.

## 1. Qué entendemos por Leviatán

El término lo propuso Jorge Salcedo, docente de Filosofía e Historia del Derecho de la Javeriana, en la reunión del 28 de octubre de 2026 con el equipo (comunicación personal). Retomando la imagen de Hobbes, Salcedo llamó Leviatán al Estado, entendido como una máquina hipercompleja de procesos y procedimientos frente a la cual las personas se sienten indefensas cuando quieren reclamar o ejercer sus derechos. Aclaró que no lo llama monstruo porque sea malo, sino porque su complejidad hace que, en un Estado tan burocratizado como el colombiano, no existan rutas claras ni un abecé que le diga al ciudadano a dónde ir. En su lectura, los sistemas de justicia son estructuras con actores, procesos, entradas, salidas y un intermedio, cuyas reglas de juego son el derecho sustancial y el procesal.

De esa definición se desprenden dos decisiones para el mapa. En primer lugar, el Leviatán se dibuja completo y no solo en su parte restaurativa, porque, según Salcedo, la justicia restaurativa no se opone a la retributiva, sino que la complementa y está inmersa en el proceso penal; por eso el mapa traza una línea que muestra dónde aparece lo restaurativo dentro del sistema. En segundo lugar, lo que interesa son las bifurcaciones: el momento en que el operador consulta a las partes si quieren una vía restaurativa, que es voluntaria, y lo que ocurre cuando no la toman, que es la vía tradicional de la cárcel, la multa y el incidente de reparación. Como referente de un Leviatán que se puede recorrer, Salcedo citó las unidades de atención y orientación integral que nacieron de la sentencia T-025 de 2004, que le evitan a la víctima tener que lidiar con el Estado entero. El equipo acordó entonces dibujar ese mapa para identificar los vacíos y los puntos de intervención, con la analogía del sistema de salud y sus niveles de atención.

## 2. Cómo se dibuja

Antes de dibujar se buscó si ya existe un mapa de procesos del sistema de justicia colombiano, en fuentes oficiales, en la literatura académica y en Scopus. No existe, ni oficial ni académico: la Fiscalía no publica los procedimientos de sus salas de atención ni de justicia restaurativa, y la única fuente oficial que describe una ruta paso a paso es el Tomo V de los lineamientos del Ministerio de Justicia para las comisarías de familia, que la presenta en una línea de ocho fases y en tablas de actividades con su responsable, pero sin flujograma ([`busqueda-de-mapas.md`](../metodo/busqueda-de-mapas.md)). Por eso el mapa se construye desde las normas y los lineamientos disponibles, con dos referentes. Por un lado, el Sequential Intercept Model (Munetz y Griffin, 2006), que mapea el sistema penal como una secuencia de puntos donde un caso puede desviarse del proceso ordinario, ordena la vista general; el modelo se formuló para personas con enfermedad mental grave, y aquí se adapta a la vía restaurativa. Por otro lado, cada proceso se dibuja en BPMN 2.0, el estándar de notación de procesos de la Object Management Group (2014), que es el que usan Bizagi y Camunda.

Cada lámina tiene un carril por actor, numera sus actividades y asocia a cada una su fuente con artículo o página en una tabla aparte. En naranja va la vía restaurativa y en gris lo que propone el proyecto y falta validar. Además, cada lámina se guarda como archivo `.bpmn`, de modo que el equipo jurídico puede abrirla en Bizagi Modeler, Camunda Modeler o [demo.bpmn.io](https://demo.bpmn.io), corregirla y devolverla, y la figura se regenera desde ese archivo.

## 3. Las láminas

La Figura 1 es la vista general. Una persona consulta en una puerta de entrada, el agente que propone el proyecto le pregunta por su conflicto, su rol y si ya hay un proceso abierto, y según la respuesta el caso va a la comisaría, al proceso penal o a otra entidad. Las preguntas salen de las reuniones del equipo de octubre y por eso van en gris. En cambio, lo que sigue está en la norma: la comisaría denuncia ante la Fiscalía, y solo desde el proceso penal se llega a la mediación.

**Figura 1.** Vista general tentativa de las rutas de acceso

![Vista general del Leviatán en BPMN](../figuras/vista-general.svg)

*Nota:* las actividades con el signo + se detallan en las Figuras 2 a 4. En gris, la propuesta del proyecto por validar; en naranja, la vía restaurativa. *Fuente:* Elaboración propia a partir de las reuniones del equipo de octubre de 2026, la Ley 906 de 2004 y la Resolución FGN 0383 de 2022. Archivo editable: [`vista-general.bpmn`](../procesos/vista-general.bpmn).

La Figura 2 detalla una de las puertas de la violencia intrafamiliar, la comisaría de familia, en tres hojas que siguen las dos primeras fases del Tomo V con el responsable de cada actividad. En la primera, la comisaría recibe a la persona y decide si el caso es de su competencia; en la segunda, el equipo psicosocial valora a la víctima y el riesgo; y en la tercera, la secretaría proyecta las medidas provisionales, diligencia la denuncia y notifica. La comisaría no tiene una salida restaurativa propia en lo penal, porque solo el fiscal o el juez remiten a mediación.

**Figura 2.** Recepción de un caso de violencia en el contexto familiar en una comisaría de familia

*Hoja 1.* Recepción y competencia

![Comisaría de familia, hoja 1](../figuras/comisaria-1.svg)

*Hoja 2.* Valoración del riesgo y entrevista

![Comisaría de familia, hoja 2](../figuras/comisaria-2.svg)

*Hoja 3.* Medidas provisionales y denuncia

![Comisaría de familia, hoja 3](../figuras/comisaria-3.svg)

*Nota:* los eventos con flecha unen una hoja con la siguiente. De la fase 1 no se dibujan las actividades 8, 9, 11 y 12, que se aplican cuando hay niños, niñas o adolescentes; de la fase 2 se omite la actividad 6 (crear la carpeta del expediente), y las actividades 9 a 19 quedan, junto con las fases 3 a 8, en la última actividad. *Fuente:* Elaboración propia a partir de Ministerio de Justicia y del Derecho y PNUD (2022), fases 1 y 2, pp. 17-26. Fuente de cada actividad en [`comisaria-fuentes.md`](../procesos/comisaria-fuentes.md); archivos editables en [`procesos/`](../procesos/).

La Figura 3 dibuja el proceso penal con sus bifurcaciones, que son las que Salcedo pidió mirar. En la primera hoja, si el delito es querellable, el proceso empieza por la conciliación preprocesal, y si hay acuerdo se archiva. Si no lo hay, o si el delito se persigue de oficio, el fiscal indaga. En la segunda, después de la imputación, el caso puede ir a mediación si la víctima o el imputado la piden y el fiscal o el juez la admiten, puede terminar con el principio de oportunidad, que también cabe desde la indagación (art. 323), o puede seguir a la acusación. Cuando nadie ofrece la vía restaurativa, el caso sigue a juicio y la reparación se discute en el incidente de reparación integral.

**Figura 3.** Proceso penal y salidas restaurativas

*Hoja 1.* De la denuncia a la indagación

![Proceso penal, hoja 1](../figuras/proceso-penal-1.svg)

*Hoja 2.* De la imputación a la sentencia

![Proceso penal, hoja 2](../figuras/proceso-penal-2.svg)

*Nota:* en naranja, las dos salidas restaurativas: la conciliación preprocesal y la mediación. *Fuente:* Elaboración propia a partir de la Ley 906 de 2004 y la Resolución FGN 0383 de 2022. Fuente de cada actividad en [`proceso-penal-fuentes.md`](../procesos/proceso-penal-fuentes.md).

Por último, la Figura 4 abre la mediación penal. La piden la víctima o el imputado, el fiscal o el juez evalúa si procede y la remite a un programa con convenio, que hace reuniones previas por separado y luego la audiencia. Si hay acuerdo, el acta vuelve al fiscal y de ahí al juez; si no, el mediador informa el fracaso y el proceso sigue.

**Figura 4.** Mediación penal

![Mediación penal en BPMN](../figuras/mediacion-penal.svg)

*Fuente:* Elaboración propia a partir de la Resolución FGN 0383 de 2022, arts. 12, 14, 16, 19 y 22, y la Ley 906 de 2004, arts. 524 y 525. Fuente de cada actividad en [`mediacion-penal-fuentes.md`](../procesos/mediacion-penal-fuentes.md).

## 4. Derivaciones entre entidades

Las láminas muestran qué pasa dentro de cada entidad, pero un caso casi nunca se resuelve en una sola. Por eso el mapa registra también las derivaciones, es decir, los momentos en que una entidad envía el caso a otra porque una norma la obliga o se lo permite. Por ejemplo, cuando una comisaría de familia recibe un caso de violencia intrafamiliar, la Ley 2126 de 2021 la obliga a enviar la denuncia a la Fiscalía; en cambio, cuando un fiscal considera que un caso puede ir a mediación, la Resolución 0383 de 2022 le permite remitirlo a un programa con convenio, pero no lo obliga, y donde no hay convenio la Resolución 0447 de 2023 permite acudir a programas de otras ciudades o a funcionarios de la Fiscalía capacitados. En las láminas, cada derivación aparece como una flecha punteada entre la entidad y un participante externo, como la que va de la comisaría a las entidades de la ruta en la Figura 2.

Las derivaciones importan para el proyecto porque son los puntos donde un caso puede perderse, demorarse o cambiar de vía, y porque un agente que oriente tiene que saber a dónde va el caso después de cada entidad. Para cada una se registró qué la dispara, si es obligatoria u opcional, el plazo que fija la norma y si el texto de la norma se verificó en la fuente oficial. Las derivaciones se agrupan en rutas, que son los recorridos típicos de un tipo de caso, como la violencia intrafamiliar o la inasistencia alimentaria. La Tabla 1 resume las 38 derivaciones levantadas, y el detalle de cada una está en [`derivaciones.csv`](../datos/derivaciones.csv), con sus columnas explicadas en el [diccionario de datos](../datos/DICCIONARIO.md).

**Tabla 1.** Derivaciones levantadas por ruta

| Ruta | Derivaciones | Obligatorias | Verificadas en la norma | Derivación que condiciona la vía restaurativa |
|---|---:|---:|---:|---|
| Violencia intrafamiliar | 13 | 11 | 11 | La comisaría remite todo caso a la Fiscalía (Ley 2126 de 2021, art. 17, par. 3) |
| Violencia contra la mujer | 5 | 1 | 1 | La casa de justicia remite primero a la Fiscalía a toda mujer víctima (procedimiento PD-AJ-24 de la SDSCJ) |
| Casas de justicia | 4 | 3 | 0 | El Centro de Recepción remite según la tipología del caso a ocho entidades (procedimiento PD-AJ-10) |
| Inasistencia alimentaria | 3 | 1 | 2 | La conciliación de la cuota ocurre antes del incumplimiento, en la comisaría, el ICBF o el consultorio |
| Fiscalía y Ministerio Público | 13 | 9 | 12 | Solo el fiscal o el juez remiten a mediación, a un programa con convenio o, si no lo hay, a otro programa o a un funcionario capacitado (Res. 0383 de 2022, art. 14; Res. 0447 de 2023, art. 2) |

*Fuente:* Elaboración propia con datos de [`derivaciones.csv`](../datos/derivaciones.csv).

Las derivaciones confirman lo que muestran las láminas. En la violencia intrafamiliar todos los caminos llevan al fiscal, y ni la comisaría ni la casa de justicia pueden remitir un caso penal a mediación, de modo que la vía restaurativa depende de una decisión del fiscal o del juez y de que exista un programa de mediación disponible, con convenio en la ciudad o, en su defecto, en otra ciudad o en la propia Fiscalía (Resolución 0447 de 2023, art. 2). En cambio, en la inasistencia alimentaria la conciliación ocurre antes del incumplimiento y fuera de lo penal, por lo que es el punto restaurativo más accesible para una primera iteración del agente. Además, ninguna norma obliga a la Fiscalía a informar a la comisaría o a la casa de justicia del resultado del caso que estas le enviaron, y solo la víctima tiene derecho a conocer el trámite (Ley 906 de 2004, art. 136). Las derivaciones de vuelta que sí existen son puntuales: la Fiscalía remite a la comisaría lo relativo a las medidas de protección (Directiva FGN 0001 de 2021, num. 26), y en la mediación el programa informa al fiscal que remitió (Ley 906 de 2004, art. 526; Resolución 0383 de 2022, art. 19). Por último, 26 de las 38 derivaciones están verificadas en el texto de la norma, 1 viene de una fuente secundaria y las 11 restantes son citas literales de fuentes oficiales que todavía no se pudieron cotejar, sobre todo porque los procedimientos de la Secretaría Distrital de Seguridad, Convivencia y Justicia no están publicados. Por eso la tabla es una base para validar con el equipo jurídico y no un resultado cerrado.

## Referencias

Ministerio de Justicia y del Derecho y Programa de las Naciones Unidas para el Desarrollo. (2022). *Modelos de justicia local y rural. Tomo V: Lineamientos para el servicio de atención en comisarías de familia*. Ministerio de Justicia y del Derecho.

Munetz, M. R. y Griffin, P. A. (2006). Use of the Sequential Intercept Model as an approach to decriminalization of people with serious mental illness. *Psychiatric Services, 57*(4), 544–549. https://doi.org/10.1176/ps.2006.57.4.544

Object Management Group. (2014). *Business Process Model and Notation (BPMN), versión 2.0.2*. https://www.omg.org/spec/BPMN/2.0.2/
