---
id: kpis-arquitetura-visao-geral
title: KPI Architecture - Overview
sidebar_position: 91
description: Reference diagrams of the SbD-ToE measurement architecture - layer cascade, chapter-dimension mapping, and adoptability funnel.
tags: [kpi, arquitectura, dashboard, metricas, governacao]
translation:
  source_locale: pt
  source_path: 010-sbd-manual/14-governanca-contratacao/kpis-arquitetura-visao-geral.md
  source_sha256: b55d1fd280d129ceddb6bfbc6664e829075c02c8eb51ed10905aa6b025b897c3
  source_commit: 895786c4e9c09e4191e51a58b865c83ff4510ec7
  target_sha256: c7f58d96757712c50d4e25f546d789cbc920337c2e294e341091a28feab3bae5
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: bee9c6ee01a569777d9cc1d02cb14939f64a74ce4571924f95ce9be1f7d53a10
  glossary_keys: [chapter_role, mapping, maturity, mcp_reading_programa, programme_line, sbdtoe_sbd, transversal]
  glossary_sha256: 9deb1ab5ce73d6a4aed8a7f71eeef2a390681ed93fb9c656dff836b7d1bde6eb
  translated_at: 2026-09-26T12:00:25Z
  stamped_at: 2026-09-26T18:36:27Z
  reviewed_by: null
---

<!--template: sbdtoe-addon -->

# KPI Architecture - Overview

For definitions, thresholds and the full catalogue of indicators, see [`kpis-governanca`](./kpis-governanca).

---

## D1 - Layer cascade {#d1---cascata-de-camadas}

```mermaid
flowchart LR
    F["**Fundação**\nF-01 · F-02 · F-03 · F-04\ndenominador comum"]
    D["**Domínio**\n14 capítulos\nCLA-K → GOV-K"]
    T["**Transversal**\n6 dimensões\nT-01 → T-06"]
    E["**Dashboard**\nexecutivo"]

    F -->|"F-02 =\ndenominador"| D
    D -->|"alimentam"| T
    T -->|"resumem"| E

    classDef layer fill:#dbeafe,stroke:#3b82f6,color:#1e3a5f
    classDef dash fill:#f3e8ff,stroke:#9333ea,color:#3b0764
    classDef found fill:#fef9c3,stroke:#ca8a04,color:#713f12

    class F found
    class D,T layer
    class E dash
```

---

## D2 - Mapping chapter → cross-cutting dimension {#d2---mapeamento-capítulo--dimensão-transversal}

| Chapter | T-01 Coverage | T-02 Exceptions | T-03 Speed | T-04 Ownership | T-05 Chain | T-06 Maturity |
|----------|:--------------:|:--------------:|:---------------:|:--------------:|:-----------:|:---------------:|
| Ch.01 · CLA-K | ✔ | - | - | - | - | ✔ |
| Ch.02 · RQS-K | ✔ | - | - | - | - | ✔ |
| Ch.03 · THR-K | ✔ | - | - | - | - | ✔ |
| Ch.04 · ARC-K | ✔ | - | - | ✔ | - | ✔ |
| Ch.05 · DEP-K | ✔ | - | ✔ | - | ✔ | - |
| Ch.06 · DEV-K | ✔ | ✔ | ✔ | - | - | - |
| Ch.07 · CIC-K | ✔ | ✔ | ✔ | - | - | - |
| Ch.08 · IAC-K | ✔ | ✔ | - | - | - | - |
| Ch.09 · CNT-K | ✔ | - | ✔ | - | ✔ | - |
| Ch.10 · TST-K | ✔ | - | ✔ | - | - | - |
| Ch.11 · DPL-K | ✔ | ✔ | - | - | - | - |
| Ch.12 · OPS-K | - | - | ✔ | - | - | - |
| Ch.13 · TRN-K | - | - | - | ✔ | - | - |
| Ch.14 · GOV-K | - | ✔ | - | ✔ | ✔ | - |
| **Contributors** | **12** | **5** | **7** | **3** | **3** | **4** |

**Reading:** T-01 (Coverage) is the most cross-cutting dimension - present in 12 of the 14 chapters. T-04 (Ownership) and T-05 (Supply chain) have concentrated coverage, which is expected: only the chapters with direct responsibility for supply chain and ownership contribute.

---

## D3 - Adoptability funnel {#d3---funil-de-adoptabilidade}

```mermaid
flowchart LR
    F1["**F-01**\nTotal de aplicações\nno portfólio"]
    F2["**F-02**\nAplicações classificadas\nL1 / L2 / L3"]
    F3["**F-03**\nRequisitos mapeados\n(Cap.02 → Cap.12)"]
    F4["**F-04**\nControlos validados\npor evidência"]

    F1 -->|"CLA-K01 = 100%"| F2
    F2 -->|"RQS-K01"| F3
    F3 -->|"KPIs de domínio\n≥ threshold"| F4

    classDef funnel fill:#fef9c3,stroke:#ca8a04,color:#713f12
    class F1,F2,F3,F4 funnel
```

| Observed gap | Diagnosis | Priority action |
|---------------|-------------|-------------------|
| F-01 unknown | Incomplete inventory - the entire measurement programme is invalid | Complete the inventory before any other metric |
| F-02 ≪ F-01 | Classification lagging behind | Activate CLA-K01; without classification there is no valid denominator |
| F-03 ≪ F-02 | Requirements not mapped - controls without a formal basis | Activate RQS-K01 |
| F-04 ≪ F-03 | Controls declared but not validated | Activate the evidence process |
| F-04 ≈ F-03 | Mature programme | Focus on T-03, T-02 and T-06 |
