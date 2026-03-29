---
id: catalogo-requisitos-deploy
title: Catálogo de Requisitos de Deploy Seguro
description: Catálogo canónico de requisitos de segurança para o processo de deploy (DPL-001 a DPL-009), com aplicabilidade por nível de risco e critérios de aceitação para aprovação formal, proveniência de artefactos, gates automáticos, rollback, credenciais de deploy, staging, monitorização pós-deploy e rastreabilidade end-to-end.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:deploy, DPL, deploy-seguro, rollback, proveniencia, gates, aprovacao, rastreabilidade, L1, L2, L3, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Deploy Seguro

## Âmbito: o processo de deploy como fronteira de segurança

Este catálogo cobre **requisitos de segurança aplicáveis ao processo de deploy** — a fase de promoção de artefactos de software entre ambientes, e em particular para produção. O processo de deploy é uma fronteira crítica: é o momento em que código, credenciais, configuração e artefactos se combinam para modificar estado em sistemas activos.

O âmbito inclui: aprovação formal antes de produção, verificação de proveniência de artefactos no momento de deploy, gates automáticos de segurança, gestão de credenciais de deploy com âmbito mínimo, validação em staging, rollback configurado e testado, monitorização pós-deploy e rastreabilidade completa de cada promoção.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 — Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de NIST SSDF (RV.3, DS.1), SLSA (Deployment requirements), DORA (operational resilience, change management), OWASP SAMM (Practice: Environment Management) e boas práticas de release engineering seguro. Deve ser adaptado à plataforma de deploy em uso e revisto com cada alteração significativa ao processo de release.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-DPL-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| — | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo DPL — Deploy Seguro

Requisitos que garantem que cada promoção a produção é aprovada, rastreável, reversível e proporcional ao risco da aplicação.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| DPL-001 | Aprovação formal obrigatória antes de deploy em produção | ✔ | ✔ | ✔ | Deploy em produção requer aprovação explícita de papel autorizado; aprovação registada com timestamp e identidade do aprovador; sem promoção automática para produção sem gate de aprovação humana. |
| DPL-002 | Promoção apenas de artefactos com proveniência verificada | ✔ | ✔ | ✔ | Artefactos promovidos a produção com assinatura digital ou hash verificado no momento do deploy; proveniência rastreável (commit SHA, pipeline run ID); artefactos sem proveniência verificável rejeitados automaticamente. |
| DPL-003 | Gates automáticos de segurança como condição de promoção | ✔ | ✔ | ✔ | Gates que verificam ausência de CVEs críticos, testes de segurança passados e ausência de segredos detectados executam antes de cada promoção; falha em qualquer gate bloqueia deploy; evidência de execução disponível por deploy. |
| DPL-004 | Rastreabilidade end-to-end de cada deploy | ✔ | ✔ | ✔ | Cada deploy identificável por ID único com registo de: quem aprovou, o que foi deployed (artefacto + commit SHA), quando, para que ambiente e que gates foram executados; rastreabilidade a partir de incidente até ao commit original. |
| DPL-005 | Rollback configurado, testado e com SLA definido | ✔ | ✔ | ✔ | Procedimento de rollback definido, documentado e testado periodicamente (pelo menos uma vez por ciclo de release ou anualmente); tempo máximo de rollback definido e verificado em teste; último teste de rollback com data registada. |
| DPL-006 | Credenciais de deploy com âmbito mínimo e vida curta | ✔ | ✔ | ✔ | Credenciais usadas no deploy com âmbito limitado ao necessário e duração mínima (tokens de curta duração preferidos a credenciais permanentes); sem credenciais de deploy partilhadas entre aplicações; logs de uso de credenciais disponíveis. |
| DPL-007 | Validação em staging antes de promoção a produção | — | ✔ | ✔ | Ambiente de staging com validação funcional e de segurança antes de promoção; critérios de aceitação de staging documentados e evidenciados; staging suficientemente representativo de produção para os fins de validação. |
| DPL-008 | Monitorização activa durante e após deploy | — | ✔ | ✔ | Métricas de saúde e alertas activos durante a janela de deploy e no período de observação pós-deploy; período de observação definido por nível de risco; anomalias nesse período disparam rollback automático ou alerta urgente com SLA de resposta. |
| DPL-009 | Deploy progressivo com contenção de impacto para aplicações críticas | — | — | ✔ | Deploy progressivo implementado para releases de componentes críticos (canary, blue-green, feature flags); thresholds de promoção automática e critérios de rollback definidos; capacidade de contenção sem rollback completo verificável. |

---

## Notas explicativas

- **DPL-001**: "Aprovação humana" não é burocracia — é o mecanismo que garante que uma decisão irreversível (modificar estado em produção) tem um responsável identificável. Em contextos de alta frequência de deploy (múltiplos deploys diários), a aprovação pode ser implementada como gate de release, não necessariamente por deploy individual, desde que o escopo e os critérios estejam documentados.
- **DPL-002**: A verificação de proveniência no momento do deploy é distinta da geração de proveniência no build (CIC-007). É possível gerar uma assinatura válida e nunca a verificar — o controlo efectivo requer verificação downstream, na promoção.
- **DPL-005**: O rollback não testado é um plano teórico, não um controlo de segurança. Incidentes reais mostram regularmente que procedimentos de rollback que nunca foram exercitados falham ou são mais lentos do que esperado quando mais necessários.
- **DPL-006**: O uso de OIDC/workload identity federation para eliminar credenciais de deploy de longa duração é a prática recomendada para L2/L3 — tokens efémeros por execução de pipeline eliminam o risco de credenciais comprometidas por exfiltração.
- **DPL-009**: O deploy progressivo é simultaneamente um controlo de segurança e de resiliência operacional. Para aplicações L3 com impacto regulatório ou de continuidade de negócio, a capacidade de conter um deploy problemático a uma fracção do tráfego é parte integrante da gestão de risco operacional.

---

> Para o modelo de controlo de execução em runtime, consultar [Modelo de Controlo de Execução](./modelo-controle-execucao).
> Para validações pré-deploy, consultar [Validações Pré-Deploy](./validacoes-pre-deploy).
> Para gestão de rollback e controlo de versão, consultar [Controlo de Versão e Rollback](./controle-versao-e-rollback).
> Para deploy progressivo e gestão de risco em release, consultar [Deploy Progressivo e Risco](./deploy-progressivo-e-risco).
> Para monitorização durante e após deploy, consultar [Monitorização e Reacção](./monitorizacao-e-reacao).
