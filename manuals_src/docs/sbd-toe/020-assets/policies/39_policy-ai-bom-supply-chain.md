---
id: policy-ai-bom-supply-chain
title: Política de AI BOM e Supply Chain de Modelos
description: Política organizacional que define o tratamento de modelos AI, datasets, MCP servers/tools, prompts embebidos e providers AI como cadeia de fornecimento auditável — geração de AI BOM por build em formato standardizado (CycloneDX 1.6 ml-bom), version pinning, lista de providers aprovados e resposta a incidentes upstream, complementando Policy 10 (dependências) e Policy 11 (SBOM), proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, AI, BOM, AI-BOM, supply-chain, CycloneDX, ml-bom, providers, modelos, datasets, MCP, pinning, AML, L1, L2, L3, governance, cap05]
grupo: supply-chain
sidebar_position: 39
---

# Política de AI BOM e Supply Chain de Modelos

## 1. Objetivo

Esta política define como **modelos AI**, **datasets**, **MCP servers/tools** e **prompts embebidos** são tratados como cadeia de fornecimento auditável — com inventário versionado, formato standardizado (preferencialmente CycloneDX 1.6 `ml-bom`), versão fixa por *build*, lista de *providers* aprovados, e processo de resposta a incidentes *upstream*.

Operacionaliza os requisitos [`DEP-011`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012), [`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013) e [`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014) do Cap. 05 e complementa a [Policy 10 — Dependências](./policy-dependencias) (anexo *Provedores AI*) e a [Policy 11 — SBOM](./policy-sbom) (anexo *AI BOM*). Existe como política autónoma — em vez de secção de uma das anteriores — porque o ciclo de vida e os riscos são suficientemente distintos para justificar tratamento próprio, à imagem do que o NIST faz separando o AI RMF do CSF.

## 2. Âmbito

Esta política aplica-se a **qualquer sistema** que use componentes AI em desenvolvimento, *staging* ou produção, incluindo:

- Modelos AI consumidos via *provider* externo (Anthropic, OpenAI, Google, Mistral, Cohere) ou *self-hosted* (HuggingFace, vLLM, Ollama)
- Datasets usados para *training*, *fine-tuning* ou avaliação
- MCP servers / *tools* / *plugins* invocados por agentes
- *Prompts* embebidos no produto (system prompts, RAG templates, *skill files*)

Não está no âmbito:
- Modelos AI usados em modo puramente exploratório, fora de qualquer pipeline de release (estes seguem Policy 16)
- Bibliotecas tradicionais de *machine learning* sem modelo treinado embebido (caem em Policy 10 / Policy 11)

## 3. Princípio fundamental: AI é supply chain

Tudo o que aprendemos nos últimos quinze anos sobre cadeia de fornecimento de software aplica-se às dependências AI — com especialização. Versão *pinned*, hash auditável, *provider* aprovado, mecanismo de actualização visível, plano de resposta a incidentes *upstream*. A diferença é que os *attack vectors* têm nomes distintos (`AML.T0019` Publish Poisoned Datasets, `AML.T0109` Supply Chain Rug Pull, `AML.T0110` AI Agent Tool Poisoning) e os artefactos são opacos (não conseguimos `npm audit` sobre um modelo).

:::warning
Operar em produção com modelo AI referenciado por `latest` (ou range, ou alias dinâmico) é o equivalente a operar com `npm install` sem *lockfile* — apenas com superfície de impacto maior e janela de detecção menor. Esta prática é proibida em qualquer nível de criticidade.
:::

## 4. AI BOM — formato e conteúdo mínimo

| Campo | Descrição | Notas |
|---|---|---|
| `format` | Formato de serialização | Preferimos CycloneDX 1.6 com extensão `ml-bom` (publicada em 2024). Alternativas: SPDX 3.0 AI extension; formatos proprietários do *provider* quando consumíveis pelo *pipeline* de governança |
| `components` | Lista de componentes AI | Cada componente com `type`, `name`, `version` (fixa), `hash`, `provider`, `license`, `provenance` |
| `models` | Subconjunto modelos AI | Inclui `model_id` (ex.: `claude-opus-4-7`), `version` (ex.: `@2026-05-20`), `sha256`, `provider`, `capabilities` |
| `datasets` | Subconjunto datasets | Inclui `dataset_id`, `version`, `source`, `hash`, `curation_process` |
| `mcp_tools` | Subconjunto MCP servers/tools | Inclui `server_id`, `version`, `scopes`, `source`, `audit_log_sink` |
| `prompts` | Subconjunto prompts embebidos | Inclui `prompt_id`, `version` (commit SHA), `owner`, `system|rag|skill` |
| `providers` | Providers utilizados | Cada um com `name`, `risk_classification` (L1/L2/L3), `contract_ref` |
| `build_ref` | Referência ao *build* | Ligação ao SBOM principal e ao *release* |

## 5. Version *pinning* — regras operacionais

- **Modelos AI**: versão fixa explícita com hash quando o provider o exponha — ex.: `claude-opus-4-7@2026-05-20#sha:…`. Ranges semver, *aliases* dinâmicos (`latest`, `stable`, `production`) e referências sem versão são **proibidos** em qualquer ambiente além de exploratório ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)).
- **Datasets**: versão imutável, ou snapshot referenciado por hash. Datasets que evoluem continuamente exigem snapshot por *release*.
- **MCP servers/tools**: versão fixa do pacote npm/pip/binary. Tools dinamicamente descobertas em runtime só são aceites em A0-A1 e fora de produção.
- **Prompts**: versão = commit SHA do repositório onde vivem.

Mudança de versão maior em qualquer destes obriga a:
1. Nova *eval suite* (Cap. 10 §C5)
2. *Threat model* revisto (Cap. 03 US-11)
3. Aprovação por `appsec` (L2) ou `appsec` + `grc` (L3) antes do *cutover*

## 6. Lista de *providers* AI aprovados

A organização mantém em VCS uma **lista versionada de *providers* AI aprovados** com, no mínimo:

- `name` · `service` · `model_families`
- `risk_classification` (L1/L2/L3 ou critério próprio)
- `contract_ref` (referência ao contrato vigente; ver Cap. 14)
- Cláusulas críticas declaradas: *data retention*, *training opt-out*, *localização*, *audit rights*, *notification of breaking changes*
- Conformidade declarada: AI Act Art. 53/55 (quando GPAI), RGPD Art. 28 + 44–49 (quando dados pessoais)
- `effective_until` — sem aprovações "para sempre"

Adicionar um *provider* exige: avaliação técnica (`appsec`) + revisão contratual (`grc` + Legal) + aprovação proporcional ao nível de risco. Remover um *provider* da lista exige plano de migração documentado quando o *provider* está em uso operacional.

## 7. Resposta a incidentes *upstream*

Os mesmos *runbooks* IR que usamos para CVE em dependências aplicam-se a incidentes em supply chain AI — com adaptações por classe:

| Classe de incidente | Exemplos | Acção mínima |
|---|---|---|
| **Modelo comprometido / *rug pull*** (`AML.T0109`) | Provider distribui versão maliciosa do modelo; *fine-tune* não anunciado degrada segurança | Rollback para versão *pinned* anterior; revisão de outputs do período afectado; comunicação ao *owner* dos sistemas afectados |
| **Dataset envenenado** (`AML.T0019`) | Dataset público contaminado por *training-time poisoning* | Re-treinar / re-fine-tune sem o dataset afectado; *eval* completa antes de novo *cutover* |
| **MCP server / tool comprometido** (`AML.T0110`) | Tool legítima injecta contexto malicioso quando invocada | Remover *tool* da `tools_allowlist` dos *mandates* afectados (Policy 38); revisão do *audit trail* de *tool invocations* (Cap. 12 OPS-012) do período suspeito; *kill-switch* dos agentes que a usaram |
| ***Provider*** *outage / breaking change* | Provider deprecia versão sem aviso; SLA violado | Activar *fallback* declarado na arquitectura (Cap. 04 §AI/ML); avaliar mudança de *provider* via excepção formal (Policy 05) |

## 8. Proporcionalidade por nível de criticidade

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| AI BOM gerado por *build* (DEP-012) | Recomendado | Obrigatório | Obrigatório |
| Versão *pinned* explícita (DEP-013) | Obrigatório | Obrigatório | Obrigatório |
| Lista de *providers* aprovados (DEP-014) | Recomendado | Obrigatório | Obrigatório + revisão GRC |
| Cláusulas contratuais detalhadas | Recomendado | Obrigatório | Obrigatório + revisão Legal |
| *Eval suite* obrigatória em mudança de versão maior | Recomendado | Obrigatório | Obrigatório |
| Revisão periódica da lista de providers | Anual | Semestral | Trimestral |

## 9. Responsabilidades

| Role | Responsabilidade |
|---|---|
| **AppSec Engineer** | Definir esquema do AI BOM; aprovar inclusão de modelos/datasets/MCP servers; avaliação técnica de novos providers |
| **DevOps / SRE** | Configurar geração de AI BOM no *pipeline*; manter *gate* CI que valida *pinning*; arquivar BOMs por release |
| **GRC / Compliance / Legal** | Avaliar cláusulas contratuais; aprovar adição de providers L2/L3; conformidade regulatória (AI Act, RGPD) |
| **Tech Lead / Software Architect** | Identificar quais componentes AI são *load-bearing* no sistema; declarar dependências AI no design |
| **Auditores** | Verificar conformidade da lista de providers com cláusulas contratuais reais; rastrear incidentes *upstream* nas BOMs publicadas |

## 10. Anti-padrões

- ❌ `model: latest` em qualquer ambiente não-exploratório — viola DEP-013 e abre porta a `AML.T0109`.
- ❌ AI BOM em formato proprietário ilegível para o *pipeline* de governança — perde-se a portabilidade que é o valor do BOM.
- ❌ Provider em uso sem entrada na lista aprovada — *shadow AI*; incidente operacional.
- ❌ Mudança de versão maior sem nova *eval* nem *threat review* — perde-se a evidência que sustentava o nível de autonomia declarado.
- ❌ Dataset "público" usado sem snapshot — ataque típico `AML.T0019` (dataset alterado entre uso e auditoria).
- ❌ Lista de providers que cresce mas nunca encolhe — providers descontinuados acumulam-se como *cruft* contratual.

## 11. Gestão de excepções

Excepções a esta política seguem o processo formal do Cap. 14 e da [Policy 05 — Gestão de Excepções](./policy-gestao-excecoes):

- Uso de versão não-*pinned* num ambiente não-exploratório exige excepção com TTL ≤ 30 dias.
- Uso de provider fora da lista aprovada exige excepção com TTL ≤ 14 dias e aprovação `appsec` + `grc`.
- Excepções recorrentes (>2 sobre o mesmo provider em 12 meses) obrigam à inclusão formal do provider na lista ou à sua substituição.

## 12. Revisão e auditoria desta política

Esta política deve ser **revista semestralmente** dada a rápida evolução do ecossistema de modelos e providers AI, ou após qualquer um dos seguintes eventos:

- Incidente em supply chain AI (qualquer classe da secção 7)
- Publicação de nova versão da especificação CycloneDX `ml-bom` ou SPDX AI
- Alteração regulatória aplicável (AI Act, NIS2, DORA) com impacto em supply chain AI
- Mudança nas cláusulas contratuais de provider em uso operacional

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 05 (`DEP-011..014`) | Requisitos de inventário AI + AI BOM + pinning + providers |
| SbD-ToE Cap. 05 — US-14 (AI BOM) | Operacionalização |
| SbD-ToE Cap. 03 §AI/ML | Threat library aplicável a supply chain AI (`AML.T0010`, `AML.T0019`, `AML.T0109`, `AML.T0110`) |
| SbD-ToE Cap. 04 ([`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)) | Patterns arquitectónicos AI/ML (origem dos componentes inventariados) |
| SbD-ToE Cap. 14 — Contratação de AI providers | Cláusulas contratuais detalhadas |
| Policy 10 — Dependências (anexo AI providers) | Acoplamento operacional |
| Policy 11 — SBOM (anexo AI BOM) | Coerência de formato |
| Policy 33 — Contratação Segura (anexo AI providers) | Cláusulas contratuais |
| Policy 38 — Mandates de Agentes AI | *Tools* AI consumidas pelos agentes |
| CycloneDX 1.6 `ml-bom` (OWASP, 2024) | Formato preferido |
| SPDX 3.0 AI Profile | Formato alternativo |
| MITRE ATLAS | Catálogo de tactics/techniques adversariais para AI supply chain |
| OWASP Top 10 for LLM Applications (2025) — LLM03 Supply Chain | Vector dedicado |
| NIST AI RMF 1.0 — MAP-4.x (third-party AI) | Mapping de risco de terceiros |
| NIST SP 800-218A | SSDF Profile for GenAI |
| EU AI Act (Reg. (UE) 2024/1689) — Art. 53/55 (GPAI), Art. 25 (cadeia de fornecimento) | Quando aplicável |
