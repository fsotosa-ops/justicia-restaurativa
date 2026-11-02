# Lectura completa: IA que orienta, clasifica o deriva, e IA en procesos restaurativos

2 de noviembre de 2026. Once textos leídos en texto completo para el estado del arte del proyecto 21871 (CAOBA y Javeriana). Cada hallazgo lleva cita literal en el idioma original y página impresa. Cuando el PDF no trae foliación impresa, se dice en la ficha y se cita la página del PDF. La marca [DATO] señala lo que el estudio midió u observó, y la marca [CONCLUSIÓN DEL AUTOR] señala lo que el autor infiere, recomienda o interpreta.

## Registro de lectura

Los once archivos están en `estado-del-arte/pdfs/` y se confirmó, por título, autores y resumen de la primera página, que cada uno corresponde al artículo que indica su nombre. Se leyó el cuerpo completo de todos; las referencias solo se consultaron para ubicar citas. Las tablas y figuras con cifras clave se leyeron además como imagen.

| Archivo | Referencia breve | Extensión | Foliación que se cita | Tablas y figuras leídas como imagen |
|---|---|---|---|---|
| westermann-2023-justicebot.pdf | Westermann y Benyekhlef (2023) | 10 págs. | sin foliación impresa; página del PDF | Tablas 1 y 2 (p. 8) |
| bridging-gap-2023.pdf | Westermann y colegas (2023) | 12 págs. | sin foliación impresa; página del PDF | Tabla 1 (p. 6), Tablas 2 y 3 y Figura 3 (p. 8) |
| chatgpt-lawyer-2023.pdf | Tan y colegas (2023) | 8 págs. | sin foliación impresa; página del PDF | no tiene tablas |
| mistica-2021.pdf | Mistica y colegas (2021) | 11 págs. | pp. 217–227 impresas | Tabla 6 (p. 223), Tabla 7 (p. 224) |
| steenhuis-2024.pdf | Steenhuis y Westermann (2024), versión arXiv | 13 págs. | sin foliación impresa; página del arXiv | Tablas 3 y 4 (p. 7), Figura 2 (p. 8) |
| steenhuis-2025.pdf | Steenhuis (2025), versión arXiv | 12 págs. | sin foliación impresa; página del arXiv | Tabla 1 (p. 6), Tabla 3 (p. 8) |
| idea-eu-labor-2026.pdf | Molinari y Giacalone (2026) | 16 págs. | pp. 1–16 impresas | Figura 11 (p. 10) |
| colombia-chatbot-guia-2025.pdf | Londoño Villarreal (2025) | 12 págs. | pp. 77–88 impresas | no tiene tablas |
| ponce-lopez-2013.pdf | Ponce-López y colegas (2013) | 7 págs. | pp. 495–501 impresas | Tabla 2 (p. 501) |
| ponce-lopez-2015.pdf | Ponce-López y colegas (2015), versión enviada | 14 págs. | pp. 1–14 del preprint | Tablas IV a VII (p. 12) |
| peleg-koriat-2026.pdf | Peleg-Koriat y Asraf (2026) | 16 págs. | pp. 1–16 impresas | Tabla 3 (p. 10) |

Las versiones de Steenhuis y Westermann (2024), Steenhuis (2025) y Ponce-López y colegas (2015) no son las publicadas, de modo que sus páginas no coinciden con las que da la sección 10 del README.

## 1. Westermann y Benyekhlef (2023), JusticeBot

**Referencia.** Westermann, H. y Benyekhlef, K. (2023). JusticeBot: A methodology for building augmented intelligence tools for laypeople to increase access to justice. En *Proceedings of the Nineteenth International Conference on Artificial Intelligence and Law (ICAIL 2023)*. ACM. https://doi.org/10.1145/3594536.3595166

**Diseño y datos.** Describe una metodología para construir herramientas de apoyo a legos que combinan reglas extraídas de la ley y la jurisprudencia con resúmenes de casos, y el primer sistema desplegado, JusticeBot TAL, sobre arrendamientos en Quebec (Canadá), lanzado en julio de 2021 con el tribunal de vivienda. La evaluación con usuarios reales se limita a estadísticas de uso y a una encuesta voluntaria al final del recorrido, que respondieron 35 personas; no hay grupo de comparación ni medición de si el problema se resolvió.

**Hallazgos.**
- [DATO] p. 7: «Between the launch on 2021-07-20 and today, 2023-05-05, the JusticeBot TAL has been used over 20k times in total, and seen over 140k pages. The largest source of traffic was the website of the TAL, which provided almost 90% of the users.»
- [DATO] p. 8, Tablas 1 y 2: «Other» fue la opción elegida por el 52% de los arrendatarios y por el 52% de los arrendadores en los 60 días anteriores. Los autores lo leen en p. 7 como «users were unable to find the appropriate pathway, or that their problem was not covered».
- [DATO] pp. 7–8: «In total, 35 users chose to do so. […] 63% of the users indicated that the JusticeBot gave them the information necessary to understand their situation. 66% of the users indicated that the JusticeBot gave them a good understanding of possible next steps».
- [CONCLUSIÓN DEL AUTOR] p. 8: «This shows that even users that were not able to get an answer to their specific situation saw the usefulness of the tool.» La encuesta no distingue a quienes encontraron su ruta de quienes no, por lo que la inferencia no se sigue de los datos reportados.
- [DATO] p. 4, sobre el diseño de la salida: «they are informed of possible next steps that they can undertake to try to resolve their issue, such as speaking to a lawyer, trying to settle their situation amicably, and filing a claim at the relevant tribunal.»

**Qué aporta al proyecto.** Es el modelo más cercano de cómo orientar a un lego sin predecir ni aconsejar, porque el sistema pregunta por criterios que vienen de la ley, muestra cómo los aplicaron los jueces y termina en próximos pasos que incluyen el arreglo directo. Sin embargo, el 52% de «Other» advierte que, sin acompañamiento, la mitad de los usuarios no encuentra su ruta en un menú de temas.

## 2. Westermann y colegas (2023), Bridging the Gap

**Referencia.** Westermann, H., Meeùs, S., Godet, M., Troussel, A., Tan, J., Savelka, J. y Benyekhlef, K. (2023). Bridging the gap: Mapping layperson narratives to legal issues with language models. En *Proceedings of the Sixth Workshop on Automated Semantic Analysis of Information in Legal Text (ASAIL 2023)*. CEUR Workshop Proceedings.

**Diseño y datos.** Propone que el lego describa su situación con sus palabras y que un codificador de oraciones multilingüe le sugiera tres rutas de JusticeBot, cada una con una explicación de lo que el sistema entendió. Se evalúa fuera de línea, en Quebec (Canadá), con 58 ejemplos redactados por el equipo y 600 descripciones reales que dejaron usuarios al elegir «Other», etiquetadas por los autores entre 3.250 revisadas. No hubo prueba con usuarios.

**Hallazgos.**
- [DATO] p. 2: «When analyzing the submitted descriptions, we noticed that a significant number of the issues described by the users were, in fact, covered by existing pathways in the JusticeBot.»
- [DATO] p. 7 y Tabla 2, p. 8: con solo los ejemplos del equipo, «Overall, 54.8% of the users would be provided with a suggestion that is relevant to them by the system», con 33,3% en chinches y 79,5% en animales.
- [DATO] p. 8 y Tabla 3: al sumar las descripciones reales con validación dejando uno fuera, «74.5% of user-submitted queries would have received the relevant suggestion at the top spot, while 93.5% of users with one of the captured situations would have received a relevant suggestion in the three suggestions that they were shown». Según la Tabla 1 (p. 6), 404 de las 600 descripciones reales son de dos clases, molestias (250) y recuperación de la vivienda (154), que además se crearon como rutas nuevas (pp. 6–7).
- [DATO] p. 10: «the evaluation presented in this paper is limited to examples where the situation described by the user is already part of the JusticeBot.»
- [CONCLUSIÓN DEL AUTOR] p. 9: «the user is given a way to meaningfully verify whether the system worked, without having to understand the legal particularities of their situation». En p. 10 los autores dejan como trabajo futuro «pilot studies with end-users».

**Qué aporta al proyecto.** Muestra un mecanismo concreto para cerrar la distancia entre el relato del lego y la categoría jurídica, que es el paso donde fallaba la mitad de los usuarios de JusticeBot, y lo hace sugiriendo y dejando que la persona confirme. No obstante, el 93,5% que se cita es un acierto entre tres sugerencias medido sobre casos ya cubiertos, no el desempeño frente a una persona.

## 3. Tan y colegas (2023), ChatGPT como abogado artificial

**Referencia.** Tan, J., Westermann, H. y Benyekhlef, K. (2023). ChatGPT as an artificial lawyer? En *Workshop on Artificial Intelligence for Access to Justice (AI4AJ 2023)*. CEUR Workshop Proceedings, 3435.

**Diseño y datos.** Estudio cualitativo y exploratorio que propone criterios para evaluar la información jurídica a legos (comprensión, exactitud, completitud, confiabilidad, inocuidad y facilidad de uso) y compara ChatGPT con JusticeBot en tres casos de arrendamiento de Quebec (Canadá) que el propio ChatGPT generó. Los autores hicieron de usuarios; no hubo usuarios reales ni conteo de errores.

**Hallazgos.**
- [DATO] p. 4: «we did not choose to select real cases, but instead used ChatGPT for case generation, and then manually selected and adjusted cases».
- [DATO] p. 6: ChatGPT citó un caso inexistente, «Tan v. Bailey [2018 ONCA 260]. Despite our repeated confirmation, ChatGPT insisted that the case was genuine.»
- [CONCLUSIÓN DEL AUTOR] p. 5: «It frequently "hallucinates" answers to legal questions, generating false legal provisions and false cases.» El texto no reporta cuántas respuestas revisó ni cuántas fallaron.
- [CONCLUSIÓN DEL AUTOR] p. 3: «legal self-help tools will serve a wide range of lay people, and every minor information error may potentially lead to harmful decisions being made by laypeople.»
- [CONCLUSIÓN DEL AUTOR] p. 7: «ChatGPT is not yet accurate enough to provide legal information directly to laypeople», y en la misma página proponen que ChatGPT sirva de capa de conversación que guíe al usuario «toward the correct legal pathway in the JusticeBot».

**Qué aporta al proyecto.** Respalda, con evidencia leída completa aunque cualitativa, que un modelo general inventa normas y casos y sostiene el error cuando el usuario duda, y propone la arquitectura que el proyecto puede seguir: el modelo conversa y una base verificada por expertos responde.

## 4. Mistica y colegas (2021), triaje de solicitudes de asistencia gratuita

**Referencia.** Mistica, M., Lau, J. H., Merrifield, B., Fazio, K. y Baldwin, T. (2021). Semi-automatic triage of requests for free legal assistance. En *Proceedings of the Natural Legal Language Processing Workshop 2021* (pp. 217–227). Association for Computational Linguistics.

**Diseño y datos.** Clasificadores BERT asignan una o más de 33 áreas del derecho, incluidas «Criminal law», «Personal safety» y «Not a legal issue», a 4.062 descripciones reales que la población envió al portal de Justice Connect en Australia entre noviembre de 2020 y abril de 2021, etiquetadas por 243 abogados (p. 219). Se evalúa con validación cruzada y por subgrupos declarados; el modelo no se probó en operación ni con usuarios.

**Hallazgos.**
- [DATO] p. 221: el modelo entrenado con pesos de confianza tiene precisión alta y cobertura baja, «when it does label instances, it gets them correct 83.8% of the time»; el mejor equilibrio (pesos por anotador) logra f1 de 0,671 (Tabla 2, p. 222).
- [CONCLUSIÓN DEL AUTOR] pp. 221–222: prefieren precisión sobre cobertura porque «a more conservative low recall, high precision, system provides greater utility than a high recall, low precision, system because we are able to trust the predictions from the system in assigning lawyers with speciality in different areas of law».
- [DATO] Tabla 7, p. 224: f1 de 0,543 para mayores de 65 años y de 0,638 para aborígenes e isleños del estrecho de Torres, frente a 0,671 en el total. El texto de p. 223 da 0,540 para el mismo grupo, de modo que hay una discrepancia menor entre texto y tabla.
- [CONCLUSIÓN DEL AUTOR] p. 224: «This points to the model being systematically biased against this particular demographic, pointing to the need for explicit model debiasing.»
- [DATO] Tabla 6, p. 223: «Personal safety» queda en el tercer nivel de confiabilidad (precisión 0,575, cobertura 0,387) y «Criminal law» en el segundo (0,721 y 0,592). Además, en p. 224: «all demographic information is volunteered and not mandatory».

**Qué aporta al proyecto.** Es el único de los once que mide la equidad entre grupos, y encuentra que el clasificador rinde peor justo con los mayores, aun en las áreas donde rinde mejor en general. También muestra que la seguridad personal, la categoría más cercana a la violencia intrafamiliar, es de las que peor se clasifican, lo que pesa a favor de que esa vía no dependa de un clasificador.

## 5. Steenhuis y Westermann (2024), admisión con modelos de lenguaje

**Referencia.** Steenhuis, Q. y Westermann, H. (2024). *Getting in the door: Streamlining intake in civil legal services with large language models* (arXiv:2410.03762). arXiv. Publicado en *Frontiers in Artificial Intelligence and Applications, 395*, 155–167.

**Diseño y datos.** Plataforma de admisión en vivienda piloteada en Misuri (Estados Unidos) con cuatro programas de asistencia legal: reglas en Python para los requisitos formales y un modelo de lenguaje que lee las reglas de cada programa y responde «califica», «no califica» o pregunta (pp. 3–4). La evaluación usa 48 pares de escenario y jurisdicción generados con ChatGPT, ocho modelos y una sola abogada revisora de 11 conversaciones simuladas. No se reportan datos de usuarios reales del piloto.

**Hallazgos.**
- [DATO] p. 5: los escenarios salieron del prompt «Create 10 scenarios of tenants seeking legal aid for landlord issues», revisados y codificados a mano.
- [DATO] p. 7, Tabla 3: «models have a weighted F1-score of between 0.56 and 0.82, with the best model being GPT-4-Turbo»; por jurisdicción, ese modelo va de 0,69 en Mid-Missouri a 0,94 en Eastern Missouri (Tabla 4).
- [DATO] p. 9 y Figura 2a, p. 8: «The most common error was unnecessary follow-up questions (83 cases), while incorrect denials (3) and incorrect acceptances (49) were less frequent». La conclusión que sigue, «even the worst-performing models could be seen as safe for screening», es [CONCLUSIÓN DEL AUTOR].
- [DATO] p. 8: «In 73% of cases, the expert rater marked the overall result as correct. In 63% of cases, follow-up questions were missed that would have improved the intake.»
- [DATO] p. 6: «Initially, the model would give inappropriate advice (e.g., suggesting the tenant work things out with their landlord)», y en p. 10: «Google Gemini censored a scenario that stated "I'm a DV survivor, and my landlord won't renew my lease because they called the cops on my boyfriend."»

**Qué aporta al proyecto.** Separa lo que se puede escribir como regla de lo que necesita interpretación, y diseña el error para que caiga del lado de preguntar o aceptar y no del lado de rechazar, con una persona que hace la admisión completa. Dos advertencias sirven al agente: el modelo empujaba por su cuenta al arreglo directo, y uno de los modelos se negó a procesar un caso de violencia doméstica. Además, la conclusión de p. 10 de que los errores son «similar to those a human intake worker might make» no se midió, porque la misma página deja como trabajo futuro «evaluate human intake staff performance».

## 6. Steenhuis (2025), FETCH

**Referencia.** Steenhuis, Q. (2025). *That's so FETCH: Fashioning ensemble techniques for LLM classification in civil legal intake and referral* (arXiv:2509.07170v2). arXiv. Publicado en *Frontiers in Artificial Intelligence and Applications, 416*, 192–203.

**Diseño y datos.** Clasificador por votación ponderada de tres modelos pequeños, palabras clave y el clasificador Spot, que ubica el problema en una taxonomía de 244 nodos y muestra los dos mejores; si no hay confianza, genera preguntas de seguimiento (p. 3). Se evalúa con 419 consultas reales del servicio de referencia del Colegio de Abogados de Oregón (Estados Unidos), etiquetadas por su personal, y está en uso en ese servicio y en Virginia (pp. 2–3). No se midió el efecto en los usuarios.

**Hallazgos.**
- [DATO] p. 4: unas 300 de las 419 consultas se etiquetaron solo en el primer nivel de la taxonomía y 119 en un nodo terminal. En p. 6 el criterio da medio punto «if at least the top-level node was present in the labels».
- [DATO] Tabla 1, p. 6: el ensamble llega a 97,37% de aciertos entre las dos primeras etiquetas, GPT-5 a 96,66% y las palabras clave a 54,18%. La nota 10 de la misma página reconoce que la diferencia de 0,71 «is likely to be statistically insignificant».
- [DATO] p. 7 y Tabla 3, p. 8: de los 11 errores del ensamble, cuatro son probables errores humanos de anotación, dos son duplicados y dos son errores claros del modelo.
- [CONCLUSIÓN DEL AUTOR] p. 9: «There was no evidence of bias in the distribution of errors and safety concerns revealed by the errors appear to be minimal.» El estudio no tiene datos demográficos, de modo que el sesgo entre grupos no se examinó.
- [DATO] p. 10: «We did not measure whether faster automated referral improved real outcomes», y «OSB was only able to collect 19 "no legal problem" scenarios». En p. 4, el diseño deja una salida humana: «Applicants who are screened out are given the option to call a human intake worker».

**Qué aporta al proyecto.** Es la evidencia más sólida de que se puede clasificar el relato de un lego en una taxonomía amplia con consultas reales y a bajo costo, y de que las preguntas de seguimiento ayudan a desambiguar. Sin embargo, no dice nada sobre lo que le pasa a la persona después, ni sobre la equidad entre grupos, y el autor no observó negativas del modelo ante violencia o abuso (nota 6, p. 4), al contrario que en el estudio de 2024.

## 7. Molinari y Giacalone (2026), proyecto IDEA

**Referencia.** Molinari, M. y Giacalone, M. (2026). AI and digital justice in EU labor law. A comparative study on predictive tools and judicial transformation. *Frontiers in Artificial Intelligence, 8*, 1742239. https://doi.org/10.3389/frai.2025.1742239

**Diseño y datos.** Encuesta en línea a profesionales del derecho laboral (jueces, personal judicial, abogados, notarios y otros) en Bélgica (n = 105), Croacia (89), República Checa (79), Estonia (48), Italia (129) y Lituania (87), con entrevistas y grupos focales de 6 a 11 personas por país (pp. 6 y 12). Sobre esa base diseñan un chatbot que oriente a trabajadores y empleadores hacia negociación, mediación o juicio en despidos por causas económicas, que aún no existe. No hay usuarios del chatbot.

**Hallazgos.**
- [DATO] p. 13, nota 12: «The IDEA chatbot is currently under development […]. At this stage, preliminary pilot results, interaction examples, and a risk assessment are not yet available.»
- [DATO] Figura 11, p. 10: la opinión sobre la justicia predictiva va de 4,3 sobre 10 en Bélgica a 6,0 en Estonia. Los autores advierten en p. 6 que las cifras agregadas «should be interpreted as indicative, rather than statistically representative».
- [DATO] p. 12: «while court staff emphasized workflow gains, judges stressed due-process externalities and potential "automation bias"».
- [CONCLUSIÓN DEL AUTOR] p. 2: «A chatbot that guides users through redundancy disputes must therefore be jurisdiction-aware: it must ask the questions that actually matter in that legal order, apply the correct triggers and timelines».
- [CONCLUSIÓN DEL AUTOR] p. 13: «the prototype would not forecast the behavior of individual judges or optimize forum selection; instead, it will constrain itself to doctrine and procedure aware guidance (e.g., thresholds, deadlines, information duties)».

**Qué aporta al proyecto.** Es el único diseño del grupo que se propone derivar hacia una vía alternativa al juicio, la mediación, y lo hace con una capa de reglas visible por jurisdicción, que es lo que el proyecto necesita para la elegibilidad restaurativa. Sin embargo, es laboral y no penal, y todavía no tiene resultados. Hay además una inconsistencia: el resumen (p. 1) llama «digital development» a las cifras 8,4 y 8,0, que en p. 9 son la satisfacción con la gestión electrónica de casos y la firma electrónica.

## 8. Londoño Villarreal (2025), guía de cumplimiento para chatbots jurídicos en Colombia

**Referencia.** Londoño Villarreal, L. F. (2025). Guía de cumplimiento: regulación de IA generativa en asesoría jurídica por chatbot en Colombia. *Revista Criminalidad, 67*(2), 77–88. https://doi.org/10.47741/17943108.731

**Diseño y datos.** Análisis normativo cualitativo de fuentes secundarias y comparación con el AI Act europeo, Estados Unidos y China (p. 79), que propone una guía para quien implemente chatbots jurídicos en Colombia. No tiene datos propios ni usuarios. Las obligaciones que siguen son la lectura del autor y conviene confirmarlas en la T-323 de 2024 y en la Circular 002 de 2024 antes de citarlas como norma.

**Hallazgos.**
- [CONCLUSIÓN DEL AUTOR] p. 81: la asesoría jurídica «está regulada en Colombia y su ejercicio profesional está limitado a los abogados», mientras que los chatbots jurídicos «se limitan a la provisión de información y orientación básica, por lo que no reemplazan la labor del abogado».
- [CONCLUSIÓN DEL AUTOR] p. 81, sobre la Ley 1480 de 2011: «el diseñador debe contemplar que no es suficiente un disclaimer si no cumple con los estándares mínimos que debería tener un chatbot jurídico, como ser entrenado en el área de conocimiento, tener acceso a información actualizada, pertinente y verídica».
- [CONCLUSIÓN DEL AUTOR] p. 83, sobre la Circular 002 de 2024 de la SIC: «La circular requiere que cualquier desarrollo de IA con potencial de tratar información sensible de los usuarios realice un estudio de impacto de privacidad». En p. 85 la guía suma aviso de privacidad, consentimiento informado y sistemas de gestión del riesgo.
- [CONCLUSIÓN DEL AUTOR] p. 83: los principios de la T-323 de 2024 «también pueden ser aplicables por analogía» a los chatbots jurídicos, y en p. 86 el autor lee que exige auditorías para «verificar el riesgo de sesgo algorítmico y evaluar el impacto en las poblaciones vulnerables».
- [DATO citado de segunda mano] p. 78: según la encuesta de HiiL de 2024, solo el 37% de las personas con problemas legales buscó asesoría, aunque el 55% identificó la necesidad de actuar. Además, el texto se contradice: en p. 80 dice que la UE clasificó los chatbots como de «riesgo moderado» y en p. 83 habla de «sistemas de alto riesgo, como los chatbots jurídicos».

**Qué aporta al proyecto.** Fija el piso regulatorio para el agente en Bogotá: debe presentarse como orientación y no como asesoría, porque esta es reservada a abogados; el aviso de alcance no lo exime de dar información correcta y actualizada; y, si trata datos sensibles, necesita estudio de impacto de privacidad y gestión del riesgo, además de auditar sesgos e impacto en población vulnerable si se sigue la lectura analógica de la T-323.

## 9. Ponce-López y colegas (2013), acuerdo en mediaciones víctima-ofensor

**Referencia.** Ponce-López, V., Escalera, S. y Baró, X. (2013). Multi-modal social signal analysis for predicting agreement in conversation settings. En *Proceedings of the 2013 ACM International Conference on Multimodal Interaction* (pp. 495–501). ACM. https://doi.org/10.1145/2522848.2532594

**Diseño y datos.** Extrae 34 indicadores de conducta no verbal (mirada, agitación, postura, turnos e interrupciones) de audio, video y profundidad grabados con Kinect en mediaciones víctima-ofensor reales, y predice el grado de acuerdo que reporta el mediador. Son 26 sesiones y 28 muestras, con validación dejando uno fuera (p. 500); el texto no dice dónde se grabaron. Los participantes no usaron el sistema.

**Hallazgos.**
- [DATO] p. 500: «Data consist of a total of 26 recorded conversational sessions of about 35 minutes-per-session», y «the total number of used samples is 28».
- [DATO] pp. 497 y 500: la verdad de referencia es la opinión del mediador, de 1 a 5, binarizada, y seis de los 34 indicadores (f7 a f12) «are extracted from a report obtained before the session, which is written by the mediators».
- [DATO] Tabla 2, p. 501: la exactitud al predecir el acuerdo es 75% con una red neuronal y 71% con los otros tres métodos.
- [DATO] p. 501: el sistema es semiautomático y requiere, en promedio, una anotación manual «for each 2000 frames».
- [CONCLUSIÓN DEL AUTOR] p. 501: «We demonstrated the applicability as a tool for the experts, obtaining results upon 75% of accuracy predicting the agreement in conversational victim-offender mediation processes».

**Qué aporta al proyecto.** Aplica la IA dentro de la sesión restaurativa, para dar retroalimentación al mediador, y no antes de ella, de modo que no informa sobre orientar ni derivar. Con 28 muestras, cada caso mal clasificado mueve la exactitud en 3,6 puntos, por lo que la cifra es frágil.

## 10. Ponce-López y colegas (2015), comunicación no verbal en mediaciones víctima-ofensor

**Referencia.** Ponce-López, V., Escalera, S., Pérez, M., Janés, O. y Baró, X. (2015). *Non-verbal communication analysis in victim-offender mediations* (arXiv:1412.2122v2) [Preprint enviado a *Pattern Recognition Letters*]. Publicado en *Pattern Recognition Letters, 67*, 19–27.

**Diseño y datos.** Versión ampliada del trabajo de 2013, con 26 sesiones de mediación víctima-ofensor grabadas en Cataluña (España) con el Departamento de Justicia, 22 individuales y 4 conjuntas, 7 mediadores y 30 partes (pp. 4–5). Predice receptividad, acuerdo y satisfacción, anotadas por el mediador, con seis clasificadores, dos formas de binarizar y con o sin dos indicadores de nerviosismo anotados a mano; usa 28 muestras y validación dejando uno fuera (p. 11). Los participantes no usaron el sistema.

**Hallazgos.**
- [DATO] p. 4: las sesiones se grabaron en Barcelona (15), Vilanova i la Geltrú (4), Manresa, Tarragona y el centro penitenciario juvenil de Granollers (2 cada uno) y Terrassa (1); el 15% fueron encuentros conjuntos.
- [DATO] pp. 4–5: la «satisfacción» que se predice no es la de la víctima, sino «degree of agreement reached between the parties in relation to the mediator's expectations». Además, en p. 4: «the data protection regulations only allow one mediator to annotate each session».
- [DATO] p. 12, Tablas IV a VII: «The most predictable social response is that of satisfaction, presenting an accuracy of 86% with the FF»; acuerdo y receptividad llegan a 79%. Esas cifras son el máximo entre 24 combinaciones de método, binarización y conjunto de indicadores, y en las mismas tablas el acuerdo baja hasta 29% con otro método.
- [DATO] p. 12: «the feature chosen as being most relevant for predicting agreement is the age of the mediator».
- [CONCLUSIÓN DEL AUTOR] p. 13: «We have demonstrated the applicability of the system for use in the restorative justice field as a tool for mediators».

**Qué aporta al proyecto.** Confirma que existe IA aplicada a un proceso restaurativo penal real, pero en la sesión y como apoyo al mediador, sin relación con orientar a la persona antes de llegar. Coincide con el trabajo de 2013 en sesiones (26), duración (35 minutos) y muestras (28), por lo que, aunque ninguno de los dos lo declara, todo indica que son la misma base de datos y no dos estudios independientes.

## 11. Peleg-Koriat y Asraf (2026), juicios humanos y de IA sobre la vía restaurativa en abuso sexual

**Referencia.** Peleg-Koriat, I. y Asraf, K. (2026). Human and AI judgements of restorative responses to sexual abuse: The role of perceived severity. *Legal and Criminological Psychology*. https://doi.org/10.1111/lcrp.70053

**Diseño y datos.** Experimento con viñetas: 469 adultos de un panel en línea de Israel (241 judíos y 228 árabes) leyeron un caso de abuso sexual intrafamiliar o extrafamiliar y calificaron su gravedad y su apoyo a la justicia restaurativa en escalas de 1 a 7 (pp. 5–6). Las mismas preguntas se hicieron 40 veces a Gemini 3, Grok 4.1 y DeepSeek 3.2 en enero de 2026, con 120 respuestas en total (p. 7). No se aplica la IA a ningún proceso restaurativo ni hay víctimas usando los modelos.

**Hallazgos.**
- [DATO] p. 8: los modelos dieron más apoyo a la vía restaurativa (M = 3,95) que las personas (M = 3,11), con g de Hedges de 0,75. En ambos grupos el promedio queda por debajo del punto medio de la escala, que es 4.
- [DATO] p. 8: entre las personas, el apoyo no difirió entre abuso intrafamiliar y extrafamiliar (p = 0,384), mientras que los modelos apoyaron menos la vía restaurativa en el intrafamiliar (p = 0,010).
- [DATO] p. 7 y Tabla 3, p. 10: ChatGPT 5.2 se excluyó porque «consistently refused to respond to the prompts», y en el caso intrafamiliar Gemini no difirió de las personas (3,37 frente a 3,06; p = 0,223), mientras que Grok y DeepSeek sí.
- [CONCLUSIÓN DEL AUTOR] p. 12: «An unregulated recommendation of RJ may expose survivors to secondary victimization, subtle coercion or the reactivation of abusive dynamics», y por eso los sistemas deberían incluir «disclaimers, professional referrals, warnings about the limits of AI-generated guidance».
- [CONCLUSIÓN DEL AUTOR] p. 12: los resultados deben leerse como apertura a la vía restaurativa «under controlled experimental conditions, rather than as evidence that LLMs would recommend RJ in real-world cases». En p. 13 se reconoce que no hubo patrón externo, como expertos o sobrevivientes, para juzgar qué respuesta era la adecuada.

**Qué aporta al proyecto.** Es el texto más cercano a la pregunta del proyecto, porque mide qué le diría un modelo general a quien pregunta por la vía restaurativa en un caso de violencia sexual intrafamiliar, y la respuesta es que varía según el modelo, que algunos se niegan a responder y que los autores piden derivación profesional. Respalda, por lo tanto, que el agente no ofrezca por sí mismo la mediación en violencia intrafamiliar.

## Qué cambia en el README

Las frases se citan tal como están hoy en las secciones 5.2, 5.6 y 6. Para cada una se indica si estos textos la confirman, la matizan o la contradicen, y se propone una redacción. Las propuestas no tocan los conteos del tamizaje que no se pueden verificar con estos once textos.

**1. Sección 5.6: «solo 10 se evaluaron con usuarios reales».** Se matiza. El conteo viene del tamizaje y no se puede rehacer con siete textos, pero la lectura completa muestra que «usuarios reales» mezcla dos cosas distintas. Mistica (2021), Bridging the Gap (2023) y FETCH (2025) usan textos reales escritos por personas, aunque nadie usó el sistema, mientras que Steenhuis y Westermann (2024) y Tan (2023) usan casos generados con ChatGPT. Solo JusticeBot recogió la opinión de usuarios, y fueron 35 respuestas voluntarias sin grupo de comparación. Además, en `tamizaje-e11.csv` JusticeBot (fila 162) figura con evaluación «no», cuando tiene esa encuesta. Redacción propuesta, a continuación de la frase actual: «La lectura completa de siete de ellos muestra que incluso los mejores se evalúan con textos reales pero sin personas usando el sistema (Mistica y colegas, 2021; Westermann y colegas, 2023; Steenhuis, 2025) o con casos generados por el propio modelo (Steenhuis y Westermann, 2024), y que ninguno mide si quien lo usó resolvió su problema. El único que consultó a sus usuarios, JusticeBot, reunió 35 respuestas voluntarias, y en él la mitad de las personas eligió “Otro” porque no encontró su ruta en el menú (Westermann y Benyekhlef, 2023).»

**2. Sección 5.6: «Los trabajos más cercanos a lo que necesita el proyecto clasifican y derivan solicitudes en asistencia legal civil (Mistica y colegas, 2021; Steenhuis y Westermann, 2024; Steenhuis, 2025)».** Se matiza. Los tres hacen tareas distintas, porque Mistica asigna áreas del derecho para repartir casos entre abogados voluntarios, Steenhuis y Westermann deciden si la persona califica para un programa de vivienda y FETCH ubica el problema en una taxonomía para referirla a un abogado. Además, dos de ellos incluyen lo penal entre sus categorías, de modo que no son solo civiles. Por otro lado, faltan los dos trabajos más cercanos a orientar a un lego, JusticeBot y Bridging the Gap. Redacción propuesta: «Los trabajos más cercanos a lo que necesita el proyecto resuelven tres pasos distintos de la puerta de entrada: orientar al lego por rutas construidas con la ley y la jurisprudencia, y traducir su relato a la ruta que le sirve (Westermann y Benyekhlef, 2023; Westermann y colegas, 2023); decidir si califica para un servicio (Steenhuis y Westermann, 2024); y clasificar su problema para asignarle un abogado o referirlo (Mistica y colegas, 2021; Steenhuis, 2025).»

**3. Sección 5.6, frase nueva sobre equidad entre grupos.** El README no la trata. Redacción propuesta, tras la frase anterior: «La equidad entre grupos casi no se mide. El único estudio que la examinó encontró que el clasificador rendía peor con los mayores de 65 años (f1 de 0,543 frente a 0,671 en el total), incluso en las áreas donde mejor funcionaba (Mistica y colegas, 2021), mientras que FETCH descarta sesgos sin contar con datos demográficos (Steenhuis, 2025).»

**4. Sección 5.6, frase sobre fiabilidad («según sus resúmenes, las herramientas comerciales […] (Magesh y colegas, 2025) y los modelos generales […] (Dahl y colegas, 2024)»).** Se confirma en la dirección y se puede sumar evidencia leída completa, aunque cualitativa. Redacción propuesta, al final de esa frase: «En una prueba cualitativa con tres casos de arrendamiento, ChatGPT inventó normas y un caso judicial, y sostuvo que el caso existía cuando se le preguntó de nuevo, por lo que sus autores proponen que el modelo converse y que una base verificada por expertos responda (Tan y colegas, 2023).»

**5. Sección 5.6: «14 tocan lo penal, pero casi siempre para identificar el artículo aplicable del código, y ninguno deriva a una vía alternativa al proceso».** Se confirma para lo penal, pero conviene agregar lo que ocurre fuera de él. Redacción propuesta, a continuación: «Fuera de lo penal, JusticeBot incluye el arreglo directo entre los próximos pasos que muestra (Westermann y Benyekhlef, 2023) y el proyecto europeo IDEA diseña un chatbot que oriente hacia la negociación, la mediación o el juicio en despidos, aunque aún no tiene resultados (Molinari y Giacalone, 2026). Además, un modelo general sugirió por su cuenta al arrendatario arreglarse con el arrendador, y los autores tuvieron que impedirlo (Steenhuis y Westermann, 2024).»

**6. Sección 5.6: «solo cinco aplican la IA a un proceso restaurativo penal: dos analizan señales no verbales en mediaciones víctima-ofensor (Ponce-López y colegas, 2013, 2015) […] uno compara juicios humanos y de IA sobre respuestas restaurativas al abuso sexual (Peleg-Koriat y Asraf, 2026)».** Se contradice en parte. Peleg-Koriat y Asraf no aplican la IA a un proceso restaurativo, sino que comparan respuestas de modelos de lenguaje con las de 469 personas ante una viñeta, y por eso su código en `tamizaje-e10.csv` (fila 15) debería cambiar. Los dos trabajos de Ponce-López sí son IA dentro de mediaciones reales en Cataluña, pero comparten las mismas 26 sesiones, y lo que llaman satisfacción es la del mediador. Lu (2025) y Ali y colegas (2026) no se leyeron aquí. Redacción propuesta: «Por último, de los 57 documentos que cruzan IA y justicia restaurativa, solo cuatro aplican la IA a un proceso restaurativo penal: dos analizan señales no verbales en las mismas 26 mediaciones víctima-ofensor de Cataluña para predecir el acuerdo que reporta el mediador, con 28 muestras (Ponce-López y colegas, 2013, 2015), uno estudia la IA en la mediación de procesos penales en China (Lu, 2025) y uno simula intervenciones restaurativas con agentes (Ali y colegas, 2026). Un quinto trabajo no aplica la IA a un proceso, pero mide lo que tres modelos de lenguaje dirían a quien pregunta por la vía restaurativa en un caso de abuso sexual: los modelos se mostraron más abiertos a ella que las personas, variaron entre sí y uno se negó a responder, por lo que los autores piden derivación profesional (Peleg-Koriat y Asraf, 2026).»

**7. Sección 5.6, frase nueva sobre regulación colombiana.** El README no dice qué exige la ley a un agente como el del proyecto. Redacción propuesta, al final de la sección: «En Colombia no hay regulación específica para estos sistemas, pero según Londoño Villarreal (2025) la asesoría jurídica está reservada a los abogados, de modo que un chatbot debe limitarse a orientar; el aviso de alcance no lo exime de dar información correcta y actualizada (Ley 1480 de 2011); si trata datos sensibles, debe hacer un estudio de impacto de privacidad y gestionar el riesgo (Ley 1581 de 2012 y Circular 002 de 2024 de la SIC); y, por analogía con la Sentencia T-323 de 2024, debería auditar el sesgo y su impacto en poblaciones vulnerables.» Conviene verificar la T-323 y la Circular 002 en la fuente primaria antes de publicar esta frase.

**8. Sección 5.2: «Las herramientas de orientación funcionan mejor con una persona al lado».** Ni se confirma ni se contradice, porque ninguno de los once textos compara el sistema con y sin acompañamiento. Sin embargo, todos los diseños que se pusieron en operación dejan a una persona al final: el triaje prioriza la precisión porque el abogado completa lo que el modelo omite (Mistica y colegas, 2021), la admisión termina con una persona (Steenhuis y Westermann, 2024) y quien queda fuera puede llamar a un funcionario (Steenhuis, 2025). Redacción propuesta, antes de «De ahí que orientar…»: «En la IA jurídica no hay estudios que comparen el rendimiento con y sin acompañamiento, pero los sistemas que llegaron a operar dejan a una persona al final del recorrido, y en JusticeBot, usado sin orientador, la mitad de los usuarios no encontró su ruta (Westermann y Benyekhlef, 2023).»

**9. Sección 6: «la IA jurídica construye asistentes que responden preguntas, pero casi no los evalúa con usuarios ni los conecta con las rutas restaurativas».** Se matiza. Los sistemas más cercanos no son asistentes que respondan preguntas, sino rutas guiadas y clasificadores que llevan a una persona, y, aunque no conectan con lo restaurativo penal, dos de ellos sí apuntan a la vía amistosa en lo civil y lo laboral. Redacción propuesta: «Por último, la IA jurídica construye asistentes y clasificadores para la puerta de entrada, pero los evalúa con textos y no con personas, casi no mide la equidad entre grupos y, aunque en lo civil y lo laboral apunta al arreglo directo o a la mediación, en lo penal no conecta con las rutas restaurativas.»

**10. Sección 6, Figura 5, fila «Cruces entre literaturas», columna «Fija límites en violencia intrafamiliar» (hoy ✗).** Se contradice en parte. Peleg-Koriat y Asraf (2026) tratan justamente el límite de ofrecer la vía restaurativa en abuso sexual intrafamiliar y advierten el riesgo de victimización secundaria, y además dos estudios registran negativas de los modelos ante violencia doméstica o abuso sexual (Steenhuis y Westermann, 2024; Peleg-Koriat y Asraf, 2026). Se propone cambiar a «~». También se propone cambiar la nota de evidencia de la figura por: «de los 57 documentos que las cruzan, cuatro aplican la IA a un proceso restaurativo penal, ninguno construye un sistema para orientar o derivar, y uno mide cómo presentan la vía restaurativa los modelos generales».

**11. Sección 10, Referencias.** Faltan las entradas de Westermann y Benyekhlef (2023), Westermann y colegas (2023), Tan y colegas (2023), Molinari y Giacalone (2026) y Londoño Villarreal (2025) si se adoptan las redacciones anteriores. Las referencias de las fichas sirven para ello.
