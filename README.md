# Justicia restaurativa e inteligencia artificial en Bogotá

Este repositorio reúne lo levantado durante septiembre y octubre del 2026. Todavía no lo han revisado el equipo jurídico ni los expertos consultados, de modo que las hipótesis, el mapa del Leviatán y las conclusiones sobre la literatura son una propuesta de trabajo para discutir y no resultados cerrados.

## Resumen

El proyecto 21871, del programa Atenea, explora cómo un agente de inteligencia artificial puede ayudar a que las personas en Bogotá lleguen a la justicia y, cuando corresponde, a la vía restaurativa. Para situarlo se revisaron tres literaturas que hoy se estudian por separado: el acceso a la justicia, la justicia restaurativa en lo penal y la inteligencia artificial aplicada al derecho, a las que se suma el lenguaje judicial sobre las víctimas. Trece ecuaciones en Scopus reunieron 7.930 documentos distintos. De ellos se leyeron 29 en texto completo con registro de páginas, a los que se suman 22 textos de una búsqueda complementaria previa, de modo que en total se leyeron 51 para contrastar las hipótesis del equipo. Cada literatura tiene un cuerpo propio, pero casi no se citan entre sí: entre la justicia restaurativa y la inteligencia artificial solo el 0,03% de los pares de documentos comparte una referencia, sin contar los que tratan ambas, y de los 57 documentos que las cruzan apenas cuatro aplican la IA a un proceso restaurativo penal y ninguno lo hace para orientar a la ciudadanía. En paralelo se empezó a dibujar el Leviatán, como llamó Jorge Salcedo al sistema de justicia colombiano, con 42 entidades, 14 etapas procesales y 38 derivaciones entre entidades, cada una con su norma, lo que muestra que en lo penal, aunque la víctima o el procesado pueden pedir la vía restaurativa, esta solo se abre cuando un fiscal o un juez admite la solicitud y remite el caso.

## Documentos

| Documento | Qué contiene |
|---|---|
| [Estado del arte](docs/01-estado-del-arte.md) | Desafío, búsqueda en Scopus con su diagrama, conexión entre literaturas, grafos de cocitación y palabras clave, contraste de las seis hipótesis del equipo y vacío en la literatura |
| [El Leviatán](docs/02-leviatan.md) | Qué se entiende por Leviatán, cómo se dibuja y las láminas BPMN de la vista general, la comisaría de familia, el proceso penal y la mediación penal, con las derivaciones entre entidades |
| [Lo que falta validar](docs/03-validacion.md) | Preguntas ya resueltas con fuentes primarias y lo que sigue abierto, con su responsable |

## Organización del repositorio

| Carpeta | Qué contiene |
|---|---|
| [`docs/`](docs/) | Los tres documentos, cada uno con sus referencias |
| [`metodo/`](metodo/) | Protocolo de búsqueda, ecuaciones E1 a E13, unificación del corpus, medida de conexión, grafos, diagrama de flujo de la búsqueda y búsqueda de mapas de procesos existentes |
| [`datos/`](datos/) | Entidades, derivaciones y etapas del Leviatán, revisión por título y resumen de los cruces y salidas bibliométricas, con su [diccionario](datos/DICCIONARIO.md) |
| [`procesos/`](procesos/) | El modelo de cada lámina, sus archivos `.bpmn` editables y la fuente de cada actividad |
| [`figuras/`](figuras/) | Todas las figuras de los documentos |
| [`evidencia/`](evidencia/) | Fichas de lectura en texto completo, con citas y páginas, y las normas consultadas |
| [`referencias.bib`](referencias.bib) | Las referencias de los documentos en BibTeX, para importarlas en Zotero u otro gestor |

Los textos completos de terceros y las exportaciones de Scopus no se versionan, porque sus licencias no permiten redistribuirlos, pero se reproducen con el protocolo.

Los metadatos están en [`CITATION.cff`](CITATION.cff).
