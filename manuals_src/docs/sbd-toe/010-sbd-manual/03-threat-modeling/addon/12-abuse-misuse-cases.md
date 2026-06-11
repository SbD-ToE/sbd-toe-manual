---
id: abuse-misuse-cases
title: Método de Abuse e Misuse Cases
description: Método para derivar abuse e misuse cases — workshop cross-functional, user stories adversariais e integração no backlog de requisitos. Técnica de elicitação adversarial que alimenta o threat model e os requisitos de segurança; complementa o threat modeling estruturado, não o substitui.
tags: [abuse-case, misuse-case, threat-modeling, requisitos, user-story, backlog, OWASP, elicitacao, L2, L3]
sidebar_position: 12
---

<!--template: sbdtoe-addon -->

# Método de Abuse e Misuse Cases

## Âmbito e propósito

O manual refere abuse cases em vários pontos, mas sem um método para os produzir. Este addon fornece-o.

Um **abuse case** descreve como um adversário usa o sistema **de forma intencionalmente hostil** — o reverso de um *use case*. Onde a user story funcional captura o que um utilizador legítimo quer fazer, o abuse case captura o que um atacante quer conseguir contra o sistema. O **misuse case** é a sua formalização (na tradição de Sindre e Opdahl): um caso de uso conduzido por um actor hostil, modelado em paralelo com os casos de uso legítimos.

A função do método é tornar adversarial uma atividade que, por omissão, é centrada no utilizador legítimo. Os abuse cases são uma **técnica de elicitação** que alimenta o threat model e os requisitos de segurança.

Aplicabilidade: **L2 e L3**, nas fases de requisitos e de threat modeling.

> Os abuse cases são uma técnica **criativa e não exaustiva**. Complementam o threat modeling estruturado (STRIDE, LINDDUN) — não o substituem. A ausência de um abuse case não é prova da ausência de um caminho de abuso.

---

## O método

1. **Workshop cross-functional.** Reunir produto, desenvolvimento, segurança e QA. A diversidade de perspetivas é o que distingue abuse cases úteis de uma lista previsível — quem conhece a regra de negócio identifica abusos que o atacante genérico não revela.
2. **Derivar o reverso adversarial.** Para cada user story ou fluxo funcional relevante, formular o seu contraponto hostil: "Como atacante, quero *&lt;objetivo&gt;*, explorando *&lt;fraqueza&gt;*". Um fluxo de upload gera o abuso "carregar um ficheiro que executa código no servidor"; um fluxo de autenticação gera "enumerar contas válidas a partir das mensagens de erro".
3. **Priorizar por risco.** Ordenar os abuse cases pela classificação de risco do sistema (Cap. 01) e pela plausibilidade face ao threat model (Cap. 03). Nem todo o abuso justifica controlo; a proporcionalidade aplica-se aqui como em todo o manual.
4. **Traduzir em requisitos e critérios de aceitação adversariais.** Cada abuse case priorizado torna-se um requisito de segurança com critério de aceitação verificável, e entra no **backlog** com o mesmo rigor de uma user story funcional (Cap. 02).
5. **Alimentar testes e threat model.** Os abuse cases priorizados tornam-se casos de teste (Cap. 10) e entradas do threat model, fechando o ciclo entre o que se receia e o que se valida.

---

## Integração no backlog

Uma user story adversarial não é uma nota informal — é um requisito rastreável. Deve ter owner, critério de aceitação e estado, e ser tratada no mesmo backlog dos requisitos funcionais. Um abuse case que fica fora do backlog é uma preocupação que se perde entre sprints.

A integração no backlog é o que separa este método de um exercício pontual: o abuso identificado num workshop só altera o produto se se materializar em trabalho priorizado e seguido.

---

## Relação com o threat modeling estruturado

Os abuse cases e o threat modeling estruturado respondem a perguntas diferentes e complementares. O abuse case parte da **função** ("como se abusa deste fluxo?"); o STRIDE parte da **propriedade de segurança** ("onde falha a integridade, a confidencialidade, a disponibilidade?"). Aplicados juntos, cobrem o que cada um isoladamente deixa escapar. Os abuse cases são, tipicamente, o ponto de entrada mais acessível para equipas sem prática de threat modeling formal.

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| [Cap. 02 — Catálogo de Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/catalogo-requisitos) | Onde os requisitos adversariais derivados entram como itens rastreáveis |
| [Cap. 02 — Exemplos de aplicação](/sbd-toe/sbd-manual/requisitos-seguranca/addon/exemplos-aplicacao) | Exemplos de abusos já traduzidos em requisitos e testes |
| [Cap. 03 — Metodologias e ferramentas](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas) | Threat modeling estruturado que os abuse cases alimentam |
| [Cap. 01 — Classificação de aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) | Base de priorização por risco |
| [Cap. 10 — Estratégia de testes](/sbd-toe/sbd-manual/testes-seguranca/addon/estrategia-testes) | Onde os abuse cases priorizados se tornam casos de teste |

> **Sobre a curadoria:** Consolidado a partir de OWASP (Abuse Case guidance) e da tradição de misuse cases (Sindre & Opdahl). Método de elicitação adversarial — complementa, não substitui, o threat modeling estruturado e a análise de risco do programa.
