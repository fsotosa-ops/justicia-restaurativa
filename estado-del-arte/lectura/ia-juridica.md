# Lectura completa de seis textos de IA aplicada al derecho

2 de noviembre de 2026. Seis textos leídos en el PDF, con página impresa. Antes de leer se confirmó que cada archivo corresponde al artículo que indica su nombre. Las cifras de las figuras y tablas se leyeron como imagen: Magesh y colegas, Figuras 4 y 5; Dahl y colegas, Figuras 1 y 8 y Tabla 6; Makasi y colegas, Figura 2. Cada hallazgo se marca como [DATO], cuando es un resultado medido por el estudio, o como [CONCLUSIÓN DEL AUTOR], cuando es una interpretación, una recomendación o un argumento normativo. Si el dato viene de otro estudio citado por los autores, se indica.

Las cuatro preguntas del proyecto con que se lee cada texto son las siguientes: (a) qué tan fiable es hoy la IA que informa sobre derecho a quien no es abogado; (b) qué puede decir un agente sin poner en riesgo a quien consulta; (c) cómo se explica o se hace auditable una respuesta; y (d) cómo se representa el conocimiento jurídico o procedimental.

| Texto | Páginas leídas | Diseño | Pregunta a la que más aporta |
|---|---|---|---|
| Magesh y colegas (2025) | 216–234 (cuerpo completo; apéndices no) | Evaluación preregistrada de 202 consultas en cuatro sistemas | (a), (c) |
| Dahl y colegas (2024), preprint arXiv | 1–36 (cuerpo); tablas 37–40 | 800.000 consultas a cuatro modelos generales sobre fallos federales | (a), (b) |
| Wachter, Mittelstadt y Russell (2024) | 1–14, 27–28, 33–34 | Análisis jurídico-conceptual del derecho de la UE | (b) |
| Makasi y colegas (2020) | 1–11 del PDF (texto completo) | Marco conceptual ilustrado con 15 chatbots públicos | (b), (c) |
| Ariai, Mackenzie y Demartini (2025) | 163:1–163:30 (sin referencias) | Revisión sistemática de 131 estudios | (c), (d) |
| Habernal y colegas (2024) | 557–583 | Corpus anotado de 373 sentencias del TEDH y modelo de minería de argumentos | (d) |

## 1. Magesh y colegas (2025)

Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., & Ho, D. E. (2025). Hallucination-free? Assessing the reliability of leading AI legal research tools. *Journal of Empirical Legal Studies, 22*(2), 216–242. https://doi.org/10.1111/jels.12413

**Diseño y datos.** Se preregistraron 202 consultas jurídicas de Estados Unidos, de las cuales 80 son de investigación general, 70 dependen de la jurisdicción o del tiempo, 22 tienen premisa falsa y 30 piden datos de un caso (p. 223). Las consultas se aplicaron entre marzo y mayo de 2024 a Lexis+ AI, Westlaw AI-Assisted Research y Ask Practical Law AI, que recuperan documentos antes de responder (RAG), y a GPT-4 sin recuperación (p. 224). Las respuestas se codificaron a mano, con un kappa de Cohen de 0,77 entre evaluadores (p. 224). Una respuesta se considera alucinada si es incorrecta o si cita una fuente que no sostiene lo que afirma (p. 221). Conviene notar que a GPT-4 se le indicó «Do not hedge unless absolutely necessary» (p. 224), lo que puede elevar su tasa de error frente a un uso sin esa instrucción.

**Hallazgos.**

- [DATO] p. 225, Figura 4 (leída como imagen): respuestas exactas, incompletas y alucinadas por sistema. Lexis+ AI 65%, 18% y 17%; Westlaw 42%, 25% y 33%; Practical Law 20%, 63% y 17%; GPT-4 49%, 8% y 43%. El texto de la misma página dice 41% y 19% de exactitud para Westlaw y Practical Law, una diferencia de un punto con la figura. En la p. 224: «Over 1 in 6 of our queries caused Lexis+ AI and Ask Practical Law AI to respond with misleading or false information. Westlaw hallucinated substantially more … one-third of its responses contained a hallucination».
- [DATO] p. 225, pie de la Figura 4: «Westlaw AI-AR and Ask Practical Law AI respond to fewer queries than GPT-4, but the responses that they do produce are not significantly more trustworthy». En otras palabras, la ventaja sobre GPT-4 de dos de las tres herramientas viene en buena parte de que se abstienen más, no de que acierten más cuando responden.
- [DATO] p. 231: «we found that Lexis+ AI, AI-AR, and GPT-4 were quite capable of navigating our false premise queries, and often corrected the false premise without hallucination». En la misma página, la Tabla 6 atribuye a la complacencia con el usuario el 6%, el 0% y el 3% de las alucinaciones de Lexis, Westlaw y Practical Law, respectivamente, mientras que el error de razonamiento explica el 28%, el 61% y el 49%. Por su parte, en la p. 225 la exactitud es más alta en las preguntas de premisa falsa que en las demás categorías.
- [CONCLUSIÓN DEL AUTOR] p. 222, sobre citar una fuente real que no dice lo afirmado: «These errors are potentially more dangerous than fabricating a case outright, because they are subtler and more difficult to spot». Verificarlas exige, según los autores, abrir la fuente, leerla y compararla con la proposición (p. 222).
- [CONCLUSIÓN DEL AUTOR] p. 233: «the evaluation of benchmarking of AI systems may be far easier for tools that accomplish specific, well-defined legal tasks». En la misma página proponen usar estas herramientas «as the first step of legal research rather than the last word». Además, en la p. 224 advierten que aceptar premisas falsas «poses a particular risk for pro se litigants and lay parties».

**Qué aporta al proyecto.** Responde a la pregunta (a) con la mejor evidencia disponible, aunque para abogados y derecho estadounidense, ya que ningún sistema bajó del 17% de respuestas alucinadas, y además separa el error de contenido del error de respaldo, lo que da un criterio para auditar una respuesta (c): que cada afirmación clave cite una fuente que efectivamente la sostenga. Para la pregunta (b) sugiere acotar la tarea, porque una herramienta con tareas bien definidas es más evaluable que un chat abierto. Los propios autores reconocen que la utilidad debe medirse con personas usando el sistema (p. 232), lo que este estudio no hace.

## 2. Dahl y colegas (2024)

Dahl, M., Magesh, V., Suzgun, M., & Ho, D. E. (2024). *Large legal fictions: Profiling legal hallucinations in large language models* (arXiv:2401.01301v2) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2401.01301. Versión publicada: *Journal of Legal Analysis, 16*(1), 64–93.

**Advertencia de paginación.** Se leyó el preprint de arXiv (v2, 21 de junio de 2024); todas las páginas citadas abajo son las del arXiv, que coinciden con las del PDF. El README cita la versión publicada en *Journal of Legal Analysis*, cuya paginación es otra y cuyas cifras podrían diferir: Magesh y colegas, citando a Dahl y colegas (2024), dan un rango de 58% a 82% (p. 218 de Magesh), mientras que el arXiv da 58% a 88%. Antes de citar cifras con la versión publicada hay que cotejarlas en ella.

**Diseño y datos.** Se tomaron 5.000 fallos por nivel de la justicia federal de Estados Unidos (Corte Suprema, cortes de apelación y cortes de distrito), por muestreo estratificado (p. 17), y se hicieron preguntas sobre cada fallo: si existe, quién lo redactó, qué resolvió, cuál es su holding, entre otras (pp. 13–17). Se ejecutaron más de 800.000 consultas a GPT-4, GPT-3.5, PaLM 2 y Llama 2 (p. 21). Las respuestas se compararon con metadatos verificados y, en las tareas sin referencia, se detectaron contradicciones entre dos respuestas del mismo modelo, de modo que en esas tareas la tasa es una cota inferior (pp. 18–20). Se trata, por tanto, de preguntas de conocimiento sobre jurisprudencia, no de consultas de personas sobre su problema.

**Hallazgos.**

- [DATO] p. 3, Figura 1 (leída como imagen), y p. 6: «LLMs hallucinate between 58% (ChatGPT 4) and 88% (Llama 2) of the time». Las tasas por modelo son 0,58 para GPT-4, 0,69 para GPT-3.5, 0,72 para PaLM 2 y 0,88 para Llama 2, con todas las tareas con referencia agrupadas.
- [DATO] p. 30, Figura 8 (leída como imagen), y p. 39, Tabla 6: ante premisas falsas construidas a propósito (un voto disidente que no existió o el año en que se revocó un fallo nunca revocado), la tasa de alucinación fue 0,69 para GPT-4, 0,52 para GPT-3.5, 0,99 para PaLM 2 y 0,02 para Llama 2. Sin embargo, en la p. 31 los autores advierten que el buen resultado de Llama 2 «is linked to a different kind of hallucination … Llama 2 often states that the case or justice does not exist at all».
- [DATO] p. 33: «In all cases, the calibration error is in the positive direction: our LLMs systematically overestimate their confidence relative to their actual rate of hallucination». En la p. 32, GPT-4, el modelo con menos alucinaciones, está peor calibrado (ECE 0,190) que PaLM 2 (0,057) y GPT-3.5 (0,099).
- [CONCLUSIÓN DEL AUTOR] p. 34: «In short, we find that the risks are highest for those who would benefit from LLMs most … under-resourced or pro se litigants». En la misma página los autores enumeran cuatro situaciones de mayor riesgo, entre ellas formular preguntas con premisas equivocadas y no saber cuánto confiar en la respuesta.
- [CONCLUSIÓN DEL AUTOR] p. 36: «developers of legal LLMs will need to make choices about which type(s) of hallucinations to minimize, and they should make these choices transparent to their downstream users». Esto se apoya en el argumento de la p. 11 de que la fidelidad a la pregunta del usuario y la fidelidad a los hechos del derecho pueden entrar en conflicto.

**Qué aporta al proyecto.** Para la pregunta (a), muestra que los modelos generales, usados sin recuperación de documentos, no son una fuente fiable de información jurídica, y que el error es mayor en los tribunales inferiores y en la información más local (pp. 34–35), que es justamente la que necesitaría un agente en Bogotá. Para la pregunta (b), el hallazgo de sobreconfianza indica que el agente no puede delegar en el modelo la decisión de cuándo dudar, y la conclusión sobre litigantes sin abogado coincide con el usuario del proyecto, aunque el estudio no observa a ninguno.

## 3. Wachter, Mittelstadt y Russell (2024)

Wachter, S., Mittelstadt, B., & Russell, C. (2024). Do large language models have a legal duty to tell the truth? *Royal Society Open Science, 11*, 240197. https://doi.org/10.1098/rsos.240197

**Diseño y datos.** Es un análisis jurídico y conceptual. Los autores definen el «careless speech» y revisan si el derecho de la Unión Europea (Carta de Derechos Fundamentales, Ley de IA, Ley de Servicios Digitales, directivas de responsabilidad por productos y por IA) y un caso alemán sobre el autocompletado de Google contienen un deber de decir la verdad aplicable a los proveedores de modelos de lenguaje. El artículo declara que no contiene datos propios (p. 34). Las páginas son las del artículo, que coinciden con las del PDF.

**Hallazgos.**

- [CONCLUSIÓN DEL AUTOR] p. 7, definición: el careless speech es «text generated in response to a factual prompt that is presented to users as authoritative, objective or factually correct», con al menos una deficiencia de contenido. Entre las deficiencias que listan en la p. 9 están «Lacking signifiers of uncertainty» y «Lacking references to source material», además de errores fácticos y resúmenes inexactos de las fuentes citadas.
- [CONCLUSIÓN DEL AUTOR] p. 5: «LLMs are incidental truth tellers. They produce accurate or truthful statements some percentage of the time». Por eso, según los autores, el riesgo principal no son las invenciones evidentes sino las inexactitudes sutiles «that only an expert would be able to detect» (p. 7).
- [CONCLUSIÓN DEL AUTOR] p. 28, sobre el artículo 50 de la Ley de IA, que obliga a avisar que se interactúa con un chatbot: «Being informed that an output is artificially generated does not provide any information about its factuality or truthfulness».
- [CONCLUSIÓN DEL AUTOR] p. 14: distinguen tres posibles titulares de deberes (usuarios, proveedores de aplicaciones de propósito específico y proveedores de modelos generales) y sostienen que «For narrow-purpose LLMs, these transfers are initially easier to justify because the systems in questions are intentionally designed to fulfil a similar purpose to existing duty-holders».
- [CONCLUSIÓN DEL AUTOR] p. 33: «we propose the creation of a legal duty to minimize careless speech for providers of both narrow- and general-purpose LLMs and derived commercial applications». Constatan además que los deberes de veracidad vigentes en el derecho de la UE son escasos y sectoriales (p. 33).

**Qué aporta al proyecto.** Para la pregunta (b), traslada el problema de la fiabilidad al de la responsabilidad: un agente de orientación jurídica es una aplicación de propósito específico que cumple una función parecida a la de quien orienta hoy, por lo que es plausible que herede sus deberes. Para la pregunta (c), su definición da una lista de verificación operativa, ya que una respuesta del agente debería señalar incertidumbre y remitir a la fuente. El análisis es del derecho europeo, de modo que la traslación a Colombia queda por hacer.

## 4. Makasi y colegas (2020)

Makasi, T., Nili, A., Desouza, K. C., & Tate, M. (2020). Chatbot-mediated public service delivery: A public service value-based framework. *First Monday, 25*(12). https://doi.org/10.5210/fm.v25i12.10598

**Advertencia de paginación.** *First Monday* publica en HTML sin paginación; el PDF es una impresión de la página web. Las páginas citadas son las del PDF, porque no existe página impresa. El nombre del archivo no indica autores: son Makasi, Nili, Desouza y Tate (p. 22 del PDF).

**Diseño y datos.** Es un marco conceptual. Los autores compilan valores del servicio público desde la literatura de valor público, los adaptan a los chatbots y llegan a 14 valores (p. 4–5 del PDF), que ilustran con ejemplos de 15 chatbots públicos de Estados Unidos, Europa, Asia y Australia (p. 5). No recogen datos de usuarios ni evalúan ningún chatbot.

**Hallazgos.**

- [CONCLUSIÓN DEL AUTOR] p. 2: distinguen tres niveles de servicio. «The first level "information provisioning" involves providing information about available services … This typically does not require authentication, and is similar to an automated 'frequently asked questions' service». El segundo nivel, de asistencia focalizada, usa datos personales, y el tercero negocia resultados con el usuario. En los tres puede intervenir un agente humano cuando el chatbot detecta que no está respondiendo bien (p. 2).
- [CONCLUSIÓN DEL AUTOR] p. 8, valor de rendición de cuentas: «if the chatbots provides a misleading advice, leading to a service failure, people know that the public service organisation accepts the responsibility for the failure. It is also important that the chatbot acknowledges its limitations».
- [CONCLUSIÓN DEL AUTOR] p. 10: «it is much more difficult to be open about the basis on which an answer is provided, if the answer is highly contextualized, personalized, and uses a generative algorithm (Level 3) than if it is simply a lookup based on a decision table (Level 1)». En la Figura 2 (leída como imagen, p. 10), la privacidad y la confianza en el gobierno crecen en importancia en el nivel 2 y la inteligencia colaborativa en el nivel 3. La figura rotula por error el tercer nivel como «Level 1».
- [DATO, de fuente secundaria citada por los autores] pp. 7–8: los chatbots MANDI y SANDI del gobierno de Queensland, que informan sobre conflictos entre vecinos ante el tribunal civil y administrativo, «engaged in more than 10,000 interactions within the first six months of inception».
- [DATO, de fuente secundaria citada por los autores] p. 9: Nadia, un chatbot del Departamento de Servicios Humanos de Australia para personas con discapacidad, se suspendió después de que varios actores, entre ellos la agencia nacional del seguro de discapacidad, expresaran falta de confianza en su capacidad de atender a ese público.

**Qué aporta al proyecto.** Para la pregunta (b), ubica a un agente de orientación en el nivel 1, que no requiere identificar a la persona y es el más defendible, y advierte que pasar al nivel 2 (preguntar por el caso concreto) eleva la exigencia de privacidad y confianza. Para la pregunta (c), sostiene que la apertura sobre el fundamento de una respuesta es más alcanzable con tablas de decisión que con generación libre. Es un marco sin evaluación empírica, y sus ejemplos de justicia (MANDI y SANDI) son datos de prensa institucional.

## 5. Ariai, Mackenzie y Demartini (2025)

Ariai, F., Mackenzie, J., & Demartini, G. (2025). Natural language processing for the legal domain: A survey of tasks, datasets, models, and challenges. *ACM Computing Surveys, 58*(6), Article 163. https://doi.org/10.1145/3777009

**Diseño y datos.** Revisión que declara seguir PRISMA, con búsquedas solo en Google Scholar e IEEE Xplore y ventanas de años distintas por tarea, por ejemplo 2020–2024 para preguntas y respuestas jurídicas (p. 163:9). De 154 estudios identificados se retuvieron 131 (p. 163:10). Admite estudios no revisados por pares (p. 163:10). Organiza el campo en seis tareas (preguntas y respuestas, predicción de sentencias, clasificación, resumen, reconocimiento de entidades y minería de argumentos), corpus y modelos, y cierra con 16 desafíos abiertos (pp. 163:26–163:30).

**Hallazgos.**

- [DATO de la revisión] p. 163:10: «Of the original 154 studies, 131 met the inclusion criteria and were retained». En la p. 163:10 los autores definen además la tarea de preguntas y respuestas como orientada a «providing legal advice, helping individuals and businesses navigate the complex legal landscape».
- [CONCLUSIÓN DEL AUTOR] p. 163:28, desafío 10: «There is a noticeable gap in the research across various areas of the legal domain, including Intellectual Property, Criminal Law, Banking Law, Family Law, and Human Rights Law».
- [CONCLUSIÓN DEL AUTOR] p. 163:28, desafío 7: «The use of ontologies in the legal domain is relatively sparse», y en el mismo párrafo: «Legal ontologies must be dynamic, reflecting changes in law and its interpretation over time».
- [CONCLUSIÓN DEL AUTOR] p. 163:29, desafío 15: «we must ensure that tools and algorithms aimed at automating legal processes do not become decision makers, rather that they are framed as decision support tools». En la misma página, el desafío 16 lista los problemas pendientes de la recuperación aumentada en derecho: varias jurisdicciones, vigencia temporal del material recuperado, textos multilingües y sesgos de recuperación.
- [DATO, de otro estudio citado por los autores] p. 163:12: el sistema de Louis y colegas para preguntas sobre legislación francesa «also outputs extractive rationales, listing the exact paragraphs that justify each response». En la p. 163:11 reseñan GerLayQA, con 21.538 preguntas reales de legos sobre derecho civil alemán respondidas por abogados.

**Qué aporta al proyecto.** Para la pregunta (d), confirma que el campo representa sobre todo textos (normas, fallos, contratos) para tareas de clasificación, búsqueda y respuesta, y que las representaciones explícitas como ontologías y grafos de conocimiento son escasas. Para la pregunta (c), el desafío 3 sobre interpretabilidad y el ejemplo de citar los párrafos exactos que justifican la respuesta dan una forma concreta de auditoría. Por otro lado, que el derecho penal y el de familia estén entre las áreas menos cubiertas refuerza el vacío que el README ya señala.

## 6. Habernal y colegas (2024)

Habernal, I., Faber, D., Recchia, N., Bretthauer, S., Gurevych, I., Spiecker genannt Döhmann, I., & Burchard, C. (2024). Mining legal arguments in court decisions. *Artificial Intelligence and Law, 32*, 557–594. https://doi.org/10.1007/s10506-023-09361-y

**Diseño y datos.** Los autores diseñan un esquema de anotación de argumentos jurídicos que cruza 16 tipos de argumento tomados de la teoría jurídica (interpretación textual, sistemática, teleológica, test de proporcionalidad, precedentes, entre otros) con 5 actores (el Tribunal, el demandante, el Estado, terceros y la Comisión o Sala) (pp. 561–563). Seis estudiantes de derecho anotaron durante 12 meses, supervisados por dos posdoctorados y asesorados por dos profesores de derecho público y penal, sentencias del Tribunal Europeo de Derechos Humanos sobre los artículos 7 y 8 del Convenio (p. 566). Con ese corpus entrenan modelos RoBERTa con preentrenamiento adicional en textos jurídicos europeos (pp. 572–573) y prueban la transferencia a 20 casos del artículo 3 (p. 577).

**Hallazgos.**

- [DATO] p. 558: el corpus tiene «373 court decisions (2,395,100 tokens and 15,205 annotated argument spans)». En la p. 560 el texto habla de 393 decisiones, una inconsistencia interna; la p. 566 explica que se anotaron 375 y se excluyeron dos, lo que respalda 373.
- [DATO] p. 566: «In the first annotation round, the αu was in 0.70 s … In the rounds after that the αu was in the 0.80 s». [CONCLUSIÓN DEL AUTOR] en la misma página: «This indicates that even for human experts the argument annotation is a difficult task».
- [DATO] p. 573, Tabla 5: el mejor modelo alcanza un F1 macro de 43,13 en el tipo de argumento y de 91,36 en el actor, en el conjunto de prueba. En la p. 567, más de la mitad de los segmentos son «aplicación al caso concreto» y cerca de la mitad de las etiquetas tiene menos del 1% de los datos.
- [DATO] p. 577: al aplicar el modelo a casos de otro artículo del Convenio, «The Macro F1-score is only 31.49 compared to 43.13 on the original test data», y el actor baja de 91,36 a 83,15.
- [CONCLUSIÓN DEL AUTOR] p. 583: «we found that there is often not enough context available for predicting an argument». En la p. 562 justifican el esquema porque sigue la categorización que usan los juristas y no la lógica de premisa y conclusión habitual en el procesamiento de lenguaje.

**Qué aporta al proyecto.** Para la pregunta (d), es un ejemplo de representar conocimiento jurídico con categorías de los juristas, y muestra el costo: un año de trabajo experto para un tribunal y dos artículos, con un desempeño bajo en los tipos de argumento y que cae al cambiar de materia. Además, el modelo distingue bien quién argumenta (F1 de 91), que es justamente una de las fallas que Magesh y colegas encontraron en las herramientas comerciales (confundir lo que alega una parte con lo que resuelve el tribunal, p. 226 de Magesh). No representa procedimientos ni rutas, sino argumentos dentro de sentencias.

## Qué cambia en el README

Las propuestas siguen el orden del README. Ninguna se aplicó al archivo.

### Cambio 1. Sección 1, segundo párrafo

**Frase actual.** «A eso se suma que la inteligencia artificial jurídica todavía inventa información con frecuencia (Dahl y colegas, 2024)».

**Veredicto: la matizan.** Dahl y colegas estudian modelos generales sin recuperación de documentos (GPT-4, GPT-3.5, PaLM 2 y Llama 2), no herramientas de IA jurídica, y su medida incluye respuestas erróneas que no son invenciones (por ejemplo, atribuir mal un fallo). La IA jurídica propiamente dicha es la que evalúan Magesh y colegas, con tasas menores pero todavía altas. Además, la cifra de Dahl viene de preguntas sobre jurisprudencia federal de Estados Unidos, no de consultas de personas.

**Redacción propuesta.** «A eso se suma que la inteligencia artificial todavía se equivoca con frecuencia cuando informa sobre derecho. Los modelos de lenguaje generales dieron respuestas falsas en el 58% a 88% de las preguntas verificables sobre fallos federales de Estados Unidos (Dahl y colegas, 2024), e incluso las herramientas comerciales de investigación jurídica, que consultan bases de datos antes de responder, lo hicieron en el 17% a 33% de las consultas (Magesh y colegas, 2025)».

*Pendiente:* el rango de Dahl sale del preprint de arXiv. Si se mantiene la referencia a *Journal of Legal Analysis*, hay que verificar la cifra en esa versión, porque Magesh y colegas la citan como 58% a 82%.

### Cambio 2. Sección 5.6, oración sobre fiabilidad

**Frase actual.** «En paralelo, la fiabilidad sigue siendo el problema central: según sus resúmenes, las herramientas comerciales de investigación jurídica inventan información en una parte relevante de sus respuestas (Magesh y colegas, 2025) y los modelos generales lo hacen con más frecuencia y aceptan las premisas falsas del usuario (Dahl y colegas, 2024)».

**Veredicto por partes.**
- «inventan información en una parte relevante»: **la confirman con matiz.** La cifra es 17% a 33%, y una parte de ese error no es inventar sino citar una fuente real que no sostiene lo afirmado, que los autores consideran más peligroso por ser más difícil de detectar (p. 222). Además, la herramienta con menos alucinaciones de un tipo deja sin respuesta útil el 63% de las consultas (Practical Law, p. 225).
- «los modelos generales lo hacen con más frecuencia»: **la confirman con matiz.** En el mismo banco GPT-4 alucinó en el 43% (p. 225), pero dos de las tres herramientas no fueron significativamente más fiables que GPT-4 cuando sí respondieron (p. 225).
- «y aceptan las premisas falsas del usuario»: **la matizan y en parte la contradicen.** Dahl y colegas encuentran que GPT-4 aceptó la premisa falsa en el 69% de las preguntas sobre fallos y PaLM 2 en el 99% (p. 30). Sin embargo, en el banco de Magesh y colegas, GPT-4 y dos herramientas a menudo corrigieron la premisa falsa (p. 231), y la complacencia explica entre el 0% y el 6% de las alucinaciones de las herramientas (p. 231). El resultado depende, por tanto, del modelo y del tipo de pregunta.
- «según sus resúmenes»: ya no aplica, porque los dos textos se leyeron completos.

**Redacción propuesta.** «En paralelo, la fiabilidad sigue siendo el problema central. En un banco de 202 consultas preregistradas, las herramientas comerciales de investigación jurídica dieron respuestas falsas o mal respaldadas en el 17% (Lexis+ AI y Ask Practical Law AI) y el 33% (Westlaw) de los casos, frente al 43% de GPT-4, y parte de ese error consiste en citar fuentes reales que no sostienen lo afirmado, lo que es más difícil de detectar que un caso inventado (Magesh y colegas, 2025). Por su parte, los modelos generales aceptaron premisas falsas en preguntas sobre fallos, GPT-4 en el 69% de ellas (Dahl y colegas, 2024), aunque en el banco de Magesh y colegas el mismo GPT-4 y dos de las herramientas a menudo corrigieron la premisa, de modo que la complacencia con el usuario depende del modelo y de la pregunta. Ambos estudios miden consultas sobre derecho de Estados Unidos y ninguno observa a personas sin formación jurídica, si bien Dahl y colegas concluyen que el riesgo es mayor precisamente para quienes litigan sin abogado».

### Cambio 3. Figura 5, columna «Representa el conocimiento jurídico para una máquina», fila «IA y derecho» (✓)

**Veredicto: la matizan.** Ariai y colegas describen un campo que representa sobre todo textos jurídicos para clasificarlos, buscarlos o responder sobre ellos, y declaran que las ontologías son escasas y difíciles de mantener al día (p. 163:28). Habernal y colegas sí representan conocimiento jurídico explícito, pero son argumentos dentro de sentencias de un solo tribunal, con un F1 de 43 en el tipo de argumento (p. 573). Ninguno de los seis textos representa rutas procedimentales, es decir, qué entidad atiende qué caso y quién decide derivarlo, que es lo que el agente necesita. La lectura cubre solo dos textos de la búsqueda E8, de modo que el cambio de ✓ a ~ no está probado para toda esa literatura.

**Redacción propuesta (dos opciones).**
- Opción A, cambiar ✓ por ~ y agregar a la nota de la figura: «En IA y derecho, lo que se representa son normas, fallos y argumentos, mientras que las ontologías son escasas (Ariai y colegas, 2025) y ninguno de los textos leídos representa rutas procedimentales».
- Opción B, mantener ✓ y precisar el encabezado de la columna como «Representa normas y fallos para una máquina», agregando a la frase de cierre de la sección 6 que falta representar las rutas y quién decide en cada una.

### Cambio 4. Figura 5, columna «Orienta con IA fiable», fila «IA y derecho» (~)

**Veredicto: la confirman.** La literatura de IA y derecho sí estudia la fiabilidad y la mide con rigor (Magesh y colegas; Dahl y colegas), pero con consultas de abogados o sobre jurisprudencia, y concluye que hoy no es fiable. No se propone cambio.

### Cambio 5. Sección 6, primer párrafo

**Frase actual.** «Por último, la IA jurídica construye asistentes que responden preguntas, pero casi no los evalúa con usuarios ni los conecta con las rutas restaurativas».

**Veredicto: la confirman.** Magesh y colegas reconocen como límite de su propio estudio que la utilidad «will still fundamentally have to be determined by use cases and evaluations that involve human interactions with the system» (p. 232). Makasi y colegas proponen un marco sin evaluar ningún chatbot, y la revisión de Ariai y colegas reporta métricas de modelos. Ninguno de los seis menciona vías restaurativas, y Ariai y colegas señalan el derecho penal y el de familia entre las áreas menos cubiertas (p. 163:28).

**Redacción propuesta (agregar al final de la oración).** «…ni los conecta con las rutas restaurativas, y el derecho penal y el de familia están entre las áreas que menos ha cubierto (Ariai y colegas, 2025)».

### Cambio 6. Agregar en la sección 5.6 lo que la literatura dice sobre qué puede decir un agente

**Veredicto: falta en el README.** La sección 1 plantea la pregunta de qué puede decir un agente sin poner en riesgo a quien lo consulta, pero ninguna sección la responde con fuentes. Tres de los textos leídos convergen en acotar la tarea y declarar los límites.

**Redacción propuesta (al final de la oración sobre fiabilidad).** «Sobre qué puede decir un agente, la literatura leída converge en acotar la tarea y declarar sus límites. Las herramientas con tareas jurídicas específicas son más fáciles de evaluar que los chats abiertos (Magesh y colegas, 2025), un chatbot público que solo informa sobre servicios no necesita identificar a la persona y puede fundar sus respuestas en tablas de decisión auditables (Makasi y colegas, 2020), y avisar que se habla con una máquina no informa sobre la veracidad de lo que dice, por lo que la respuesta debería señalar su incertidumbre y remitir a la fuente (Wachter y colegas, 2024)».

### Cambio 7. Sección 10, referencias

**Veredicto: falta coherencia entre la referencia y la lectura.** La referencia de Dahl y colegas apunta a *Journal of Legal Analysis*, pero lo leído es el preprint de arXiv. Si se adoptan los cambios 1 y 2, se agregan además Wachter y colegas (2024), Makasi y colegas (2020) y Ariai y colegas (2025), con las referencias APA de las fichas de arriba.

**Redacción propuesta.** Mantener la referencia publicada solo si las cifras se verifican en ella; de lo contrario, citar el preprint: «Dahl, M., Magesh, V., Suzgun, M., & Ho, D. E. (2024). *Large legal fictions: Profiling legal hallucinations in large language models* (arXiv:2401.01301v2) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2401.01301».
