---
id: kpis-arquitetura-visao-geral
title: Arquitectura KPI - Visão Geral
sidebar_position: 91
description: Diagramas de referência da arquitectura de medição SbD-ToE - cascata de camadas, mapeamento capítulo-dimensão, e funil de adoptabilidade.
tags: [kpi, arquitectura, dashboard, metricas, governacao]
---

<!--template: sbdtoe-addon -->

# Arquitectura KPI - Visão Geral

Para definições, thresholds e catálogo completo de indicadores, ver [`kpis-governanca`](./kpis-governanca).

---

## D1 - Cascata de camadas

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

## D2 - Mapeamento capítulo → dimensão transversal

| Capítulo | T-01 Cobertura | T-02 Excepções | T-03 Velocidade | T-04 Ownership | T-05 Cadeia | T-06 Maturidade |
|----------|:--------------:|:--------------:|:---------------:|:--------------:|:-----------:|:---------------:|
| Cap.01 · CLA-K | ✔ | - | - | - | - | ✔ |
| Cap.02 · RQS-K | ✔ | - | - | - | - | ✔ |
| Cap.03 · THR-K | ✔ | - | - | - | - | ✔ |
| Cap.04 · ARC-K | ✔ | - | - | ✔ | - | ✔ |
| Cap.05 · DEP-K | ✔ | - | ✔ | - | ✔ | - |
| Cap.06 · DEV-K | ✔ | ✔ | ✔ | - | - | - |
| Cap.07 · CIC-K | ✔ | ✔ | ✔ | - | - | - |
| Cap.08 · IAC-K | ✔ | ✔ | - | - | - | - |
| Cap.09 · CNT-K | ✔ | - | ✔ | - | ✔ | - |
| Cap.10 · TST-K | ✔ | - | ✔ | - | - | - |
| Cap.11 · DPL-K | ✔ | ✔ | - | - | - | - |
| Cap.12 · OPS-K | - | - | ✔ | - | - | - |
| Cap.13 · TRN-K | - | - | - | ✔ | - | - |
| Cap.14 · GOV-K | - | ✔ | - | ✔ | ✔ | - |
| **Contribuintes** | **12** | **5** | **7** | **3** | **3** | **4** |

**Leitura:** T-01 (Cobertura) é a dimensão mais transversal - presente em 12 dos 14 capítulos. T-04 (Ownership) e T-05 (Cadeia de fornecimento) têm cobertura concentrada, o que é esperado: apenas os capítulos com responsabilidade directa sobre supply chain e ownership contribuem.

---

## D3 - Funil de adoptabilidade

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

| Gap observado | Diagnóstico | Acção prioritária |
|---------------|-------------|-------------------|
| F-01 desconhecido | Inventário incompleto - todo o programa de medição é inválido | Completar inventário antes de qualquer outra métrica |
| F-02 ≪ F-01 | Classificação em atraso | Activar CLA-K01; sem classificação não há denominador válido |
| F-03 ≪ F-02 | Requisitos não mapeados - controlos sem base formal | Activar RQS-K01 |
| F-04 ≪ F-03 | Controlos declarados mas não validados | Activar processo de evidência |
| F-04 ≈ F-03 | Programa maduro | Focar em T-03, T-02 e T-06 |
