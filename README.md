---
title: "Restorative Justice PoC"
titleEs: "Justicia restaurativa (PoC 21871)"
slug: justicia-restaurativa
excerpt: ""
date: 2026-10-30
lang: es
type: transversal
term: ""
course: ""
courseTitle: ""
tags: [Research]
publish: false
---

# Justicia restaurativa: acompañamiento a la PoC 21871

Proyecto 21871 «Tecnología para fortalecer el acceso y la restauración en la justicia», del programa Atenea (Inteligencia Artificial Urbana para Bogotá, sistema urbano Seguridad). Lo ejecuta la Alianza CAOBA con el equipo investigador de Ciencias Jurídicas de la Javeriana. La primera iteración es una prueba de concepto RAG que responde preguntas ciudadanas generales sobre acceso a la justicia y justicia restaurativa a partir de fuentes oficiales, cita la evidencia y se abstiene cuando esta no alcanza ([propuesta](contexto/propuesta-poc.md)).

Felipe participa como apoyo técnico con 20 h al mes, que corresponden a las horas de acompañamiento de la beca ICETEX, y se encarga del estado del arte, el diseño experimental y el desarrollo.

## Estado

| | |
|---|---|
| Periodo de la PoC | 1-oct-2026 a 30-ene-2027, 8 sprints quincenales ([cronograma](contexto/cronograma.md)) |
| Sprint actual | S3 (1–15 nov): inventario de fuentes (E2) y comienzo del corpus (E3) |
| Lo inmediato | Mapa del Leviatán y criterios de búsqueda para la próxima sesión ([hoja de ruta](leviatan.md)) |
| Estado del arte | Síntesis de Consensus sin lectura completa ([estado-del-arte/](estado-del-arte/)) |

## Equipo (según las reuniones)

| Persona | Rol |
|---|---|
| Lorena Vega | Investigadora principal, Ciencias Jurídicas (justicia transicional y restaurativa) |
| Edgar Efraín Castrillón | Director de la Alianza CAOBA, gerente del proyecto |
| Luis Gabriel Moreno | Vinculación técnica, NLP; tutor de Felipe para el informe ICETEX |
| Fabián Orlando Ramírez | Equipo técnico CAOBA |
| Juan, Norberto | Nombrados el 7-oct (Biblioteca Javeriana, protocolos del consultorio) |
| Jorge Salcedo | JEP, despacho del magistrado Roberto Vidal; experto consultado a título personal |

## Contenido

- [`contexto/`](contexto/): propuesta técnica, entregables E1–E7 y cronograma, extraídos de los documentos de CAOBA. Los originales están en `contexto/originales/`, fuera de git.
- [`reuniones/`](reuniones/): resúmenes de Granola del 22-sep, 23-sep, 7-oct y 28-oct.
- [`marco-de-analisis.md`](marco-de-analisis.md): el marco del equipo (cinco dimensiones salidas de las reuniones), lo levantado leído desde él y dónde se cruza con la IA.
- [`leviatan.md`](leviatan.md): las seis capas del mapa, las consultas para Gemini Notebook y Consensus, y las fuentes con su criterio de consulta.
- [`estado-del-arte/`](estado-del-arte/): el Doc del equipo, lo que falta leer y el [contraste de H1–H6](estado-del-arte/contraste-hipotesis.md) con literatura, casos aplicados y contexto.

## Discrepancias entre documentos

- La propuesta (10-sep) habla de 6 meses y un estudiante analista. El plan en Excel la reduce a 4 meses y sin estudiante.
- El 22-sep el caso de uso eran las víctimas del conflicto y la restitución de derechos. Desde el 23-sep es la justicia penal ordinaria en Bogotá.
- Granola transcribe «CAOVA»; el nombre correcto es CAOBA.

## Herramientas

- **Consensus** (MCP en `.mcp.json` del repo): búsqueda académica, autenticado el 30-oct (20 resultados con DOI; `page_size` para limitar).
- **Gemini Notebook** (`nlm`): cuaderno [Leviatán · justicia restaurativa Bogotá](https://notebook.google.com/notebook/0d8f078d-4f14-43cc-9d68-d1d4487e226d), con las 6 investigaciones por capa (30-oct, 178 fuentes).
- **Granola**: notas de las reuniones. Este plan no da acceso a las transcripciones.
