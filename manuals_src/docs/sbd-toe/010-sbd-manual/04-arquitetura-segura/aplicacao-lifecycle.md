---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração das práticas de Arquitetura Segura ao longo do ciclo de desenvolvimento
tags: [tipo:aplicacao, ciclo-vida, arquitetura, requisitos, seguranca]
genia: us-format-normalization
---

# Aplicação de Arquitetura Segura no Ciclo de Vida

Este anexo prescreve **como aplicar sistematicamente as práticas de Arquitetura Segura definidas no Capítulo 4** ao longo do ciclo de desenvolvimento, garantindo **rastreabilidade**, **proporcionalidade ao risco (L1–L3)** e integração com requisitos e ameaças.

Inclui **modelos reutilizáveis de user stories**, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade.

---

## 🧭 Quando aplicar Arquitetura Segura

| Fase / Evento | Ação esperada | Quem participa | Artefacto principal |
|---|---|---|---|
| Início de projeto / épico | Definir princípios e baseline inicial | Arquitetos de Software, AppSec Engineer, DevOps/SRE | `principios-arquitetura.md` |
| Design de solução | Produzir ficha de solução com controlos e decisões | Arquitetos de Software, AppSec Engineer | `solution-architecture.md` |
| Grooming / Planeamento | Validar requisitos arquiteturais e planeamento de controlos | Developer, Arquitetos de Software, AppSec Engineer | `design-review.md` |
| Decisão arquitetural relevante | Registar ADR com alternativas, trade-offs e impacto | Arquitetos de Software, AppSec Engineer | `adr/ADR-XXXX.md` |
| Integrações / fronteiras de confiança | Rever trust boundaries, integrações e fluxos de dados (incl. observabilidade) | Arquitetos de Software, AppSec Engineer, Developer | `trust-boundaries.md` |
| Alteração arquitetural significativa | Atualizar baseline e invalidar/atualizar decisões afetadas | Developer, Arquitetos de Software, AppSec Engineer | `architecture-update.md` |
| Exceção arquitetural | Solicitar/avaliar/aprovar exceção com controlos compensatórios e *sunset* | Product Owner, AppSec Engineer, Arquitetos de Software | `excecao-arquitetura.md` |
| Triggers “arquitetura viva” | Reavaliar docs/ADR/TM quando ocorrerem eventos definidos | Arquitetos de Software, DevOps/SRE, AppSec Engineer | `arquitetura-triggers.md` |
| Release / Go-live | Gate arquitetural: verificar controlos e exceções | QA, AppSec Engineer, Arquitetos de Software | `checklist-arquitetura.md` |
| CI/CD pipeline | Validar automaticamente controlos arquiteturais automatizáveis (quando aplicável) | DevOps/SRE, AppSec Engineer | `ci-architecture-report.*` |

---

## 👥 Quem faz o quê

| Papel / Função | Responsabilidades-chave |
|---|---|
| Arquitetos de Software | Definir princípios, criar fichas de solução, manter baseline e ADR, rever designs e integrações |
| Developer | Implementar decisões arquiteturais e controlos especificados, sinalizar alterações significativas |
| QA | Garantir que requisitos arquiteturais e controlos estão refletidos em testes e evidência de release |
| AppSec Engineer | Definir/rever controlos, validar decisões e exceções, assegurar ligação a ameaças (Cap. 3) e requisitos (Cap. 2) |
| Product Owner | Priorizar investimento/mitigação, aprovar trade-offs de negócio e exceções com impacto em scope/prazos |
| DevOps/SRE | Integrar validações automatizáveis no pipeline, garantir evidência reprodutível, suportar “arquitetura viva” |

---

## 📝 User Stories reutilizáveis

> **Nota editorial:** cada user story inclui, de forma consistente, **História**, **BDD**, **Checklist**, **Artefactos & evidências**, **Proporcionalidade (L1–L3)**, **Integração no SDLC** e **Ligações úteis**.

---

### US-01 - Definição de princípios e baseline de arquitetura segura

**Contexto.**  
No arranque de um projeto (ou épico significativo), é obrigatório estabelecer **princípios** e uma **baseline inicial**, para orientar decisões e evitar deriva arquitetural.

:::userstory
**História.**  
Como **Arquitetos de Software**, quero definir e versionar princípios de arquitetura segura, para que todas as decisões técnicas sejam consistentes, rastreáveis e proporcionais ao risco.

**Critérios de aceitação (BDD).**
- **Dado** que um projeto inicia ou um épico estrutural é criado  
  **Quando** documento princípios e baseline inicial  
  **Então** os princípios ficam versionados, aprovados e referenciáveis por release

**Checklist.**
- [ ] `principios-arquitetura.md` criado e versionado
- [ ] Princípios incluem: isolamento, trust boundaries, minimização de exposição, gestão de dependências, observabilidade segura
- [ ] Aprovação registada (AppSec + Arquitetura)
- [ ] Ligação explícita ao nível de risco (L1–L3)
:::

**Artefactos & evidências.**
- `principios-arquitetura.md`
- Registo de aprovação (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Princípios mínimos e baseline simplificada |
| L2 | Sim | Princípios completos e baseline formal |
| L3 | Sim | Princípios completos + revisão independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Início | Novo projeto / épico estrutural | Arquitetos de Software | Antes do design detalhado |

**Ligações úteis.**
- 🔗 Cap. 2 - Requisitos de Segurança: `/sbd-manual/requisitos-seguranca/intro`
- 🔗 Cap. 3 - Threat Modeling: `/sbd-manual/threat-modeling/intro`

---

### US-02 - Ficha de solução com controlos e rastreabilidade arquitetural

**Contexto.**  
Durante o design, a solução deve ser descrita com **controlos arquiteturais explícitos**, minimização de exposição e ligação a requisitos/ameaças.

:::userstory
**História.**  
Como **Arquitetos de Software**, quero produzir uma ficha de arquitetura com controlos de segurança e rastreabilidade para requisitos arquiteturais, para garantir que a solução é segura e verificável antes da implementação.

**Critérios de aceitação (BDD).**
- **Dado** que o design está em definição  
  **Quando** documento a solução  
  **Então** a ficha inclui trust boundaries, exposição externa justificada, controlos arquiteturais e referências a requisitos e ameaças relevantes

**Checklist.**
- [ ] `solution-architecture.md` criado com template aprovado
- [ ] Trust boundaries e fluxos (incl. logs/métricas/telemetria) identificados
- [ ] Exposição externa minimizada e justificada
- [ ] Controlos arquiteturais especificados (isolamento, segmentação, quotas, *timeouts*, *fallbacks*, segregação)
- [ ] Dependências externas identificadas e tratadas como decisões arquiteturais
- [ ] Rastreabilidade registada (requisitos arquiteturais ↔ decisões ↔ ameaças ↔ controlos)
- [ ] Aprovação registada (AppSec + Arquitetura)
:::

**Artefactos & evidências.**
- `solution-architecture.md`
- `controlos-arquitetura.md` (opcional, se necessário para detalhe)
- Registo de aprovação (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Ficha simplificada e controlos essenciais |
| L2 | Sim | Ficha detalhada + rastreabilidade mínima |
| L3 | Sim | Ficha completa + revisão independente + evidência reforçada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design | Definição de solução | Arquitetos de Software + AppSec Engineer | Antes da implementação |

**Ligações úteis.**
- 🔗 Catálogo de requisitos arquiteturais (ARC-*): `addon/01-catalogo-requisitos`
- 🔗 Diagramas/modelos de referência: `addon/04-diagramas-referencia`

---

### US-03 - Revisão formal do design arquitetural

**Contexto.**  
Antes de implementar, o design deve ser revisto quanto a conformidade com princípios, requisitos e mitigação de ameaças.

:::userstory
**História.**  
Como **AppSec Engineer**, quero rever formalmente o design arquitetural, para garantir que os controlos necessários estão especificados e que as decisões são defensáveis e rastreáveis.

**Critérios de aceitação (BDD).**
- **Dado** que existe uma ficha de solução candidata  
  **Quando** executo a revisão  
  **Então** o design é aprovado, ou é devolvido com ações corretivas rastreáveis

**Checklist.**
- [ ] Revisão registada (checklist + comentários)
- [ ] Desvios e ações corretivas registados em backlog
- [ ] Aprovação ou rejeição documentada e versionada
:::

**Artefactos & evidências.**
- `design-review.md`
- Registo de aprovação/rejeição (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Revisão simplificada |
| L2 | Sim | Revisão formal |
| L3 | Sim | Revisão formal + segregação de funções (revisão independente) |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento | Design pronto para implementação | AppSec Engineer | Antes da implementação |

**Ligações úteis.**
- 🔗 Cap. 3 - Threat Modeling: `/sbd-manual/threat-modeling/intro`

---

### US-04 - Gestão de decisões arquiteturais (ADR)

**Contexto.**  
Decisões de arquitetura críticas devem ser documentadas com alternativas e trade-offs, para preservar rastreabilidade e permitir revisão/invalidação.

:::userstory
**História.**  
Como **Arquitetos de Software**, quero registar decisões arquiteturais (ADR) com alternativas e impacto em segurança, para que a baseline seja auditável e evolutiva.

**Critérios de aceitação (BDD).**
- **Dado** que é tomada uma decisão arquitetural relevante  
  **Quando** crio uma ADR com template aprovado  
  **Então** ficam registados contexto, alternativas, decisão, trade-offs, impacto e revisão por AppSec

**Checklist.**
- [ ] ADR criada em `adr/ADR-XXXX.md`
- [ ] Alternativas consideradas e trade-offs documentados
- [ ] Impacto em segurança e risco explicitado (incl. L1–L3 quando aplicável)
- [ ] Ligação a requisitos arquiteturais e ameaças relevantes
- [ ] Aprovação registada
:::

**Artefactos & evidências.**
- `adr/ADR-XXXX.md`
- Registo de aprovação (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas ADR de alto impacto |
| L2 | Sim | ADR para decisões significativas |
| L3 | Sim | ADR para todas as decisões relevantes + revisão independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design | Decisão arquitetural relevante | Arquitetos de Software | Antes da implementação |

**Ligações úteis.**
- 🔗 Decisão e evidência arquitetural (addon): `addon/decisao-evidencia-arquitetural`

---

### US-05 - Revisão de fronteiras de confiança e integrações

**Contexto.**  
Integrações internas e com terceiros exigem revisão explícita de fronteiras de confiança e fluxos de dados (incluindo fluxos implícitos).

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero rever trust boundaries e integrações, para validar autenticação, autorização, encriptação, isolamento e exposição de dados.

**Critérios de aceitação (BDD).**
- **Dado** que existe uma integração nova ou alterada  
  **Quando** avalio trust boundaries e controlos  
  **Então** documento decisões, riscos residuais e controlos mitigadores, com rastreabilidade

**Checklist.**
- [ ] Inventário de integrações atualizado
- [ ] Trust boundaries e fluxos (incl. logs/métricas/telemetria) documentados
- [ ] Controlos por integração definidos (AuthN/AuthZ/TLS/segregação/minimização)
- [ ] Risco residual e exceções (se existirem) formalizados
:::

**Artefactos & evidências.**
- `trust-boundaries.md`
- `integration-review.md`
- ADR (quando aplicável)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Âmbito reduzido (integrações críticas) |
| L2 | Sim | Âmbito completo |
| L3 | Sim | Âmbito completo + validações reforçadas (conforme risco) |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Alteração | Nova integração / alteração | Arquitetos de Software + AppSec Engineer | Antes da implementação |

**Ligações úteis.**
- 🔗 Riscos de processo na arquitetura (addon): `addon/riscos-processo-arquitetura`

---

### US-06 - Atualização da baseline após alteração arquitetural significativa

**Contexto.**  
Alterações arquiteturais significativas invalidam decisões anteriores e exigem atualização da baseline e (quando aplicável) reavaliação de ameaças/requisitos.

:::userstory
**História.**  
Como **Developer**, quero atualizar a baseline arquitetural quando ocorrem alterações significativas, para manter coerência entre o sistema real e a evidência arquitetural aprovada.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre uma alteração arquitetural significativa  
  **Quando** atualizo a documentação e decisões afetadas  
  **Então** a baseline fica consistente, e as revisões necessárias são desencadeadas

**Checklist.**
- [ ] Alteração classificada como “significativa” segundo critérios do capítulo
- [ ] `architecture-update.md` atualizado e versionado
- [ ] ADR impactadas atualizadas (ou invalidadas e substituídas)
- [ ] Revisão AppSec acionada quando aplicável
- [ ] (Se aplicável) revisão de ameaças e requisitos associada
:::

**Artefactos & evidências.**
- `architecture-update.md`
- ADR atualizadas
- Registo de revisão (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas alterações estruturais relevantes |
| L2 | Sim | Todas as alterações significativas |
| L3 | Sim | Todas + revisão independente quando aplicável |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Desenvolvimento | Alteração significativa | Developer + Arquitetos de Software | No mesmo sprint |

**Ligações úteis.**
- 🔗 Cap. 3 - Threat Modeling: `/sbd-manual/threat-modeling/intro`

---

### US-07 - Validação arquitetural automatizável no CI/CD (quando aplicável)

**Contexto.**  
Determinados controlos arquiteturais podem ser validados de forma automatizada (ou semi-automatizada). O objetivo é **produzir evidência reprodutível**, não “substituir” revisão humana.

:::userstory
**História.**  
Como **DevOps/SRE + AppSec Engineer**, quero integrar validações automatizáveis de controlos arquiteturais no pipeline, para detetar desconformidades cedo e gerar evidência auditável.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre uma alteração com impacto em arquitetura, configuração ou infraestrutura  
  **Quando** o pipeline executa  
  **Então** são produzidos resultados determinísticos (pass/fail quando aplicável) e artefactos de evidência versionados

**Checklist.**
- [ ] Critérios de quando executar a validação definidos (paths/labels/condições)
- [ ] Verificações automatizáveis implementadas (ex.: políticas, configurações, invariantes arquiteturais, requisitos verificáveis)
- [ ] Evidência produzida como artefacto (`ci-architecture-report.*`)
- [ ] Regras de bloqueio por risco definidas (ex.: L2 bloqueia falhas críticas; L3 bloqueia falhas de severidade elevada e acima)
- [ ] SLA de remediação definido e rastreável
:::

**Artefactos & evidências.**
- Configuração de pipeline (`ci-pipeline.*`)
- `ci-architecture-report.*` (relatórios, logs, artefactos)
- Registos de bloqueio e remediação (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Alertas e evidência básica |
| L2 | Sim | Evidência formal + bloqueio de desconformidades críticas |
| L3 | Sim | Evidência completa + regras de bloqueio reforçadas + auditoria centralizada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| CI/CD | Alteração com impacto | DevOps/SRE + AppSec Engineer | Em cada build relevante |

**Ligações úteis.**
- 🔗 Cap. 7 - CI/CD Seguro: `/sbd-manual/cicd-seguro//intro`

---

### US-08 - Avaliação de impacto no negócio e priorização de trade-offs

**Contexto.**  
Decisões arquiteturais implicam trade-offs com impacto no negócio. A priorização deve ser explícita e rastreável.

:::userstory
**História.**  
Como **Product Owner**, quero avaliar impacto no negócio de requisitos e decisões arquiteturais, para priorizar mitigação e aceitar trade-offs de forma consciente e auditável.

**Critérios de aceitação (BDD).**
- **Dado** que existem requisitos/decisões com impacto em custo/prazo/UX  
  **Quando** avalio impacto e priorizo  
  **Então** a decisão fica documentada e ligada ao backlog e às decisões técnicas

**Checklist.**
- [ ] Impacto avaliado e registado (custo/prazo/risco)
- [ ] Priorização refletida no backlog
- [ ] Trade-off documentado e aprovado quando necessário
:::

**Artefactos & evidências.**
- `impacto-arquitetura.md` (ou registo equivalente)
- Backlog/epics com ligação a ADR/requisitos

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas impactos críticos |
| L2 | Sim | Avaliação formal |
| L3 | Sim | Avaliação formal + validação executiva quando aplicável |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento | Requisitos/decisões definidas | Product Owner | Antes da priorização de sprint |

**Ligações úteis.**
- 🔗 Cap. 1 - Classificação / risco: `/sbd-manual/classificacao-aplicacoes/intro`

---

### US-09 - Sincronização Threat Modeling ↔ Arquitetura

**Contexto.**  
Decisões de arquitetura devem refletir ameaças priorizadas e, em sentido inverso, alterações arquiteturais exigem atualização do modelo de ameaças quando aplicável.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero sincronizar arquitetura e threat modeling, para garantir que controlos arquiteturais cobrem as ameaças priorizadas e que a rastreabilidade permanece válida.

**Critérios de aceitação (BDD).**
- **Dado** que existe decisão ou alteração arquitetural significativa  
  **Quando** verifico impacto no modelo de ameaças  
  **Então** atualizo os artefactos necessários e mantenho rastreabilidade decisão ↔ ameaça ↔ controlo ↔ requisito

**Checklist.**
- [ ] Impacto da alteração avaliado
- [ ] Modelo de ameaças atualizado quando aplicável
- [ ] Ficha de solução e ADR alinhadas
- [ ] Evidência de cobertura atualizada
:::

**Artefactos & evidências.**
- `solution-architecture.md`
- Artefacto de threat model (conforme Cap. 3)
- Registo de atualização (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Modelo simplificado quando aplicável |
| L2 | Sim | Modelo completo |
| L3 | Sim | Modelo detalhado + revisão independente quando aplicável |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Alteração | Decisão/alteração significativa | Arquitetos de Software + AppSec Engineer | Antes do release |

**Ligações úteis.**
- 🔗 Cap. 3 - Threat Modeling: `/sbd-manual/threat-modeling/intro`

---

### US-10 - Gestão de exceções arquiteturais com controlos compensatórios

**Contexto.**  
Quando um requisito/controlo arquitetural não pode ser aplicado, é necessária exceção formal com controlos compensatórios, *owner* e *sunset*.

:::userstory
**História.**  
Como **Product Owner + AppSec Engineer**, quero gerir exceções arquiteturais com aprovação e controlos compensatórios, para equilibrar risco e entrega mantendo auditabilidade.

**Critérios de aceitação (BDD).**
- **Dado** que é solicitada uma exceção arquitetural  
  **Quando** avalio impacto, compensações e prazo  
  **Então** a exceção é aprovada/rejeitada, com evidência, *owner* e data de revisão (*sunset*)

**Checklist.**
- [ ] Pedido de exceção documentado
- [ ] Impacto e risco residual avaliados
- [ ] Controlos compensatórios definidos e verificáveis
- [ ] *Owner* do risco definido
- [ ] *Sunset* e revisão agendada
- [ ] Aprovação registada e versionada
:::

**Artefactos & evidências.**
- `excecao-arquitetura.md`
- Registo de aprovação (PR/issue)
- Evidência de compensações (tests/configs)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Processo simplificado |
| L2 | Sim | Processo formal |
| L3 | Sim | Governação reforçada + auditoria |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Release | Impossibilidade de cumprir controlo | Product Owner + AppSec Engineer | Antes do go-live |

**Ligações úteis.**
- 🔗 Cap. 14 - Governação: `/cap14/intro`

---

### US-11 - Triggers de “arquitetura viva” e disciplina de revisão

**Contexto.**  
A arquitetura deve ser tratada como baseline viva. Existem eventos que obrigam a revisão e sincronização de evidência.

:::userstory
**História.**  
Como **Arquitetos de Software + DevOps/SRE**, quero manter uma lista de triggers que despoletam revisão de arquitetura, para garantir que a baseline, ADR e evidências permanecem válidas ao longo do tempo.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre um trigger definido (ex.: nova integração, alteração de dados sensíveis, mudança de fronteira de confiança, mudança estrutural de infraestrutura/pipeline)  
  **Quando** executo a revisão associada  
  **Então** atualizo baseline, ADR afetadas e evidência necessária, com registo verificável

**Checklist.**
- [ ] `arquitetura-triggers.md` publicado e versionado
- [ ] Triggers definidos com ações mínimas por trigger
- [ ] Execução do trigger gera evidência (PR/issue/ata)
- [ ] Rastreabilidade mantida (decisão ↔ evidência)
:::

**Artefactos & evidências.**
- `arquitetura-triggers.md`
- Registos de execução (PR/issue)
- ADR/baseline atualizadas quando aplicável

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Subconjunto mínimo de triggers |
| L2 | Sim | Conjunto completo |
| L3 | Sim | Conjunto completo + deteção/alertas quando viável |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Contínuo | Trigger arquitetural | Arquitetos de Software + DevOps/SRE | Dentro do sprint corrente (ou SLA definido) |

---

### US-12 - Gate arquitetural antes do Go-live

**Contexto.**  
Antes de produção, deve existir um **gate arquitetural** que confirme: controlos implementados, decisões válidas e exceções tratadas.

:::userstory
**História.**  
Como **QA + AppSec Engineer + Arquitetos de Software**, quero executar um gate arquitetural antes do go-live, para garantir que a arquitetura implementada corresponde à baseline aprovada e que controlos/exceções estão verificados.

**Critérios de aceitação (BDD).**
- **Dado** que a aplicação está pronta para release  
  **Quando** executo a checklist de validação arquitetural  
  **Então** confirmo conformidade, ou bloqueio o go-live com desvios rastreáveis

**Checklist.**
- [ ] `checklist-arquitetura.md` preenchido e versionado
- [ ] Controlos críticos verificados com evidência
- [ ] Exceções confirmadas com compensações e *sunset*
- [ ] Desvios registados e aceites formalmente quando aplicável
- [ ] Aprovação final registada
:::

**Artefactos & evidências.**
- `checklist-arquitetura.md`
- Evidência de verificação (tests/configs/logs)
- Registo de aprovação (PR/issue)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Checklist simplificada |
| L2 | Sim | Checklist formal |
| L3 | Sim | Checklist completa + revisão independente quando aplicável |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Release / Go-live | Preparação de release | QA + AppSec + Arquitetura | Antes da entrada em produção |

**Ligações úteis.**
- 🔗 Critérios e evidência arquitetural (addon): `addon/decisao-evidencia-arquitetural`

---

### US-13 - Catálogo de padrões de arquitetura segura (reutilização governada)

**Contexto.**  
Padrões aprovados reduzem variação e risco de omissão. A reutilização deve ser governada e versionada.

:::userstory
**História.**  
Como **Arquitetos de Software**, quero manter um catálogo versionado de padrões de arquitetura segura, para que novos projetos reutilizem designs aprovados com requisitos, ameaças mitigadas e checklist de implementação.

**Critérios de aceitação (BDD).**
- **Dado** que um novo projeto inicia  
  **Quando** seleciono um padrão do catálogo  
  **Então** o padrão fornece baseline, requisitos aplicáveis, ameaças cobertas e checklist verificável

**Checklist.**
- [ ] Catálogo publicado e versionado
- [ ] Padrões têm: diagrama, decisões chave, requisitos aplicáveis, ameaças mitigadas, checklist
- [ ] Aprovação formal (Arquitetura + AppSec)
- [ ] Histórico de alterações (changelog)
:::

**Artefactos & evidências.**
- `modelos-referencia.md`
- `padroes-checklist.md` (se necessário)
- Registos de aprovação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Catálogo reduzido |
| L2 | Sim | Catálogo formal com padrões principais |
| L3 | Sim | Catálogo completo e evolução contínua |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design | Novo projeto / alteração estrutural | Arquitetos de Software + AppSec Engineer | Antes da ficha de solução |

**Ligações úteis.**
- 🔗 Diagramas/modelos: `addon/04-diagramas-referencia`

---

### US-14 - Revisão formal de arquitetura para L3 (governação reforçada)

**Contexto.**  
Aplicações L3 exigem validação formal reforçada (incluindo segregação de funções e decisão auditável).

:::userstory
**História.**  
Como **Gestão Executiva/CISO + Arquitetos de Software**, quero estabelecer um processo formal de aprovação de arquitetura para L3, para garantir que riscos estruturais são identificados, mitigados e aceites de forma auditável antes do go-live.

**Critérios de aceitação (BDD).**
- **Dado** que uma aplicação L3 está pronta para aprovação  
  **Quando** é submetida a revisão formal reforçada  
  **Então** existe parecer registado (aprovar, aprovar com exceções, rejeitar) com ações e prazos

**Checklist.**
- [ ] Processo e participantes definidos (responsabilidades explícitas)
- [ ] Documentação submetida (baseline, ADR, integrações, exceções, evidência)
- [ ] Revisão concluída com parecer formal
- [ ] Desvios geram plano de remediação ou exceção com compensações
- [ ] Decisão arquivada e referenciável por release
:::

**Artefactos & evidências.**
- `governance-checklist-l3.md` (ou equivalente)
- Parecer formal registado
- Plano de remediação / exceções aprovadas

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não | - |
| L2 | Recomendado | Revisão *peer* reforçada |
| L3 | Sim | Processo formal e auditável |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Release / Go-live | Release L3 | Gestão/CISO + Revisores definidos | SLA interno (ex.: ≥ 2 semanas antes) |

**Ligações úteis.**
- 🔗 Cap. 14 - Governação: `/cap14/intro`

---

### US-15 - Identificação e governação de componentes não determinísticos

**Contexto.**  
Arquiteturas modernas podem incluir componentes cujo comportamento **não é estritamente determinístico** (ex.: motores de decisão probabilísticos, scoring heurístico, modelos estatísticos ou componentes de inferência). Estes componentes introduzem desafios específicos em termos de segurança, auditoria, explicabilidade e controlo operacional, que devem ser explicitamente tratados ao nível da arquitetura.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero identificar e governar componentes arquiteturais não determinísticos, documentando o seu impacto em segurança, auditoria e controlo, para garantir que a arquitetura permanece rastreável, governável e proporcional ao risco.

**Critérios de aceitação (BDD).**
- **Dado** que a solução inclui um componente cujo comportamento não é totalmente determinístico  
  **Quando** desenho ou revejo a arquitetura  
  **Então** o componente é explicitamente identificado e classificado  
- **E** o impacto em segurança, auditoria e controlo é documentado  
- **E** são definidos controlos arquiteturais adequados (isolamento, supervisão, *fallback*, logging)  
- **E** existe rastreabilidade entre o componente, ameaças relevantes e requisitos ARC-XXX aplicáveis

**Checklist.**
- [ ] Componentes não determinísticos identificados na ficha de arquitetura
- [ ] Tipo de não determinismo classificado (ex.: probabilístico, heurístico, inferencial)
- [ ] Impacto analisado em:
  - [ ] Segurança (abuso, *bypass*, comportamento inesperado)
  - [ ] Auditoria e explicabilidade
  - [ ] Controlo operacional e mecanismos de *fallback*
- [ ] Fronteiras de confiança e isolamento revistos (quando aplicável)
- [ ] Logging e evidência definidos para decisões relevantes
- [ ] Rastreabilidade documentada (componente ↔ ameaça ↔ controlo ↔ requisito ARC-XXX)
- [ ] Evidência arquivada em repositório de arquitetura
:::

**Artefactos & evidências.**
- Atualização da `solution-architecture.md`
- Documentação de decisão/evidência arquitetural (ex.: `decision-evidence.md`)
- Atualização do modelo de ameaças (quando aplicável)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Identificação simples e nota de impacto |
| L2 | Sim | Identificação formal e controlos definidos |
| L3 | Sim | Governação completa, isolamento explícito e validação independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Revisão | Introdução ou alteração de componente não determinístico | Arquitetos de Software + AppSec Engineer | Antes da aprovação do design |

**Ligações úteis.**
- 🔗 Cap. 3 - Threat Modeling  
- 🔗 Requisitos ARC-XXX aplicáveis à arquitetura

---

### US-16 - Revisão de arquitectura para agente AI em A2+ {#us-16}

**Contexto.**
A US-15 cobre *componentes não determinísticos* em geral (modelos preditivos, RAG, LLMs em interface). Quando o componente é um **agente autónomo** que executa acções com efeito real em sistemas externos via *tool-use* — e opera em nível A2 ou superior — exige-se uma camada adicional de validação arquitectónica: confirmar que a arquitectura cumpre [`ARC-015`](./addon/catalogo-requisitos-arquitetura#arc-015) antes da activação, para que falhas estruturais não fiquem apenas detectadas no incidente.

:::userstory
**História.**
Como **Software Architect** e **AppSec Engineer**, quero validar que a arquitectura do sistema cumpre integralmente [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (identidade dedicada, *least privilege* per-tool, *intent declaration*, aprovação humana *out-of-band*, *kill-switch* exercitado, audit completo por *tool invocation*) **antes** de aprovar a operação de um agente AI em A2 ou superior, para evitar que problemas estruturais sejam descobertos só quando já tiveram efeito em produção.

**Critérios de aceitação (BDD).**
- **Dado** que um agente AI vai operar em A2+
  **Quando** se executa a revisão de arquitectura prévia à activação do *mandate*
  **Então** existe checklist [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) preenchida, com evidência de cada item, ligada ao `mandate_ref`
- **Dado** que um item da checklist falha
  **Quando** a revisão é concluída
  **Então** o agente **não** opera no nível pedido; opera-se em nível inferior até o item estar resolvido (descida é sempre legítima; subida exige nova revisão)
- **Dado** que o *kill-switch* nunca foi exercitado nesta arquitectura
  **Quando** se pretende activar A3 ou A4
  **Então** o exercício é executado em sandbox/staging com cronómetro e *log* arquivado antes da activação

**Critérios de aceitação (DoD).**
- [ ] **Identidade dedicada** — agente tem *workload identity* efémera (OIDC) por ambiente; sem reuso de credenciais humanas; TTL ≤ 1h
- [ ] **Scope mínimo per-tool** — cada *tool* na *allowlist* com argumentos limitados ao necessário; etiquetada `read`/`write`/`destructive`/`external`
- [ ] **Intent declaration** — mecanismo ([`REQ-AGN-004`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)) emite *intent event* estruturado antes de cada *tool call* destrutivo, com schema mínimo: `agent_id`, `mandate_ref`, `tool`, `args`, `intent`, `expected_outcome`, `risk_self_assessment`
- [ ] **Aprovação out-of-band** — canal independente do canal do agente (Slack approval com 2FA, GitHub review, webhook assinado, *push notification*); ataques de *prompt injection* no canal principal não conseguem aprovar
- [ ] **Kill-switch operacional** — revogação de credenciais + terminação de *runtime* + isolamento de *namespace* + alerta on-call; exercitado em sandbox/staging com cadência registada (trimestral A3; mensal A4)
- [ ] **Audit completo per-tool** — *event* estruturado com `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII e segredos redactados), `intent_event_ref`, `outcome`, `external_effect`; integrado com observabilidade do Cap. 12
- [ ] *Threat model* do agente (US-11 do Cap. 03) referenciado e *mitigations* mapeadas a este checklist

:::

**Artefactos & evidências.**
- `arc-015-review.md` — checklist preenchida com referência a `mandate_ref` e `threat_model_ref`
- *Log* de exercício de *kill-switch* (data inicial + cadência registada)
- Diagrama de arquitectura agentic versionado (DFD com cinco participantes — humano · cliente · modelo · *tool runtime* · sistema externo — e quatro fronteiras)
- Configuração da *workload identity* (referência IaC) e evidência de TTL ≤ 1h
- Exemplo redactado de *intent event* + *tool invocation audit event* (uma sessão real)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | A2+ tipicamente fora de produção; revisão simplificada quando aplicável | Checklist [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) essencial; *kill-switch* exercitado anualmente |
| L2 | Obrigatório para A2+ | Checklist [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) completa; *kill-switch* exercitado trimestralmente (A3) |
| L3 | Obrigatório para A2+; A3/A4 com revisão `appsec` independente | Checklist [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) completa + revisão independente; A4 com assinatura formal do `CISO` no *mandate*; *kill-switch* exercitado mensalmente (A4) |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Revisão | Activação de agente em A2+ | `software_architect` + `appsec` | Antes da activação do *mandate* |
| Subida de nível | Promoção A2→A3 ou A3→A4 | `appsec` (+ `grc` em A3; + `CISO` em A4) | Antes da nova activação |
| Revisão periódica | `review_cadence` do *mandate* | `appsec` | Conforme cadência (anual A2; semestral A3; trimestral A4) |

**Ligações úteis.**
- 🔗 [`ARC-015` — agente como *principal* isolado](./addon/catalogo-requisitos-arquitetura#arc-015)
- 🔗 [Padrões arquitectónicos para agentes (recomendações avançadas)](./recomendacoes-avancadas#agentes-principals)
- 🔗 [Catálogo `REQ-AGN-*` (Cap. 02)](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#req-agn)
- 🔗 [Playbook agentic de Threat Modeling (Cap. 03)](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic)
- 🔗 [Policy 38 — Mandates de Agentes AI](/sbd-toe/assets/policies/policy-mandates-agentes)

---

### US-17 - Segmentação de ambientes e validação de topologia como código (L3)

Em L3 a separação entre `dev`, `staging` e `prod` deixa de ser convenção e passa a ser invariante verificável no pipeline.  

**Contexto.** A `ARC-011` exige segregação de rede, permissões e identidade entre ambientes; a `ARC-013` exige que a topologia seja validada automaticamente em CI/CD, com bloqueio de promoção em falha. Sem operacionalização, a segmentação fica como intenção em diagrama — sem garantia de que o estado real dos ambientes a respeita, nem deteção de *drift* quando alguém reutiliza credenciais ou abre *peering* indevido entre `staging` e `prod`. A US-07 cobre validação automatizável genérica; esta US prescreve a verificação específica da segmentação e da topologia como código para aplicações de risco elevado.  

:::userstory
**História.**   
Como **DevOps/SRE** e **AppSec Engineer**, quero validar automaticamente, em CI/CD, a segregação de rede, permissões e identidade entre `dev`/`staging`/`prod` e a conformidade da topologia com o baseline aprovado, para que uma promoção que viole a segmentação seja bloqueada antes de chegar a produção.  

**Critérios de aceitação (BDD).**  
- **Dado** que uma aplicação L3 possui ambientes `dev`, `staging` e `prod`  
  **Quando** o pipeline executa a validação de topologia  
  **Então** é produzido um output verificável que confirma segregação de rede, permissões e identidade entre ambientes (sem credenciais *cross-env*), com logs de execução arquivados  
- **Dado** que uma alteração introduz *peering*, partilha de identidade ou exposição entre ambientes não previstos no baseline  
  **Quando** a validação corre na promoção  
  **Então** a promoção é bloqueada e o desvio é registado para remediação ou exceção formal  

**Checklist.**  
- [ ] Segregação de rede entre `dev`/`staging`/`prod` evidenciada (VLANs, *namespaces*, *peering policies*)  
- [ ] Segregação de identidade e permissões evidenciada (IAM/*service accounts* distintas, sem credenciais *cross-env*)  
- [ ] Job de CI valida topologia como código (ex.: diagramas-como-código, Cartography, verificação `checkov`/Terraform) com logs disponíveis  
- [ ] Falha de validação bloqueia a promoção; desvio gera registo de remediação ou exceção aprovada  

:::

**Artefactos & evidências.** Configuração do job de validação de topologia (`ci-pipeline.*`); `ci-architecture-report.*` com output de segregação e topologia; evidência IaC de segregação de rede/identidade; registo de bloqueio/remediação (PR/issue).  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Não obrigatório | Recomendado: segregação documentada de ambientes | Obrigatório: segregação de rede/permissões/identidade verificável + validação de topologia como código em CI/CD com bloqueio de promoção (`ARC-011`, `ARC-013`) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Promoção entre ambientes (L3) | DevOps/SRE + AppSec Engineer | Em cada promoção; bloqueio imediato em falha |

**Ligações úteis.** [Catálogo de requisitos arquiteturais (ARC-011, ARC-013)](./addon/catalogo-requisitos-arquitetura) · [Cap. 7 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)

---

### US-18 - Padrões arquitetónicos para sistemas AI/ML não-agentic

Sistemas que integram LLMs, modelos preditivos ou RAG sem *tool-use* exigem trust boundaries e controlos próprios, distintos do caso agentic.  

**Contexto.** A US-15 trata componentes não determinísticos em geral e a US-16 cobre o agente autónomo com *tool-use* (`ARC-015`). Falta operacionalizar a `ARC-014` para o caso **não-agentic** — LLMs em interface conversacional, modelos preditivos e RAG que produzem *output* mas não executam ações em sistemas externos. Aqui a superfície de ataque é o próprio modelo e os seus dados: prompt injection direta e indireta (LLM01-2025, `AML.T0051.001`), *training data poisoning* (`AML.T0020`), *model theft* (ML05-2023) e ausência de proveniência de modelos/datasets (LLM03-2025). A arquitetura tem de marcar as trust boundaries de *training-time* e *inference-time* explicitamente e tratar a IA como participante distinto no DFD, não como biblioteca opaca.  

:::userstory
**História.**   
Como **Arquitetos de Software** e **AppSec Engineer**, quero aplicar padrões arquitetónicos dedicados a sistemas AI/ML não-agentic, com trust boundaries explícitas, controlos anti-prompt-injection e proveniência de modelos/datasets, para que o risco específico de IA fique contido e auditável ao nível da arquitetura.  

**Critérios de aceitação (BDD).**  
- **Dado** que a solução integra um componente AI/ML que produz *output* sem invocar *tools* (LLM conversacional, modelo preditivo, RAG)  
  **Quando** desenho ou revejo a arquitetura  
  **Então** o DFD marca as trust boundaries de *training-time* e *inference-time*, com a IA como participante distinto, e os controlos de fronteira ficam documentados  
- **Dado** que existe entrada de utilizador ou conteúdo externo no contexto do modelo  
  **Quando** especifico os controlos arquitetónicos  
  **Então** há *input sanitization* e *output filtering* contra prompt injection direta e indireta, *rate limiting* e isolamento das chamadas ao modelo  
- **Dado** que o sistema usa modelos e datasets  
  **Quando** registo a proveniência  
  **Então** origem e versão de modelos e datasets ficam documentadas, com consideração explícita de *model theft* e *training data poisoning*  

**Checklist.**  
- [ ] Trust boundaries *training-time* e *inference-time* marcadas no DFD, com a IA como participante distinto  
- [ ] Controlos anti-prompt-injection (input/output) para injeção direta e indireta (LLM01-2025, `AML.T0051.001`)  
- [ ] *Rate limiting* e isolamento das chamadas ao modelo de inferência  
- [ ] Proveniência de modelos e datasets documentada (`AML.T0010`, LLM03-2025); cenários de *model theft* (ML05-2023) e *data poisoning* (`AML.T0020`) considerados  

:::

**Artefactos & evidências.** Atualização da `solution-architecture.md` com trust boundaries AI/ML; DFD versionado com a IA como participante distinto; registo de proveniência de modelos/datasets; ligação ao modelo de ameaças AI/ML (Cap. 3).  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Identificação simples do componente AI/ML e nota de impacto | Obrigatório: trust boundaries, controlos anti-prompt-injection e proveniência documentados (`ARC-014`) | Obrigatório + isolamento reforçado das chamadas ao modelo e revisão independente da arquitetura AI/ML |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Design / Revisão | Introdução ou alteração de componente AI/ML não-agentic | Arquitetos de Software + AppSec Engineer | Antes da aprovação do design |

**Ligações úteis.** [`ARC-014` — padrões arquitetónicos AI/ML](./addon/catalogo-requisitos-arquitetura#arc-014) · [Recomendações Avançadas — §AI/ML](./recomendacoes-avancadas#ai-ml) · [Cap. 3 - Metodologias AI/ML](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#ai-ml)

---

## 📑 Artefactos esperados

| Artefacto | Origem / US | Evidência associada |
|---|---|---|
| `principios-arquitetura.md` | US-01 | Commit + aprovação |
| `solution-architecture.md` | US-02 | PR/issue + aprovação |
| `design-review.md` | US-03 | Registo de revisão + backlog |
| `adr/ADR-XXXX.md` | US-04 | ADR + aprovação |
| `trust-boundaries.md` | US-05 | Inventário + controlos |
| `integration-review.md` | US-05 | Revisão por integração |
| `architecture-update.md` | US-06 | Atualização + revisão |
| `ci-architecture-report.*` | US-07 | Artefactos do pipeline |
| `impacto-arquitetura.md` | US-08 | Registo + backlog |
| `excecao-arquitetura.md` | US-10 | Exceção + *sunset* + compensações |
| `arquitetura-triggers.md` | US-11 | Lista + evidências de execução |
| `checklist-arquitetura.md` | US-12 | Gate + aprovações |
| `modelos-referencia.md` | US-13 | Catálogo + changelog |
| `governance-checklist-l3.md` | US-14 | Parecer formal |

---

## ⚖️ Matriz de proporcionalidade (L1–L3)

| Nível | Aplicação de práticas de Arquitetura Segura |
|---|---|
| L1 | Princípios mínimos; decisões (ADR) apenas para alto impacto; integrações críticas; gate simplificado quando aplicável; triggers mínimos |
| L2 | Princípios completos; ficha detalhada; revisão formal; ADR para decisões significativas; exceções formais; validações automatizáveis quando aplicável; sincronização com threat modeling |
| L3 | Cobertura integral; segregação de funções; evidência reforçada; governação formal; gates rigorosos; revisão independente quando aplicável; disciplina de “arquitetura viva” |

---

## 📌 Recomendações finais

- Centralizar artefactos em repositório versionado e referenciável por release (baseline, ADR, integrações, exceções).
- Tratar **dependências externas** e **fluxos implícitos** (observabilidade) como parte da arquitetura, com decisão e evidência.
- Integrar validações automatizáveis no pipeline **como geração de evidência**, não como substituto de revisão humana.
- Usar *sunset* e revisão periódica para exceções arquiteturais, evitando dívida estrutural permanente.
