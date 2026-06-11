---
id: checklist-revisao
title: Checklist SbD-ToE - Governança e Contratação
sidebar_position: 20
description: Checklist binário de controlo da aplicação das práticas de governação por projeto
tags: [checklist, revisao, controlo, projeto, excecoes, aprovacao, contratacao]
sidebar_label: Checklist de Revisão
---


# Checklist de Revisão Periódica - Governança e Contratação

Este checklist aplica-se a **projetos, aplicações ou contratos** com impacto técnico e visa validar a aplicação prática das práticas prescritas no Capítulo 14 - Governança e Contratação (`GOV-001` a `GOV-012`).

> 📌 Deve ser usado em revisões formais, auditorias internas, milestones de projeto ou ciclos de revalidação técnica.

---

## 📋 Itens de Verificação

| Item                                                                                                                   | Verificado? |
|------------------------------------------------------------------------------------------------------------------------|-------------|
| Existe modelo formal de governação de segurança aprovado pela direção e revisto há ≤12 meses? (`GOV-001`)             | ☐           |
| A aplicação ou projeto tem owner de segurança formalmente designado e registado? (`GOV-002`)                          | ☐           |
| O nível de criticidade (L1–L3) está documentado e justificado?                                                         | ☐           |
| As alçadas de aprovação por nível de risco estão documentadas e conhecidas pelos decisores, com escalonamento rastreável? (`GOV-003`) | ☐           |
| Os requisitos mínimos proporcionais ao risco estão identificados e aplicados?                                         | ☐           |
| Existe processo formal de gestão de exceções, registando cada exceção com owner, medida compensatória, evidência referenciável, data de expiração e alerta de revalidação (máx. 90 dias)? (`GOV-004`/`GOV-005`) | ☐           |
| Os contratos com terceiros incluem cláusulas de segurança proporcionais ao risco? (`GOV-006`)                         | ☐           |
| Os fornecedores com acesso técnico foram validados (questionário/checklist; L3: SBOM, SLA de incidentes, direito de auditoria) antes de onboarding? (`GOV-007`) | ☐           |
| Existe rastreabilidade organizacional por aplicação ligando risco → requisitos → exceções → fornecedores → owner? (`GOV-008`) | ☐           |
| A cadeia de autoridade de cada decisão de risco (quem pediu, avaliou, aprovou) é verificável, com evidência referenciável e retida? (`GOV-009`) | ☐           |
| Existe ciclo de revisão periódica de conformidade por tipo de ativo (L3 trimestral, L2 semestral, fornecedores anual), com ações corretivas (owner e prazo)? (`GOV-010`) | ☐           |
| Existem KPIs de governação definidos, recolhidos e reportados à gestão, com thresholds que despoletam ação corretiva? (`GOV-011`) | ☐           |
| Existe avaliação de maturidade ativa (SAMM/DSOMM ou equivalente) há ≤12 meses, com plano de evolução (L3)? (`GOV-012`) | ☐           |
| A aplicação consta da matriz de controlo das práticas SbD-ToE e as políticas organizacionais relevantes estão formalmente aprovadas e auditadas? | ☐           |
| Os contratos com provedores de modelos de IA incluem data retention, training opt-out, localização RGPD (Art. 44–49), audit rights, SLA de notificação de mudanças e conformidade AI Act (Art. 53/55 GPAI), constando o provedor da lista aprovada (`DEP-014`)? | ☐           |
| Existe processo formal de offboarding seguro (revogação de acesso, recuperação de ativos, rotação de segredos) e os decisores têm formação SbD válida nos últimos 12 meses (Cap. 13)? | ☐           |

---

## 🔄 Integração Operacional

- Pode ser usado como **template de revisão recorrente** em Jira, Confluence, SharePoint ou Forms;
- Deve ter validação conjunta por **AppSec, GRC e gestão de produto**;
- Cada item exige **evidência rastreável e versionada**, conforme práticas do Cap. 14.

---

## 🎯 Conformidade e Indicadores

- A validação positiva deste checklist permite declarar **conformidade com o Capítulo 14 - Governança e Contratação**.
- Os resultados podem ser integrados em **dashboards, ciclos de auditoria e métricas de maturidade**.
- Permite derivar **KPIs objetivos** como:
  - % de aplicações com exceções formalmente aprovadas;
  - % de fornecedores validados;
  - % de contratos com cláusulas de segurança;
  - % de projetos com matriz de controlo SbD-ToE atualizada.

---

## 🔗 Ligações cruzadas

- **Cap. 01** - Classificação de risco (base para aplicação proporcional)
- **Cap. 02** - Requisitos de segurança (alvo de exceções, rastreabilidade)
- **Cap. 05** - Dependências e SBOM (cláusulas e validações contratuais)
- **Cap. 10** - Testes de segurança (validação prática de controlos)
- **Cap. 13** - Formação (validação obrigatória de funções críticas)
- **Cap. 14** `addon/11-controlos-praticas-sbd` - Controlo consolidado das práticas SbD-ToE

> ✅ Este checklist é um mecanismo central de controlo contínuo, proporcional e rastreável da adoção do modelo SbD-ToE em contextos reais de governação e contratação.
