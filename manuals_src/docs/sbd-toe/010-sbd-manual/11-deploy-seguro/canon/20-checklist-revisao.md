---
id: checklist-revisao
title: Checklist - Deploy Seguro
sidebar_label: Checklist de Revisão
description: Verificação objetiva e binária da aplicação das práticas de deploy seguro num projeto específico.
tags: [checklist, controlo, deploy, rollback, validação]
sidebar_position: 20
---

# Checklist de Revisão Periódica - Deploy Seguro

Este checklist aplica-se a todas as aplicações em vias de serem colocadas em produção, especialmente as classificadas como L2 ou L3.
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 11** (`DPL-001` a `DPL-009`), permitindo:

- Controlo formal da execução segura
- Verificação da existência de rollback testado
- Confirmação da validação operacional antes do deploy

> 🗓️ **Recomenda-se a sua revisão antes de qualquer release, rollback ou alteração de configuração relevante**, conforme indicado na `aplicacao-lifecycle`.

---

## 📋 Itens de Verificação

| Item                                                                                              | Verificado? |
|---------------------------------------------------------------------------------------------------|-------------|
| Existe aprovação formal humana do deploy registada com timestamp e identidade do aprovador? (`DPL-001`) | ☐           |
| Os artefactos promovidos têm assinatura/hash e proveniência (commit SHA, run id) verificados no deploy, com rejeição automática dos que não a têm? (`DPL-002`) | ☐           |
| Os gates automáticos de segurança (CVEs críticos, testes, secret scanning) bloqueiam o deploy em caso de falha, com evidência de execução? (`DPL-003`) | ☐           |
| As validações estão integradas em gates condicionais parametrizados por criticidade (L1–L3)?     | ☐           |
| Existe SBOM atualizado ligado ao artefacto e todos os findings estão resolvidos ou com exceção formal aprovada (aprovador e validade)? | ☐           |
| Cada deploy tem ID único e registo que associa quem aprovou, artefacto, commit SHA, momento, ambiente e gates, permitindo traçar de incidente a commit? (`DPL-004`) | ☐           |
| Existe procedimento de rollback documentado e testado no último ciclo de release ou ano, com data e tempo máximo verificados? (`DPL-005`) | ☐           |
| Existem mecanismos de reversibilidade imediata (blue/green, toggles), com releases anteriores documentadas e reversíveis? (`DPL-009`) | ☐           |
| As credenciais de deploy têm âmbito mínimo e vida curta (OIDC/workload identity), não partilhadas entre aplicações, com logs de uso? (`DPL-006`) | ☐           |
| A validação em staging representativo (mesmas versões/configuração, dados não reais) foi executada antes da promoção (L2/L3)? (`DPL-007`) | ☐           |
| A pipeline de produção está segregada, com segredos em cofres distintos e acesso por MFA e RBAC? | ☐           |
| Existe monitorização durante a janela de deploy e período de observação pós-deploy por nível, com thresholds para rollback automático e playbook de reação por incidente? (`DPL-008`) | ☐           |
| Para componentes críticos, o deploy é progressivo (canary, blue-green ou feature flags) com thresholds e critérios de rollback por etapa (L3)? (`DPL-009`) | ☐           |
| As feature flags têm metadata obrigatória (owner, âmbito, ativação, expiração), são versionadas como código, auditáveis, avaliadas no backend e revistas periodicamente? | ☐           |
| A release segue versionamento semântico com changelog técnico e de segurança (CVEs corrigidas, breaking changes)? | ☐           |
| As exceções a gates seguem template versionado (aprovador por severidade, validade máx. 6 meses), e as ações irreversíveis e decisões de go/no-go exigem registo humano (quem, quando, porquê, evidência)? | ☐           |

---

## 🔄 Integração Operacional

- Este checklist pode ser integrado em **pipelines, fluxos de aprovação de release, gates de produção ou auditorias técnicas**.
- Cada item deve ser validado com **evidência objetiva** (ex: logs de aprovação, ficheiros SBOM, relatórios de rollback, prints do pipeline).
- Os resultados podem ser ligados ao ciclo de vida do artefacto, da aplicação ou do serviço.

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada e documentada conforme o modelo do capítulo.

---

## ✅ Conformidade e KPI

- A validação deste checklist permite declarar **conformidade com o Capítulo 11 - Deploy Seguro**.
- A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**.
- Este resultado pode ser agregado por equipa, domínio ou organização como **indicador de maturidade operacional**.

> 📌 Este mecanismo de controlo está alinhado com o modelo de confiança rastreável e reversível defendido pelo SbD-ToE.
