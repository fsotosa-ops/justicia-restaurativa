# Justicia restaurativa e inteligencia artificial en Bogotá

Se revisaron tres campos de estudio que hoy se investigan por separado: el acceso a la justicia, la justicia restaurativa en lo penal y la inteligencia artificial aplicada al derecho, a los que se suma el lenguaje judicial sobre las víctimas. Trece búsquedas en Scopus reunieron 7.930 documentos distintos. De ellos se leyeron 29 completos, anotando las páginas de cada cita, a los que se suman 22 textos de una búsqueda complementaria previa, de modo que en total se leyeron 51 para contrastar las hipótesis de trabajo. Cada campo tiene un cuerpo propio, pero casi no se citan entre sí: entre la justicia restaurativa y la inteligencia artificial, menos de 3 de cada 10.000 pares de documentos citan una misma fuente, y de los 57 documentos que tratan ambos temas apenas cuatro aplican la IA a un proceso restaurativo penal y ninguno lo hace para orientar a la ciudadanía. En paralelo se empezó a dibujar el Leviatán, figura descrita por Jorge Salcedo, donde define al sistema judicial  al Estado y su complejidad, aplicado aquí al sistema de justicia colombiano, con 42 entidades, 14 etapas del proceso penal y 38 derivaciones entre entidades, cada una con su norma, lo que muestra que en lo penal, aunque la víctima o la persona investigada pueden pedir la vía restaurativa, esta solo se abre cuando un fiscal o un juez admite la solicitud y remite el caso. Todo lo anterior se recopiló en septiembre y octubre de 2026 y todavía no lo han revisado el equipo jurídico ni los expertos consultados, de modo que las hipótesis, el mapa del Leviatán y las conclusiones sobre los estudios son una propuesta de trabajo para discutir y no resultados cerrados.

## Documentos

| Documento | Qué contiene |
|---|---|
| [Estado del arte](docs/01-estado-del-arte.md) | Desafío, búsqueda en Scopus con su diagrama, cuánto se citan entre sí los campos, redes de las fuentes y los temas más citados, contraste de las seis hipótesis de trabajo y lo que la literatura no ha estudiado |
| [El Leviatán](docs/02-leviatan.md) | Qué se entiende por Leviatán, cómo se dibuja y los diagramas de procesos (en notación BPMN) de la vista general, la comisaría de familia, el proceso penal y la mediación penal, con las derivaciones entre entidades |
| [Lo que falta validar](docs/03-validacion.md) | Preguntas ya resueltas con fuentes primarias y lo que sigue abierto, con su responsable |

## Organización del repositorio

| Carpeta | Qué contiene |
|---|---|
| [`docs/`](docs/) | Los tres documentos, cada uno con sus referencias |
| [`metodo/`](metodo/) | Protocolo y código de las 13 búsquedas en Scopus, unión de sus resultados, cálculo de cuánto se citan entre sí los campos, redes de citas, diagrama de flujo de la búsqueda y búsqueda de mapas de procesos ya publicados |
| [`datos/`](datos/) | Entidades, derivaciones y etapas del Leviatán, selección de documentos por título y resumen, y datos de las redes de citas, con su [diccionario](datos/DICCIONARIO.md) |
| [`procesos/`](procesos/) | El código de cada diagrama de procesos, sus archivos `.bpmn` editables y la fuente de cada actividad |
| [`figuras/`](figuras/) | Todas las figuras de los documentos |
| [`evidencia/`](evidencia/) | Fichas de lectura en texto completo, con citas y páginas, y las normas consultadas |
| [`referencias.bib`](referencias.bib) | Las referencias de los documentos en BibTeX, para importarlas en Zotero u otro gestor |

Los textos completos de terceros y las exportaciones de Scopus no se suben al repositorio, porque sus licencias no permiten redistribuirlos, pero se pueden volver a descargar siguiendo el protocolo.
