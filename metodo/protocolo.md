# Protocolo de búsqueda en Scopus

2 de noviembre de 2026. Cada búsqueda se escribe como una ecuación de bloques de conceptos, para que se pueda repetir y verificar, y para medir cuánto cubre cada campo de estudio y si los campos se citan entre sí.

## Los campos de estudio

La búsqueda cubre tres campos: el acceso a la justicia, la justicia restaurativa en lo penal y la IA aplicada al derecho, a los que se suma el lenguaje judicial sobre las víctimas. Las ecuaciones combinadas miden si esos campos se encuentran.

## Bloques de conceptos

Cada bloque se busca en título, resumen y palabras clave (`TITLE-ABS-KEY`), sin filtro de años. La lista completa de términos está en [`ecuaciones.py`](ecuaciones.py).

| Bloque | Concepto | Ejemplos de términos |
|---|---|---|
| AJ | Acceso a la justicia | access to justice, legal need*, justiciable problem*, legal capabilit*, legal aid, rights consciousness |
| RUTA | Puertas, rutas y orientación | one-stop, justice centre*, referral*, triage, legal information, justice journey*, help-seeking, online court* |
| JR | Justicia restaurativa en lo penal | restorative justice, victim-offender mediation, penal mediation, restorative conferenc*, peacemaking circle* |
| DER | Derivación y operador | referral*, gatekeep*, eligib*, diversion, discretion*, prosecutor*, police |
| VIF | Violencia intrafamiliar y de género | domestic violence, domestic abuse, intimate partner violence, violence against women |
| RES | Resultados | recidivism, reoffending, victim satisfaction, procedural justice, cost-benefit |
| EV | Diseño de mayor evidencia | meta-analy*, systematic review, randomi?ed, controlled trial, quasi-experiment* |
| IA | Inteligencia artificial | AI, machine learning, natural language processing, large language model*, chatbot* |
| LEG | Dominio jurídico | legal, judicial, court*, justice system, jurisprud*, statut* |
| INFO | Información a la ciudadanía | chatbot*, question answering, retrieval-augmented, legal information, self-represented, access to justice |
| HAL | Fiabilidad | hallucinat*, faithful*, citation accuracy, abstention, false premise* |
| KG | Conocimiento jurídico computable | knowledge graph*, ontolog*, legal informatics, argument mining, rhetorical role*, GraphRAG |
| LANG | Lenguaje judicial | judicial language, plain language, euphemism*, agent deletion, victim blaming, sentencing remarks |
| VIC | Víctimas y violencia | victim*, violence, sexual assault, rape |
| G | América Latina (filtro) | Latin America*, Colombia*, Bogot*, Mexic*, Brazil*, Chile* |

## Ecuaciones

Cada ecuación responde una pregunta del estado del arte. La Tabla 1 las ordena por campo y deja al final las combinadas.

**Tabla 1.** Ecuaciones por campo.

| Ecuación | Campo | Pregunta | Bloques |
|---|---|---|---|
| E1 | Acceso | ¿Por qué la gente llega o no al sistema de justicia, y quién la orienta? | AJ y RUTA |
| E2 | Acceso | ¿Qué se sabe de las necesidades jurídicas en América Latina? | AJ y G |
| E3 | Restaurativa | ¿Quién deriva a la vía restaurativa, con qué criterio y en qué etapa? | JR y DER |
| E4 | Restaurativa | ¿Cabe la vía restaurativa en la violencia intrafamiliar? | JR y VIF |
| E5 | Restaurativa | ¿Qué efectos tiene, según los estudios de mejor diseño? | JR, RES y EV |
| E6 | IA | ¿Cómo se usa la IA para informar y orientar a la ciudadanía en asuntos jurídicos? | IA, LEG e INFO |
| E7 | IA | ¿Qué tan fiable es la IA en preguntas jurídicas? | IA, LEG y HAL |
| E8 | IA | ¿Cómo se representa el conocimiento jurídico para que una máquina lo use? | IA, LEG y KG |
| E9 | IA | ¿Qué se ha medido del lenguaje judicial sobre las víctimas? | LANG, LEG y VIC |
| E10 | Combinada | IA y justicia restaurativa | IA y JR |
| E11 | Combinada | IA para la orientación y la derivación en el acceso a la justicia | IA, AJ y RUTA |
| E12 | Combinada | La vía restaurativa vista desde el acceso a la justicia | JR y AJ |
| E13 | Combinada de los tres campos | IA, justicia restaurativa y acceso o derivación | IA, JR y (AJ, RUTA o DER) |

## Prueba de sensibilidad

Una estrategia es verificable si recupera textos que ya se sabe que pertenecen al campo. Para eso se usan los artículos de la búsqueda complementaria: primero se buscan por título para saber si Scopus los indexa, y después se comprueba si la ecuación correspondiente los trae. Cuando una ecuación pierde un artículo indexado, se amplía el bloque y se corre de nuevo. Las ecuaciones E6, E8, E9, E10, E11 y E13 no tienen artículos conocidos de antemano, de modo que en ellas la prueba se reemplaza por una revisión de los veinte primeros resultados.

**Tabla 2.** Artículos de control por ecuación.

| Ecuación | Artículos que debería recuperar |
|---|---|
| E1 | Pleasence y colegas (2003); Chaara y colegas (2022); Sykes y colegas (2020) |
| E2 | Hilbink y colegas (2022); Guarin y colegas (2024) |
| E3 | Hoekstra (2022); Sandbye y colegas (2024); Rasmussen (2020); Jauhiainen (2025) |
| E4 | Westmarland y colegas (2018); De Campos y De Oliveira (2021); Hudson y Berger (2026); Kettrey y Reynolds (2026) |
| E5 | Fulham y colegas (2025); Sherman y colegas (2015); Islam y colegas (2023) |
| E7 | Magesh y colegas (2025); Dahl y colegas (2024) |
| E12 | Lounkaew (2026); Charkoudian y colegas (2021) |

## Registro de corridas

Las dos corridas se hicieron el 2 de noviembre de 2026 en Scopus, con el acceso institucional de la Javeriana. La primera corrida mostró dos problemas. Por un lado, E1 perdía a Pleasence y colegas (2003) y a Chaara y colegas (2022), que están indexados, porque el bloque de rutas no reconocía «advice» a secas ni el uso de tribunales. Por otro lado, las ecuaciones de IA traían demasiados documentos, porque «citizen*» en E6 y «reliab*» en E7 son términos genéricos. En la segunda corrida se amplió el bloque de rutas y se quitaron esos dos términos, de modo que la Tabla 3 muestra cómo cambió cada ecuación.

**Tabla 3.** Documentos por ecuación en las dos corridas.

| Ecuación | Corrida 1 | Corrida 2 |
|---|---:|---:|
| E1 | 1.016 | 1.814 |
| E2 | 806 | 806 |
| E3 | 789 | 789 |
| E4 | 288 | 288 |
| E5 | 52 | 52 |
| E6 | 3.380 | 2.667 |
| E7 | 2.684 | 625 |
| E8 | 1.465 | 1.465 |
| E9 | 374 | 374 |
| E10 | 57 | 57 |
| E11 | 191 | 248 |
| E12 | 71 | 71 |
| E13 | 7 | 12 |

En la segunda corrida, cada ecuación recupera todos sus artículos de control indexados, salvo uno: E12 no trae a Charkoudian y colegas (2021), porque estudia la mediación comunitaria en faltas y no nombra la justicia restaurativa. Sykes y colegas (2020) no está indexado en Scopus.

**Tabla 4.** Resultado de la prueba de sensibilidad en la segunda corrida.

| Ecuación | Indexados | Recuperados | No indexados |
|---|---:|---:|---|
| E1 | 2 | 2 | Sykes y colegas (2020) |
| E2 | 2 | 2 | |
| E3 | 4 | 4 | |
| E4 | 4 | 4 | |
| E5 | 3 | 3 | |
| E7 | 2 | 2 | |
| E12 | 2 | 1 | |

Los 12 documentos de la ecuación que combina los tres campos (E13) muestran el vacío de forma directa, porque casi ninguno trata de justicia restaurativa con IA: aparecen, entre otros, un estudio sobre el trigo y el cambio climático, uno sobre integridad académica y otro sobre difamación en redes sociales.
