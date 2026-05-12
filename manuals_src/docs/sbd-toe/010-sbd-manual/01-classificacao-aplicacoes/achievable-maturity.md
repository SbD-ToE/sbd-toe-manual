# Achievable Maturity — Classificação de Aplicações

## Sumário

Postura de maturidade credível atingível se este capítulo for implementado as written. Análise segue **§26 canon §4 discipline**: SAMM v2.1 + DSOMM são fontes primárias; SLSA só onde fizer sentido como progressão de build/integridade; **alinhamento regulatório NÃO é maturity score** e é registado em § Out-of-Maturity scope.

Cinco secções:

- **§ Manual ontology V2 entities** — MaturityMapping + Practice + Control entities relevantes
- **§ SAMM v2 / DSOMM maturity progression** — primary maturity sources per §26 §4
- **§ SLSA build/integrity progression** — onde aplicável a este capítulo
- **§ Out-of-Maturity scope** — regulatory alignment (NÃO maturity score)
- **§ Future-work register** — maturity gaps registered para P8 §10

---

## § Manual ontology V2 — entities relevantes para maturity

Total: **14 MaturityMapping entities** mapped a este capítulo (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:compliance-mapping` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:governance-metrics` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:risk-management` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:owasp-dsomm-governance-risk-management-requirements:security-requirements` | OWASP DSOMM | Governance, Risk Management, Requirements | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Derivação de requisitos, rastreabilidade, decisão proporcion | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:owasp-samm-governance-risk-management:1` | OWASP SAMM | Governance → Risk Management | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:owasp-samm-governance-risk-management:2` | OWASP SAMM | Governance → Risk Management | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:owasp-samm-governance-risk-management:3` | OWASP SAMM | Governance → Risk Management | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Classificação de risco por eixos, integração no SDLC | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:1` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:2` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:3` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:slsa-supply-chain-levels-for-software-artifacts:4` | SLSA | Supply Chain Levels for Software Artifacts | external | derived |
| MaturityMapping | `01-classificacao-aplicacoes:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Definição proporcional de requisitos à criticidade | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Governance, Risk Management, Requirements | Rastreabilidade a frameworks de referência presente | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Governance, Risk Management, Requirements | Não define KPIs quantitativos nem reporting formal | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Governance, Risk Management, Requirements | Modelo de classificação estruturado e aplicado sistematicamente | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Governance, Risk Management, Requirements | Permite derivação proporcional baseada em risco | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Derivação de requisitos, rastreabilidade, decisão proporcional | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Governance → Risk Management | Realiza-se classificação básica dos riscos das aplicações | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Governance → Risk Management | Integração com processos organizacionais e rastreabilidade | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Governance → Risk Management | Análise quantitativa e retroalimentação contínua | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Classificação de risco por eixos, integração no SDLC | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Supply Chain Levels for Software Artifacts | — | Classificação por eixos | `achievable-maturity.md` | Explícito |
| Supply Chain Levels for Software Artifacts | — | Fora do âmbito | `achievable-maturity.md` | Explícito |
| Supply Chain Levels for Software Artifacts | — | Coberto noutros capítulos | `achievable-maturity.md` | Explícito |
| Supply Chain Levels for Software Artifacts | — | Coberto noutros capítulos | `achievable-maturity.md` | Explícito |
| — | — | Definição proporcional de requisitos à criticidade | `achievable-maturity.md` | Explícito |

---

## § Out-of-Maturity scope (regulatory alignment NÃO maturity)

Per §26 §4 discipline: alinhamento regulatório (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **NÃO deve ser tratado como maturity score**. Items regulatórios são registados aqui para visibility editorial; conformance vive em obrigações separadas, não em maturity progression.

_(Regulatory alignment para este capítulo é tratado via Manual ontology V2 ExternalObligation entities + capítulos de governança (Cap. 14); não enumerado aqui para evitar conflation com maturity claim.)_

---

## § Future-work register (maturity gaps)

_(Nenhuma maturity claim em gap state para este capítulo.)_

---

## Generation provenance

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74`
- **Maturity mappings:** `data/entities/maturity_mappings.json` (168 items)
- **§26 methodology layer:** `00-fundamentos/canon/26-metodologia-validacao-claims.md` (Run 1 state @ a9e70c98)
- **§26 label rule:** deterministic per `confidence` field (≥0.85 Explícito; ≥0.65 Semântico; ≥0.4 Parcial; &lt;0.4 Gap)
- **§26 §4 discipline applied:** SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity
- **Generated by:** Manual Agent Run 2 (achievable-maturity enrichment)
- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony
