---
id: intro
title: Papéis e Responsabilidades Organizacionais
sidebar_label: Papéis e Responsabilidades
description: Os 17 papéis que intervêm na implementação do SbD-ToE, com responsabilidades mapeadas aos capítulos técnicos e regulamentos (NIS2, DORA, GDPR)
tags: [roles, responsabilidades, governance, organizacao, nis2, dora]
sidebar_position: 0
---

# Papéis e Responsabilidades Organizacionais

## Estrutura e âmbito {#estrutura-e-âmbito}

O SbD-ToE define 17 papéis organizacionais com responsabilidades específicas ligadas aos capítulos técnicos e às obrigações regulatórias (NIS2, DORA, GDPR). Cada papel é documentado com User Stories mapeadas aos capítulos onde intervêm.

Um papel é um conjunto de responsabilidades, não uma pessoa. Uma pessoa pode acumular papéis; as únicas restrições sobre quem os acumula são as incompatibilidades (por exemplo, quem escreve uma alteração não a aprova, e quem pede uma exceção não a aprova). A lista formal — papéis, aliases, especializações, compostos e incompatibilidades — é mantida como dado nesta pasta (`_roles.yaml`) e é a fonte que o grafo de conhecimento lê.

## Princípios de Atribuição {#princípios-de-atribuição}

### Atividades Existentes, Formalizadas {#atividades-existentes-formalizadas}

As atividades prescritas no SbD-ToE formalizam processos que já existem:

- Correcção de vulnerabilidades → papel Developer
- Validação de critérios de segurança → papel QA
- Priorização de requisitos de segurança → papel Product Owner
- Pipelines com controlos de segurança → papel DevOps

O manual tipifica estas atividades para rastreabilidade e conformidade regulatória.

### Flexibilidade Estrutural {#flexibilidade-estrutural}

A atribuição de papéis varia por organização. Múltiplos papéis podem concentrar-se numa pessoa, ou distribuir-se por equipas especializadas. O SbD-ToE exige execução das atividades; não prescreve estrutura organizacional.

---

## Os 17 Roles {#os-13-roles}
## 📋 Roles Cobertos {#-roles-cobertos}

Cada role tem o seu próprio documento detalhado com:
- Descrição do papel e responsabilidades gerais
- Atividades específicas por capítulo do manual
- Enquadramento regulatório (NIS2, DORA, GDPR, AI Act)
- Referências aos lifecycles onde essas atividades são detalhadas

**Roles técnicos:**
- [Developer](developer)
- [Quality Assurance (QA)](qa)
- [DevOps / SRE](devops-sre)
- [AppSec Engineer](appsec-engineer)
- [Arquitetos de Software](arquitetos-software)
- [SecOps (Operações de Segurança)](operacoes)

**Roles de produto e gestão:**
- [Product Owner](product-owner)
- [Scrum Master / Team Lead](scrum-master)
- [Tech Lead](tech-lead)
- [Gestão Executiva](gestao-executiva)

**Roles de segurança e governance:**
- [Security Champion](security-champion)
- [GRC / Compliance](grc-compliance)

**Outros domínios da organização** (o Manual diz o que tem de existir, não como trabalham):
- [RH / PeopleOps](rh-peopleops)
- [Procurement](procurement)
- [Jurídico](legal)

**Terceiros:**
- [Fornecedores / Terceiros](fornecedores-terceiros)
- [Auditores](auditores)

## Cada Papel Inclui {#cada-papel-inclui}

- Responsabilidade primária e âmbito de atuação
- Enquadramento regulatório (NIS2, DORA, GDPR, ISO, NIST)
- User Stories por capítulo
- Links aos capítulos técnicos
- Métricas de cobertura

---

## Nota: funções compostas (operacionais, não canónicas) {#nota-funções-compostas-operacionais-não-canónicas}

Em organizações com **adopção significativa de agentes AI** com tool-use no SDLC (níveis de autonomia A2+, ver [Cap. 02](../../requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia)), surge naturalmente a necessidade de operar o risco específico desses agentes — *mandates*, *intent events*, *kill-switches*, telemetria agentic, *prompt injection* em produção, *drift* de provider.

Não se cria um papel canónico novo para isto. Em vez disso, reconhece-se uma **função composta** — informalmente chamada **"AI Reliability Engineer"** — que combina, com proporções variáveis consoante a organização, três dos papéis já definidos:

- **`AppSec Engineer`** — *threat modeling* agentic, validação de *mandates*, revisão de *intent events*, resposta a *off-policy actions*
- **`DevOps / SRE`** — provisionamento de *workload identity* para agentes, *kill-switch* operacional, *sinks* de telemetria, exercício do *kill-switch*
- **`GRC / Compliance`** — conformidade regulatória dos *mandates* (AI Act, RGPD), aprovação A3/A4, auditoria periódica do registo

A função opera sob **mandate explícito do `CISO`** (ou equivalente) que delimita o que esta função pode decidir sem escalar, e mantém os papéis canónicos inalterados — preserva a estabilidade da ontologia SbD-ToE e a sua compatibilidade com o que já foi escrito no manual e nos artigos académicos que citam estes papéis.

> 🧭 **Em uma frase:** organizações maduras em agentes precisam desta função; o manual não precisa de a tipificar como papel novo. Combina-se a partir dos papéis canónicos.

---
