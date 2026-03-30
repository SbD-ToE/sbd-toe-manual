---
id: policy-rastreabilidade-organizacional
title: Política de Rastreabilidade Organizacional
description: Política organizacional que define os requisitos para a rastreabilidade das práticas de segurança ao longo do ciclo de vida das aplicações, incluindo repositório de conformidade por aplicação, designação de owners de segurança, validações periódicas por capítulo SbD-ToE, evidências auditáveis e dashboard organizacional, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, rastreabilidade, conformidade, owners, Security Champion, repositório conformidade, auditoria, dashboard, cap14, L1, L2, L3, governance, SSDF, ISO27001]
grupo: governacao
sidebar_position: 34
---

# Política de Rastreabilidade Organizacional

## 1. Objetivo

Esta política define os requisitos para a **rastreabilidade das práticas de segurança ao nível organizacional** - o conjunto de mecanismos que permitem demonstrar, a qualquer momento, o estado de conformidade de cada aplicação com os requisitos do SbD-ToE, identificar os responsáveis por cada decisão de segurança, e apresentar evidência auditável a auditores internos, externos ou reguladores.

Conformidade sem rastreabilidade é uma declaração de intenção, não uma postura de segurança verificável. A rastreabilidade transforma práticas dispersas em evidência estruturada: permite detetar desvios antes de incidentes, suportar decisões de risco com dados históricos, e demonstrar maturidade de forma objectiva. Sem um mecanismo de rastreabilidade organizacional, o estado real de segurança das aplicações fica invisível para a gestão e para a auditoria.

O objetivo desta política é garantir que:

- Cada aplicação tem um repositório de conformidade que reflecte o estado real das práticas SbD-ToE
- Cada aplicação classificada como L2/L3 tem um owner de segurança designado formalmente
- As validações periódicas de conformidade são executadas com cadência proporcional ao nível de risco
- Toda a evidência de conformidade é auditável, versionada e ligada à decisão que a originou
- A organização tem visibilidade agregada do estado de segurança do seu portfólio

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Básico; registo de classificação e owner técnico; revisão anual |
| L2 | Obrigatório; repositório de conformidade por aplicação; Security Champion designado; validação semestral; dashboard recomendado |
| L3 | Obrigatório; repositório completo versionado; Security Champion com formação; validação trimestral; dashboard obrigatório; evidência formal para auditoria |

---

## 3. Repositório de conformidade por aplicação

Cada aplicação deve ter um repositório de conformidade - um artefacto estruturado, versionado e auditável que consolida o estado de conformidade com todos os capítulos do SbD-ToE aplicáveis.

### 3.1 Formato e conteúdo mínimo

O repositório pode ser implementado como ficheiro YAML ou Markdown versionado em repositório de código, ferramenta GRC, ou sistema de gestão de conformidade. O formato específico não é prescrito - a auditabilidade e a acessibilidade são os requisitos determinantes.

| Campo | Descrição | Obrigatoriedade |
|---|---|---|
| `application.id` | Identificador único da aplicação | Obrigatório |
| `application.level` | Nível de criticidade (L1/L2/L3) e data de última classificação | Obrigatório |
| `owner.security_champion` | Identidade do Security Champion designado | L2/L3 |
| `owner.tech_lead` | Identidade do Tech Lead responsável | Obrigatório |
| `compliance.chapters[]` | Estado por capítulo SbD-ToE (Cap. 02–13): `Sim / Não / Exceção` | Obrigatório |
| `compliance.evidence[]` | Links para evidências por capítulo (relatórios, scans, revisões) | L2/L3 |
| `exceptions[]` | Excepções activas com referência ao registo de excepções | L2/L3 |
| `last_validated` | Data e responsável pela última validação | Obrigatório |
| `next_validation` | Data prevista para a próxima validação | Obrigatório |

### 3.2 Atualização

O repositório deve ser actualizado:

- Após cada validação periódica de conformidade
- Após cada alteração significativa de arquitectura, nível de criticidade ou owner
- Após resolução ou aprovação de excepção
- Após release major ou evento de segurança relevante

---

## 4. Designação formal de owners de segurança

Para cada aplicação classificada como L2 ou L3, deve existir um **Security Champion formalmente designado**, com responsabilidades de segurança documentadas e registadas.

### 4.1 Requisitos de designação

| Requisito | Descrição |
|---|---|
| Designação formal | Por escrito - e-mail oficial, sistema de RH, ou documento assinado por gestor |
| Responsabilidades documentadas | Submissão de excepções, validações periódicas, comunicação de risco, manutenção do repositório de conformidade |
| Formação mínima concluída | O Security Champion deve ter completado o trilho de formação de segurança obrigatório para a sua função |
| Substituto designado | Para continuidade em ausências prolongadas (L3 obrigatório) |

### 4.2 Registo centralizado

A organização deve manter um registo centralizado de todos os Security Champions activos, com identificação da aplicação, identidade, data de designação e estado de formação. Este registo é a fonte de verdade para escalamento, comunicação de risco e auditoria.

:::note
A designação de Security Champion não exime os restantes membros da equipa das responsabilidades de segurança que lhes cabem nos termos das políticas aplicáveis. O Security Champion é o ponto de coordenação e de responsabilização - não o único responsável pela segurança da aplicação.
:::

---

## 5. Validações periódicas de conformidade

As validações periódicas de conformidade têm como objectivo verificar se os requisitos do SbD-ToE continuam aplicados e eficazes, detectar desvios e recolher evidência actualizada.

### 5.1 Cadência de validação

| Nível | Cadência | Gatilhos adicionais |
|---|---|---|
| L1 | Anual | Alteração significativa de arquitectura |
| L2 | Semestral | Release major; incidente de segurança; alteração de nível |
| L3 | Trimestral | Release major; incidente; alteração de proprietário; auditoria externa |

### 5.2 Processo de validação

Cada ciclo de validação deve cobrir:

- [ ] Verificação do estado de cada capítulo SbD-ToE aplicável (checklist por capítulo)
- [ ] Recolha de evidência actualizada para capítulos em estado `Sim` (ligação a relatórios, scans, revisões)
- [ ] Revisão de excepções activas: validade, progresso de remediação, necessidade de renovação
- [ ] Identificação de novos desvios ou de capítulos sem evidência actualizada
- [ ] Plano de acção para desvios identificados (owner, prazo, prioridade)
- [ ] Actualização do repositório de conformidade com resultado da validação

### 5.3 Resultado e decisão

O resultado da validação deve ser documentado com:

- Estado global: `Conforme / Conforme com desvios / Não conforme`
- Lista de desvios identificados com severidade
- Plano de acção com owners e prazos
- Data da próxima validação

---

## 6. Dashboard organizacional

A organização deve manter visibilidade agregada do estado de conformidade do seu portfólio de aplicações:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Dashboard de estado de conformidade por aplicação | Não aplicável | Recomendado | Obrigatório |
| Métricas de adopção por capítulo SbD-ToE | Não aplicável | Recomendado | Obrigatório |
| Visibilidade de excepções activas e expiradas | Não aplicável | Recomendado | Obrigatório |
| Alertas automáticos para desvios críticos | Não aplicável | Recomendado | Obrigatório |
| Relatórios periódicos para gestão executiva | Não aplicável | Semestral | Trimestral |

O dashboard não substitui o repositório de conformidade por aplicação - é uma vista agregada para gestão e decisão executiva. Os dados devem ser derivados dos repositórios de conformidade individuais para manter consistência.

---

## 7. Evidência auditável

Toda a evidência de conformidade deve satisfazer os seguintes requisitos para ser considerada auditável:

| Requisito | Descrição |
|---|---|
| Rastreabilidade | A evidência deve ser ligável à prática, ao capítulo e à aplicação que suporta |
| Datação | Timestamp de produção e de validação |
| Autoria | Identidade do responsável pela produção ou validação |
| Imutabilidade | Evidência não alterável após produção (ex: artefacto de pipeline assinado, relatório arquivado) |
| Acessibilidade | Disponível a auditores internos e externos sem dependência de acesso a sistemas de produção |

### 7.1 Tipos de evidência aceite

| Tipo | Exemplos |
|---|---|
| Relatórios de ferramentas | Relatório SAST, SCA, DAST, PenTest - com versão de ferramenta, data e âmbito |
| Logs de pipeline | Evidência de execução de gate de segurança com resultado e timestamp |
| Registos de revisão | Pull request com aprovação documentada e referência a checklist de segurança |
| Decisões de excepção | Registo de excepção com aprovação, justificação e data de validade |
| Resultados de testes periódicos | Relatórios de tabletop, war room ou simulação de playbook |

---

## 8. Retenção de artefactos de conformidade

| Artefacto | Retenção mínima |
|---|---|
| Repositório de conformidade (estado actual e histórico) | Vigência da aplicação + 3 anos |
| Evidências de validação | 3 anos |
| Registos de designação de Security Champion | Duração da designação + 2 anos |
| Relatórios de validação periódica | 3 anos |
| Registos de excepções (incluindo expiradas) | 5 anos |

:::note
Em ambientes regulados (DORA, NIS2, RGPD), os prazos regulatórios prevalecem sobre os mínimos desta política. O período mais longo é sempre o aplicável.
:::

---

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Security Champion | Manter o repositório de conformidade da aplicação actualizado; executar ou coordenar validações periódicas; submeter excepções; comunicar risco ao GRC |
| AppSec Engineer | Definir estrutura e requisitos do repositório de conformidade; apoiar validações em L3; auditar qualidade das evidências; alimentar dashboard organizacional |
| Tech Lead | Garantir que a equipa mantém as práticas de conformidade; aprovar planos de acção de desvios identificados |
| GRC / Compliance | Gerir registo centralizado de owners; executar ou auditar validações periódicas; produzir relatórios para gestão executiva; verificar conformidade regulatória |
| Gestão / CISO | Analisar relatórios de estado do portfólio; tomar decisões de risco estratégico; garantir recursos para resolução de desvios críticos |

---

## 10. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Auditoria que identifique lacunas no estado de rastreabilidade de uma ou mais aplicações
- Alteração da estrutura de capítulos do SbD-ToE que requeira actualização dos repositórios de conformidade
- Alteração regulatória que modifique os requisitos de evidência ou retenção

---

## 11. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 14 - Governança & Contratação | US-04: rastreabilidade organizacional; US-08: repositório de conformidade; US-09: designação de owners; US-10: validação periódica; US-13: controlo sistemático por capítulo |
| Política de KPIs de Governação (`35_policy-kpis-governacao.md`) | Métricas derivadas dos dados de rastreabilidade |
| Política de Contratação Segura (`33_policy-contratacao-segura.md`) | Rastreabilidade de fornecedores e contractors |
| NIST SSDF - PO.3, PO.7 | Implementação de práticas de segurança e rastreabilidade |
| OWASP SAMM - PO2, PO3 | Maturidade organizacional em segurança |
| ISO/IEC 27001 - A.18 | Compliance and information security reviews |
| DORA - Art. 17 | ICT risk management documentation and evidence |
| NIS2 - Art. 21 | Cybersecurity measures and accountability |
