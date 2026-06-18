---
id: playbook
title: "SbD-ToE 4 AI Act: Playbook de Implementação"
description: Roadmap prático para implementar o SbD-ToE conforme os requisitos do Regulamento (UE) 2024/1689 (AI Act) - mapeamento de artigos para ações, por papel e categoria de risco
tags: [playbook, ai-act, regulamento-ia, implementacao, roadmap, gpai]
sidebar_position: 2
---

# SbD-ToE 4 AI Act: Playbook de Implementação

## Visão Geral

Este playbook mapeia **requisitos do AI Act (Regulamento UE 2024/1689) para ações SbD-ToE práticas**, focando-se nas obrigações técnicas dos sistemas de IA de **alto risco** e dos modelos de **finalidade geral (GPAI)**.

**Princípio:** O SbD-ToE cobre o **núcleo técnico** do AI Act - exatidão, robustez, cibersegurança (Art. 15), logging (Art. 12), gestão de risco (Art. 9), QMS (Art. 17), monitorização pós-mercado (Art. 72) e incidentes (Art. 73). As dimensões de **domínio de IA** (dados/enviesamento, supervisão humana, transparência) e **jurídicas** (classificação de risco, FRIA, avaliação de conformidade, marcação CE) exigem articulação com equipas de ciência de dados, produto, jurídico e compliance.

**Estrutura:** Cada secção mostra:
- AI Act requisito (artigo)
- SbD-ToE capítulo/addon aplicável
- O que fazer (ação concreta)
- Evidência regulatória

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e relatórios de incidentes reutilizáveis para AI Act e outros frameworks.

---

## Passo 0: Determinar papel e categoria de risco (pré-requisito)

Antes de qualquer ação técnica, é necessário estabelecer o enquadramento jurídico - **trabalho de compliance/jurídico, não de AppSec**, mas que condiciona todo o playbook:

1. **Qual é o papel?** Fornecedor (*provider*), utilizador implementador (*deployer*), importador ou distribuidor. O grosso das obrigações técnicas recai sobre o **fornecedor de alto risco**.
2. **Qual a categoria de risco?**
   - **Inaceitável** (Art. 5) → proibido; não há playbook técnico que o legitime.
   - **Alto risco** (Art. 6, Anexos I/III) → aplica-se a generalidade deste playbook.
   - **Risco limitado** (Art. 50) → apenas deveres de transparência.
   - **Risco mínimo** → sem obrigações específicas.
3. **É um modelo GPAI?** Se sim, aplicam-se Art. 53 (todos) e Art. 55 (risco sistémico) - ver Fase 7.

> ⚠️ **Saída do âmbito SbD-ToE:** a classificação de risco e a qualificação de papéis são determinações jurídicas. O SbD-ToE assume o resultado desta análise como input.

---

## Mapa Rápido: AI Act Art. → SbD-ToE

> ✏️ **Refresh 2026-05-30.** Mapa actualizado com a camada agentic — `REQ-AGN-*` (Cap. 02), [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (Cap. 04), `DEP-012..014` (Cap. 05), `OPS-012..014` (Cap. 12), Policy 38 (*mandates*), Policy 39 (AI BOM).

| AI Act Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|---|---|---|---|
| **4** | Literacia em IA | [Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro) + [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca) | Trilho formativo por *role*; obrigatório com agentes A1+ |
| **9** | Gestão de risco | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 02 §A0–A4](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia), [Cap. 03 playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) | Classificar L1–L3 + nível A0–A4; threat model com ATLAS |
| **10** | Dados e governação | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) (`DEP-011..014`) + [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain) | AI BOM (CycloneDX 1.6 *ml-bom*) + *pinning* + *providers* aprovados |
| **11 / Anexo IV** | Documentação técnica | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Policy 38](/sbd-toe/assets/policies/policy-mandates-agentes) (mandate) | Índice Anexo IV + *model card* + mandate + AI BOM |
| **12 / 19** | Logging e retenção | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) + `OPS-011..014` + Cap. 12 US-13 | Logs de inferência + audit per *tool invocation* |
| **13** | Transparência aos *deployers* | Cap. 04 + [Policy 38](/sbd-toe/assets/policies/policy-mandates-agentes) (mandate) | *Mandate* como fonte de capabilities/limitations/supervisão |
| **14** ⚡ | Supervisão humana | [Cap. 02 §A0–A4](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia) + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + Policy 38 | Modelo de níveis de autonomia + *kill-switch* + *intent declaration* + OOB approval |
| **15** | Robustez e cibersegurança | [Cap. 03 playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic), `ARC-014/015`, [Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) (*eval suites*), [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak*) | *Eval suites* contínuas + threat library + *off-policy detection* |
| **17** | QMS | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), Cap. 14, Policy 38 (mandate lifecycle), Policy 39 (AI BOM lifecycle) | Mapear gates + ciclos formais para Art. 17 |
| **25** | Cadeia de fornecimento | `DEP-013/014` + Policy 39 + Cap. 14 US-21 | *Pinning* + *providers* aprovados + cláusulas |
| **26** | Obrigações do *deployer* | Policy 38 (mandate) + Cap. 00 (função composta) + Cap. 12 US-13 | Mandate do *deployer* + supervisão qualificada + logs sob controlo |
| **53 / 55** | GPAI | [Cap. 03 playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) + Cap. 05 (`DEP-011..014`) + [Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Cap. 14 US-21 | AI red teaming via *eval suites* + proteção de pesos + cláusulas Art. 53/55 |
| **72** | Monitorização pós-mercado | Cap. 12 + `OPS-011..014` + Cap. 12 US-13 | Telemetria agentic + *drift detection* + ciclo de melhoria |
| **73** | Incidentes graves | Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 16 §11.4 + Policy 30 §9.3 + Policy 39 §7 | *Runbook* + classes de incidente agentic + *upstream* IR |

---

## Como Implementar (Ordem Lógica)

### Fase 1: Governação e QMS (M0–M3)
**AI Act Art. 17** - Estabelecer sistema de gestão da qualidade

1. **Definir governação de IA**
   - Membros: CISO, responsável de IA/ML, GRC, jurídico, produto
   - **Evidência:** Atas, política de IA aprovada
   - Referência: [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

2. **Mapear gates SbD-ToE para os elementos do QMS (Art. 17)**
   - Procedimentos de desenvolvimento → [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)
   - Controlo de qualidade e validação → [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)
   - Reaproveitar **ISO/IEC 42001** se já existir
   - 📄 **Template:** [RACI e Governance](../exemplo-playbook/exemplo-raci-governance)

3. **Definir RACI de IA**
   - Quem aprova release de modelo, quem assina exceções, quem comunica incidentes (Art. 73)

---

### Fase 2: Classificação e gestão de risco (M2–M5)
**AI Act Art. 9** - Sistema de gestão de risco contínuo

1. **Inventariar sistemas de IA**
   - Finalidade, dados processados, modelo(s), serviço de inferência, dependências
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar criticidade (L1–L3) e alinhar com categoria AI Act**
   - Sistema de alto risco (Anexo III) → tipicamente L3
   - Documentar que a proporcionalidade segue a categoria AI Act

3. **Threat model estendido ao vetor adversarial**
   - Base: STRIDE / MITRE ATT&CK ([Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro))
   - Extensão: **MITRE ATLAS** e **OWASP ML/LLM Top 10**
   - Cobrir (Art. 15.º, n.º 5): *data poisoning*, *model poisoning*, *adversarial examples* / *model evasion*, ataques à confidencialidade, *model flaws*
   - **Evidência:** Threat model documentado, risco residual e medidas (Art. 9)

---

### Fase 3: Dados e documentação (M3–M6)
**AI Act Art. 10, 11, Anexo IV**

1. **Proveniência e integridade de dados e modelos (AI-BOM)**
   - Estender o inventário do [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) a *datasets*, *checkpoints* e modelos
   - Verificação de integridade (mitiga *poisoning* e modelos comprometidos de repositórios públicos)

2. **Data governance de IA (delegado à equipa de dados)**
   - Representatividade, deteção de enviesamento, qualidade estatística (Art. 10)
   - *Datasheets for datasets* / *data cards*
   - **Fora do âmbito AppSec** - SbD-ToE garante integridade/proveniência, não fairness

3. **Documentação técnica (Anexo IV)**
   - Construir "índice Anexo IV" apontando para artefactos SbD-ToE (arquitetura, requisitos, threat model, evidência de pipeline/testes) + **model card**
   - Referência: [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)

---

### Fase 4: Segurança técnica e robustez (M5–M10) — NÚCLEO
**AI Act Art. 15** - Exatidão, robustez e cibersegurança

#### 4.1 Arquitetura defensiva
- **O que:** Fronteiras de confiança (incluindo *agentic boundary* — [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)), validação de input, isolamento do serviço de inferência, redução de superfície. Quando há agentes AI com *tool-use*, aplicar [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (agente como *principal* isolado): identidade dedicada via OIDC, *scope* mínimo por *tool*, *intent declaration*, OOB approval, *kill-switch* exercitado.
- **Referência:** [Cap. 04 — `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Cap. 09 — Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro)

#### 4.2 Threat modeling + *eval suites* + *red teaming* (CRÍTICO PARA Art. 15)
- **O que:** O catálogo de testes inclui agora *eval suites* contínuas (Cap. 10 §C5) — regression de prompt/skill, *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*), *drift detection*, *A/B testing*. Para sistemas com agentes A2+, suite obrigatória; para A4 em GPAI com risco sistémico, cadência mensal.
- **Threat model:** [Cap. 03 playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) com threat library MITRE ATLAS já incluída — DFD canónico (5 participantes / 4 *trust boundaries*) + *threats* por fronteira (`AML.T0051.001`, `T0086`, `T0101`, `T0109`, `T0110`, LLM01/06/07).
- **Referência:** [Cap. 10 §C5 — *Eval suites*](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Policy 19 §7](/sbd-toe/assets/policies/policy-estrategia-testes)
- 📄 **Template:** [Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)

#### 4.3 Pipeline seguro de ML + agentes como *principals*
- **O que:** Gates de segurança no pipeline (SAST/SCA, *secrets*, integridade de artefactos) + agentes AI que operam a pipeline com *workload identity* efémera OIDC, *scope* per-*tool*, *audit per tool invocation* (Cap. 07 US-19).
- **Referência:** [Cap. 07 — US-19](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle), [Cap. 08 — IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Policy 18 §9](/sbd-toe/assets/policies/policy-gestao-segredos)

#### 4.4 Exatidão (delegado à equipa de IA)
- Declarar métricas de exatidão e limiares aceitáveis — **conteúdo de domínio de IA**, suportado pela evidência de *eval suite* (Cap. 10 §C5) e telemetria operacional (Cap. 12 US-13).

---

### Fase 5: Logging e monitorização pós-mercado (M8–M12)
**AI Act Art. 12, 19, 72**

#### 5.1 Logging de inferência + audit per *tool invocation*
- **O que:** Esquema de logs estendido com metadados de inferência (id/versão do modelo, *features* relevantes, decisão e confiança, *correlation id*) + **audit per *tool invocation*** ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) quando há agentes AI: `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redactada), `intent_event_ref`, `outcome`, `external_effect`.
- **Retenção:** Alinhada com a vida útil do sistema e com o RGPD; imutabilidade.
- **Referência:** [Cap. 12 — `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) + [Cap. 12 US-13](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)

#### 5.2 Plano de monitorização pós-mercado (Art. 72)
- **O que:** *Dashboards* de desempenho, *model drift*, *token budget* ([`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013)) e detecção de *jailbreak* / *off-policy actions* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)). Para sistemas com agentes em A2+, telemetria agentic (Cap. 12 US-13) é a base evidencial.
- **Gatilhos:** Degradação, *drift*, *budget overrun* ou *off-policy* alimentam a reavaliação do Art. 9.
- **Referência:** [Cap. 12 US-13](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle), [Policy 30 §9](/sbd-toe/assets/policies/policy-monitorizacao-seguranca)

---

### Fase 6: Incidentes graves (M10–M12)
**AI Act Art. 73**

- **O que:** Parametrizar o *runbook* e o esquema de incidente com a tipologia e prazos do Art. 73 (≤15 dias em regra; ≤10 dias em caso de morte; ≤2 dias em caso de infração generalizada ou perturbação grave e irreversível de infraestrutura crítica). **Classes de incidente agentic-específicas** (Policy 16 §11.4): *off-policy action*, *intent-action divergence*, *prompt injection* bem-sucedida, falha de *kill-switch*, *credential exposure*. **Incidentes *upstream*** (Policy 39 §7): *rug pull*, *dataset poisoning*, *MCP tool poisoning*, *provider outage*.
- **Como:** Exportadores SIEM/ITSM → notificação pronta para a autoridade de fiscalização do mercado. [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) alimenta o fluxo IR (Cap. 12 US-04).
- **Referência:** [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Policy 16 §11.4](/sbd-toe/assets/policies/policy-uso-ferramentas-apoio), [Policy 30 §9.3](/sbd-toe/assets/policies/policy-monitorizacao-seguranca), [Policy 39 §7](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)
- 📄 **Template:** [Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)

---

### Fase 7: GPAI (quando aplicável)
**AI Act Art. 53, 55**

#### 7.1 Proteção do modelo (Art. 55 — cibersegurança)
- **O que:** Tratar pesos, *checkpoints*, *datasets*, MCP *tools* e prompts embebidos como ativos críticos de *supply chain*: proveniência, integridade, *pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)), *providers* aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)), AI BOM por *release* ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)), controlo de acesso.
- **Referência:** [Cap. 05 — `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [Cap. 04 `ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)

#### 7.2 AI red teaming contínuo (Art. 55)
- **O que:** Programa contínuo de avaliação adversarial materializado em [Cap. 10 §C5 — *eval suites*](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites): regression de prompt/skill, *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*), *drift detection*, *A/B*. Para A4 (GPAI com risco sistémico), cadência mensal de *kill-switch* e actualização do corpus de detecção [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014).
- **Referência:** [Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Policy 19 §7](/sbd-toe/assets/policies/policy-estrategia-testes)

#### 7.3 Hardening de infraestrutura física e lógica (Art. 55)
- **Referência:** [Cap. 08 — IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 09 — Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro), [Cap. 04 `ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)

#### 7.4 Conformidade contratual declarada (Art. 53/55 *providers*)
- **O que:** Quando consumimos GPAI de um *provider*, o contrato declara conformidade Art. 53 (documentação técnica, *summary of training data*, política de *copyright*) e — quando aplicável — Art. 55 (*AI red teaming* contínuo, hardening, *post-market monitoring*).
- **Referência:** [Cap. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle), [Policy 33 §10](/sbd-toe/assets/policies/policy-contratacao-segura)

#### 7.5 Documentação GPAI, copyright e resumo de dados (delegado)
- **Fora do âmbito AppSec** — obrigações de domínio e jurídicas (Art. 53). Aplica-se quando a organização é *provider* de GPAI.

---

## Checklist de Alinhamento Técnico (AI Act)

A lista abaixo permite validar o **alinhamento técnico** do programa SbD-ToE com os requisitos do AI Act — não emite o juízo de conformidade legal. Recomenda-se revisão periódica:

- [ ] **Enquadramento:** Papel e categoria de risco determinados (jurídico)
- [ ] **Literacia (Art. 4):** Trilho formativo activado conforme [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca) (obrigatório com agentes A1+)
- [ ] **Governação/QMS (Art. 17):** Política de IA aprovada; gates mapeados; Policy 38 (mandates) + Policy 39 (AI BOM lifecycle) operacionais
- [ ] **Classificação:** Sistemas de IA inventariados e classificados (L1–L3); níveis A0–A4 declarados nos *mandates*
- [ ] **Gestão de risco (Art. 9):** Threat model com [playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) executado; threat library MITRE ATLAS + OWASP LLM Top 10 já incluída
- [ ] **Supervisão (Art. 14):** `REQ-AGN-001..004` operacional; [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) validado; *kill-switch* exercitado com cadência registada
- [ ] **Dados (Art. 10):** AI BOM CycloneDX 1.6 *ml-bom* gerado por *build* ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)); *providers* aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)); *data governance* de IA em curso
- [ ] **Documentação (Art. 11/Anexo IV):** Índice Anexo IV + *model card* + *mandate* + AI BOM
- [ ] **Robustez (Art. 15):** *Eval suites* contínuas operacionais (Cap. 10 §C5); *off-policy* / *jailbreak detection* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014))
- [ ] **Supply chain (Art. 25):** *Pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)); lista de *providers* aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)); cláusulas contratuais (Cap. 14 US-21)
- [ ] **Deployer (Art. 26):** *Mandate* do *deployer* documentado quando organização opera (não fornece) sistema
- [ ] **Logging (Art. 12/19):** Logs de inferência + audit per *tool invocation* ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) com retenção e imutabilidade
- [ ] **Monitorização (Art. 72):** Telemetria agentic + *dashboards* de *drift*, *budget*, *off-policy*
- [ ] **Incidentes (Art. 73):** *Runbook* parametrizado + classes agentic (Policy 16 §11.4) + *upstream* IR (Policy 39 §7)
- [ ] **GPAI (Art. 53/55, se aplicável):** AI BOM + *eval suites* + *kill-switch* exercitado mensalmente + cláusulas declaradas
- [ ] **Evidência:** *Data room* com documentação técnica, *mandates*, AI BOMs, eval reports, audit trails, telemetria

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida)

> ✏️ **Refresh 2026-05-30.** Tabela actualizada para reflectir a camada agentic. Onde diz "extensível a", agora diz "incorpora" — várias extensões propostas em 2026-05 já estão dentro do canon.

| Capítulo | AI Act Artigos | O Que Faz |
|---|---|---|
| **[Cap. 00 — Fundamentos](/sbd-toe/sbd-manual/fundamentos/intro)** | Art. 4, 26 | Roles canónicos + função composta "AI Reliability Engineer" |
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 9 | Classificação de criticidade (L1–L3) |
| **[Cap. 02 §A0–A4 + `REQ-AGN`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos)** | Art. 9, 14 | Modelo de níveis de autonomia A0–A4 + mandate + *intent declaration* |
| **[Cap. 03 playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic)** | Art. 9, 15 | Threat modeling com MITRE ATLAS + OWASP LLM Top 10 2025 |
| **[Cap. 04 — `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)** | Art. 14, 15 | Arquitetura defensiva + agente como *principal* isolado + *kill-switch* |
| **[Cap. 05 — `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011)** | Art. 10, 15, 25, 55 | AI BOM + *pinning* + *providers* aprovados |
| **[Cap. 06 — Prompts como código](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#prompts-como-codigo)** | Art. 15, 17 | Versionamento + revisão de *system prompts*, *skill files*, *agent files* |
| **[Cap. 07 US-19](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle)** | Art. 15, 17 | Pipeline seguro + agentes AI como *principals* com OIDC + audit |
| **[Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro)** | Art. 15, 55 | Hardening de runtime/inferência |
| **[Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites)** | Art. 15, 55 | *Eval suites* contínuas (regression, abuse, drift, A/B) |
| **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 17 | Gate de release, validação pré-produção |
| **[Cap. 12 US-13 + `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)** | Art. 12, 19, 72, 73 | Telemetria agentic + audit per tool + jailbreak detection |
| **[Cap. 13 (formação)](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 4 | Literacia em IA por *role* |
| **[Cap. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle)** | Art. 17, 25, 26, 73 | Governança + contratação de *providers* AI + escalonamento |

---

## Métrica Simples: Estou Alinhado?

Estas perguntas são um auto-diagnóstico **técnico** — respondê-las não emite o juízo de conformidade legal. Se consegues responder SIM a todas, o núcleo técnico está alinhado:

1. **Enquadramento:** Conheço o meu papel e a categoria de risco?
2. **Risk Management:** Tenho threat model que cobre o vetor adversarial (ATLAS)?
3. **Robustez (Art. 15):** Faço testes adversariais / AI red teaming?
4. **Cadeia:** Tenho proveniência e integridade de datasets e modelos?
5. **Logging:** Registo eventos de inferência com retenção adequada?
6. **Monitorização:** Tenho plano pós-mercado com deteção de drift?
7. **Incidentes:** Consigo comunicar um incidente grave nos prazos do Art. 73?
8. **QMS:** Os meus gates mapeiam para os elementos do Art. 17?
9. **Documentação:** Tenho índice Anexo IV + model card?
10. **Evidência:** Consigo demonstrar tudo isto numa auditoria?

≥8/10 → Boa maturidade técnica face ao AI Act (maturidade técnica, **não conformidade legal**). `<`6 → Priorizar Art. 15 (robustez), logging (Art. 12) e gestão de risco (Art. 9).

> ⚠️ **Nota:** esta métrica cobre o **núcleo técnico**. A conformidade plena exige ainda governação de dados (Art. 10), supervisão humana (Art. 14), transparência (Art. 13/50) e avaliação de conformidade / marcação CE (Art. 43, 47–49) - dimensões fora do âmbito SbD-ToE.

---

## Nota Crítica: Gestão de Exceções no AI Act

O AI Act exige conformidade com os requisitos de alto risco. Exceções (desvios) devem ser formais e auditadas, com trilho documental e aprovação adequada. Uma exceção **interna** não altera a obrigação legal do AI Act — apenas documenta um risco técnico aceite para o dossiê de evidência; a obrigação legal subsiste.

O que caracteriza uma exceção em SbD-ToE/AI Act:
- Desvio formal de um requisito (ex.: vetor adversarial mitigado por compensação enquanto se prepara *retraining*)
- Aprovação formal, justificação, TTL (Time-To-Live), plano de remediação

Quem aprova (por nível de criticidade):
- L1 (baixo risco): Tech lead / AppSec Engineer
- L2 (médio risco): CISO / responsável de IA
- L3 (alto risco AI Act): Governação de IA + gestão (accountable)

Implicação regulatória:
- Exceções sem aprovação formal comprometem a evidência de gestão de risco (Art. 9) e do QMS (Art. 17)
- **Algumas situações nunca são exceptuáveis** - desde logo, qualquer uso que recaia nas práticas proibidas do Art. 5
- Trilho auditado é obrigatório para demonstrar controlo à autoridade

**Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (addon de exceções) e [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro) (exceções formalizadas).

---

## Próximos Passos

1. **Enquadramento jurídico:** Determinar papel e categoria de risco (jurídico/compliance)
2. **Auditoria técnica atual:** Verificar [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) contra os requisitos técnicos do AI Act
3. **Definir roadmap:** Sequenciar fases conforme contexto e categoria de risco
4. **Articular com domínio:** Coordenar com ciência de dados, produto e jurídico as dimensões fora do âmbito AppSec
5. **Implementar e validar:** Iterar e demonstrar a **evidência técnica** em auditoria

Documentação completa: ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências

- **SbD-ToE Manual:** Capítulos 01–14 (detalhe técnico por domínio)
- **Cross-Check AI Act:** [Análise normativa completa](/sbd-toe/cross-check-normativo/ai-act/intro)
- **AI Act:** Regulamento (UE) 2024/1689
- **Frameworks de Referência:** ISO/IEC 42001, ISO/IEC 23894, NIST AI RMF 1.0, MITRE ATLAS, OWASP ML Security Top 10, OWASP Top 10 for LLM Applications

---

**Versão:** 1.0
**Data:** Maio 2026
**Nota:** Este playbook complementa a [análise normativa AI Act](intro) com implementação prática.
