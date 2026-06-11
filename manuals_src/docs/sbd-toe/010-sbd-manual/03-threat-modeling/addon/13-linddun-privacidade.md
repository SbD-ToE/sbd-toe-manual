---
id: linddun-privacidade
title: LINDDUN — Threat Modeling de Privacidade
description: Metodologia LINDDUN para threat modeling de privacidade — as sete categorias de ameaça, mapeamento a data flow diagrams e aplicação a sistemas L3 e a dados pessoais ou regulados. Complementa o threat modeling de segurança (STRIDE); não substitui a avaliação legal de conformidade.
tags: [LINDDUN, privacidade, threat-modeling, RGPD, DPIA, dados-pessoais, DFD, KU-Leuven, L3]
sidebar_position: 13
---

<!--template: sbdtoe-addon -->

# LINDDUN — Threat Modeling de Privacidade

## Âmbito e propósito

O threat modeling de segurança (STRIDE) protege o sistema contra um adversário. O threat modeling de **privacidade** protege a pessoa cujos dados o sistema processa — um problema distinto, com ameaças que o STRIDE não captura. O LINDDUN, desenvolvido na KU Leuven, é a metodologia de referência para esse problema.

O manual já inclui um [exemplo aplicado de LINDDUN](/sbd-toe/sbd-manual/threat-modeling/exemplo-privacidade-lindunn). Este addon fornece o **método** que o sustenta, para que possa ser aplicado a qualquer sistema, e não apenas seguido como exemplo.

Aplicabilidade: **L3**, e qualquer sistema que processe **dados pessoais ou regulados**, independentemente do nível. Onde existe obrigação de *Data Protection Impact Assessment* (DPIA) sob o RGPD, o LINDDUN é o instrumento que estrutura a sua componente técnica.

> O LINDDUN estrutura a **elicitação** de ameaças à privacidade. Não substitui a avaliação legal de conformidade nem o parecer do DPO — a categoria *Non-compliance* aponta para obrigações legais, não as resolve.

---

## As sete categorias de ameaça

O acrónimo nomeia sete tipos de ameaça à privacidade:

| Categoria | Ameaça |
|-----------|--------|
| **Linking** | Relacionar dois itens de interesse (dados ou ações) referentes à mesma pessoa, sem necessariamente a identificar |
| **Identifying** | Identificar uma pessoa concreta a partir de um conjunto de dados |
| **Non-repudiation** | Impossibilitar a pessoa de negar uma ação ou alegação que lhe é atribuída |
| **Detecting** | Inferir a existência de um item de interesse sobre a pessoa, mesmo sem aceder ao seu conteúdo |
| **Data Disclosure** | Expor ou aceder indevidamente a dados pessoais |
| **Unawareness** | A pessoa não está informada sobre a recolha, o processamento ou a partilha dos seus dados |
| **Non-compliance** | O sistema não cumpre os princípios e obrigações de proteção de dados |

> A nomenclatura atual (*Linking, Identifying, Detecting, Data Disclosure*) substitui os termos anteriores ainda encontrados em material mais antigo (*Linkability, Identifiability, Detectability, Disclosure of information*). São equivalentes.
>
> A categoria *Non-repudiation* é, em privacidade, uma **ameaça** — o oposto do seu papel em segurança, onde a não-repudiação é um objetivo. Para a pessoa, a impossibilidade de negar uma ação pode ser um risco (por exemplo, expor uma orientação política ou de saúde). A inversão é deliberada e deve ser compreendida ao aplicar o modelo.

---

## O método

1. **Modelar o sistema num DFD.** Representar o sistema num *data flow diagram* — entidades externas, processos, data stores e fluxos de dados. O DFD é a base sobre a qual as ameaças são mapeadas; sem ele, a elicitação é difusa.
2. **Mapear categorias aos elementos do DFD.** Cada tipo de elemento é suscetível a um subconjunto das sete categorias. O mapeamento elemento-categoria é o que torna a análise sistemática em vez de dependente da intuição.
3. **Elicitar ameaças concretas.** A partir de cada par (elemento, categoria), derivar ameaças específicas, apoiado pelas *threat trees* do LINDDUN ou, numa abordagem mais leve, pelas cartas do **LINDDUN GO**.
4. **Priorizar e mitigar.** Ordenar as ameaças por risco para a pessoa e por sensibilidade dos dados (Cap. 01), e derivar requisitos de privacidade e medidas de mitigação — minimização, anonimização, consentimento, transparência.
5. **Ligar às obrigações legais.** Ancorar as ameaças e mitigações às obrigações aplicáveis (RGPD, DPIA), em articulação com o DPO. A categoria *Non-compliance* é a ponte para esta camada.

---

## Relação com o threat modeling de segurança

LINDDUN e STRIDE são complementares e não intermutáveis. Um sistema pode ser seguro e, ao mesmo tempo, violar a privacidade — recolher dados em excesso, reter sem base legal, permitir reidentificação. A privacidade não é um subconjunto da segurança. Sistemas que processam dados pessoais devem aplicar ambos, sobre o mesmo DFD.

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| [Cap. 03 — Exemplo de privacidade (LINDDUN)](/sbd-toe/sbd-manual/threat-modeling/exemplo-privacidade-lindunn) | Aplicação concreta deste método |
| [Cap. 03 — Metodologias e ferramentas](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas) | Threat modeling de segurança (STRIDE), complementar |
| [Cap. 01 — Classificação de aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) | Sensibilidade de dados como base de priorização |

> **Sobre a curadoria:** Consolidado a partir de LINDDUN (KU Leuven, linddun.org), RGPD (obrigações de DPIA e minimização) e NIST Privacy Framework. Metodologia de elicitação de ameaças à privacidade — complementa o threat modeling de segurança e não substitui a avaliação legal de conformidade.
