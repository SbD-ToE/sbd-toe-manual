---
id: policy-excecoes-cve
title: Política de Exceções a CVEs
description: Política organizacional que define os critérios, o processo formal, as alçadas de aprovação, os controlos compensatórios e os prazos de reavaliação aplicáveis a exceções a vulnerabilidades conhecidas (CVEs) em dependências de software, proporcional ao nível de criticidade da aplicação (L1, L2, L3).
tags: [policy, CVE, exceções, VEX, SCA, risco residual, compensação, reavaliação, cap05, L1, L2, L3, governance, supply chain]
sidebar_position: 12
---

# Política de Exceções a CVEs

## 1. Objetivo

Esta política define os requisitos para a **formalização, aprovação, controlo e reavaliação de exceções a vulnerabilidades conhecidas (CVEs)** detetadas em dependências de software.

A existência de um CVE num componente utilizado não implica necessariamente exploitabilidade imediata - pode tratar-se de uma vulnerabilidade sem vetor de ataque acessível no contexto da aplicação, de um componente que não está exposto, ou de uma situação em que o fix disponível introduz regressões que inviabilizam a atualização imediata. Contudo, a ausência de exploitabilidade direta não dispensa a formalização: exceções não registadas são risco invisível.

O objetivo desta política é garantir que:

- Toda a exceção a um CVE é formalizada, aprovada por alçada adequada e rastreável
- O controlo compensatório que justifica a aceitação é verificável e monitorizado
- Os prazos de reavaliação são definidos por severidade e nível de criticidade da aplicação
- Exceções expiradas ou inválidas são detetadas automaticamente e não persistem silenciosamente

---

## 2. Âmbito

Esta política aplica-se a todas as vulnerabilidades conhecidas (CVEs, GHSA, OSV, ou equivalente) identificadas por ferramentas SCA em dependências de software, incluindo:

- Dependências diretas e transitivas de aplicações
- Componentes presentes em imagens de container
- Módulos e providers em artefactos IaC quando sujeitos a SCA

Não se aplica a vulnerabilidades de código próprio (SAST findings) - essas são cobertas pela Política de Gestão de Exceções de Segurança.

---

## 3. Definição de exceção a CVE

Uma **exceção a CVE** é o registo formal que documenta a decisão de manter um componente com uma vulnerabilidade conhecida em produção durante um período limitado, com base em:

- Análise de impacto que demonstra não-exploitabilidade no contexto específico da aplicação, ou
- Inexistência de fix disponível (upstream ainda não corrigiu), ou
- Fix disponível que introduz regressões inaceitáveis com plano de resolução temporal definido

:::warning
A ausência de exploit público conhecido não é, por si só, justificação suficiente para uma exceção. É necessário demonstrar que o vetor de ataque não está acessível no contexto da aplicação, com evidência técnica verificável.
:::

Uma exceção não é uma dispensa permanente. É uma aceitação temporária de risco residual, com prazo e controlo compensatório.

---

## 4. Tipos de exceção

| Tipo | Situação | Requisito adicional |
|---|---|---|
| **Not affected** | CVE existe mas o componente vulnerável não é utilizado no caminho de código acessível | Evidência técnica de code path analysis |
| **Fix not available** | Upstream não disponibilizou patch; sem versão alternativa | Plano de monitorização e prazo de reavaliação obrigatório |
| **Fix deferred** | Fix disponível mas a atualização requer trabalho de compatibilidade | Plano de atualização com data e owner definidos |
| **Risk accepted** | CVE exploitável mas risco mitigado por controlo compensatório | Controlo compensatório verificável e documentado |

Cada tipo tem requisitos distintos de aprovação e prazo máximo (ver secções 5 e 6).

---

## 5. Processo formal de exceção

### 5.1 Etapas obrigatórias

| Etapa | Responsável | Artefacto |
|---|---|---|
| Identificação do finding | Scanner SCA (automatizado) | CVE + componente + severidade |
| Análise de impacto e exploitabilidade | Developer + AppSec Engineer | Justificação técnica documentada |
| Definição de controlo compensatório | AppSec Engineer / Arquiteto | Evidência do controlo alternativo |
| Aprovação formal | Alçada conforme secção 5.2 | Registo em `excecoes.yaml` ou `vex.yaml` |
| Agendamento de reavaliação | AppSec Engineer | Calendário de revisão com alertas |

### 5.2 Alçadas de aprovação

| Nível da aplicação | Severidade CVE | Aprovador mínimo |
|---|---|---|
| L1 | Low / Medium | Tech Lead |
| L1 | High / Critical | Tech Lead + AppSec Engineer |
| L2 | Low / Medium | AppSec Engineer |
| L2 | High | AppSec Engineer + gestor de aplicação |
| L2 | Critical | AppSec Engineer + gestor de aplicação + Security Officer |
| L3 | Qualquer | AppSec Engineer + Security Officer + CISO (ou delegado) |

### 5.3 Conteúdo mínimo do registo de exceção

Cada exceção deve ser registada em `excecoes.yaml` (ou equivalente, ex: `vex.yaml` em formato VEX) com os seguintes campos:

- [ ] Identificador CVE (ex: `CVE-2024-XXXXX`) ou GHSA equivalente
- [ ] Componente afetado, versão e ecossistema
- [ ] Tipo de exceção (conforme secção 4)
- [ ] Justificação técnica (exploitabilidade no contexto da aplicação)
- [ ] Controlo compensatório aplicado (se tipo "Risk accepted")
- [ ] Aprovador e data de aprovação
- [ ] Data de expiração da exceção
- [ ] Referência ao finding SCA que originou a exceção

---

## 6. Prazos máximos e reavaliação

### 6.1 TTL por severidade e tipo

| Severidade CVE | Tipo | L1 | L2 | L3 |
|---|---|---|---|---|
| Critical | Fix deferred / Risk accepted | 30 dias | 15 dias | 7 dias |
| High | Fix deferred / Risk accepted | 60 dias | 30 dias | 15 dias |
| Medium | Qualquer | 180 dias | 90 dias | 45 dias |
| Low | Qualquer | 365 dias | 180 dias | 90 dias |
| Fix not available | Qualquer | 90 dias | 60 dias | 30 dias |
| Not affected | - | Sem TTL* | Sem TTL* | Sem TTL* |

*Exceções do tipo "Not affected" devem ser reavaliadas sempre que o componente é atualizado ou quando é publicada nova informação sobre o CVE que altere o contexto de exploitabilidade.

### 6.2 Reavaliação

Antes da expiração de cada exceção, deve ser realizada uma reavaliação que determine:

- **Mantém-se**: a situação não mudou; controlo compensatório continua eficaz; nova data de expiração é definida (requer nova aprovação da mesma alçada)
- **Resolve-se**: o fix foi aplicado; a exceção é encerrada
- **Escala**: a situação agravou (ex: exploit público publicado); a exceção é reclassificada e a alçada de aprovação sobe

:::warning
Uma exceção expirada sem reavaliação documentada é tratada como não-conformidade. O pipeline deve detetar exceções expiradas em `excecoes.yaml` e bloquear o build em L2/L3 até que a reavaliação seja concluída.
:::

---

## 7. Controlos compensatórios

Quando o tipo de exceção é "Risk accepted", deve ser definido e verificado um controlo compensatório que reduza a probabilidade ou o impacto de exploração. Exemplos de controlos compensatórios aceites:

| Controlo | Descrição |
|---|---|
| WAF / filtering | Filtragem de payloads associados ao vector de exploração na camada de rede ou aplicação |
| Isolamento de rede | Componente vulnerável sem acesso externo direto; tráfego controlado por firewall ou service mesh |
| Desativação de feature | Funcionalidade vulnerável desativada na configuração da aplicação |
| Runtime protection | RASP ou eBPF-based monitoring com deteção de tentativas de exploração |
| Acesso restrito | Componente acessível apenas por utilizadores autenticados e autorizados, com MFA ativo |

Os controlos compensatórios devem ser verificáveis - a sua eficácia deve poder ser demonstrada em auditoria.

---

## 8. Integração no pipeline

O pipeline CI/CD deve verificar o estado das exceções ativas em cada build:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| Bloquear build se CVE Critical/High sem exceção aprovada | Não | Sim | Sim |
| Bloquear build se exceção expirada sem reavaliação | Não | Sim | Sim |
| Alertar se exceção com menos de 7 dias para expirar | Recomendado | Obrigatório | Obrigatório |
| Gerar relatório de exceções ativas por build | Recomendado | Obrigatório | Obrigatório |

---

## 9. Artefactos

| Artefacto | Descrição | Retenção |
|---|---|---|
| `excecoes.yaml` / `vex.yaml` | Registo de exceções ativas com aprovações e prazos | Enquanto a exceção estiver ativa + 1 ano |
| `sca-report.*` | Relatório SCA com findings e estado de exceções | 90 dias (L2), 1 ano (L3) |
| Histórico de reavaliações | Registos de reavaliações anteriores com decisões | 2 anos (L3), 1 ano (L2) |

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Identificar e comunicar CVEs sem fix imediato; propor justificação e tipo de exceção |
| AppSec Engineer | Analisar impacto e exploitabilidade; validar controlos compensatórios; aprovar/rejeitar exceções; gerir calendário de reavaliação |
| Tech Lead | Definir plano de atualização para "Fix deferred"; garantir reavaliação dentro do prazo |
| Security Officer / CISO | Aprovar exceções Critical em L2/L3; ser notificado de exceções expiradas sem resolução |
| DevOps / SRE | Configurar gate de exceções no pipeline; integrar alertas de expiração |
| GRC / Compliance | Auditar registo de exceções; verificar conformidade com prazos; reportar exceções persistentes |

---

## 11. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em CVE com exceção ativa (independentemente de expiração)
- Alteração regulatória que imponha prazos mais restritivos
- Alteração das ferramentas SCA que afete a forma de gestão de exceções (ex: suporte a VEX)

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 05 - Dependências, SBOM e SCA | Processo SCA, gates, exceções formais |
| SbD-ToE Cap. 14 - Governança e Contratação | Alçadas de exceção por nível de risco |
| Política de Dependências (`10_policy-dependencias.md`) | SCA gates e bloqueios por severidade |
| Política de SBOM (`11_policy-sbom.md`) | Inventário de componentes e correlação CVE-runtime |
| Política de Gestão de Exceções (`05_policy-gestao-excecoes.md`) | Framework transversal de exceções de segurança |
| CycloneDX VEX | Formato de declaração de exploitabilidade |
| CVSS v3.1 / v4.0 | Sistema de pontuação de severidade de vulnerabilidades |
| EPSS (Exploit Prediction Scoring System) | Complemento ao CVSS para avaliação de probabilidade de exploração |
| NIST NVD | Base de dados de referência para CVEs |
| OSV (Open Source Vulnerabilities) | Base de dados alternativa para vulnerabilidades em OSS |
| SSDF PW.4.2 | Review software for vulnerabilities and remediate |
