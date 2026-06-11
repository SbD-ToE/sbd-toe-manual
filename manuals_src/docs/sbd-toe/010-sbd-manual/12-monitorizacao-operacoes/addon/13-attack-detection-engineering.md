---
id: attack-detection-engineering
title: MITRE ATT&CK como Vocabulário de Detection Engineering
description: Uso do MITRE ATT&CK como vocabulário de referência para detection engineering — mapeamento de deteções a técnicas e táticas adversariais e medição de cobertura. ATT&CK é vocabulário partilhado e referência threat-informed, não uma autoridade completa nem um checklist de cobertura total.
tags: [ATT&CK, MITRE, detection-engineering, detecao, cobertura, SIEM, correlacao, threat-informed, L2, L3]
sidebar_position: 13
---

<!--template: sbdtoe-addon -->

# MITRE ATT&CK como Vocabulário de Detection Engineering

## Âmbito e propósito

O detection engineering precisa de um vocabulário comum para descrever **o que** se deteta. Sem ele, as deteções são descritas em linguagem ad-hoc por equipa, e a cobertura torna-se impossível de medir ou comparar. O MITRE ATT&CK fornece esse vocabulário: um catálogo estruturado do comportamento adversarial observado, organizado em táticas (o objetivo do adversário) e técnicas (a forma como o atinge).

Este addon integra o ATT&CK como **vocabulário de referência** para correlação e deteção — mapear cada deteção às técnicas que cobre, e medir cobertura face ao comportamento adversarial relevante. Não o integra como autoridade completa sobre deteção nem como checklist cuja meta seja "cobrir tudo".

Aplicabilidade: **L2 e L3**. O ATT&CK formaliza as menções já existentes no Cap. 12 (catálogo de requisitos, exemplos de eventos) num método de cobertura mensurável.

> Esta integração é **threat-informed e ancorada**: o ATT&CK descreve comportamento adversarial observado, não o universo do que é possível. A cobertura de técnicas é um indicador de visibilidade, não uma prova de deteção eficaz.

---

## O que o ATT&CK fornece

- **Táticas** — o objetivo do adversário num momento da intrusão. A matriz Enterprise tem 14 táticas de referência: Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact.
- **Técnicas e sub-técnicas** — a forma concreta como cada tática é executada, com um identificador estável (por exemplo, `T1059` — *Command and Scripting Interpreter*).
- **Procedimentos** — implementações específicas de uma técnica observadas em grupos e malware reais.

> O ATT&CK é versionado e evolui. A versão v19 (2026) iniciou a reestruturação da tática *Defense Evasion*. O programa deve fixar a **versão do ATT&CK em uso** ao reportar cobertura, para que medições de períodos diferentes sejam comparáveis.

---

## Integração no programa de deteção

A integração assenta em três passos:

1. **Mapear deteções a técnicas.** Cada regra de deteção, alerta ou conteúdo de correlação deve declarar a(s) técnica(s) ATT&CK que cobre, pelo identificador. O mapeamento é metadata da regra, não documentação separada.
2. **Priorizar de forma threat-informed.** Nem todas as técnicas são igualmente relevantes para um dado sistema. A priorização deve partir do threat model do sistema (Cap. 03) e do seu nível de risco (Cap. 01) — cobrir primeiro as técnicas que o modelo de ameaça identifica como plausíveis para aquele contexto.
3. **Medir cobertura.** A cobertura é a percentagem de técnicas **relevantes** com pelo menos uma deteção validada. O denominador é o conjunto de técnicas priorizadas pelo threat model, não o catálogo ATT&CK completo.

---

## Disciplina epistémica

- **Mapeado não é detetado.** Uma regra associada a uma técnica só conta como cobertura quando foi validada — testada contra a execução real ou simulada da técnica. Sem validação, o mapeamento mede intenção, não capacidade.
- **Uma deteção por técnica raramente é cobertura total.** Uma técnica tem múltiplos procedimentos; uma regra cobre tipicamente um subconjunto. A cobertura por contagem de técnicas sobrestima a deteção real.
- **A ausência de uma técnica no ATT&CK não é a ausência de uma ameaça.** O catálogo regista comportamento observado; comportamento novo precede sempre a sua catalogação.

---

## Métricas associadas

O indicador `OPS-K06` (cobertura de correlação entre fontes) ganha precisão quando expresso em termos de ATT&CK: a correlação entre fontes deve cobrir as técnicas priorizadas, não um número abstrato de regras. A cobertura de técnicas por tática revela lacunas estruturais — uma tática inteira sem deteção é um ponto cego.

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| [Cap. 12 — Correlação e anomalias](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/correlacao-anomalias) | Onde o mapeamento a técnicas estrutura as regras de correlação |
| [Cap. 12 — Exemplos de eventos](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/exemplos-eventos) | Eventos já relacionados com OSC&R / ATT&CK |
| [Cap. 12 — Integração com SIEM](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem) | Plataforma onde as deteções mapeadas são operacionalizadas |
| [Cap. 12 — KPIs e Métricas](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/kpis-metricas-operacoes) | OPS-K06, cobertura de correlação |
| [Cap. 03 — Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro) | Fonte da priorização threat-informed das técnicas a cobrir |

> **Sobre a curadoria:** Consolidado a partir de MITRE ATT&CK Enterprise (attack.mitre.org) e da prática de detection engineering threat-informed. O ATT&CK é uma referência externa versionada; a versão em uso deve ser registada nas medições de cobertura. Esta integração é metodológica — não substitui a deteção baseada no threat model próprio do sistema.
