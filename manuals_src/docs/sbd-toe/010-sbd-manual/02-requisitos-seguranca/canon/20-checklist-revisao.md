---
id: checklist-revisao
title: Checklist de Revisão - Requisitos de Segurança
description: Verificações obrigatórias por projeto para garantir a aplicação dos requisitos definidos
tags: [checklist, validação, requisitos, auditoria, rastreabilidade]
sidebar_position: 20
sidebar_label: Checklist de Revisão
---

# Checklist de Verificação - Requisitos de Segurança

Este ficheiro fornece uma lista objetiva e auditável para avaliar se os requisitos de segurança foram devidamente definidos, aplicados e rastreados ao longo do ciclo de vida da aplicação, conforme prescrito neste capítulo.

> Pode ser utilizado como instrumento de controlo por projeto, por sprint ou por tipo de risco.

---

## 📋 Itens de Verificação

| Item                                                                                                       | Verificado? |
|------------------------------------------------------------------------------------------------------------|-------------|
| Existe um catálogo de requisitos de segurança aplicacional adaptado à organização e derivado do catálogo canónico SbD-ToE? | ☐           |
| A seleção dos requisitos aplicáveis ao projeto foi feita com base na classificação de risco (L1–L3) e na matriz por nível? | ☐           |
| Cada requisito selecionado tem um critério de aceitação explícito, verificável e testável?                | ☐           |
| O catálogo de requisitos do projeto está versionado, com histórico de alterações e owner identificado?    | ☐           |
| Foram atribuídas tags de rastreabilidade normalizadas (`SEC-Lx-DOMINIO-CODIGO`) ligadas ao ID canónico aos requisitos definidos? | ☐           |
| Existe uma matriz de rastreabilidade que liga risco → requisito → tag → controlo → validação → evidência, com o tipo de controlo (Preventivo, Detetivo ou Corretivo) classificado? | ☐           |
| Foram consideradas as restrições legais, normativas e contratuais aplicáveis na definição dos requisitos? | ☐           |
| Os requisitos de segurança estão integrados no backlog ou nos artefactos de arquitetura como trabalho rastreável? | ☐           |
| Existe um processo de revisão e re-versionamento dos requisitos disparado por alterações materiais, com nova análise de Threat Modeling registada? | ☐           |
| Cada requisito aplicável foi validado por método adequado (SAST, DAST, teste, revisão ou gate de CI/CD), com validação independente ou gate de bloqueio para requisitos críticos e evidência ligada ao ID? | ☐           |
| Existe um processo formal de exceções com ID, justificação, aprovação, TTL e revalidação obrigatória antes da expiração? | ☐           |
| O uso de ferramentas de automatização ou IA assistida está autorizado, conhecido e coberto por política interna? | ☐           |
| Todo o código, configuração ou teste gerado por automatismos é sujeito a revisão humana e validação técnica independente antes da integração? | ☐           |
| Cada agente de IA em uso operacional (A1+) tem um mandate documentado e versionado em VCS? (`REQ-AGN-001`) | ☐           |
| O nível de autonomia (A0–A4) de cada agente está classificado por contexto e reavaliado em mudança de contexto? (`REQ-AGN-002`) | ☐           |
| Os agentes de IA A2+ têm kill-switch operacional documentado e exercitado na cadência definida? (`REQ-AGN-003`) | ☐           |
| Os agentes de IA A2+ declaram a intenção (audit event) antes de cada tool-call destrutivo ou com efeito externo? (`REQ-AGN-004`) | ☐           |
| Os indicadores RQS de cobertura, rastreabilidade e validação de requisitos são recolhidos e cumprem os thresholds do nível? | ☐           |

---

## 📌 Utilização recomendada

- Esta checklist pode ser utilizada como instrumento de verificação por projeto, sprint ou release.
- Os resultados podem servir como **indicador de controlo operacional** e **KPI de maturidade de aplicação do modelo SbD-ToE**.
- A existência de um catálogo de requisitos e a sua seleção proporcional ao risco devem ser consideradas **pré-condições obrigatórias** para a adoção das restantes práticas.
- O alinhamento com frameworks como OWASP SAMM, SSDF e DSOMM reforça o valor destas verificações, especialmente nos domínios de **Security Requirements** e **Reusable Controls** (ver `achievable-maturity`).
