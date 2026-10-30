# Marco de análisis: lo nuestro y lo levantado

**Fecha:** 30-oct-2026. El marco sale de las cuatro reuniones con Efraín, Luis Gabriel y Jorge ([`reuniones/`](reuniones/)), tal como las resumió Granola; no hay otro documento que lo fije. Sobre ese marco se lee lo levantado en el [Leviatán](leviatan.md) y en el [contraste de hipótesis](estado-del-arte/contraste-hipotesis.md). No se mira desde el producto ni se baja a medición.

## 1. El marco que ya usamos sin haberlo escrito

En las reuniones aparecen cinco dimensiones. Cada una tiene su origen en lo que se dijo.

| Dimensión | Qué se planteó | Dónde |
|---|---|---|
| **A. El Leviatán como sistema** | El ecosistema de justicia es un sistema con puertas, rutas y bifurcaciones que hay que dibujar completo para ver vacíos y puntos de intervención. La analogía es el sistema de salud, con niveles de atención y protocolos de urgencia. Como referente de rutas claras está la T-025, con unidades de orientación integral | 28-oct (Jorge, Luis Gabriel, Efraín) |
| **B. El conocimiento jurídico como objeto** | La base de conocimiento (normativa, jurisprudencia y academia) es independiente de los procesos, y hay que inventariar antes de modelar. A eso se suman la morfología de los textos jurídicos, la segmentación, el graph RAG y las folksonomías ontológicas, con un corpus que se actualiza solo | 22-sep y 7-oct (Luis Gabriel); 23-sep |
| **C. Lo restaurativo como concepto** | La justicia restaurativa complementa a la retributiva y no se le opone. Tiene un sentido estricto (sanciones propias, obras reparadoras) y uno amplio (el proceso mismo es restaurativo). En la justicia ordinaria es voluntaria. El reto es cultural, porque la justicia se asocia a venganza | 28-oct (Jorge) |
| **D. El lenguaje** | LEIRA corrige tres fallas del lenguaje judicial: el eufemismo, la supresión agéntica (no nombrar quién lo hizo) y la invisibilización de las víctimas. El lenguaje puede ser restaurativo o no serlo | 28-oct (Jorge) |
| **E. La infraestructura de datos** | Interoperabilidad, gobierno de datos, privacidad y reserva judicial. Los expedientes son masivos: el subcaso Casanare tiene 2,2 millones de folios. Se propuso un data mesh federado por oficina con una «oficina virtual judicial». Antecedente ético-técnico: «Ventana, la Verdad» | 28-oct; 22-sep |

Dos sujetos cruzan todas las dimensiones: **la ciudadanía**, que no sabe a qué institución acudir, y **los operadores**, que tampoco conocen las rutas (23-sep y 28-oct).

En este marco la IA no es un añadido. Ya aparece en tres dimensiones: como forma de organizar el conocimiento (B), como análisis del lenguaje (D) y como capa sobre la infraestructura (E).

## 2. Lo levantado, leído por dimensión

### A. El Leviatán
- **Lo que confirma:** las seis capas del Leviatán ya dibujan puertas, triaje, mecanismos y salidas. El Decreto 225 de 2026 crea un Sistema Distrital de Justicia con comités locales y pide interoperabilidad; es el Leviatán bogotano formalizado. El CRI de las casas de justicia (PD-AJ-10) ya funciona como «nivel de atención» que recibe, clasifica y remite, igual que en la analogía de salud.
- **Lo que matiza:** el PNUD (gráfico 31, p. 53) muestra que en los delitos casi nadie deja de actuar por no saber a qué puerta ir (4%). Pesan más la desconfianza (21%), la falta de pruebas (20%) y creer que no vale la pena (36%). En el Leviatán el problema está menos en la entrada y más en lo que pasa dentro: los cuatro puntos de quiebre de la capa 4.

### B. El conocimiento jurídico
- **Lo que hay:** el inventario de fuentes (Senado, Función Pública, Régimen Legal de Bogotá, Corte Constitucional, Fiscalía, portal MIPG de la SDSCJ) y la distinción entre norma y procedimiento que pidió Luis Gabriel.
- **Lo que no hay:** nada de lo levantado trata la morfología de los textos jurídicos, las ontologías ni los grafos de conocimiento aplicados a rutas de justicia. Esta dimensión es la propuesta propia del equipo y **todavía no tiene literatura**.

### C. Lo restaurativo
- **Lo que confirma la distinción de Jorge:** en lo ordinario la vía es voluntaria y depende de que alguien la ofrezca. La literatura de la capa 4 muestra que quien la ofrece decide por intuición y juicio moral: Hoekstra (2022) con «más intuición que criterios objetivos», Sandbye (2024) con la «formalidad blanda» y Rasmussen (2020) con el acceso arbitrario.
- **Lo que pone a prueba el reto cultural:** el 36% de quienes no actúan ante un delito dice que «no era importante» y el 21% que no confía. Eso es compatible con la lectura de Jorge (la justicia entendida como castigo), pero los datos no lo prueban; es una inferencia.
- **En el sentido amplio**, el proceso es restaurativo en sí. La evidencia más sólida apunta ahí: lo robusto es la satisfacción y la justicia procedimental de la víctima (Fulham 2023, d = 0,63; Strang 2013). En reincidencia el efecto es pequeño y frágil.
- **En violencia de género** la crítica es fuerte: Campos (2021) en Brasil y Westmarland (2018) en Inglaterra muestran la etiqueta restaurativa usada como reconciliación forzada o como cierre sin respuesta.

### D. El lenguaje
- Lo levantado no toca esta dimensión, salvo LEIRA. Campos y Westmarland muestran, sin hablar de lenguaje, que **la palabra «restaurativo» puede encubrir lo contrario**. Eso conecta con lo que LEIRA corrige en las sentencias.

### E. La infraestructura de datos
- **Lo que hay:** el art. 174.10 del Decreto 225 pide interoperabilidad; SIDIJUS tiene un módulo de mediaciones; la T-323 y el Acuerdo PCSJA24-12243 fijan privacidad, transparencia y control humano.
- **Lo que no hay:** literatura sobre arquitecturas federadas de datos judiciales o sobre la oficina virtual.

## 3. El cruce con IA: qué hay y qué falta

| Dimensión | Lo que tenemos sobre IA | Lo que falta |
|---|---|---|
| A. Leviatán | Zacatecas: priorización de carpetas (predice cierre, no ruta). CRT y LegalApp: orientación digital, que funciona mejor con alguien que acompañe (80% frente a 17%) | IA que **modele el sistema**: rutas, bifurcaciones y procedimientos como grafo, más allá de responder preguntas. El ejemplo de México del 28-oct va en esa línea |
| B. Conocimiento | Magesh (2024) y Dahl (2024): los RAG legales inventan entre 17% y 88%. Wallat (2025): las citas pueden no ser fieles | **Todo lo propio del equipo**: grafos de conocimiento jurídico, ontologías de procedimientos y segmentación de textos legales en español |
| C. Restaurativo | Nada. La literatura restaurativa no habla de IA | IA y justicia restaurativa: si un sistema puede sostener la voluntariedad y el encuentro, y cómo cambia la discrecionalidad del operador cuando decide un sistema (discrecionalidad digital, burocracia «de sistema») |
| D. Lenguaje | Solo LEIRA, como práctica sin publicar | Análisis computacional del lenguaje judicial: eufemismo, agencia y víctimas en sentencias |
| E. Infraestructura | T-323 y PCSJA24-12243 (control humano); AI Act anexo III | Gobierno de datos judiciales federados e interoperabilidad con IA |

**Lectura de conjunto.** Lo levantado sirve para la **justicia** (dimensiones A y C) y para los **riesgos de la IA** (B, por las alucinaciones, y E). El cruce entre las dos casi no existe. Y las dimensiones donde el equipo tiene su apuesta técnica, B y D, son justo las que no tienen literatura. Las fuentes del 28-oct en Consensus (Yadav 2026, Sobrino 2026 y otras) no se leyeron; son el primer lugar donde buscar ese cruce.

## 4. Preguntas para Efraín, Luis Gabriel y Jorge

1. **¿Cuál de las cinco dimensiones ordena la investigación?** La A pone el foco en el sistema y sus vacíos. La B pone el foco en el conocimiento y su forma computable. La C y la D ponen el foco en lo restaurativo y su lenguaje. Cada una lleva a una pregunta de investigación distinta.
2. Si los datos dicen que la gente no deja de actuar por no saber a dónde ir (A), sino por desconfianza y porque cree que no sirve, **¿dónde se pone la IA en el Leviatán: en la puerta o dentro, con los operadores?**
3. **¿LEIRA se cruza con este proyecto?** El lenguaje restaurativo podría ser un eje (D) que nadie más está trabajando en la justicia ordinaria.
4. **¿La JEP es un contraste o un campo?** Jorge trae el sentido estricto desde la JEP, y el proyecto está en la justicia ordinaria.
