---
id: playbook
title: "SbD-ToE 4 AI Act: Playbook de Implementação"
description: Roadmap prático para implementar o SbD-ToE conforme os requisitos do Regulamento (UE) 2024/1689 (AI Act) - mapeamento de artigos para ações, por papel e categoria de risco
tags: [playbook, ai-act, regulamento-ia, implementacao, roadmap, gpai]
sidebar_position: 2
---

# SbD-ToE 4 AI Act: Playbook de Implementação

## Visão Geral {#visão-geral}

Este playbook mapeia **requisitos do AI Act (Regulamento UE 2024/1689) para ações SbD-ToE práticas**, focando-se nas obrigações técnicas dos sistemas de IA de **risco elevado** e dos modelos de **finalidade geral (GPAI)**.

A resposta do Manual a cada obrigação (coberta, lacuna declarada ou fora de âmbito) está em [«O que este Manual cobre e o que fica de fora»](./intro#o-que-este-manual-cobre-e-o-que-fica-de-fora).

**Princípio:** o SbD-ToE cobre a cibersegurança (Art. 15), o registo (Art. 12/19), a supervisão humana (Art. 14), a transparência do Art. 50, o acompanhamento pós-comercialização (Art. 72) e os incidentes graves (Art. 73). A exatidão e a solidez estão pendentes da ronda AISVS/SAIF do AppSec Core. Ficam fora de âmbito, com razão: a gestão de riscos (Art. 9), a governação de dados de treino (Art. 10), a gestão da qualidade (Art. 17), as especificidades da identificação biométrica, a qualificação jurídica (classificação de risco, papéis) e a avaliação da conformidade. Nestas, o Manual fornece evidência às equipas de ciência de dados, produto, jurídico e compliance.

**Estrutura:** Cada secção mostra:
- AI Act requisito (artigo)
- SbD-ToE capítulo/addon aplicável
- O que fazer (ação concreta)
- Evidência regulatória

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e relatórios de incidentes reutilizáveis para AI Act e outros frameworks.

---

## Passo 0: Determinar papel e categoria de risco (pré-requisito) {#passo-0-determinar-papel-e-categoria-de-risco-pré-requisito}

Antes de qualquer ação técnica, é necessário estabelecer o enquadramento jurídico - **trabalho de compliance/jurídico, não de AppSec**, mas que condiciona todo o playbook:

1. **Qual é o papel?** Prestador (*provider*), responsável pela implantação (*deployer*), importador ou distribuidor (AI Act, art. 3.º, pontos 3, 4, 6 e 7). O grosso das obrigações técnicas recai sobre o **prestador de sistemas de IA de risco elevado** (art. 16.º).
2. **Qual a categoria de risco?**
   - **Inaceitável** (Art. 5) → proibido; não há playbook técnico que o legitime.
   - **Risco elevado** (Art. 6, Anexos I/III) → aplica-se a generalidade deste playbook.
   - **Determinados sistemas de IA** (Art. 50 — interação direta com pessoas, conteúdos sintéticos, reconhecimento de emoções ou categorização biométrica, falsificações profundas) → obrigações de transparência, que se somam às do capítulo III quando o sistema é também de risco elevado (art. 50.º, n.º 6).
   - **Restantes sistemas de IA** → sem os requisitos do capítulo III; aplica-se, ainda assim, o Art. 4 (literacia no domínio da IA), dirigido aos prestadores e responsáveis pela implantação de sistemas de IA.
3. **É um modelo GPAI?** Se sim, aplicam-se Art. 53 (com a exceção do n.º 2 para modelos lançados ao abrigo de licença gratuita e aberta sem risco sistémico) e Art. 55 (risco sistémico) - ver Fase 7.

> ⚠️ **Saída do âmbito SbD-ToE:** a classificação de risco e a qualificação de papéis são determinações jurídicas. O resultado declara-se por aplicação como contexto CTX-AIA-RE (ou só com o grau ART50, para sistemas abrangidos apenas pelo art. 50.º), com a qualificação jurídica anexada, e os pisos do contexto aplicam-se em qualquer nível L1–L3 (ver [Requisitos aplicáveis — Quando se aplica](./requisitos-aplicaveis#quando-se-aplica)).

---

## Mapa Rápido: AI Act Art. → SbD-ToE {#mapa-rápido-ai-act-art--sbd-toe}

> ✏️ **Revisão 2026-09-27.** Mapa alinhado com a matriz de cobertura do AI Act e com o contexto CTX-AIA-RE (pisos e requisitos acrescentados), sobre a camada agentic — `REQ-AGN-*` (Cap. 02), [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (Cap. 04), `DEP-012..014` (Cap. 05), `OPS-012..014` (Cap. 12), Policy 38 (*mandates*), Policy 39 (AI BOM).

| AI Act Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|---|---|---|---|
| **4** | Literacia no domínio da IA (medidas para a promover — redação do Reg. (UE) 2026/1744) | [Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro) + [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca) | Trilho formativo por *role*; obrigatório com agentes A1+ (escolha do Manual) |
| **5.º, n.º 1-A** | Salvaguardas de geradores de conteúdo realista | `THR-008`, `ARC-014` (pisos CTX-AIA-RE-P09, P10; grau ART50) | Threat model do conteúdo gerado + red-team + filtros de entrada e de saída |
| **9** | Gestão de risco | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 02 §A0–A4](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia), [Cap. 03 playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) | Fora de âmbito (decisão do programa): sistema de gestão da organização; a classificação L1–L3, o nível A0–A4 e o threat model com ATLAS servem de evidência |
| **10** | Dados e governação de dados | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) (`DEP-011..014`) + [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain) | Fora de âmbito (decisão do programa): governação de dados de treino; AI BOM (CycloneDX 1.6 *ml-bom*), *pinning* e fornecedores aprovados dão evidência de proveniência |
| **11 / Anexo IV** | Documentação técnica | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Policy 38](/sbd-toe/assets/policies/policy-mandates-agentes) (mandate) | Índice Anexo IV ([mapa de evidência](./requisitos-aplicaveis#mapa-evidencia)) + *model card* + mandate + AI BOM |
| **12 / 19** | Logging e retenção | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) + `OPS-011..014` + Cap. 12 US-13 | Logs de inferência + audit per *tool invocation* |
| **13** | Transparência e prestação de informações aos responsáveis pela implantação | Cap. 04 + [Policy 38](/sbd-toe/assets/policies/policy-mandates-agentes) (mandate) | *Mandate* como fonte de capabilities/limitations/supervisão; redacção das instruções pelo prestador |
| **14** ⚡ | Supervisão humana | [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) (piso CTX-AIA-RE-P08) + [Cap. 02 §A0–A4](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia) + [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) + Policy 38 | Interface de supervisão em qualquer sistema de risco elevado; *kill-switch*, *intent declaration* e OOB approval nos agentes |
| **15** | Exatidão, solidez e cibersegurança | [Cap. 03 playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic), `ARC-014/015`, [Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) (*eval suites*), [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) (*jailbreak*) | *Eval suites* contínuas + threat library + *off-policy detection*; exatidão e solidez pendentes da ronda AISVS/SAIF |
| **17** | QMS | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), Cap. 14, Policy 38 (mandate lifecycle), Policy 39 (AI BOM lifecycle) | Fora de âmbito (decisão do programa); os gates e os ciclos das Policies 38/39 servem de evidência |
| **25** | Responsabilidades ao longo da cadeia de valor da IA | `DEP-013/014` + Policy 39 + Cap. 14 US-21 | *Pinning* + fornecedores de serviços de IA aprovados + cláusulas |
| **26** | Obrigações dos responsáveis pela implantação | Policy 38 (mandate) + Cap. 00 (função composta) + Cap. 12 US-13 | Mandate do *deployer* + supervisão qualificada + logs sob controlo |
| **43.º, n.º 4** | Modificação substancial | `ARC-009` (piso CTX-AIA-RE-P11) | Classificar e registar cada alteração |
| **50** | Transparência | CTX-AIA-RE-R01, R02 (grau ART50) | Informar; marcar conteúdo sintético |
| **53 / 55** | GPAI | [Cap. 03 playbook](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) + Cap. 05 (`DEP-011..014`) + [Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites) + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Cap. 14 US-21 | AI red teaming via *eval suites* + proteção de pesos + cláusulas Art. 53/55 |
| **72** | Acompanhamento pós-comercialização | [CTX-AIA-RE-R04](./requisitos-aplicaveis#acrescentos) + Cap. 12 + `OPS-011..014` + Cap. 12 US-13 | Plano por sistema + telemetria agentic + *drift detection* |
| **73** | Incidentes graves | Cap. 12 + [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) + Policy 16 §11.4 + Policy 30 §9.3 + Policy 39 §7 | *Runbook* alinhado com a Política 32 §6 + classes de incidente agentic + *upstream* IR |
| **86** | Explicação a pessoas afectadas | CTX-AIA-RE-R03 + `OPS-011` | Registar o resultado e os elementos de cada decisão |

---

## Como Implementar (Ordem Lógica) {#como-implementar-ordem-lógica}

### Fase 1: Governação de IA (M0–M3) {#fase-1-governação-e-qms-m0m3}
> O sistema de gestão da qualidade do Art. 17 fica fora do âmbito do Manual; os passos abaixo produzem evidência que o alimenta.

1. **Definir governação de IA**
   - Membros: CISO, responsável de IA/ML, GRC, jurídico, produto
   - **Evidência:** Atas, política de IA aprovada
   - Referência: [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

2. **Mapear gates SbD-ToE como evidência para o QMS da organização (Art. 17)**
   - Procedimentos de desenvolvimento → [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)
   - Controlo de qualidade e validação → [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)
   - Reaproveitar **ISO/IEC 42001** se já existir
   - 📄 **Template:** [RACI e Governance](../exemplo-playbook/exemplo-raci-governance)

3. **Definir RACI de IA**
   - Quem aprova release de modelo, quem assina exceções, quem comunica incidentes (Art. 73)

---

### Fase 2: Classificação e threat model (M2–M5) {#fase-2-classificação-e-gestão-de-risco-m2m5}
**AI Act Art. 6** - Declaração do contexto CTX-AIA-RE (o sistema de gestão de riscos do Art. 9 fica fora de âmbito; o threat model serve-lhe de evidência)

1. **Inventariar sistemas de IA**
   - Finalidade, dados processados, modelo(s), serviço de inferência, dependências
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar criticidade (L1–L3) e declarar o contexto regulatório**
   - Declarar o contexto CTX-AIA-RE na aplicação (ou só o grau ART50); o nível L1–L3 decide-se pelos critérios do Cap. 01, e os pisos do contexto aplicam-se em qualquer nível
   - L3 é a classificação de risco do Manual; não equivale a sistema de IA de risco elevado na acepção do AI Act (art. 6.º)

3. **Threat model estendido ao vetor adversarial**
   - Base: STRIDE / MITRE ATT&CK ([Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro))
   - Extensão: **MITRE ATLAS** e **OWASP ML/LLM Top 10**
   - Cobrir (Art. 15.º, n.º 5): contaminação de dados (*data poisoning*), contaminação de modelos (*model poisoning*), exemplos antagónicos ou evasão de modelos (*adversarial examples* / *model evasion*), ataques de confidencialidade, falhas do modelo (*model flaws*)
   - **Evidência:** Threat model documentado, risco residual e medidas

---

### Fase 3: Dados e documentação (M3–M6) {#fase-3-dados-e-documentação-m3m6}
**AI Act Art. 10, 11, Anexo IV**

1. **Proveniência e integridade de dados e modelos (AI-BOM)**
   - Estender o inventário do [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) a *datasets*, *checkpoints* e modelos
   - Verificação de integridade (mitiga *poisoning* e modelos comprometidos de repositórios públicos)

2. **Data governance de IA (fora de âmbito)**
   - Representatividade, deteção de enviesamento, qualidade estatística (Art. 10)
   - *Datasheets for datasets* / *data cards*
   - **Fora de âmbito** (decisão do programa): o SbD-ToE garante integridade e proveniência; a governação de dados de treino e o enviesamento são trabalho de ciência de dados

3. **Documentação técnica (Anexo IV)**
   - Construir "índice Anexo IV" apontando para artefactos SbD-ToE (arquitetura, requisitos, threat model, evidência de pipeline/testes) + **model card**, a partir do [mapa de evidência](./requisitos-aplicaveis#mapa-evidencia) da página gerada
   - Referência: [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)

---

### Fase 4: Segurança técnica e solidez (M5–M10) — NÚCLEO {#fase-4-segurança-técnica-e-robustez-m5m10--núcleo}
**AI Act Art. 15** - Exatidão, solidez e cibersegurança

#### 4.1 Arquitetura defensiva {#41-arquitetura-defensiva}
- **O que:** Fronteiras de confiança (incluindo *agentic boundary* — [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014)), validação de input, isolamento do serviço de inferência, redução de superfície. Quando há agentes AI com *tool-use*, aplicar [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (agente como *principal* isolado): identidade dedicada via OIDC, *scope* mínimo por *tool*, *intent declaration*, OOB approval, *kill-switch* exercitado.
- **Referência:** [Cap. 04 — `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Cap. 09 — Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro)

#### 4.2 Threat modeling + *eval suites* + *red teaming* (CRÍTICO PARA Art. 15) {#42-threat-modeling--eval-suites--red-teaming-crítico-para-art-15}
- **O que:** O catálogo de testes inclui agora *eval suites* contínuas (Cap. 10 §C5) — regression de prompt/skill, *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*), *drift detection*, *A/B testing*. Para sistemas com agentes A2+, suite obrigatória; para A4 em GPAI com risco sistémico, cadência mensal (escolha do Manual).
- **Threat model:** [Cap. 03 playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) com threat library MITRE ATLAS já incluída — DFD canónico (5 participantes / 4 *trust boundaries*) + *threats* por fronteira (`AML.T0051.001`, `T0086`, `T0101`, `T0109`, `T0110`, LLM01/06/07).
- **Referência:** [Cap. 10 §C5 — *Eval suites*](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Policy 19 §7](/sbd-toe/assets/policies/policy-estrategia-testes)
- 📄 **Template:** [Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)

#### 4.3 Pipeline seguro de ML + agentes como *principals* {#43-pipeline-seguro-de-ml--agentes-como-principals}
- **O que:** Gates de segurança no pipeline (SAST/SCA, *secrets*, integridade de artefactos) + agentes AI que operam a pipeline com *workload identity* efémera OIDC, *scope* per-*tool*, *audit per tool invocation* (Cap. 07 US-19).
- **Referência:** [Cap. 07 — US-19](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle), [Cap. 08 — IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Policy 18 §9](/sbd-toe/assets/policies/policy-gestao-segredos)

#### 4.4 Exatidão e solidez (lacuna declarada) {#44-exatidão-delegado-à-equipa-de-ia}
- Pendente da ronda AISVS/SAIF do AppSec Core. Até lá, registar as métricas obtidas nas *eval suites* (Cap. 10 §C5) e na telemetria operacional (Cap. 12 US-13) como evidência, sem as apresentar como cumprimento.

#### 4.5 Supervisão humana (Art. 14) {#45-supervisão-humana-art-14}
- **O que:** Em qualquer sistema de risco elevado, com ou sem agentes, interface de supervisão conforme o [`ARC-014`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-014) com o piso CTX-AIA-RE-P08: compreender as capacidades e limitações do sistema, detetar anomalias, interpretar o resultado, decidir não o usar ou anulá-lo e parar o sistema; quem supervisiona é advertido para o enviesamento da automatização. Nos agentes, `REQ-AGN-001..004` e [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) (*kill-switch*, *intent declaration*, OOB approval).
- **Fora de âmbito:** a verificação por duas pessoas da identificação biométrica (art. 14.º, n.º 5).
- **Referência:** [Requisitos aplicáveis — Pisos](./requisitos-aplicaveis#pisos), [Cap. 02 §A0–A4](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos#niveis-autonomia)

#### 4.6 Salvaguardas de conteúdo gerado (Art. 5.º, n.º 1-A) {#46-salvaguardas-de-conteúdo-gerado-art-5-n-1-a}
- **O que:** Em sistemas que geram ou manipulam imagem, vídeo ou áudio realistas (grau ART50), o threat model cobre a utilização indevida razoavelmente previsível do conteúdo gerado, avaliada com red-team e testes de segurança de conteúdo (`THR-008`, piso CTX-AIA-RE-P09), e há filtros e classificadores de segurança de conteúdo na entrada e na saída (`ARC-014`, piso CTX-AIA-RE-P10).
- **Referência:** [Requisitos aplicáveis — Pisos](./requisitos-aplicaveis#pisos)

---

### Fase 5: Logging e acompanhamento pós-comercialização (M8–M12) {#fase-5-logging-e-monitorização-pós-mercado-m8m12}
**AI Act Art. 12, 19, 72**

#### 5.1 Logging de inferência + audit per *tool invocation* {#51-logging-de-inferência--audit-per-tool-invocation}
- **O que:** Esquema de logs estendido com metadados de inferência (id/versão do modelo, *features* relevantes, decisão e confiança, *correlation id*) + **audit per *tool invocation*** ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) quando há agentes AI: `timestamp`, `agent_id`, `session_id`, `mandate_ref`, `autonomy_level`, `tool`, `tool_version`, `args` (PII redactada), `intent_event_ref`, `outcome`, `external_effect`.
- **Retenção:** Período adequado à finalidade prevista do sistema, de pelo menos seis meses (AI Act, art. 19.º, n.º 1, e art. 26.º, n.º 6); no SbD-ToE, 1 ano em L2 e 2 anos em L3 (escolha do Manual; [Política 29 §7](/sbd-toe/assets/policies/policy-logging-estruturado#7-retenção-de-logs)); conservação limitada pelo RGPD quando houver dados pessoais; imutabilidade.
- **Referência:** [Cap. 12 — `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes) + [Cap. 12 US-13](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)

#### 5.2 Plano de acompanhamento pós-comercialização (Art. 72) {#52-plano-de-monitorização-pós-mercado-art-72}
- **O que:** Plano de acompanhamento por sistema ([CTX-AIA-RE-R04](./requisitos-aplicaveis#acrescentos)), quando a organização é o prestador, integrado na documentação técnica (anexo IV, ponto 9), com os sinais de produção (`OPS-011`) e os dos responsáveis pela implantação, os critérios de desempenho, a cadência e o responsável da análise. Base técnica: *dashboards* de desempenho, *model drift*, *token budget* ([`OPS-013`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-013)) e deteção de *jailbreak* / *off-policy actions* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014)). Para sistemas com agentes em A2+, telemetria agentic (Cap. 12 US-13) é a base evidencial.
- **Gatilhos:** Degradação, *drift*, *budget overrun* ou *off-policy* desencadeiam rollback, reclassificação, revisão do threat model ou notificação de incidente grave.
- **Referência:** [Cap. 12 US-13](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle), [Policy 30 §9](/sbd-toe/assets/policies/policy-monitorizacao-seguranca)

#### 5.3 Transparência e explicação (Art. 50, Art. 86) {#53-transparência-e-explicação-art-50-art-86}
- **O que:** Informar as pessoas de que interagem com um sistema de IA e divulgar as falsificações profundas (CTX-AIA-RE-R01); marcar o conteúdo sintético num formato legível por máquina (CTX-AIA-RE-R02); ambos verificados em teste, sob o grau ART50. Quando um sistema do anexo III apoia decisões sobre pessoas, informá-las e registar, por decisão, o resultado e os principais elementos que o determinaram (CTX-AIA-RE-R03, `OPS-011`).
- **Fora de âmbito:** a divulgação de texto gerado por IA publicado sobre matérias de interesse público (art. 50.º, n.º 4, segundo parágrafo).
- **Referência:** [Requisitos aplicáveis — Requisitos acrescentados](./requisitos-aplicaveis#acrescentos)

#### 5.4 Modificação substancial (Art. 43.º, n.º 4) {#54-modificação-substancial-art-43-n-4}
- **O que:** Cada alteração é classificada como predeterminada ou como modificação substancial, e a classificação fica registada; uma modificação substancial é sinalizada para nova avaliação da conformidade (`ARC-009`, piso CTX-AIA-RE-P11).
- **Referência:** [Requisitos aplicáveis — Pisos](./requisitos-aplicaveis#pisos)

---

### Fase 6: Incidentes graves (M10–M12) {#fase-6-incidentes-graves-m10m12}
**AI Act Art. 73**

- **O que:** Alinhar o *runbook* e o esquema de incidente com a Política 32 (§4.1 e [§6](/sbd-toe/assets/policies/policy-irp#6-notificação-regulatória)), que fixa a definição e os prazos do Art. 73 (imediatamente após determinar a relação causal e, o mais tardar, ≤15 dias em regra; ≤10 dias em caso de morte; ≤2 dias em caso de infração generalizada ou de incidente grave do art. 3.º, ponto 49, alínea b); prazos a contar do conhecimento pelo prestador ou pelo responsável pela implantação; admite relatório inicial incompleto). **Classes de incidente agentic-específicas** (Policy 16 §11.4): *off-policy action*, *intent-action divergence*, *prompt injection* bem-sucedida, falha de *kill-switch*, *credential exposure*. **Incidentes *upstream*** (Policy 39 §7): *rug pull*, *dataset poisoning*, *MCP tool poisoning*, *provider outage*. Acrescentar ao *runbook* a informação prévia à autoridade antes de qualquer alteração ao sistema que afecte a análise de causas (art. 73.º, n.º 6; lacuna parcial do Manual).
- **Como:** Exportadores SIEM/ITSM → notificação pronta para a autoridade de fiscalização do mercado. [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014) alimenta o fluxo IR (Cap. 12 US-04).
- **Referência:** [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Policy 16 §11.4](/sbd-toe/assets/policies/policy-uso-ferramentas-apoio), [Policy 30 §9.3](/sbd-toe/assets/policies/policy-monitorizacao-seguranca), [Policy 39 §7](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)
- 📄 **Template:** [Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)

---

### Fase 7: GPAI (quando aplicável) {#fase-7-gpai-quando-aplicável}
**AI Act Art. 53, 55**

#### 7.1 Proteção do modelo (Art. 55 — cibersegurança) {#71-proteção-do-modelo-art-55--cibersegurança}
- **O que:** Tratar pesos, *checkpoints*, *datasets*, MCP *tools* e prompts embebidos como ativos críticos de *supply chain*: proveniência, integridade, *pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)), fornecedores de serviços de IA aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)), AI BOM por *release* ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)), controlo de acesso.
- **Referência:** [Cap. 05 — `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011), [Cap. 04 `ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015), [Policy 39](/sbd-toe/assets/policies/policy-ai-bom-supply-chain)

#### 7.2 AI red teaming contínuo (Art. 55) {#72-ai-red-teaming-contínuo-art-55}
- **O que:** Programa contínuo de avaliação adversarial materializado em [Cap. 10 §C5 — *eval suites*](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites): regression de prompt/skill, *abuse corpus* (LLM01-2025 *prompt injection*, LLM06-2025 *excessive agency*), *drift detection*, *A/B*. Para agentes em nível A4 (escala interna do SbD-ToE) — e, independentemente do nível, quando se é prestador de GPAI com risco sistémico (Art. 51) —, cadência mensal (escolha do Manual) de *kill-switch* e atualização do corpus de deteção [`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014).
- **Referência:** [Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites), [Policy 19 §7](/sbd-toe/assets/policies/policy-estrategia-testes)

#### 7.3 Hardening de infraestrutura física e lógica (Art. 55) {#73-hardening-de-infraestrutura-física-e-lógica-art-55}
- **Referência:** [Cap. 08 — IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 09 — Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro), [Cap. 04 `ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)

#### 7.4 Conformidade contratual declarada (art. 53.º e, com risco sistémico, art. 55.º — fornecedores de serviços de IA) {#74-conformidade-contratual-declarada-art-5355-providers}
- **O que:** Quando a organização consome GPAI de um fornecedor de serviços de IA, o contrato declara conformidade Art. 53 (documentação técnica, *summary of training data*, política de *copyright*) e — quando aplicável — Art. 55 (avaliação do modelo com testagem antagónica documentada, avaliação e atenuação de riscos sistémicos, comunicação de incidentes graves ao Serviço para a IA, cibersegurança do modelo e da infraestrutura física).
- **Referência:** [Cap. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle), [Policy 33 §10](/sbd-toe/assets/policies/policy-contratacao-segura)

#### 7.5 Documentação GPAI, copyright e resumo de dados (delegado) {#75-documentação-gpai-copyright-e-resumo-de-dados-delegado}
- A documentação dos anexos XI e XII é redigida pelo prestador do modelo; o AI BOM e as *eval suites* arquivadas dão-lhe evidência. A política de direitos de autor e o resumo dos conteúdos de treino (art. 53.º, n.º 1, als. c) e d)) ficam **fora de âmbito**: são plano jurídico. Aplica-se quando a organização é prestadora de modelos de IA de finalidade geral.

---

## Checklist de Alinhamento Técnico (AI Act) {#checklist-de-alinhamento-técnico-ai-act}

A lista abaixo permite validar o **alinhamento técnico** do programa SbD-ToE com os requisitos do AI Act — não emite o juízo de conformidade legal. Recomenda-se revisão periódica:

- [ ] **Enquadramento:** Papel e categoria de risco determinados (jurídico); contexto CTX-AIA-RE (ou grau ART50) declarado na aplicação
- [ ] **Literacia (Art. 4):** Trilho formativo activado conforme [Policy 37 §11](/sbd-toe/assets/policies/policy-formacao-seguranca) (obrigatório com agentes A1+ — escolha do Manual)
- [ ] **Governação de IA:** Política de IA aprovada; gates mapeados como evidência; Policy 38 (mandates) + Policy 39 (AI BOM lifecycle) operacionais
- [ ] **Classificação:** Sistemas de IA inventariados e classificados (L1–L3); níveis A0–A4 declarados nos *mandates*
- [ ] **Threat model:** Threat model com [playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic) executado; threat library MITRE ATLAS + OWASP LLM Top 10 já incluída
- [ ] **Supervisão (Art. 14):** interface de supervisão (`ARC-014`, piso P08) validada em todos os sistemas de risco elevado; `REQ-AGN-001..004` operacional; [`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015) validado; *kill-switch* exercitado com cadência registada
- [ ] **Proveniência de dados e modelos:** AI BOM CycloneDX 1.6 *ml-bom* gerado por *build* ([`DEP-012`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-012)); fornecedores de serviços de IA aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014))
- [ ] **Documentação (Art. 11/Anexo IV):** Índice Anexo IV + *model card* + *mandate* + AI BOM
- [ ] **Cibersegurança (Art. 15):** *Eval suites* contínuas operacionais (Cap. 10 §C5); *off-policy* / *jailbreak detection* ([`OPS-014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-014))
- [ ] **Supply chain (Art. 25):** *Pinning* ([`DEP-013`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-013)); lista de fornecedores de serviços de IA aprovados ([`DEP-014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-014)); cláusulas contratuais (Cap. 14 US-21)
- [ ] **Responsável pela implantação (Art. 26):** *Mandate* do responsável pela implantação documentado quando a organização utiliza o sistema de IA sob a sua própria autoridade (art. 3.º, ponto 4) sem ser o seu prestador
- [ ] **Logging (Art. 12/19):** Logs de inferência + audit per *tool invocation* ([`OPS-012`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#ops-012)) com retenção e imutabilidade
- [ ] **Monitorização (Art. 72):** Plano por sistema (CTX-AIA-RE-R04) + telemetria agentic + *dashboards* de *drift*, *budget*, *off-policy*
- [ ] **Transparência e explicação (Art. 50, Art. 86):** R01 e R02 verificados em teste; R03 aplicado quando um sistema do anexo III apoia decisões sobre pessoas
- [ ] **Salvaguardas de conteúdo (Art. 5.º, n.º 1-A):** pisos P09 e P10 aplicados em geradores de imagem, vídeo ou áudio realistas
- [ ] **Modificação substancial (Art. 43.º, n.º 4):** alterações classificadas e registadas (`ARC-009`, piso P11)
- [ ] **Incidentes (Art. 73):** *Runbook* alinhado com a Política 32 §6 + classes agentic (Policy 16 §11.4) + *upstream* IR (Policy 39 §7)
- [ ] **GPAI (art. 53.º; art. 55.º se o modelo tiver risco sistémico):** AI BOM + *eval suites* + *kill-switch* exercitado mensalmente (cadência do Manual) + cláusulas declaradas
- [ ] **Evidência:** *Data room* com documentação técnica, *mandates*, AI BOMs, eval reports, audit trails, telemetria

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida) {#o-que-cada-capítulo-sbd-toe-cobre-referência-rápida}

> ✏️ **Revisão 2026-09-27.** Tabela alinhada com a matriz de cobertura: os arts. 9, 10 e 17 estão fora do âmbito do Manual e aparecem marcados «(evidência)», porque os capítulos lhes servem apenas de evidência.

| Capítulo | AI Act Artigos | O Que Faz |
|---|---|---|
| **[Cap. 00 — Fundamentos](/sbd-toe/sbd-manual/fundamentos/intro)** | Art. 4, 26 | Roles canónicos + função composta "AI Reliability Engineer" |
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 6 (contexto CTX-AIA-RE), 9 (evidência) | Classificação de criticidade (L1–L3) |
| **[Cap. 02 §A0–A4 + `REQ-AGN`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/governanca-automatismos)** | Art. 9 (evidência), 14 | Modelo de níveis de autonomia A0–A4 + mandate + *intent declaration* |
| **[Cap. 03 playbook agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic)** | Art. 5, 9 (evidência), 15 | Threat modeling com MITRE ATLAS + OWASP LLM Top 10 2025 |
| **[Cap. 04 — `ARC-014`/`ARC-015`](/sbd-toe/sbd-manual/arquitetura-segura/addon/catalogo-requisitos-arquitetura#arc-015)** | Art. 14, 15, 43 (n.º 4) | Arquitetura defensiva + agente como *principal* isolado + *kill-switch* |
| **[Cap. 05 — `DEP-011..014`](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/catalogo-requisitos-dependencias#dep-011)** | Art. 10 (evidência), 15, 25, 55 | AI BOM + *pinning* + fornecedores de serviços de IA aprovados |
| **[Cap. 06 — Prompts como código](/sbd-toe/sbd-manual/desenvolvimento-seguro/addon/genia-e-seguranca#prompts-como-codigo)** | Art. 15, 17 (evidência) | Versionamento + revisão de *system prompts*, *skill files*, *agent files* |
| **[Cap. 07 US-19](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle)** | Art. 15, 17 (evidência) | Pipeline seguro + agentes AI como *principals* com OIDC + audit |
| **[Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro)** | Art. 15, 55 | Hardening de runtime/inferência |
| **[Cap. 10 §C5](/sbd-toe/sbd-manual/testes-seguranca/addon/ia-nos-testes#c5-eval-suites)** | Art. 15, 55 | *Eval suites* contínuas (regression, abuse, drift, A/B) |
| **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 17 (evidência) | Gate de release, validação pré-produção |
| **[Cap. 12 US-13 + `OPS-011..014`](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)** | Art. 12, 19, 72, 73, 86 | Telemetria agentic + audit per tool + jailbreak detection |
| **[Cap. 13 (formação)](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 4 | Literacia no domínio da IA por *role* |
| **[Cap. 14 US-21](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle)** | Art. 17 (evidência), 25, 26, 73 | Governança + contratação de fornecedores de serviços de IA + escalonamento |

---

## Métrica Simples: Estou Alinhado? {#métrica-simples-estou-alinhado}

Estas perguntas são um auto-diagnóstico **técnico** — respondê-las não emite o juízo de conformidade legal. Um SIM a todas indica que o núcleo técnico está alinhado:

1. **Enquadramento:** Conheço o meu papel e a categoria de risco?
2. **Supervisão (Art. 14):** Tenho interface de supervisão humana em cada sistema de risco elevado?
3. **Cibersegurança (Art. 15):** Tenho threat model que cobre o vetor adversarial (ATLAS) e faço AI red teaming?
4. **Cadeia:** Tenho proveniência e integridade de datasets e modelos?
5. **Logging:** Registo eventos de inferência com retenção adequada?
6. **Monitorização:** Tenho plano de acompanhamento pós-comercialização por sistema (R04) com deteção de drift?
7. **Incidentes:** Consigo comunicar um incidente grave nos prazos do Art. 73?
8. **Transparência (Art. 50):** Informo as pessoas e marco o conteúdo sintético?
9. **Documentação:** Tenho índice Anexo IV + model card?
10. **Evidência:** Consigo demonstrar tudo isto numa auditoria?

≥8/10 → Boa maturidade técnica face ao AI Act (maturidade técnica, **não conformidade legal**). `<`6 → Priorizar Art. 15 (cibersegurança), logging (Art. 12) e supervisão (Art. 14).

> ⚠️ **Nota:** esta métrica cobre o **núcleo técnico**. A conformidade plena exige ainda o que fica fora do âmbito do Manual — gestão de riscos (Art. 9), governação de dados de treino (Art. 10), gestão da qualidade (Art. 17), avaliação da conformidade, declaração UE de conformidade, marcação CE e registo (Art. 43, 47–49) — e a exatidão e a solidez, pendentes da ronda AISVS/SAIF do AppSec Core.

---

## Nota Crítica: Gestão de Exceções no AI Act {#nota-crítica-gestão-de-exceções-no-ai-act}

O AI Act exige que os sistemas de IA de risco elevado cumpram os requisitos do capítulo III, secção 2 (art. 8.º, n.º 1). Exceções (desvios) devem ser formais e auditadas, com trilho documental e aprovação adequada. Uma exceção **interna** não altera a obrigação legal do AI Act — apenas documenta um risco técnico aceite para o dossiê de evidência; a obrigação legal subsiste.

O que caracteriza uma exceção em SbD-ToE/AI Act:
- Desvio formal de um requisito (ex.: vetor adversarial mitigado por compensação enquanto se prepara *retraining*)
- Aprovação formal, justificação, TTL (Time-To-Live), plano de remediação

Quem aprova (por nível de criticidade):
- L1 (baixo risco): Tech lead / AppSec Engineer
- L2 (médio risco): CISO / responsável de IA
- L3 (risco elevado na escala do Manual, que não equivale a risco elevado no AI Act): Governação de IA + gestão (accountable)

Implicação regulatória:
- Exceções sem aprovação formal comprometem a evidência técnica apresentada à autoridade
- **Algumas situações nunca são exceptuáveis** - desde logo, qualquer uso que recaia nas práticas proibidas do Art. 5
- Trilho auditado é obrigatório para demonstrar controlo à autoridade

**Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (addon de exceções) e [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro) (exceções formalizadas).

---

## Próximos Passos {#próximos-passos}

1. **Enquadramento jurídico:** Determinar papel e categoria de risco (jurídico/compliance) e declarar o contexto CTX-AIA-RE na aplicação
2. **Auditoria técnica atual:** Verificar [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) contra os requisitos técnicos do AI Act
3. **Definir roadmap:** Sequenciar fases conforme contexto e categoria de risco
4. **Articular com domínio:** Coordenar com ciência de dados, produto e jurídico o que fica fora do âmbito do Manual
5. **Implementar e validar:** Iterar e demonstrar a **evidência técnica** em auditoria

Documentação completa: ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências {#referências}

- **SbD-ToE Manual:** Capítulos 01–14 (detalhe técnico por domínio)
- **Cross-Check AI Act:** [Análise normativa completa](/sbd-toe/cross-check-normativo/ai-act/intro)
- **AI Act:** Regulamento (UE) 2024/1689
- **Frameworks de Referência:** ISO/IEC 42001, ISO/IEC 23894, NIST AI RMF 1.0, MITRE ATLAS, OWASP ML Security Top 10, OWASP Top 10 for LLM Applications

---

**Versão:** 1.1
**Data:** Setembro 2026
**Nota:** Este playbook complementa a [análise normativa AI Act](intro) com implementação prática.
