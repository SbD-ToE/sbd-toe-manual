---
id: tech-lead
title: Tech Lead
sidebar_label: 🧑‍🔧 Tech Lead
description: Responsabilidades do Tech Lead no SbD-ToE
tags: [tech-lead, lideranca-tecnica, aprovacao, responsabilidades]
sidebar_position: 9.5
---

# Tech Lead

## Visão Geral {#visão-geral}

O Tech Lead é a **autoridade técnica da equipa**.
Decide no nível em que a decisão ainda é da equipa: aprova o que o nível de risco lhe atribui, fecha o modelo de ameaças e responde pelo que entra no código, incluindo o que foi gerado por assistentes.

Não se confunde com o [Scrum Master / Team Lead](scrum-master): este facilita o processo da equipa; o Tech Lead decide sobre o conteúdo técnico.

### Responsabilidades Principais {#responsabilidades-principais}
- Aprovam o que o nível de risco lhes atribui (L1 na classificação; A1 nos *mandates* de agentes AI)
- Tomam a decisão final do modelo de ameaças da equipa (baseline e revisões)
- Revêem o código e a configuração gerados com assistentes antes do merge
- Validam, com o Security Champion, que o acesso de contractors se limita ao necessário

### Contexto Organizacional {#contexto-organizacional}
A aprovação proporcional ao risco concretiza a **responsabilização** que NIS2 e DORA pedem: a decisão fica com quem tem competência técnica para a tomar, e sobe para AppSec Engineer e CISO quando o risco sobe.

## Enquadramento Regulatório {#enquadramento-regulatório}

Suporta:
- **NIS2** e **DORA**: Decisão técnica atribuída, registada e proporcional ao risco
- **AI Act**: Supervisão humana (art. 14.º, para sistemas de IA de risco elevado); no SbD-ToE estendida ao código e às ações de agentes AI (escolha do Manual)

---

## Atividades por Capítulo {#atividades-por-capítulo}

### Cap. 01 - Classificação de Aplicações {#cap-01---classificação-de-aplicações}
Propor a classificação com os Developers e **aprovar a entrada no inventário em L1**; a aprovação sobe para AppSec Engineer em L2 e para CISO em L3.

### Cap. 02 - Requisitos de Segurança {#cap-02---requisitos-de-segurança}
Rever requisitos em alterações críticas, responder pelo código gerado com assistentes e **classificar e aprovar o nível de autonomia dos agentes AI**.

**User Stories:**
- [US-02: Revisão por alteração relevante](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-02---revisão-por-alteração-relevante) - Requisitos atualizados em mudanças críticas (com Arquitetos de Software e Scrum Master / Team Lead)
- [US-14: Uso controlado de assistentes automatizados](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-14---uso-controlado-de-assistentes-automatizados-incluindo-ia-no-desenvolvimento) - Código gerado identificado e revisto (com Developer e AppSec Engineer)
- [US-15: Classificação e registo do *mandate* de agente AI](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-15) - Aprovador de A1; co-aprovador de A2 e A3 (com AppSec Engineer)
- [US-18: Intent declaration por tool-call destrutivo](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-18---intent-declaration-por-tool-call-destrutivo-de-agente-ai) - Ações de risco precedidas de intenção registada (com AppSec Engineer)

### Cap. 03 - Threat Modeling {#cap-03---threat-modeling}
Tomar a **decisão final do modelo** no contexto da equipa e aprovar formalmente o baseline e as revisões.

**User Stories:**
- [US-09: Aprovação formal do Threat Model](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-09---aprovação-formal-do-threat-model-baseline-e-revisões) - Decisão explícita e auditável (com AppSec Engineer)
- [US-14: Revisão independente em L2 e PASTA em alto risco](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-14---revisão-independente-em-l2-e-pasta-em-alto-risco) - Revisão por elemento externo à equipa de entrega (com AppSec Engineer)

### Cap. 10 - Testes de Segurança {#cap-10---testes-de-segurança}
Receber as escalações de conflito de triagem e **co-aprovar overrides em L3** (dupla aprovação com AppSec Engineer).

### Cap. 11 - Deploy Seguro {#cap-11---deploy-seguro}
Aprovar as **exceções de severidade MEDIUM**; HIGH sobe para AppSec Engineer e CRITICAL para AppSec Engineer com Gestão Executiva.

### Cap. 13 - Formação e Onboarding {#cap-13---formação-e-onboarding}
Dar o sign-off de conclusão do onboarding técnico de contractors, que condiciona o acesso real (com AppSec Engineer).

### Cap. 14 - Governança e Contratação {#cap-14---governança-e-contratação}
Validar a necessidade de cada acesso de contractors e dar feedback pós-projeto.

**User Stories:**
- [US-19: Revisão trimestral de acesso de contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-19---revisão-trimestral-de-acesso-de-contractors-least-privilege) - Least privilege mantido (com Security Champion e DevOps / SRE)
- [US-20: Feedback pós-projeto e rating de contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-20---feedback-pós-projeto-e-rating-de-contractors) - Decisões de re-contratação informadas (com Security Champion)

---

## Referências aos Capítulos {#referências-aos-capítulos}

Para contexto e enquadramento completo:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
