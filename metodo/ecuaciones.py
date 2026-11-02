"""Ecuaciones de búsqueda en Scopus para el estado del arte de justicia restaurativa e IA.

Tres literaturas, que salen del marco de análisis y no del producto:
  acceso         acceso a la justicia: necesidades jurídicas, capacidad legal, puertas y rutas (dimensión A)
  restaurativa   justicia restaurativa en lo penal: derivación, operadores, VIF y efectos (dimensión C)
  ia             IA y derecho: información a la ciudadanía, fiabilidad, conocimiento jurídico computable
                 y lenguaje judicial (dimensiones B, D y E)
y cuatro ecuaciones de cruce entre ellas.

Campo TITLE-ABS-KEY, sin filtro de años. El comodín * trunca y ? reemplaza un carácter.

    python3 metodo/ecuaciones.py      # escribe ecuaciones.json con la URL de cada una
"""
import json
import urllib.parse
from pathlib import Path

B = {
    # Literatura 1: acceso a la justicia
    'AJ': '"access to justice" OR "legal need*" OR "justiciable problem*" OR "justiciable event*" OR "legal problem*" '
          'OR "legal capabilit*" OR "legal empowerment" OR "legal aid" OR "legal assistance" OR "legal literacy" '
          'OR "legal consciousness" OR "rights consciousness" OR "acceso a la justicia" OR "necesidades jurídicas"',
    'RUTA': '"one-stop" OR "justice centre*" OR "justice center*" OR "casas de justicia" OR referral* OR triage '
            'OR "legal information" OR "legal advice" OR "legal pathway*" OR "justice pathway*" OR "justice journey*" '
            'OR navigat* OR "help-seeking" OR "advice-seeking" OR "first point of contact" OR "online dispute resolution" '
            'OR "online court*" OR advice OR adviser* OR advisor* OR "dispute resolution" OR "use of court*" OR "court use" '
            'OR inaction OR "no action" OR pathway*',

    # Literatura 2: justicia restaurativa en lo penal
    'JR': '"restorative justice" OR "victim-offender mediation" OR "victim offender mediation" OR "penal mediation" '
          'OR "criminal mediation" OR "restorative conferenc*" OR "restorative practice*" OR "peacemaking circle*" '
          'OR "circles of peace" OR "justicia restaurativa" OR "mediación penal"',
    'DER': 'referral* OR refer OR gatekeep* OR "gate-keep*" OR eligib* OR "case selection" OR diversion '
           'OR discretion* OR prosecutor* OR police OR "decision-making"',
    'VIF': '"domestic violence" OR "domestic abuse" OR "intimate partner violence" OR "family violence" '
           'OR "gender-based violence" OR "violence against women" OR "violencia intrafamiliar"',
    'RES': 'recidivism OR reoffending OR "re-offending" OR "repeat offending" OR "victim satisfaction" '
           'OR "procedural justice" OR "cost-effective*" OR "cost-benefit"',
    'EV': '"meta-analy*" OR "systematic review" OR "randomi?ed" OR "controlled trial" OR "quasi-experiment*"',

    # Literatura 3: IA y derecho
    'IA': 'AI OR "artificial intelligence" OR "machine learning" OR "deep learning" OR "natural language processing" '
          'OR "large language model*" OR "language model*" OR LLM* OR GPT* OR ChatGPT OR "generative AI" OR chatbot*',
    'LEG': 'legal OR judicial OR court* OR "justice system" OR jurisprud* OR lawyer* OR statut*',
    'INFO': 'chatbot* OR "conversational agent*" OR "question answering" OR "retrieval-augmented" OR "legal information" '
            'OR "legal advice" OR "legal aid" OR "self-represented" OR "self-help" OR "access to justice" OR "lay user*" OR "layperson*"',
    'HAL': 'hallucinat* OR faithful* OR "citation accuracy" OR abstention OR "factual accuracy" OR "false premise*" OR "legal reasoning error*"',
    'KG': '"knowledge graph*" OR ontolog* OR "knowledge representation" OR "legal informatics" OR "argument mining" '
          'OR "rhetorical role*" OR "legal text segmentation" OR "graph RAG" OR "GraphRAG"',
    'LANG': '"judicial language" OR "legal language" OR "plain language" OR euphemism* OR "agent deletion" '
            'OR "agentless passive" OR "victim blaming" OR "judgment* text*" OR "court decision* text*" OR "sentencing remarks"',
    'VIC': 'victim* OR violence OR "sexual assault" OR rape',

    # Filtro regional
    'G': '"Latin America*" OR Colombia* OR Bogot* OR Mexic* OR Brazil* OR Chile* OR Peru* OR Argentin*',
}


def T(*ks):
    return ' AND '.join(f'TITLE-ABS-KEY({B[k]})' for k in ks)


def O(*ks):
    return 'TITLE-ABS-KEY(' + ' OR '.join(B[k] for k in ks) + ')'


E = {
    # Literatura 1
    'E1': ('acceso', '¿Por qué la gente llega o no al sistema de justicia, y quién la orienta?', T('AJ', 'RUTA')),
    'E2': ('acceso', '¿Qué se sabe de las necesidades jurídicas en América Latina?', T('AJ', 'G')),
    # Literatura 2
    'E3': ('restaurativa', '¿Quién deriva a la vía restaurativa, con qué criterio y en qué etapa?', T('JR', 'DER')),
    'E4': ('restaurativa', '¿Cabe la vía restaurativa en la violencia intrafamiliar?', T('JR', 'VIF')),
    'E5': ('restaurativa', '¿Qué efectos tiene, según los estudios de mejor diseño?', T('JR', 'RES', 'EV')),
    # Literatura 3
    'E6': ('ia', '¿Cómo se usa la IA para informar y orientar a la ciudadanía en asuntos jurídicos?', T('IA', 'LEG', 'INFO')),
    'E7': ('ia', '¿Qué tan fiable es la IA en preguntas jurídicas?', T('IA', 'LEG', 'HAL')),
    'E8': ('ia', '¿Cómo se representa el conocimiento jurídico para que una máquina lo use?', T('IA', 'LEG', 'KG')),
    'E9': ('ia', '¿Qué se ha medido del lenguaje judicial sobre las víctimas?', T('LANG', 'LEG', 'VIC')),
    # Cruces
    'E10': ('cruce', 'Cruce: IA y justicia restaurativa', T('IA', 'JR')),
    'E11': ('cruce', 'Cruce: IA para la orientación y la derivación en el acceso a la justicia', T('IA', 'AJ', 'RUTA')),
    'E12': ('cruce', 'Cruce: la vía restaurativa vista desde el acceso a la justicia', T('JR', 'AJ')),
    'E13': ('cruce', 'Cruce completo: IA, justicia restaurativa y acceso o derivación', T('IA', 'JR') + ' AND ' + O('AJ', 'RUTA', 'DER')),
}

# Prueba de sensibilidad: artículos leídos en texto completo que cada ecuación debería recuperar.
# Se buscan con TITLE("...") para saber primero si están indexados.
SENSIBILIDAD = {
    'E1': ['Causes of Action: First Findings of the LSRC Periodic Survey',
           'Does legal aid improve access to justice in',
           'User Experiences with British Columbia'],
    'E2': ['Why People Turn to Institutions They Detest',
           "Family issues and custodial mothers' quest for justice"],
    'E3': ['Messy victims and sympathetic offenders',
           'Police Discretion and Morality in the Danish Victim-Offender Mediation',
           'The Police as Gatekeepers of Restorative Justice',
           'Gatekeeping or Gate-pushing Restorative Justice'],
    'E4': ['Using restorative justice approaches to police domestic violence and abuse',
           'Judicial Restorative Justice and Domestic Violence in Brazil',
           'Restorative Justice Processes and Intimate Partner Violence',
           'Is restorative justice appropriate for sexual assault and domestic violence'],
    'E5': ['The effectiveness of restorative justice programs: A meta-analysis',
           'Are Restorative Justice Conferences Effective in Reducing Repeat Offending',
           'An assessment of the potential outcomes in practising restorative justice'],
    'E7': ['Assessing the Reliability of Leading AI Legal Research Tools',
           'Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models'],
    'E12': ['Beyond diversion: the economic and institutional impact of criminal mediation in Thailand',
            'Mediation in Criminal Misdemeanor Cases'],
}

if __name__ == '__main__':
    salida = {}
    for k, (lit, pregunta, eq) in E.items():
        url = 'https://www.scopus.com/results/results.uri?sort=plf-f&src=s&sot=a&sdt=a&s=' + urllib.parse.quote(eq)
        salida[k] = {'literatura': lit, 'pregunta': pregunta, 'ecuacion': eq, 'url': url,
                     'sensibilidad': SENSIBILIDAD.get(k, [])}
    destino = Path(__file__).with_name('ecuaciones.json')
    destino.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding='utf-8')
    for k, v in salida.items():
        print(f"{k:4} {v['literatura']:13} {len(v['ecuacion']):5} car.  {v['pregunta']}")
