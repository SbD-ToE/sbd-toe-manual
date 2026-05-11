---
id: catalogo-requisitos-threat-modeling
title: Catálogo de Requisitos de Threat Modeling
description: Catálogo canónico de requisitos de threat modeling (THR-001 a THR-007), com aplicabilidade por nível de risco e critérios de aceitação para identificação de ameaças, disposição formal, derivação de requisitos e rastreabilidade metodológica.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:threat-modeling, THR, STRIDE, LINDDUN, DFD, ameacas, requisitos, rastreabilidade, L2, L3, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Threat Modeling

## Âmbito: o threat modeling como mecanismo formal de derivação de controlos

Este catálogo cobre os **requisitos do processo de threat modeling** — os controlos que garantem que as ameaças relevantes a um sistema são identificadas com rigor metodológico, têm disposição documentada e geram requisitos rastreáveis de segurança.

O threat modeling não é uma actividade académica: é o mecanismo pelo qual a arquitectura de um sistema traduz riscos abstractos em controlos concretos e verificáveis. Um threat model superficial ou desactualizado dá falsa confiança — é pior do que a ausência formal do artefacto, porque oculta lacunas de controlo sob a aparência de conformidade.

Os requisitos THR são verificáveis: a existência de um threat model com DFDs actuais, de disposição formal por ameaça, de rastreabilidade para o backlog e de revisão independente antes de go-live são factos auditáveis. A ausência de evidência equivale a ausência de controlo.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de NIST SSDF, NIST SP 800-30, ISO/IEC 27001, ISO/IEC 27005, OWASP SAMM v2.1, OWASP DSOMM, BSIMM13 e práticas de governação aplicacional orientadas a risco. Deve ser adaptado ao modelo organizacional de risco, mas sem perder a rastreabilidade para L1, L2 e L3.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-THR-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo THR - Threat Modeling

Requisitos que garantem que o processo de threat modeling é conduzido com rigor metodológico, produz disposição verificável para cada ameaça identificada e gera rastreabilidade de ponta a ponta para os controlos derivados.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| THR-001 | Threat modeling formal em aplicações L2+ e alterações arquitecturais significativas | - | ✔ | ✔ | Aplicações com classificação L2 ou superior têm threat model formal documentado; o processo é aplicado em novas aplicações antes de go-live e em alterações arquitecturais significativas (novo componente, nova integração externa, nova superfície de exposição); o artefacto é rastreável à versão de arquitectura avaliada. |
| THR-002 | Arquitectura actual representada com DFDs e trust boundaries explícitos | - | ✔ | ✔ | O threat model inclui Data Flow Diagrams (DFDs) actualizados que reflectem a arquitectura real em produção; trust boundaries são explicitamente marcadas e justificadas; cada fluxo de dados sensíveis identifica origem, destino, canal e nível de confiança; DFDs desactualizados invalidam a validade do threat model. |
| THR-003 | Metodologia estruturada aplicada com cobertura mínima garantida | - | ✔ | ✔ | O processo utiliza uma metodologia estruturada — STRIDE como baseline; LINDDUN em aplicações com fluxos de dados pessoais ou contexto de privacidade; PASTA ou equivalente para contextos de alto risco; a metodologia escolhida é declarada no artefacto, aplicada de forma consistente e cobre no mínimo os elementos críticos identificados nos DFDs. |
| THR-004 | Disposição formal de cada ameaça identificada com owner | - | ✔ | ✔ | Cada ameaça identificada tem disposição explícita documentada — mitigado, aceite, transferido ou excluído — com justificação racional, controlo ou compensação associado e owner nomeado; ameaças sem disposição declarada são tratadas como lacuna de controlo activa; a lista de ameaças é parte do artefacto de evidência. |
| THR-005 | Rastreabilidade ameaça → requisito → backlog → validação | - | ✔ | ✔ | As ameaças identificadas com disposição de mitigação geram requisitos de segurança rastreáveis; esses requisitos estão registados no backlog com referência ao threat ID de origem; a validação do requisito em test ou review referencia o threat ID correspondente; a cadeia é verificável sem reconstrução manual. |
| THR-006 | Threat model versionado e actualizado dentro do ciclo ou após trigger | - | ✔ | ✔ | O threat model tem controlo de versão explícito; é revisto e actualizado no máximo a cada ciclo de release significativo ou no prazo máximo de 30 dias após trigger de mudança (nova integração, alteração de trust boundary, incidente de segurança ou nova ameaça com impacto relevante); a versão do threat model é referenciada nos artefactos de arquitectura e no processo de go-live. |
| THR-007 | Revisão independente por AppSec antes de go-live em L2 e L3 | - | ✔ | ✔ | Antes de go-live de novas aplicações L2+ ou de alterações arquitecturais com impacto material num sistema L2+, o threat model é revisto por AppSec ou elemento com competência equivalente independente da equipa; a revisão produz evidência (registo, aprovação ou lista de desvios com plano); ausência de revisão bloqueia o go-live. |
| THR-008 | Threat modeling estendido para sistemas com componentes AI/ML | - | ✔ | ✔ | Sistemas que integram componentes de inteligência artificial ou machine learning (modelos preditivos, LLMs em interface conversacional, sistemas de RAG, agentes autónomos com tool invocation) têm threat model estendido que cobre ameaças adversariais específicas — model poisoning, prompt injection directa e indirecta, training data poisoning, model theft, evasion attacks, AI supply chain compromise — referenciadas a catálogos estabelecidos (MITRE ATLAS, NIST AI 100-2 e2025); o modelo identifica trust boundaries adicionais para training data, model artifacts, inference endpoints e tool invocations; STRIDE ou LINDDUN são complementados (não substituídos) com framing AI/ML conforme aplicável. |

---

## Notas explicativas

- **THR-001**: A aplicabilidade a partir de L2 é intencional — o threat modeling é um controlo com custo de execução que deve ser proporcional ao risco. Para L1, práticas de análise informal de risco são suficientes e recomendadas; para L2 e L3, a formalidade é necessária porque a complexidade dos sistemas e o impacto de comprometimento justificam o investimento.
- **THR-002**: DFDs desactualizados são o vector mais comum de invalidação de threat models em produção. Um sistema que evoluiu sem actualização do DFD tem trust boundaries erradas, fluxos não mapeados e ameaças que o threat model não cobre porque simplesmente desconhece os componentes actuais.
- **THR-003**: A distinção entre STRIDE e LINDDUN é operacionalmente importante. STRIDE cobre as categorias de ameaça clássicas de segurança (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege); LINDDUN é específico para fluxos de dados pessoais e privacidade — é insuficiente usar apenas STRIDE em sistemas com tratamento de dados pessoais sujeitos ao RGPD ou equivalente.
- **THR-004**: A disposição "excluído" (out of scope) é legítima mas requer justificação rigorosa — não é uma forma de ignorar ameaças inconvenientes. A ausência de disposição documentada é a forma mais comum de threat model formalmente existente mas operacionalmente inútil.
- **THR-005**: A rastreabilidade bidirecional (ameaça→requisito→backlog→validação e validação→backlog→requisito→ameaça) é o que transforma o threat modeling num controlo verificável. Sem ela, o threat model é um documento isolado que não influencia os controlos reais do sistema.
- **THR-006**: O TTL de 30 dias após trigger é conservador por design. Em contextos L3, o trigger de revisão pode ser mais granular (qualquer PR com impacto em trust boundaries, por exemplo). A integração do threat modeling no ciclo de CI — mesmo que em modo de revisão lightweight — é a prática recomendada para L3.
- **THR-007**: A revisão independente serve dois propósitos: cobertura de pontos cegos da equipa (que pode ter dificuldade em identificar ameaças em sistemas que conhece profundamente) e como gate de governação formal antes de go-live. A independência pode ser assegurada por equipa AppSec centralizada, por peer review de arquitecto sénior ou por consultoria especializada — o critério é a ausência de conflito de interesse com a entrega.
- **THR-008**: A extensão para sistemas AI/ML é mandatória quando o sistema integra componentes que produzem decisões, classificações ou conteúdo baseados em modelos treinados ou prompts a LLMs. As ameaças adversariais a estes componentes são qualitativamente distintas — não se reduzem a STRIDE clássico porque os alvos (training data, model weights, prompt context) e os mecanismos (adversarial examples, prompt injection, data poisoning) não têm equivalente directo em ameaças tradicionais. MITRE ATLAS fornece um catálogo de tactics/techniques específico para AI systems (formato análogo a MITRE ATT&CK); NIST AI 100-2 e2025 estabelece a taxonomia formal de adversarial ML attacks; NIST AI RMF 1.0 fornece o framework de gestão de risco AI a nível organizacional. Para metodologia operacional, consultar [Metodologias e Ferramentas — §AI/ML](./metodologias-e-ferramentas#ai-ml).

---

> Para metodologias e ferramentas de threat modeling, consultar [Metodologias e Ferramentas](./metodologias-e-ferramentas).
> Para validação e evidência do processo de threat modeling, consultar [Validação e Evidência](./validacao-evidencia-threat-modeling).
> Para os riscos do próprio processo de threat modeling, consultar [Riscos do Processo de Threat Modeling](./riscos-processo-threat-modeling).
> Para mapeamento de threats para requisitos de segurança, consultar [Mapeamento Threats → Requisitos](./mapeamento-threats-requisitos).
> Para integração de threat modeling em CI/CD, consultar [Threat Modeling em CI/CD](./threat-modeling-ci).
> Para KPIs e métricas de threat modeling, consultar [KPIs e Métricas de Threat Modeling](./11-kpis-metricas.md).
