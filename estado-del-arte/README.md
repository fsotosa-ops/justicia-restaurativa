# Estado del arte

La síntesis del estado del arte está en el [README del repositorio](../README.md), secciones 1 a 6. Esta carpeta guarda lo que la sostiene.

| Archivo o carpeta | Qué contiene |
|---|---|
| [`busqueda/protocolo.md`](busqueda/protocolo.md) | Bloques de conceptos, ecuaciones E1 a E13, prueba de sensibilidad y registro de las dos corridas en Scopus |
| [`busqueda/ecuaciones.py`](busqueda/ecuaciones.py) | Genera las ecuaciones y la URL de cada una |
| [`busqueda/corpus.py`](busqueda/corpus.py) y [`busqueda/conexion.txt`](busqueda/conexion.txt) | Unifica las exportaciones y mide cuántos pares de documentos comparten referencias |
| [`busqueda/grafos.R`](busqueda/grafos.R) y [`busqueda/grafos/`](busqueda/grafos/) | Cocitación, palabras clave y mapa temático con bibliometrix, más los grupos de cada red |
| [`busqueda/revision-e10.csv`](busqueda/revision-e10.csv), [`revision-e11.csv`](busqueda/revision-e11.csv) y [`revision-e12.csv`](busqueda/revision-e12.csv) | Revisión por título y resumen de los cruces E10 a E12, con la decisión y su motivo |
| [`busqueda/prisma.py`](busqueda/prisma.py) | Diagrama de flujo PRISMA 2020 de la búsqueda |
| [`lectura/`](lectura/) | Fichas de lectura en texto completo, con citas y páginas, y el cotejo de fuentes |
| [`contraste-hipotesis.md`](contraste-hipotesis.md) | Contraste de las hipótesis H1 a H6, primero con resúmenes y después con 22 textos completos cotejados en el PDF |
| [`lectura-gemini-2026-10-30.md`](lectura-gemini-2026-10-30.md) y [`prompt-lectura-gemini.md`](prompt-lectura-gemini.md) | Salida sin editar del cuaderno de lectura de Gemini y las reglas que se le dieron |
| [`consensus-hilo-2026-10-30.md`](consensus-hilo-2026-10-30.md) | Consultas de Consensus usadas para el contraste inicial |

El documento de trabajo del equipo es el Google Doc [«Justicia restaurativa en Colombia y agentes de IA»](https://docs.google.com/document/d/1rVOEqIFU9WSb554K3JUJLBeF2PCU98-E6-1-WaPMuyE), que se edita en su lugar. Los PDF (`pdfs/`) y las exportaciones de Scopus (`busqueda/scopus/`) no se versionan.
