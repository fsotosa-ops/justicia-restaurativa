# Diccionario de datos

Los archivos están en UTF-8, separados por comas y con una fila de encabezado. Cuando una celda reúne varios valores, se separan con `|`.

## Mapa del Leviatán

### `entidades.csv`

Una fila por entidad del sistema de justicia que interviene en las rutas del proyecto (42 filas).

| Columna | Descripción |
|---|---|
| `id` | Identificador corto de la entidad, usado en `derivaciones.csv` |
| `entidad` | Nombre oficial |
| `bloque` | Rama o sector del Estado: Rama Judicial, Fiscalía, Ministerio Público, Ejecutivo nacional, Distrito o No formal |
| `nivel` | Alcance territorial u orgánico: nacional, distrital, local, comunitario, universitario o mixto |
| `depende_de` | `id` de la entidad de la que depende, si la hay |
| `norma` | Norma que crea la entidad o le asigna la función |
| `funcion_en_ruta` | Qué hace la entidad en las rutas del proyecto |
| `etapa` | Etapa del proceso en la que actúa |
| `restaurativo` | Mecanismo alterno o restaurativo que ofrece, si lo hay (conciliación, mediación, justicia restaurativa) |
| `presencia_bogota` | Sedes o cobertura en Bogotá |
| `verificacion` | Grado de verificación del dato (ver abajo) |

### `derivaciones.csv`

Una fila por derivación, es decir, por envío de un caso de una entidad a otra porque una norma lo obliga o lo permite (38 filas).

| Columna | Descripción |
|---|---|
| `id` | Identificador de la derivación (r01 a r39) |
| `ruta` | Ruta a la que pertenece: `vif` (violencia intrafamiliar), `mujeres`, `casas_justicia`, `alimentos` o `fiscalia` |
| `origen`, `destino` | `id` de las entidades que envían y reciben el caso |
| `cuando` | Qué dispara la derivación |
| `tipo` | Obligatoria, opcional u orientativa, con su matiz entre paréntesis |
| `plazo` | Plazo legal, si existe |
| `norma` | Norma que la establece, con artículo |
| `cita_corta` | Texto literal de la norma |
| `fuente` | Enlace o documento de donde se tomó |
| `verificacion` | Grado de verificación del dato (ver abajo) |

### `etapas.csv`

Una fila por etapa del proceso penal (14 filas), en el procedimiento ordinario de la Ley 906 de 2004 y el abreviado de la Ley 1826 de 2017.

| Columna | Descripción |
|---|---|
| `orden` | Posición de la etapa |
| `etapa` | Nombre de la etapa |
| `procedimiento` | Ordinario, abreviado o ambos |
| `articulos` | Artículos que la regulan |
| `dirige`, `intervienen` | Quién conduce la etapa y quién participa |
| `plazo` | Plazo legal |
| `salidas` | Formas en que el caso puede terminar en esa etapa |
| `restaurativo` | Salida restaurativa disponible en la etapa |

## Búsqueda en Scopus

### `revision-e10.csv`, `revision-e11.csv` y `revision-e12.csv`

Revisión por título y resumen de los documentos de las búsquedas combinadas E10 (IA y justicia restaurativa), E11 (IA para orientar y derivar en el acceso a la justicia) y E12 (la vía restaurativa vista desde el acceso a la justicia).

| Columna | Descripción |
|---|---|
| `n` | Número de orden en la exportación de Scopus |
| `año`, `titulo`, `doi` | Datos bibliográficos |
| `decision` | `incluye` (diseña o evalúa un sistema o aporta datos), `conceptual` (discute el tema sin sistema ni datos) o `excluye` |
| `motivo` | Razón de la decisión |
| `evaluacion_usuarios` | Solo E11: si el sistema se evaluó con usuarios (`sí`, `no` o `solo técnica`) |
| `materia` | Solo E11: área del derecho (civil, familia, laboral, consumo, general u otra) |
| `pais` | Solo E11: país de los autores o del caso |

### `bibliometria/`

Salidas de [`metodo/corpus.py`](../metodo/corpus.py) y [`metodo/grafos.R`](../metodo/grafos.R).

| Archivo | Descripción |
|---|---|
| `conexion.txt` | Fracción de pares de documentos que citan al menos una misma fuente, dentro de cada campo y entre campos (Tabla 2 del estado del arte) |
| `co-citacion-grupos.csv` | Grupo y centralidades (intermediación, cercanía y PageRank) de las 40 fuentes de la Figura 2 del estado del arte |
| `palabras-clave-grupos.csv` | Lo mismo para las 35 palabras clave de la Figura 3 |
| `mapa-tematico-terminos.csv` | Términos del mapa temático de la Figura 4, con su grupo, frecuencia y centralidades |

## Grados de verificación

| Valor | Significado |
|---|---|
| `verificado` | Se abrió el texto oficial de la norma o del documento; el paréntesis precisa la copia usada o la inferencia hecha |
| `PDF` | Solo en las fichas de evidencia: la cita se cotejó en el documento con su página |
| `cita` | Texto literal de una fuente oficial que todavía no se pudo cotejar en el original |
| `secundaria` | Viene de prensa o de un sitio jurídico, no de la fuente oficial |
| `sin verificar` | No tiene respaldo y no se usa en los documentos hasta verificarlo |
