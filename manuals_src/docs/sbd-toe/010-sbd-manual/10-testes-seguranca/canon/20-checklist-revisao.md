---
id: checklist-revisao
title: Checklist - Testes de Segurança
description: Instrumento de verificação binária e auditável da adoção prática das práticas de validação contínua de segurança.
tags: [checklist, revisão, testes, segurança, conformidade, rastreabilidade]
sidebar_position: 20
sidebar_label: Checklist de Revisão
---


# Checklist de Revisão Periódica - Testes de Segurança

Este checklist aplica-se a todas as aplicações que exigem validação de segurança no seu ciclo de vida, e serve como instrumento de verificação **binária e auditável** da **adoção prática das prescrições do Capítulo 10 - Testes de Segurança** (`TST-001` a `TST-010`), permitindo:

- Controlo da aplicação proporcional de testes (por nível L1–L3);
- Verificação objetiva da presença, execução e tratamento dos testes;
- Geração de indicadores operacionais agregáveis por projeto, equipa ou organização.

> 🗓️ **Recomenda-se a sua revisão a cada release, mudança de arquitetura, ou regressão relevante**, conforme indicado na `aplicacao-lifecycle`.

---

## 📋 Itens de Verificação

| Item                                                                                                      | Verificado? |
|-----------------------------------------------------------------------------------------------------------|-------------|
| Existe estratégia de testes documentada e versionada, proporcional ao risco (L1–L3), mapeada aos requisitos do Cap. 02 e revista no último ano ou após alteração de risco/arquitetura? (`TST-001`) | ☐           |
| O pipeline executa SAST automático e rastreável, com perfil de regras versionado e baseline de falsos positivos aprovada por AppSec? (`TST-002`) | ☐           |
| O DAST é executado em staging com âmbito, autenticação e política de findings definidos, sem dados reais (quando aplicável)? (`TST-005`) | ☐           |
| As aplicações L3 têm IAST instrumentado em staging com cobertura de fluxos críticos verificada? (`TST-010`) | ☐           |
| Foi aplicado fuzzing aos componentes de processamento de input complexo, com corpus gerido (quando aplicável)? (`TST-009`) | ☐           |
| Cada vulnerabilidade corrigida tem teste de regressão de segurança integrado no pipeline e ligado ao finding original? (`TST-006`) | ☐           |
| Estão definidos e medidos thresholds mínimos de cobertura de testes por nível de risco? (`TST-007`)        | ☐           |
| Os testes estão integrados no pipeline com gates que bloqueiam a promoção quando os critérios mínimos não são atingidos, e a build bloqueia findings críticos não justificados? | ☐           |
| Os findings são triados, classificados e geridos com ciclo de vida e SLA de correção por severidade, centralizados numa plataforma de gestão? (`TST-003`) | ☐           |
| As exceções de segurança são aprovadas formalmente, com justificação, prazo e plano de reteste, e as vencidas são revalidadas? | ☐           |
| A evidência de testes é reproduzível e auditável a partir do mesmo estado do código, ligada ao commit ou release? (`TST-004`) | ☐           |
| Cada decisão pass/fail e cada override têm responsável humano explícito registado?                        | ☐           |
| Os ativos do processo de teste são protegidos (dados reais proibidos por omissão, credenciais segregadas e de privilégio mínimo, masking de segredos nos logs)? | ☐           |
| Foi realizado PenTesting com âmbito, metodologia documentada e rules of engagement, com reteste de correções e integração dos findings (quando aplicável)? (`TST-008`) | ☐           |
| A eficácia do programa é medida com KPIs (cobertura, SLA de resolução, regressão, ruído) e os findings são comunicados automaticamente às equipas? | ☐           |
| O uso de IA em testes está coberto por política (minimização, masking, sem auto-merge de patches), com eval suites versionadas como gate para agentes de IA, e a TLPT readiness preparada para entidades sujeitas a DORA (quando aplicável)? | ☐           |

---

## 🔄 Integração Operacional

- Este checklist pode ser integrado em **pipelines, revisões de release, auditorias internas ou gates de produção**;
- Os resultados podem ser rastreados por **commit, release, aplicação ou equipa**;
- Cada item deve ser validado com **evidência objetiva** (ex: logs de pipeline, relatórios de testes, issues, comentários em PRs, relatórios de PenTesting).

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada e documentada.

---

## ✅ Conformidade e KPI

- A validação deste checklist permite declarar **conformidade com o Capítulo 10 - Testes de Segurança**;
- A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**;
- Este resultado pode ser agregado por equipa ou projeto como **indicador de maturidade operacional**.

> 📌 Este mecanismo está alinhado com o modelo de controlo contínuo, rastreabilidade e proporcionalidade definido no SbD-ToE.
