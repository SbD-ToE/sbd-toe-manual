---
id: validacao-assistida-ferramentas
title: Tool-Assisted Validation - Process Risk
sidebar_position: 11
tags: [tipo:risco-processo, tema:automacao, validacao, decisao, rastreabilidade]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/01-classificacao-aplicacoes/addon/11-validacao-assistida-ferramentas.md
  source_sha256: 1cc54ccd3ac5b6fc1c04402650052d9c4bebbf67b7178912d6253d9c33c4dd4a
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: a7e54fff6e13ca08a867aad2bf7db326f53a4c165e13b79b405154e74d377e1f
  engine: claude-fable-5-1
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: f3ae07385fc10c458f9087ea5ea231fd2bbf0e4852b0e4c0e84ec84618762443
  glossary_keys: [audit_trail, avaliacao, cycle_iteration, framework_source_corpus, lifecycle_phase, mapping, practitioner_manual, risk_level, threat, traceability, validation_evaluation]
  glossary_sha256: 0f9ea9f102dc99e99b6c3b26684b206d76e17e0db9a588c6c79e62d96ffb3e99
  translated_at: 2026-09-25T17:59:17Z
  reviewed_by: null
---

<!--template: sbdtoe-core -->

# Tool-Assisted Validation - Process Risk

## 🎯 Objective {#-objetivo}

This document prescribes how to manage **process risks** when automated tools (scoring algorithms, analysis systems, or other forms of assistance) take part in **application classification, change detection, or threat mapping**.

The objective **is not to prohibit tools**, but rather to:

- ensure that **tool suggestions never replace human decisions**;
- identify **plausible errors** that machines may introduce;
- require **mandatory validation** and **explicit traceability**;
- establish **escalation paths** in case of disagreement;
- keep **auditable evidence** of all decisions.

---

## 📋 Fundamental Invariants (from agent.md) {#-invariantes-fundamentais-do-agentmd}

Regardless of the type of tool or lifecycle phase, **all use of automation in classification must respect**:

### I1 - Separation between Suggestion and Decision {#i1---separação-entre-sugestão-e-decisão}

- Tools **suggest, analyse, or correlate**.
- The **final decision is always human**, assigned to an explicit role (Developer, AppSec Engineer, GRC/Compliance).
- The suggestion may be ignored, modified, or accepted - but responsibility always lies with the human decision-maker.

### I2 - Evidence Above Plausibility {#i2---evidência-acima-de-plausibilidade}

- A **plausible** result (e.g. "L2 because E=2, D=2, I=1") does not replace **verifiable evidence**.
- Examples of evidence:
  - Documented and reviewed technical architecture.
  - Data specified and classified manually.
  - Threats validated by domain experts.
  - Formally approved exceptions.

### I3 - Reproducibility and Auditability {#i3---reprodutibilidade-e-auditabilidade}

- Every suggestion must be **reproducible** and **traceable**:
  - Which tool was used? (name, version, date)
  - Which inputs did it receive? (application, axes, raw data)
  - Which output did it generate? (score, E/D/I scoring, proposed level)
  - Which decision criterion was applied? (threshold, rules, weighting)

### I4 - Protection of Critical Assets {#i4---proteção-de-ativos-críticos}

- Any external tool (SaaS, cloud, or third parties) is a **supply chain risk**:
  - Sensitive application data (data processed, architecture, customers) must not be sent to unknown systems.
  - Explicit approval is required before using any tool at L2/L3.

### I5 - Traceability of Decision and Execution {#i5---rastreabilidade-de-decisão-e-execução}

- Every classification decision must answer:
  - **Who decided?** (Developer, AppSec Engineer, Product Owner, etc.)
  - **On what basis?** (manual E/D/I, tool suggestion, feedback from Software Architects, etc.)
  - **Which validations were performed?** (checklist, review, tests)
  - **What evidence supports the decision?** (documentation, reports, scans, approvals)

---

## 🚨 Plausible Errors - By Type of Assistance {#-erros-plausíveis---por-tipo-de-assistência}

### A. Automatic E/D/I Scoring {#a-scoring-automático-de-edi}

**How it works**: The tool analyses the project description, endpoints, data types, and proposes scores for E, D, I.

**Typical plausible errors**:

| Error | Examples | Impact | Mitigation |
|---|---|---|---|
| **Over-weighting of one axis** | "Has many public endpoints → E=3 always", neglecting that the data is public | Biased classification, disproportionate controls | Mandatory narrative explanation: "Why E=3?" |
| **Omission of context** | Does not detect that a critical dependency is optional or that isolation is possible | Underestimation of risk | Manual review of dependencies + feedback from Software Architects |
| **Inflexible rules** | "Application with more than 10 APIs → always L3", without considering that they may be internal | Over-classification | Criterion "if the tool proposes L3, the AppSec Engineer validates the presence of real public exposure" |
| **Lack of temporal nuance** | Classifies based on the current state, ignores forecast data growth | Risk of hasty reclassification | Include a "12-month forecast" in the assessment; review periodically |
| **Misalignment with the organisational model** | Tool uses a generic threshold (e.g. "PII data=D2"), the organisation uses "customer data=D3" | Inconsistency with policy | Explicit policy: "All tool results are re-calibrated against organisational policy" |

---

### B. Automatic Change Detection (Event-Based Triggers) {#b-deteção-automática-de-alterações-event-based-triggers}

**How it works**: The tool analyses commits, PRs, configurations, and proposes reclassification (e.g. "New critical dependency detected").

**Typical plausible errors**:

| Error | Examples | Impact | Mitigation |
|---|---|---|---|
| **False positive** | Detects `npm update lodash` as a "critical change" | Excessive alarm, distrust in the system | Whitelist + context: "Patch updates are ignored; only minor/major generate an alert" |
| **Omission of context** | Sees "integration with external API" but does not know whether it is critical or optional | Under-detection | AppSec Engineer performs validation: "Is this new integration critical to the business?" |
| **Time lag** | Tool detects the change 2 weeks later | Delay in review | Weekly or per-sprint analysis, not ad hoc |
| **Lack of prioritisation** | Treats "new telemetry endpoint" with the same urgency as "new access to customer data" | Confusion of priorities | Categorisation: critical (reclassify now), important (schedule review), informative (log only) |

---

### C. Automatic Threat Mapping {#c-mapeamento-automático-de-ameaças}

**How it works**: The tool generates a STRIDE or MITRE ATT&CK mapping based on the application type.

**Typical plausible errors**:

| Error | Examples | Impact | Mitigation |
|---|---|---|---|
| **Generic, non-contextual threats** | Maps "Denial of Service" to all apps, without considering a critical SLA | Noise, wasted effort | Filter: "Include only threats with high probability or critical impact for this domain" |
| **Omission of contextual threats** | Generates generic STRIDE, ignores "IP theft by an insider" (a threat specific to R&D) | Unidentified residual risk | Validation by Software Architects + domain experts: "Are specific threats missing?" |
| **Lack of prioritisation** | Lists 50 threats, without indicating critical vs. minor | Analysis paralysis | Classification: critical (mandatory coverage), major (recommended coverage), minor (optional) |
| **Misalignment with risk level** | Same mapping for L1 and L3 | Proportion lost | Requirement: "Critical threats +60% for L3, +30% for L2, -50% for L1" |

---

## ✅ Validation Checklist - By Practice {#-checklist-de-validação---por-prática}

### Checklist 1: US-01 (Initial Classification - Assisted) {#checklist-1-us-01-classificação-inicial---assistida}

**When**: The tool proposes E/D/I or an L1/L2/L3 level.

**Checklist (additional DoD)**:

- [ ] **Clear data source**: Which inputs did the tool receive? (project description, endpoints, data types)
- [ ] **Narrative explanation**: Did the tool justify why E=X, D=Y, I=Z? (output with attached reasoning)
- [ ] **Axis validation**: Developer/Team Lead manually validated each axis against the technical reality
- [ ] **Context review**: Software Architects confirm that E/D/I reflect the real exposure, data, and impact
- [ ] **Signed decision**: The AppSec Engineer signed the final decision with an explicit record:
  ```
  Classificação: L2
  Origem: Sugestão de ferramenta (v1.2, data: 2025-01-15)
  Ajustes humanos: E mantido em 2 (confirmado por Arquitetos), 
                   D aumentado para 3 (dados de cliente identificados), 
                   I mantido em 1
  Aprovação: AppSec Engineer [nome], data
  ```
- [ ] **Benchmark vs. history**: Compared with similar applications already classified?
- [ ] **Re-validation TTL**: Next review scheduled (time-based per level + event-based triggers)

---

### Checklist 2: US-03 & US-07 (Review - Assisted by Change Detection) {#checklist-2-us-03--us-07-revisão---assistida-por-deteção-de-alteração}

**When**: The tool detects a change and proposes reclassification.

**Checklist (additional DoD)**:

- [ ] **Documented trigger**: What was detected? (new dependency, new endpoint, new data, etc.)
- [ ] **Tool & method**: Who detected it? (manual commit analysis, tool X version Y, etc.)
- [ ] **Technical context**: AppSec Engineer/Software Architects confirm that the change is relevant and not a false positive
- [ ] **Impact on E/D/I**: Which axis is affected? (example: "E increases due to a new endpoint", "D increases due to a new data type")
- [ ] **Proposed reclassification**: old E/D/I → new (with an explanation of each change)
- [ ] **Validation path**: In case of disagreement (machine proposes L2, AppSec wants L3):
  - Document: "Tool proposed L2 for [reason X], AppSec override to L3 for [reason Y]"
  - Escalation: Product Owner informed if there is business impact
  - Final decision recorded with signature
- [ ] **GRC/Compliance audit trail**: Record in the compliance tool with timestamp

---

### Checklist 3: US-06 (Threat Mapping - Assisted) {#checklist-3-us-06-mapeamento-de-ameaças---assistido}

**When**: The tool generates a STRIDE/MITRE ATT&CK mapping.

**Checklist (additional DoD)**:

- [ ] **Tool & version**: Which algorithm? (e.g. "Automated STRIDE Generator v2.1")
- [ ] **Correct scope**: Does the mapping include threats appropriate to the L1/L2/L3 level?
- [ ] **Noise filter**: Have generic, non-contextual threats been omitted? (e.g. filter out "slow DDoS" if criticality is low)
- [ ] **Validation by experts**: Software Architects/AppSec Engineer validated:
  - Have no critical threats been omitted?
  - Have domain-specific threats been included?
  - Is the prioritisation (critical vs. minor) correct?
- [ ] **Tracking**: Each threat has:
  - [ ] Clear description
  - [ ] Control applied (or exception with justification)
  - [ ] Status: covered / partially covered / not covered (residual risk)
- [ ] **Escalation if a critical risk is not covered**: Triggers US-04 (residual risk) or mandatory mitigation

---

## 🔀 Escalation Path - Human ↔ Machine Disagreement {#-trilho-de-escalação---discordância-humano--máquina}

### Scenario 1: Developer proposes L1, Tool proposes L2 {#cenário-1-developer-propõe-l1-ferramenta-propõe-l2}

```
┌─────────────────────────────────────────────────────┐
│ DISCORDÂNCIA DETECTADA                              │
│ Developer: "Apenas APIs internas, dados públicos"   │
│ Ferramenta: "E=2 (múltiplos endpoints) → L2"        │
└──────────────────┬──────────────────────────────────┘
                   ▼
         ┌─────────────────────┐
         │ AppSec Engineer     │
         │ Valida contexto:    │
         │ - Endpoints realmente│
         │   apenas internos?   │
         │ - Dados realmente    │
         │   públicos?          │
         └────────┬────────────┘
                  ▼
        ┌──────────────────────────────┐
        │ Decisão Final:               │
        │ L1 (concordou com Developer) │
        │ Motivo: "Ferramenta         │
        │  incorreu em falso positivo" │
        │ Registro: [assinado]         │
        └──────────────────────────────┘
```

### Scenario 2: AppSec proposes L3, Tool proposes L1 (Under-detection) {#cenário-2-appsec-propõe-l3-ferramenta-propõe-l1-subdeteção}

```
┌──────────────────────────────────────────────────────┐
│ DISCORDÂNCIA CRÍTICA DETECTADA                       │
│ AppSec: "Dados de cliente + APIs públicas → L3"      │
│ Ferramenta: "Apenas E=1, D=1 → L1"                   │
└───────────────────┬────────────────────────────────────┘
                    ▼
        ┌─────────────────────────────────────┐
        │ Investigação: Por quê ferramenta    │
        │ sub-classificou?                    │
        │ - Não detectou dados de cliente?    │
        │ - Não mapeou APIs públicas?         │
        │ Ação: Feedback para ferramenta      │
        │ (treino, ajuste de regras, etc.)    │
        └──────────┬──────────────────────────┘
                   ▼
        ┌──────────────────────────────┐
        │ Decisão Final:               │
        │ L3 (concordou com AppSec)    │
        │ Motivo: "Ferramenta errou;   │
        │  dados de cliente omissos"   │
        │ Escalação: Product Owner     │
        │  (impacto de negócio L3)     │
        │ Registro: [assinado]         │
        └──────────────────────────────┘
```

### Scenario 3: Disagreement not resolved within the SLA {#cenário-3-discordância-não-resolvida-no-sla}

```
┌────────────────────────────────────────────┐
│ Sem consenso em 5 dias úteis (SLA)         │
├────────────────────────────────────────────┤
│ Developer: L1                              │
│ Ferramenta: L2                             │
│ AppSec Engineer: Indeciso                  │
└─────────────────┬──────────────────────────┘
                  ▼
        ┌────────────────────────────┐
        │ Escalonamento automático:  │
        │ Product Owner arbitral     │
        │ (aspectos de negócio)      │
        │ + CISO (aspectos técnicos) │
        └──────────┬─────────────────┘
                   ▼
        ┌────────────────────────┐
        │ Decisão Final Oficial  │
        │ Registro formal com    │
        │ assinatura(s)          │
        │ Motivo documentado     │
        └────────────────────────┘
```

---

## 📝 Examples - Good and Bad Practices {#-exemplos---boas-e-más-práticas}

### ❌ Bad Practice 1: Accepting a Suggestion without Validation {#-má-prática-1-aceitar-sugestão-sem-validação}

```
Ferramenta: "L2" (score: E=2, D=2, I=1)
Developer: "OK, vou com L2"
AppSec Engineer: (não revê)
Artefacto registado: classificacao-app.yaml com L2, sem explicação

PROBLEMA:
- Ninguém sabe por quê L2
- Impossível auditar decisão
- Ferramenta pode ter errado (ex: omitiu dados sensíveis)
- Reclassificação futura sem baseline
```

### ✅ Good Practice 1: Validation with Traceability {#-boa-prática-1-validação-com-rastreabilidade}

```
Ferramenta: "L2" (E=2, D=2, I=1)
Output: {
  "eixos": {
    "exposicao": 2,
    "dados": 2,
    "impacto": 1
  },
  "raciocinio": "E=2: APIs internas (5 endpoints), 
                 D=2: Dados de utilizador, 
                 I=1: Downtime ~30min aceitável"
}

Developer + Arquitetos: Revisam E/D/I narrativa
- E=2: Confirmado? SIM (APIs internas, não públicas)
- D=2: Confirmado? SIM (dados de utilizador, não PII)
- I=1: Confirmado? NÃO - se cair, impacto é crítico → I=2

AppSec Engineer: Reclassifica E/D/I → L2 mantém-se (após ajuste I)

Artefacto registado:
  classificacao-app.yaml:
    nível: L2
    eixos_originais: {E: 2, D: 2, I: 1}
    eixos_finais: {E: 2, D: 2, I: 2}
    assistida_por_ferramenta: true
    ferramenta: "Automated Classifier v1.2"
    data_ferramenta: "2025-01-15"
    validadores: ["Developer-X", "Arquiteto-Y"]
    aprovador: "AppSec-Z"
    data_aprovacao: "2025-01-16"
    observações: "I ajustado de 1→2 por Arquitetos (impacto crítico)"

VANTAGENS:
✓ Totalmente rastreável
✓ Auditável ("quem decidiu o quê, quando, por quê")
✓ Benchmarkável contra outras apps
✓ Reclassificações futuras têm baseline claro
```

---

### ❌ Bad Practice 2: Tool Detects a Change, Nobody Validates {#-má-prática-2-ferramenta-detecta-alteração-ninguém-valida}

```
Commit: "Add dependency on critical-auth v2.0"
Ferramenta: [Alerta automático] "Nova dependência crítica detectada!"
GRC/Compliance: Vê alerta, não faz nada (assume que já foi validado)
Developer: Não vê alerta (não subscrito)
AppSec Engineer: Não viu (não reviewou)

Resultado: Ninguém reviu, classificação não foi atualizada
RISCO: Controlo de segurança insuficiente, gap de conformidade
```

### ✅ Good Practice 2: Detection with Explicit Validation {#-boa-prática-2-deteção-com-validação-explícita}

```
Commit: "Add dependency on critical-auth v2.0"
Ferramenta: [Alerta] "Nova dependência crítica detectada!"
Email automático: AppSec Engineer + GRC/Compliance
Issue automática: "Reclassifique se necessário"

AppSec Engineer (3 dias úteis):
- Valida: "critical-auth é realmente crítica?"
- Resultado: SIM, acesso centralizado a dados de cliente
- Decisão: E (exposição) não muda; D (dados) permanece 2
- Nível: L2 → L2 (sem mudança, mas com ameaças críticas agora)
- Ação: Dispara US-06 (mapeamento de ameaças para nova dependência)

Artefacto registado:
  classificacao-revisao.md:
    data: 2025-01-20
    trigger: "Nova dependência crítica (critical-auth v2.0)"
    ferramenta_detetor: "Dependency Scanner v1.5"
    nível_anterior: L2
    nível_novo: L2
    decisão: "Mantém-se L2; novo mapeamento de ameaças requerido"
    validador: "AppSec-Z"
    próxima_revisão: "2025-02-20" (30 dias)

GRC/Compliance: Registra em audit trail
```

---

## 🔗 Integration with User Stories {#-integração-com-user-stories}

### For US-01 (Initial Classification) {#para-us-01-classificação-inicial}

Add to the DoD:

```markdown
- [ ] **Se assistida por ferramenta:**
  - [ ] Output de ferramenta (scores, raciocínio) anexado
  - [ ] Justificação narrativa humana clara (por quê E=X, D=Y, I=Z)
  - [ ] Validação de cada eixo por especialistas (Developer, Arquitetos)
  - [ ] Aprovação final por AppSec Engineer com registo explícito
  - [ ] Ferramenta, versão, data documentados
```

### For US-03 (Event-Based Review) {#para-us-03-revisão-event-based}

Add to the DoD:

```markdown
- [ ] **Se assistida por ferramenta detetor:**
  - [ ] Ferramenta & método de deteção documentados
  - [ ] Trigger técnico validado (falso positivo excluído)
  - [ ] Contexto de negócio confirmado (alteração realmente relevante)
  - [ ] Impacto em E/D/I explicado
  - [ ] Se nível alterou: trilho de escalação documentado
```

### For US-07 (Time-Based Review) {#para-us-07-revisão-time-based}

Add to the DoD:

```markdown
- [ ] **Se assistida por ferrameta de análise:**
  - [ ] Ferramenta forneceu re-scoring de E/D/I?
  - [ ] Comparação: score anterior vs. score novo documentada
  - [ ] Se discordância (máquina vs. AppSec): trilho de resolução registado
```

### For US-06 (Threat Mapping) {#para-us-06-mapeamento-de-ameaças}

Add to the DoD:

```markdown
- [ ] **Se assistido por ferramenta de mapeamento:**
  - [ ] Ferramenta & versão documentados
  - [ ] Ameaças genéricas não-contextuais filtradas?
  - [ ] Ameaças específicas de domínio adicionadas (validação especialistas)?
  - [ ] Priorização (crítica vs. minor) correcta?
  - [ ] Ameaças críticas não cobertas dispararam US-04 (risco residual)?
```

---

## 📊 Proportionality Matrix - Validation Effort {#-matriz-de-proporcionalidade---esforço-de-validação}

| Practice | L1 | L2 | L3 |
|---|---|---|---|
| **Mandatory validation of suggestions** | Recommended | Mandatory | Mandatory + Executive Management |
| **Benchmark vs. history** | Optional | Recommended | Mandatory |
| **Formalised escalation path** | Ad hoc | Documented | Documented + SLA |
| **Assisted re-validation TTL** | 12m | 6m | 3m |
| **Audit of assisted decisions** | Annual | Half-yearly | Quarterly |

---

## 🎯 Summary & Operational Recommendations {#-resumo--recomendações-operacionais}

1. **Tools are aids, not authorities**: Suggestions are valuable, decisions are human.
2. **Traceability is non-negotiable**: All use of automation must leave an auditable trail.
3. **Validation proportional to risk**: L1 may be lighter, L3 requires maximum rigour.
4. **Tool errors are expected**: Keep a checklist of plausible errors + mitigations.
5. **Clear escalation**: When machine and human disagree, a formalised process leads to consensus.
6. **Continuous feedback**: If the tool has erred systematically, adjust it (training, rules, etc.).
7. **Regulatory compliance**: Audits must be able to trace "who decided on what basis".

---

## 🔗 Internal References {#-referências-internas}

- [Theory of Everything - Introduction](/sbd-toe/teory-of-everything/intro)
- [US-01 - Initial Classification](../aplicacao-lifecycle#us-01---classificação-inicial-da-aplicação)
- [US-03 - Event-Based Review](../aplicacao-lifecycle#us-03---revisão-por-alteração-relevante-event-based)
- [US-06 - Threat Mapping](../aplicacao-lifecycle#us-06---mapeamento-de-ameaças-por-nível-de-risco)
- [US-07 - Time-Based Review](../aplicacao-lifecycle#us-07---revisão-periódica-time-based-da-classificação-cadência-obrigatória)
