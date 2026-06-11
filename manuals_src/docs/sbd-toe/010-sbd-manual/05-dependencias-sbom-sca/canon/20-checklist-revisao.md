---
id: checklist-revisao
title: Checklist - Dependências, SBOM e SCA
description: Verificação binária da aplicação das práticas prescritas no Capítulo 05
tags: [checklist, controlo, dependencias, sbom, sca, supply-chain]
sidebar_position: 20
sidebar_label: Checklist de Revisão
---


# Checklist de Revisão Periódica - Dependências, SBOM e SCA

Este checklist aplica-se a todas as aplicações que utilizem bibliotecas de terceiros, SDKs, pacotes open-source ou artefactos binários.
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 05** (`DEP-001` a `DEP-014`), permitindo:

* Controlo contínuo da aplicação de práticas de SCA e SBOM
* Verificação por projeto em momentos-chave do ciclo de vida
* Geração de indicadores operacionais agregáveis por equipa ou organização

> 🗓️ **Recomenda-se a sua revisão a cada release, alteração de dependência ou exceção de segurança**, conforme indicado no `aplicacao-lifecycle`.

---

## 📋 Itens de Verificação

| Item                                                                                               | Verificado? |
| -------------------------------------------------------------------------------------------------- | ----------- |
| Existe SBOM gerado automaticamente por build (CycloneDX ou SPDX), incluindo dependências transitivas, versionado e ligado ao artefacto? (`DEP-001`) | ☐           |
| O SBOM é arquivado e acessível para auditoria, e assinado com integridade verificada (L3)? (`DEP-001`) | ☐           |
| Existe scanner SCA integrado no pipeline CI/CD? (`DEP-002`)                                         | ☐           |
| Existe política de severidade documentada que distingue findings que bloqueiam dos que apenas alertam? (`DEP-002`) | ☐           |
| O pipeline bloqueia a promoção perante findings críticos/elevados não justificados, conforme o limiar do nível? (`DEP-002`) | ☐           |
| Os relatórios SCA estão acessíveis e associados a cada versão/release, com findings triados por severidade, exposição e correção? (`DEP-002`) | ☐           |
| Existe lockfile versionado sem referências `latest`/`*`/ranges não limitados, com integridade verificável por hash? (`DEP-003`) | ☐           |
| Não existem bibliotecas copiadas manualmente fora do package manager, com auditoria periódica e enforcement em CI/CD (L2–L3)? (`DEP-004`) | ☐           |
| Apenas registries aprovados são usados no build (allowlist enforced), com fallback para registries externos controlado e auditado? (`DEP-005`) | ☐           |
| Existe processo formal de aprovação de novas dependências (manutenção, licença, CVEs, popularidade), com registo rastreável (versão, hash, responsável, data)? (`DEP-006`) | ☐           |
| Existe validação automática de compatibilidade de licenças contra allowlist organizacional?        | ☐           |
| Existe política de atualização com SLA/TTL por severidade de CVE e bot ativo que gera PRs com análise de impacto, exigindo intervenção humana para breaking changes? (`DEP-007`/`DEP-008`) | ☐           |
| Existe rastreabilidade entre findings, CVE, exceções e artefactos entregues (CVE → release)? (`DEP-010`) | ☐           |
| As exceções a vulnerabilidades são formalizadas (justificação, contexto de uso, prazo, aprovador, compensação) e as vencidas revistas? | ☐           |
| A fronteira de inventário (SBOM boundary) está definida e documentada, com deteção de dependências emergentes (delta inesperado) e processo de aprovação? (`DEP-009`) | ☐           |
| Existe deteção de drift de composição entre o SBOM e o runtime, com abertura de incidente perante divergência (L3)? | ☐           |
| Os sistemas com componentes AI/ML têm inventário de dependências AI (modelos, datasets, MCP servers/tools, prompts) e AI BOM por build (CycloneDX 1.6 `ml-bom`) ligado ao SBOM? (`DEP-011`/`DEP-012`) | ☐           |
| Os modelos AI têm versão pinned (sem `latest`/aliases), constam de lista de providers aprovados com classificação de risco, e a mudança de versão maior aciona nova eval suite e revisão do threat model? (`DEP-013`/`DEP-014`) | ☐           |
| As práticas estão documentadas e rastreáveis no repositório ou pipeline? | ☐           |

---

## 🔄 Integração Operacional

* Este checklist pode ser integrado em **pipelines, revisões de PR, gates de release ou auditorias técnicas**.
* Os resultados podem ser rastreados por commit, por release ou por artefacto.
* Cada item deve ser validado com **evidência objetiva** (ex: ficheiros `.sbom.json`, relatórios, comentários de PR, issues).

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada e documentada conforme o modelo de exceções do capítulo.

---

## ✅ Conformidade e KPI

* A validação deste checklist permite declarar **conformidade com o Capítulo 05 - Dependências, SBOM e SCA**.
* A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**.
* Este resultado pode ser agregado por equipa, domínio ou organização como **indicador de maturidade operacional**.

> 📌 Este mecanismo operacional está alinhado com o modelo de controlo contínuo e rastreabilidade definido no SbD-ToE.
