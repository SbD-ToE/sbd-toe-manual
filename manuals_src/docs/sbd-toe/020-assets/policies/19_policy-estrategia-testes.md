---
id: policy-estrategia-testes
title: Política de Estratégia de Testes de Segurança
description: Política organizacional que define os requisitos para a estratégia de testes de segurança ao longo do ciclo de vida de aplicações, incluindo SAST, DAST, SCA, IAST, fuzzing e testes manuais, com gates obrigatórios, SLAs de triagem de findings e gestão centralizada de resultados, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, testes de segurança, SAST, DAST, IAST, SCA, fuzzing, gates, findings, triagem, SLA, cap10, L1, L2, L3, governance, DevSecOps]
sidebar_position: 19
---

# Política de Estratégia de Testes de Segurança

## 1. Objetivo

Esta política define os requisitos para a **estratégia de testes de segurança** ao longo do ciclo de vida de aplicações classificadas como L1, L2 ou L3.

Testes de segurança não são uma fase — são um conjunto de práticas complementares que devem ser integradas em cada etapa do SDLC, desde a revisão de código até à validação em produção. Cada técnica tem âmbito e limitações distintas: o SAST encontra padrões no código estático mas não vê comportamento em runtime; o DAST valida a aplicação em execução mas não cobre todos os caminhos de código; o fuzzing descobre condições inesperadas que nenhuma das anteriores encontra de forma sistemática. A cobertura eficaz requer uma estratégia composta e proporcional ao risco.

O objetivo desta política é garantir que:

- A cobertura de testes de segurança é proporcional ao nível de criticidade da aplicação
- Os gates automáticos bloqueiam regressões graves antes da promoção a produção
- Os findings são geridos de forma centralizada, com triagem formal e SLA definido
- Os relatórios de testes são arquivados como evidência auditável por release

---

## 2. Técnicas de teste e obrigatoriedade

### 2.1 Matriz de obrigatoriedade por nível

| Técnica | L1 | L2 | L3 |
|---|---|---|---|
| **SAST** (análise estática) | Recomendado | Obrigatório | Obrigatório |
| **Secret detection** | Obrigatório | Obrigatório | Obrigatório |
| **SCA** (composição de software) | Obrigatório (alerta) | Obrigatório (gate) | Obrigatório (gate) |
| **DAST** (análise dinâmica) | Recomendado | Obrigatório em staging | Obrigatório em staging + critérios de cobertura |
| **IAST** (instrumentação em runtime) | Opcional | Recomendado | Recomendado |
| **Fuzzing** | Opcional | Recomendado (endpoints críticos) | Obrigatório (endpoints públicos + parsing) |
| **Testes manuais de segurança** | Não obrigatório | Recomendado por release | Obrigatório por release major |
| **PenTesting** | Não obrigatório | Recomendado anual | Obrigatório (ver Política de PenTesting) |

### 2.2 SAST

- Executado em cada PR e em cada build de integração
- Configurado com rulesets derivados das guidelines de desenvolvimento por stack
- Findings classificados por severidade (Critical, High, Medium, Low, Informational)
- Supressões inline requerem comentário de justificação e são reportadas como métrica

### 2.3 DAST

- Executado em ambiente de staging após cada promoção bem-sucedida
- Requer ambiente com autenticação configurada para cobertura de endpoints protegidos
- Âmbito definido para evitar teste em sistemas externos reais (mocks ou sandbox para integrações)
- Cobertura mínima de endpoints por release documentada e medida

### 2.4 Fuzzing

- Focado em parsers de input, endpoints de upload, APIs que aceitem estruturas complexas
- Executado como job noturno ou por release, não necessariamente em cada PR
- Findings classificados e integrados no sistema centralizado de gestão

---

## 3. Gates de segurança por nível

Os thresholds de bloqueio devem ser documentados e versionados em `gates-config.yaml` ou equivalente:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| SAST Critical/High | Alerta | Bloqueia merge | Bloqueia merge |
| SAST Medium | Não aplicável | Alerta | Bloqueia merge |
| Secret detection (qualquer finding) | Bloqueia | Bloqueia | Bloqueia |
| SCA High/Critical CVE sem exceção | Alerta | Bloqueia promoção | Bloqueia promoção |
| DAST High/Critical em staging | Não aplicável | Bloqueia promoção a produção | Bloqueia promoção a produção |
| Cobertura DAST abaixo de threshold | Não aplicável | Alerta | Bloqueia (threshold: 80% de endpoints) |
| Fuzzing com crash confirmado | Não aplicável | Bloqueia release | Bloqueia release |

:::warning
Um gate configurado em modo apenas-alerta em L2/L3 deve ser registado como exceção formal com data de expiração. Exceções a gates de segurança expiradas sem reavaliação são tratadas como não-conformidade.
:::

---

## 4. Gestão centralizada de findings

### 4.1 Plataforma unificada

Todos os findings de SAST, DAST, IAST, SCA e fuzzing devem ser consolidados numa plataforma centralizada (ex: DefectDojo, SonarQube Security Dashboard, GitHub Security, GitLab Security Dashboard), com:

- [ ] Deduplicação de findings com a mesma origem em múltiplas ferramentas
- [ ] Metadados unificados: CVE/CWE, severidade, ferramenta, commit, módulo, estado
- [ ] Histórico de estado (aberto, em progresso, resolvido, aceite, suprimido)
- [ ] Rastreabilidade entre finding e PR/commit de resolução

### 4.2 Triagem formal

Cada finding bloqueante deve ser triado com decisão documentada:

| Decisão | Condição | Requisito |
|---|---|---|
| **CORRIGIR** | Finding válido e exploitável | Estimativa de resolução; ticket criado |
| **ACEITAR** | Risco avaliado e aceite explicitamente | Exceção formal conforme Política de Exceções |
| **SUPRIMIR (FP)** | Falso positivo demonstrado | Evidência técnica; aprovação de AppSec |
| **DIFERIR** | Resolução adiada com justificação | Prazo definido; aceitação de risco temporária |

### 4.3 SLAs de triagem e resolução

| Severidade | SLA de triagem | SLA de resolução (L2) | SLA de resolução (L3) |
|---|---|---|---|
| Critical | 24 horas | 7 dias | 3 dias |
| High | 48 horas | 30 dias | 15 dias |
| Medium | 5 dias úteis | 90 dias | 45 dias |
| Low | 10 dias úteis | 180 dias | 90 dias |

---

## 5. Rastreabilidade e evidência por release

Para cada release, deve existir evidência dos testes realizados:

- [ ] Relatórios de SAST, DAST, SCA e fuzzing (quando aplicável) arquivados como artefactos do pipeline
- [ ] Checklist de release preenchida com estado de cada gate
- [ ] Findings críticos com estado documentado (corrigidos, exceções aprovadas)
- [ ] Cobertura de DAST medida e registada
- [ ] Aprovação formal de release com referência aos relatórios (ver Política de Release Seguro)

---

## 6. Tratamento de falsos positivos

Falsos positivos (FP) são inevitáveis em qualquer ferramenta de análise estática ou dinâmica. O processo para suprimir um finding como FP deve ser formal:

- [ ] Evidência técnica da não-exploitabilidade documentada (code path analysis, prova de conceito falhada)
- [ ] Aprovação por AppSec Engineer para findings High/Critical
- [ ] Registo da supressão na plataforma centralizada com motivo, responsável e data
- [ ] Supressões inline no código (ex: `# nosec`, `// noqa`) associadas ao identificador do finding suprimido e sujeitas a revisão periódica

Métricas de FP por ferramenta devem ser acompanhadas para calibrar as configurações dos scanners.

---

## 7. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Executar análise local antes de submeter PR; triar findings de SAST em PRs; não suprimir sem registo |
| AppSec Engineer | Definir e calibrar thresholds; gerir plataforma centralizada de findings; aprovar supressões de FP High/Critical; definir estratégia de DAST |
| DevOps / SRE | Integrar ferramentas no pipeline; configurar jobs de DAST em staging; arquivar relatórios |
| Tech Lead | Garantir resolução de findings dentro de SLA; escalar conflitos entre timeline e gates |
| Product Manager | Aprovar aceitação de risco em findings que não podem ser resolvidos antes da release |

---

## 8. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Vulnerabilidade introduzida em produção que deveria ter sido detetada por uma das técnicas cobertas
- Adoção de nova técnica de teste ou ferramenta com impacto na estratégia
- Alteração de thresholds com impacto material na taxa de bloqueio de builds

---

## 9. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 10 — Testes de Segurança | Estratégia, gates, findings, triagem, SLA |
| SbD-ToE Cap. 07 — CI/CD Seguro | SAST, DAST e SCA integrados no pipeline |
| Política de DAST e Fuzzing (`01_policy-dast-fuzzing.md`) | Requisitos específicos de DAST e Fuzzing |
| Política de Release Seguro (`20_policy-release-seguro.md`) | Checklist de release e aprovação com base nos testes |
| OWASP Testing Guide (v4.2) | Metodologia de referência para testes de segurança |
| OWASP DAST Guide | Boas práticas de análise dinâmica |
| NIST SP 800-115 | Technical Guide to Information Security Testing |
| SSDF PW.8.2 | Test, evaluate, and remediate the software |
| DefectDojo | Plataforma de referência para gestão centralizada de findings |
