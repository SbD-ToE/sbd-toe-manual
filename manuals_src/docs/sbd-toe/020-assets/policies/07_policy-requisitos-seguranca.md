---
id: policy-requisitos-seguranca
title: Política de Requisitos de Segurança
description: Política organizacional que define como os requisitos de segurança devem ser selecionados, documentados, rastreados, validados e mantidos ao longo do ciclo de vida de cada aplicação, de forma proporcional ao nível de risco classificado.
tags: [policy, requisitos, segurança, catálogo, backlog, rastreabilidade, validação, SDLC, cap02, L1, L2, L3, governance]
sidebar_position: 7
---

# Política de Requisitos de Segurança

## 1. Objetivo

Esta política define como os **requisitos de segurança** devem ser selecionados, documentados, rastreados, validados e mantidos ao longo de todo o ciclo de vida de cada aplicação desenvolvida ou operada pela organização.

A inclusão de requisitos de segurança no processo de desenvolvimento não é opcional — é a base que garante que a segurança é considerada por design e não corrigida a posteriori. Sem requisitos formais, a equipa desenvolve sem critérios explícitos de segurança, o que torna a validação impossível e a conformidade não demonstrável.

---

## 2. Âmbito

Esta política aplica-se a todas as aplicações com classificação de risco ativa (L1, L2 ou L3), em todas as fases do ciclo de vida: conceção, desenvolvimento, integração, testes, deploy e manutenção.

---

## 3. Catálogo de requisitos

### 3.1 Baseline organizacional

A organização mantém um **catálogo baseline de requisitos de segurança**, organizado por domínio e nível de aplicabilidade (L1, L2, L3), alinhado com o modelo SbD-ToE Cap. 02.

O catálogo baseline é versionado, mantido por AppSec e revisto pelo menos anualmente.

### 3.2 Catálogo do projeto

No arranque de cada projeto (ou na integração de uma aplicação existente no modelo SbD-ToE), deve ser criado um **catálogo de requisitos do projeto** (`REQ-XXX`), derivado da baseline organizacional e filtrado pelo nível de criticidade da aplicação.

**Requisitos do catálogo do projeto:**

- [ ] Derivado da baseline organizacional com filtro explícito pelo nível L1/L2/L3
- [ ] Identificadores únicos por requisito (`REQ-XXX`)
- [ ] Owner definido e periodicidade de revisão estabelecida
- [ ] Mapeamento para critérios de validação associados
- [ ] Versionado no repositório do projeto ou plataforma de gestão de requisitos
- [ ] Atualizado sempre que o nível de criticidade ou o âmbito da aplicação se altere

---

## 4. Seleção proporcional de requisitos

A seleção de requisitos deve ser **proporcional ao nível de risco** da aplicação:

| Prática | L1 | L2 | L3 |
|---|---|---|---|
| Subconjunto essencial do catálogo | Obrigatório | — | — |
| Catálogo completo aplicável ao nível | — | Obrigatório | Obrigatório |
| Requisitos de domínio específico (auth, logging, API, etc.) | Recomendado | Obrigatório | Obrigatório |
| Revisão independente da seleção | Não aplicável | Recomendado | Obrigatório |
| Rastreabilidade bidirecional requisito → código | Recomendado | Obrigatório | Obrigatório |

---

## 5. Integração no ciclo de desenvolvimento

Os requisitos de segurança devem ser aplicados nos seguintes momentos do SDLC:

| Fase / Evento | Ação esperada | Artefacto principal |
|---|---|---|
| Início de projeto | Selecionar requisitos proporcionais ao nível de criticidade | `matriz-controlos-por-risco.md` |
| Grooming / Planeamento | Transformar requisitos em cartões rastreáveis no backlog | Backlog com tags `SEC-Lx-*` |
| Nova funcionalidade ou refactor | Revalidar requisitos aplicáveis à alteração | Story/tarefa técnica atualizada |
| Nova integração ou exposição externa | Rever requisitos de autenticação, logging, controlo de acesso e APIs | Issue/checklist de integração |
| Sprint review / Testes | Verificar critérios de aceitação de segurança e recolher evidência | Critérios + testes + evidência |
| Release | Confirmar que todos os requisitos aplicáveis têm evidência de validação | Checklist de release |
| Pós-incidente | Rever se o incidente evidencia lacuna nos requisitos; atualizar catálogo | Catálogo atualizado |

---

## 6. Taxonomia e tags

Os requisitos de segurança no backlog devem ser identificados com uma taxonomia rastreável. O formato de referência é:

```
SEC-Lx-Tyy-ZZZ
```

Onde:
- `Lx` — nível de criticidade (L1, L2, L3)
- `Tyy` — categoria do domínio (ex: AUT, LOG, VAL, API, CFG, ENC, INT...)
- `ZZZ` — número sequencial do requisito

A validação automática da presença de tags `SEC-Lx-*` nos PRs relevantes deve ser configurada no pipeline CI/CD em L2 e L3.

---

## 7. Critérios de validação

Cada requisito selecionado deve ter **critérios de aceitação explícitos e verificáveis**, definidos antes do início do desenvolvimento:

- [ ] Critérios de aceitação formais definidos no cartão ou documento de requisito
- [ ] Alinhamento com o catálogo de requisitos do projeto
- [ ] Validação prevista em testes automáticos e/ou revisões formais
- [ ] Evidência de validação registada e rastreável ao requisito

Requisitos sem critérios de validação definidos não devem ser considerados como implementados, independentemente do estado do desenvolvimento.

---

## 8. Revisão por alteração relevante

Os requisitos aplicáveis devem ser revistos sempre que ocorra uma das seguintes alterações:

| Trigger | Ação |
|---|---|
| Nova integração externa | Rever requisitos de autenticação, integridade e logging |
| Novo tipo de dado tratado | Rever requisitos de encriptação, controlo de acesso e logging |
| Alteração de exposição | Rever requisitos de API, autenticação e configuração |
| Alteração de arquitetura | Rever requisitos de arquitetura segura e threat modeling |
| Novo perfil de utilizador | Rever requisitos de controlo de acesso e sessões |
| Resultado de incidente | Atualizar catálogo com requisitos que o incidente evidenciou como ausentes |

A revisão deve ser documentada com referência ao trigger, aos requisitos atualizados e à aprovação.

---

## 9. Gestão de exceções a requisitos

Quando um requisito obrigatório para o nível não pode ser implementado, aplica-se o processo definido na **Política de Gestão de Exceções de Segurança** (`05_policy-gestao-excecoes`):

- Justificação técnica obrigatória
- Mitigação compensatória definida
- TTL proporcional ao nível e severidade
- Aprovação pela alçada adequada
- Registo formal com referência ao requisito excecionado

---

## 10. Proporcionalidade por nível

| Requisito da política | L1 | L2 | L3 |
|---|---|---|---|
| Catálogo do projeto criado e versionado | Recomendado | Obrigatório | Obrigatório |
| Tags `SEC-Lx-*` no backlog | Recomendado | Obrigatório | Obrigatório |
| Critérios de validação por requisito | Recomendado | Obrigatório | Obrigatório |
| Validação automática de tags no pipeline | Não aplicável | Recomendado | Obrigatório |
| Revisão independente da seleção | Não aplicável | Recomendado | Obrigatório |
| Relatório de rastreabilidade exportável | Opcional | Recomendado | Obrigatório |
| Reavaliação por alteração relevante | A pedido | Obrigatório | Obrigatório |
| Exceções formalizadas com TTL | Simplificado | Obrigatório | Obrigatório (TTL curto) |

---

## 11. Artefactos

| Artefacto | Localização sugerida | Retenção |
|---|---|---|
| Catálogo de requisitos do projeto (`REQ-XXX`) | `docs/req/` ou plataforma de gestão | Enquanto a aplicação estiver ativa |
| Matriz de controlos por nível | `docs/security/` | Enquanto a aplicação estiver ativa |
| Backlog com tags `SEC-Lx-*` | Ferramenta de gestão de projetos | Histórico preservado |
| Evidências de validação por requisito | Repositório de evidências / CI/CD | Conforme Política de Rastreabilidade |
| Relatório de rastreabilidade | GRC / export periódico | 2 anos |

---

## 12. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Product Owner | Garantir que requisitos de segurança entram no backlog com critérios de aceitação |
| Tech Lead / Arquiteto | Selecionar requisitos proporcionais ao nível; rever por alteração relevante |
| Developer | Implementar requisitos com evidência rastreável; reportar bloqueios |
| AppSec Engineer | Manter catálogo baseline; validar seleção em L2/L3; conduzir revisões independentes |
| QA | Verificar critérios de aceitação; recolher e arquivar evidências de validação |
| GRC / Compliance | Monitorizar cobertura de requisitos; emitir relatórios de rastreabilidade |

---

## 13. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Atualização do catálogo baseline SbD-ToE Cap. 02
- Incidente que evidencie lacuna no processo de seleção ou validação de requisitos
- Alteração regulatória com impacto nos requisitos mínimos de segurança

---

## 14. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 02 — Requisitos de Segurança | Catálogo base, taxonomia, user stories de seleção e rastreabilidade |
| SbD-ToE Cap. 01 — Classificação de Aplicações | Nível de criticidade que determina a seleção proporcional |
| SbD-ToE Cap. 03 — Threat Modeling | Trigger para revisão de requisitos após identificação de ameaças |
| OWASP ASVS | Application Security Verification Standard — catálogo de referência |
| NIST SP 800-160 | Systems Security Engineering |
| SSDF PW.1 | Definição de requisitos de segurança com base em risco |
| ISO/IEC 27001 — Cláusula 8.1 | Planeamento e controlo operacional |
