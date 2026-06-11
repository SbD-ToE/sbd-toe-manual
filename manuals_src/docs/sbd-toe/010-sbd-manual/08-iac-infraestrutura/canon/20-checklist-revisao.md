---
id: checklist-revisao
title: Checklist de Revisão - Infraestrutura como Código (IaC)
sidebar_position: 20
sidebar_label: Checklist de Revisão
description: Checklist binário e auditável para verificar a aplicação prática das prescrições de segurança para IaC.
tags: [checklist, validação, revisão, iac, infraestrutura como código, controlo]
---


# Checklist de Revisão Periódica de Práticas de IaC

Este checklist aplica-se a todos os projetos de **Infraestrutura como Código (IaC)** desenvolvidos ou mantidos internamente. Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 08**, permitindo:

* Controlo objetivo da aplicação dos requisitos `IAC-001` a `IAC-013`;
* Integração com processos de PR, release, auditoria e onboarding;
* Geração de indicadores operacionais e de conformidade.

> 🗓️ **Recomenda-se revisão a cada nova release, PR relevante ou alteração em ambiente crítico.**

---

## 📋 Itens de Verificação

| Item                                                                             | Verificado? |
| -------------------------------------------------------------------------------- | ----------- |
| O backend remoto está configurado com autenticação e locking, com logs de lock disponíveis? (`IAC-001`) | ☐           |
| Os ambientes dev/staging/prod estão segregados e versionados em diretórios ou workspaces distintos? (`IAC-002`) | ☐           |
| O pipeline executa validações bloqueantes (lint/sintaxe, scanner de segurança e policy) cujo insucesso impede o `apply`? (`IAC-003`) | ☐           |
| Os módulos usam versão fixa ou hash (sem `latest`/`main`), de fontes em allowlist, com proveniência/integridade verificada? (`IAC-004`) | ☐           |
| Existe histórico versionado com tags semânticas e notas por release? (`IAC-005`) | ☐           |
| As convenções de naming/tagging/layout são validadas automaticamente e os recursos sem tags obrigatórias são rejeitados? (`IAC-006`) | ☐           |
| Cada `apply` ocorre apenas após aprovação humana registada sobre o `plan` anexado ao PR, sem `apply` manual fora do pipeline? (`IAC-007`) | ☐           |
| É possível rastrear, para qualquer recurso, o ficheiro IaC, o ambiente e o pipeline de origem? (`IAC-008`) | ☐           |
| O enforcement de policy-as-code é bloqueante em pre-merge e pre-apply, com policy versionada e logs de bloqueio? (`IAC-009`) | ☐           |
| Os artefactos `plan`/manifests são versionados com hash, com integridade confirmada antes do `apply` e sem reutilização entre ambientes? (`IAC-010`) | ☐           |
| Existe secret scanning automatizado e proibição de segredos em código, com integração a cofre (Vault/KMS/OIDC) e credenciais efémeras de curta duração? (`IAC-011`) | ☐           |
| Existe deteção automatizada de drift entre o IaC e o estado real, com alertas, tratada como falha de segurança corrigida via PR? (`IAC-012`) | ☐           |
| Existe revisão periódica formal de módulos/templates com registos (data, responsável, findings) e remoção de obsoletos ou vulneráveis? (`IAC-013`) | ☐           |
| Todo o IaC proposto é tratado como entrada não confiável por origem (humana, template, gerador ou ferramenta assistida)? | ☐           |
| As exceções são geridas em formato versionado com TTL bloqueante, e existe procedimento de rollback/kill-switch para `destroy` em produção? | ☐           |

---

## 🔄 Integração Operacional

* Este checklist pode ser aplicado manualmente (ex: revisão de PR) ou integrado no CI/CD como gate.
* Pode ser usado em revisões formais de arquitetura, releases ou onboarding de novos repositórios.
* Cada item deve ser validado com **evidência objetiva**:

  * Ficheiros `backend.tf`, logs de `tfsec`, screenshots de CI, hashes em releases, etc.

> ⚠️ Respostas negativas requerem exceção formal, aprovada e documentada (ver modelo de governação).

---

## 📊 Conformidade e KPI

* A validação deste checklist permite declarar **conformidade com o Capítulo 08 - Infraestrutura como Código**.
* A contagem de itens verificados pode ser usada para **KPIs operacionais de adoção e maturidade**.
* Pode ser incluído como evidência em auditorias, processos de exceção ou gates de release.

> 📌 Este mecanismo está alinhado com o modelo de **controlo contínuo e rastreabilidade** definido no SbD-ToE.
