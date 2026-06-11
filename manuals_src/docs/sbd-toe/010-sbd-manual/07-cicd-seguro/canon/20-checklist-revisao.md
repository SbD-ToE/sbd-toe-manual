---
id: checklist-revisao
title: Checklist - CI/CD Seguro
sidebar_label: Checklist de Revisão
description: Lista de verificação objetiva da adoção das práticas de segurança em pipelines CI/CD
tags: [checklist, auditoria, cicd, devsecops, pipelines]
sidebar_position: 20
---

# Checklist de Revisão Periódica de CI/CD Seguro

Este checklist aplica-se a todas as aplicações com pipelines de integração e entrega contínua, avaliadas segundo os critérios do **Capítulo 07 - CI/CD Seguro** (`CIC-001` a `CIC-010`).
Serve como instrumento de verificação e auditoria da **conformidade com os controlos mínimos prescritos para segurança de pipelines, artefactos, segredos e ambientes de execução**.

Este ficheiro funciona como:

- Instrumento de **controlo binário** (sim / não) por projeto
- **Mecanismo de auditoria** técnica e organizacional
- **KPI operativo** de maturidade em DevSecOps
- Critério objetivo para **promoção de aplicações** para produção

> 🗓️ **Recomenda-se revisão no mínimo a cada 6 meses**, ou sempre que existam alterações relevantes ao pipeline, runners, segredos, políticas, integrações externas ou modelo de promoção.

---

## 📋 Itens de Verificação

| Item                                                                                                               | Verificado? |
|--------------------------------------------------------------------------------------------------------------------|-------------|
| O pipeline está definido como código e versionado, com alterações sujeitas a PR e branches principais protegidas (sem push direto nem force push)? (`CIC-001`) | ☐           |
| O acesso de escrita é granular por branch/projeto com identidade empresarial (SSO/RBAC), e as aplicações L3 exigem assinatura de commits ou tags? | ☐           |
| Os triggers estão restritos a fontes autorizadas, com execuções originadas em forks externos desativadas ou mediadas por aprovação? (`CIC-002`) | ☐           |
| O CI e o CD estão separados por função, com templates reutilizáveis versionados, e a configuração efetiva de execução é registada para auditoria? | ☐           |
| Os segredos são injetados via cofre ou variáveis protegidas, fora de YAML/logs/artefactos, mascarados nos logs e eliminados após uso? (`CIC-003`) | ☐           |
| Os segredos têm âmbito mínimo, segregados por ambiente e aplicação, com rotação periódica e revogação imediata de comprometidos? (`CIC-009`) | ☐           |
| O pipeline usa OIDC ou tokens de curta duração em vez de segredos estáticos long-lived, sem credenciais partilhadas entre aplicações distintas? (`CIC-009`) | ☐           |
| O pipeline executa as validações de segurança aplicáveis (SAST, secrets scanning, IaC scanning, container scanning, SBOM/SCA e DAST em staging para L2/L3)? (`CIC-004`) | ☐           |
| Os resultados dos scanners correspondem a execução observável (logs, run id, exit code) e a build falha automaticamente em findings críticos não justificados? | ☐           |
| O nível de risco (L1–L3) está declarado e condiciona o pipeline, com políticas aplicadas como policy-as-code versionada? | ☐           |
| Os gates de segurança são explícitos, binários e bloqueantes antes de ações irreversíveis, com aprovação humana nominal e separação entre sinal automático e decisão? (`CIC-004`) | ☐           |
| Os runners são efémeros e segregados por projeto/risco, com hardening e integridade de imagens base verificada, sem execução privilegiada, acesso ao Docker socket ou a produção? (`CIC-006`/`CIC-010`) | ☐           |
| As fases de build, test e deploy estão separadas, sem permissões cruzadas e com âmbito de credenciais por stage? (`CIC-008`) | ☐           |
| Os artefactos são assinados com proveniência automática (modelo SLSA), verificada antes da promoção, com armazenamento/transporte seguros e deteção de manipulação? (`CIC-007`) | ☐           |
| Existe rastreabilidade ponta-a-ponta (commit → pipeline → artefacto → release → deploy) com ID único por execução e retenção de logs/evidências conforme política? (`CIC-005`) | ☐           |
| As exceções a controlos CI/CD estão registadas, aprovadas, temporárias e sinalizadas no pipeline, e os agentes de IA que o operam recebem credenciais OIDC efémeras com audit por tool invocation e kill-switch? | ☐           |

---

## 🔄 Notas finais

- Este checklist deve ser aplicado **por pipeline e por aplicação**, não apenas de forma genérica.
- O resultado pode ser usado diretamente como:
  - tarefa técnica (`[SEC] Revisão CI/CD Seguro`);
  - evidência de auditoria;
  - input para dashboards de maturidade;
  - critério objetivo de aprovação de *release*.
- Um item assinalado como **não conforme** implica:
  - correção técnica,
  - registo de exceção formal,
  - ou bloqueio de promoção, conforme o nível de risco da aplicação.

A validação completa deste checklist permite afirmar **conformidade prática e auditável** com o Capítulo 07 do SbD-ToE.
