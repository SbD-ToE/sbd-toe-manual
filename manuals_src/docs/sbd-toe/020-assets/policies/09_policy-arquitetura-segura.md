---
id: policy-arquitetura-segura
title: Política de Arquitetura Segura
description: Política organizacional que define os requisitos para a aplicação de princípios de arquitetura segura ao longo do ciclo de vida de aplicações classificadas L2 e L3, incluindo a definição de baseline, gestão de decisões arquiteturais (ADR), revisão de trust boundaries, integração com threat modeling e requisitos de aprovação formal.
tags: [policy, arquitetura, ADR, trust boundaries, solution-architecture, padrões, cap04, L2, L3, governance, design]
sidebar_position: 9
---

# Política de Arquitetura Segura

## 1. Objetivo

Esta política define os requisitos para a aplicação sistemática de **arquitetura segura** ao longo do ciclo de vida de aplicações classificadas como L2 ou L3.

Arquitetura segura não é um documento — é um conjunto de decisões técnicas deliberadas, documentadas, aprovadas e mantidas atualizadas. Sem uma baseline arquitetural explícita, os controlos aplicados carecem de fundamento estrutural, os riscos de design passam despercebidos, e a rastreabilidade entre ameaças, requisitos e implementação torna-se impossível.

O objetivo desta política é garantir que:

- A baseline de arquitetura segura é definida no arranque e mantida atualizada ao longo do ciclo de vida
- As decisões arquiteturais relevantes são registadas com alternativas, trade-offs e impacto em segurança (ADR)
- As trust boundaries e os fluxos de dados são identificados, documentados e controlados
- O catálogo de padrões de arquitetura segura é versionado, aprovado e reutilizável
- A arquitetura está sincronizada com o modelo de ameaças e com os requisitos de segurança aplicáveis

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Opcional; recomendado para sistemas com exposição externa ou lógica crítica |
| L2 | Obrigatório; baseline, ADRs e revisão de trust boundaries |
| L3 | Obrigatório; com revisão independente, aprovação formal e gate no pipeline |

---

## 3. Princípios de arquitetura segura

A baseline organizacional de arquitetura segura deve incorporar os seguintes princípios fundamentais:

| Princípio | Descrição |
|---|---|
| **Isolamento** | Componentes com diferentes níveis de confiança devem estar isolados; acesso entre zonas controlado e mínimo |
| **Minimização de exposição** | Nenhum componente, serviço ou dado deve ter exposição superior à necessária para a sua função |
| **Trust boundaries explícitas** | Todas as fronteiras de confiança devem ser identificadas, documentadas e associadas a controlos |
| **Defense in depth** | Controlos de segurança em múltiplas camadas; falha de um controlo não compromete o sistema |
| **Fail secure** | Em caso de falha, o comportamento padrão deve ser o mais restritivo, não o mais permissivo |
| **Gestão de dependências** | Dependências externas devem ser inventariadas, avaliadas e monitoradas como vetores de risco |
| **Observabilidade segura** | Logs, métricas e traces são componentes arquiteturais — devem ser planeados, não adicionados a posteriori |
| **Imutabilidade de artefactos** | Artefactos de produção devem ser imutáveis; alterações implicam nova build e nova promoção |

---

## 4. Baseline e documentação obrigatória

### 4.1 Arranque de projeto ou épico significativo

No arranque de cada projeto L2/L3 (ou de um épico estrutural relevante), deve ser produzido e aprovado o seguinte conjunto mínimo de artefactos:

| Artefacto | Conteúdo mínimo | Obrigatoriedade |
|---|---|---|
| `principios-arquitetura.md` | Princípios aplicáveis, desvios justificados, versão e aprovação | L2/L3 |
| `solution-architecture.md` | Trust boundaries, fluxos de dados, exposição externa, controlos arquiteturais, ligação a requisitos e ameaças | L2/L3 |
| `trust-boundaries.md` | Inventário de trust boundaries, fluxos entre zonas, controlos por fronteira | L2/L3 |

### 4.2 Conteúdo mínimo da ficha de solução

- [ ] Trust boundaries e fluxos de dados (incluindo telemetria, logs e métricas) identificados
- [ ] Exposição externa justificada e minimizada
- [ ] Controlos arquiteturais explícitos por componente ou zona
- [ ] Ligação a requisitos de segurança aplicáveis (`REQ-*`)
- [ ] Ligação ao modelo de ameaças (`threat-model-*`) quando disponível
- [ ] Versão, data e responsável pela elaboração
- [ ] Aprovação formal registada

---

## 5. Gestão de decisões arquiteturais (ADR)

### 5.1 Quando registar uma ADR

Deve ser criada uma ADR sempre que uma decisão arquitetural tenha impacto em segurança, incluindo:

| Trigger | Exemplos |
|---|---|
| Nova tecnologia ou componente crítico | Escolha de broker de mensagens, base de dados, runtime |
| Alteração de modelo de autenticação ou autorização | Migração para OAuth2, adição de MFA, mudança de modelo de sessão |
| Decisão de exposição de superfície | Abertura de endpoint público, nova integração externa |
| Adoção ou abandono de padrão de arquitetura | Migração de monolito para microsserviços, adoção de service mesh |
| Desvio deliberado a um princípio da baseline | Aceitar exposição adicional por constrangimento técnico |

### 5.2 Conteúdo mínimo de uma ADR

- [ ] Identificador único (`ADR-XXXX`)
- [ ] Contexto e problema a resolver
- [ ] Alternativas consideradas com trade-offs
- [ ] Decisão tomada e justificação
- [ ] Impacto em segurança (explícito, mesmo que nulo)
- [ ] Ligação a ameaças relevantes no modelo de ameaças
- [ ] Ligação a requisitos de segurança afetados
- [ ] Revisão por AppSec Engineer (L2/L3)
- [ ] Estado: Proposta / Aceite / Substituída / Revogada

### 5.3 Proporcionalidade

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| ADR para decisões com impacto de segurança | Opcional | Obrigatório | Obrigatório |
| Revisão de ADR por AppSec | Recomendado | Obrigatório | Obrigatório |
| ADR referenciada no commit ou PR | Recomendado | Obrigatório | Obrigatório |

---

## 6. Trust boundaries e integrações

### 6.1 Inventário de trust boundaries

Cada aplicação L2/L3 deve manter um inventário atualizado das suas trust boundaries, incluindo:

- [ ] Identificação de cada fronteira de confiança (ex: user-to-app, app-to-db, app-to-external-api)
- [ ] Fluxos de dados que atravessam cada fronteira
- [ ] Controlo aplicado em cada fronteira (autenticação, autorização, validação, encriptação)
- [ ] Nível de confiança de cada parte envolvida
- [ ] Integração com o modelo de ameaças (trust boundaries mapeadas no DFD)

### 6.2 Revisão por nova integração

Sempre que é adicionada uma nova integração externa ou uma nova fronteira de confiança, deve ser produzida uma `integration-review.md` com:

- [ ] Identificação do sistema externo e do nível de confiança atribuído
- [ ] Fluxos de dados envolvidos e classificação dos dados
- [ ] Controlos aplicados na integração
- [ ] Alteração ao modelo de ameaças (se aplicável)
- [ ] Aprovação formal antes da promoção a produção

---

## 7. Atualização por alteração arquitetural

O documento de arquitetura deve ser atualizado **antes da promoção a produção** sempre que ocorra uma alteração significativa:

- [ ] Alteração significativa identificada e documentada em `architecture-update.md`
- [ ] Artefactos afetados (`solution-architecture.md`, `trust-boundaries.md`) atualizados
- [ ] ADR criada se a decisão o justificar
- [ ] Modelo de ameaças atualizado se a alteração introduzir novas superfícies ou fluxos
- [ ] Nova versão aprovada formalmente
- [ ] Ligação ao commit ou PR que originou a alteração

:::warning
Alterações arquiteturais não refletidas na documentação e no modelo de ameaças são tratadas como desvio a esta política. O pipeline CI/CD deve verificar a consistência entre alterações de código relevantes e a atualização dos artefactos de arquitetura em L2/L3.
:::

---

## 8. Catálogo de padrões de arquitetura segura

A organização mantém um **catálogo versionado de padrões de arquitetura segura** (`modelos-referencia.md` ou equivalente), que serve como referência reutilizável para novos projetos e decisões de design.

Cada padrão no catálogo deve incluir:

- [ ] Diagrama de arquitetura com trust boundaries
- [ ] Decisões chave e justificação
- [ ] Requisitos de segurança aplicáveis ao padrão
- [ ] Ameaças mitigadas pelo padrão
- [ ] Checklist de implementação verificável
- [ ] Aprovação formal (Arquitetura + AppSec)
- [ ] Histórico de alterações (changelog)

A reutilização de um padrão sem verificação da sua adequação ao contexto específico não isenta a equipa da responsabilidade de validar os controlos aplicáveis.

---

## 9. Aprovação formal

| Artefacto | Nível | Aprovação mínima requerida |
|---|---|---|
| `principios-arquitetura.md` (inicial) | L2 | Arquiteto de Software + AppSec Engineer |
| `principios-arquitetura.md` (inicial) | L3 | Arquiteto de Software + AppSec Engineer + revisão independente |
| `solution-architecture.md` | L2 | Arquiteto de Software + AppSec Engineer |
| `solution-architecture.md` | L3 | Arquiteto de Software + AppSec Engineer + revisão independente |
| ADR com impacto de segurança | L2/L3 | AppSec Engineer |
| `integration-review.md` | L2/L3 | Arquiteto de Software + AppSec Engineer |

---

## 10. Integração com threat modeling

Arquitetura segura e threat modeling estão sincronizados de forma bidirecional:

- O diagrama de arquitetura (`solution-architecture.md`, `trust-boundaries.md`) é a base para o DFD do modelo de ameaças
- Alterações arquiteturais devem despoletar atualização do modelo de ameaças quando introduzem novas superfícies, fluxos ou fronteiras de confiança
- ADRs com impacto de segurança devem referenciar as ameaças relevantes do modelo
- Ameaças identificadas no threat modeling devem ser refletidas em decisões e controlos arquiteturais

---

## 11. Gate no pipeline CI/CD

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| Verificação de existência de `solution-architecture.md` | Não aplicável | Recomendado | Obrigatório |
| Verificação de ADR para PRs com impacto arquitetural | Não aplicável | Recomendado | Obrigatório |
| Bloqueio se arquitetura desatualizada sem justificação aprovada | Não aplicável | Recomendado | Obrigatório |

A configuração do gate deve ser feita pelo DevOps/SRE, em coordenação com AppSec Engineer, e calibrada de forma a não bloquear alterações que não têm impacto arquitetural relevante.

---

## 12. Proporcionalidade por nível

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Baseline de arquitetura documentada | Recomendado | Obrigatório | Obrigatório |
| `solution-architecture.md` aprovado | Recomendado | Obrigatório | Obrigatório |
| ADR para decisões com impacto de segurança | Opcional | Obrigatório | Obrigatório |
| Inventário de trust boundaries | Recomendado | Obrigatório | Obrigatório |
| `integration-review.md` por nova integração | Recomendado | Obrigatório | Obrigatório |
| Revisão independente | Não aplicável | Recomendado | Obrigatório |
| Gate de consistência no pipeline CI/CD | Não aplicável | Recomendado | Obrigatório |
| Catálogo de padrões reutilizável | Opcional | Recomendado | Obrigatório |

---

## 13. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Arquiteto de Software | Definir e manter a baseline; produzir fichas de solução e ADRs; atualizar por alteração relevante |
| AppSec Engineer | Rever e aprovar artefactos de arquitetura; verificar alinhamento com modelo de ameaças e requisitos |
| Tech Lead / Developer | Identificar alterações com impacto arquitetural; referenciar ADRs nos PRs relevantes |
| DevOps / SRE | Configurar gate de consistência no pipeline; garantir armazenamento e controlo de acesso dos artefactos |
| GRC / Compliance | Verificar que todas as aplicações L2/L3 têm artefactos atualizados e aprovados |

---

## 14. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em decisão arquitetural não documentada ou não aprovada
- Alteração significativa dos princípios de referência da organização
- Atualização das metodologias ou frameworks de arquitetura segura adotados

---

## 15. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 04 — Arquitetura Segura | Princípios, user stories, artefactos, aplicação no ciclo de vida |
| SbD-ToE Cap. 03 — Threat Modeling | Sincronização DFD ↔ trust boundaries ↔ modelo de ameaças |
| SbD-ToE Cap. 02 — Requisitos de Segurança | Ligação ADR e solução → requisitos (`REQ-*`) |
| SbD-ToE Cap. 07 — CI/CD Seguro | Gate de consistência arquitetural no pipeline |
| NIST SP 800-160 | Systems Security Engineering — integração de segurança no design |
| NIST SP 800-207 | Zero Trust Architecture |
| TOGAF / SABSA | Frameworks de arquitetura empresarial com dimensão de segurança |
| OWASP Application Security Architecture Cheat Sheet | Padrões de arquitetura segura para aplicações |
| ISO/IEC 27001 — Cláusula 8.1 | Planeamento e controlo operacional de segurança |
