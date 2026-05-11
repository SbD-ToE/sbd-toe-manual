# Achievable Maturity — Arquitetura Segura

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

Total: **12 MaturityMapping entities** mapped a este capítulo (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:owasp-dsomm-architecture-requirements-risk:architecture` | OWASP DSOMM | Architecture, Requirements, Risk | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:owasp-dsomm-architecture-requirements-risk:requirements` | OWASP DSOMM | Architecture, Requirements, Risk | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:owasp-dsomm-architecture-requirements-risk:risk-analysis` | OWASP DSOMM | Architecture, Requirements, Risk | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Requisitos ARC-XXX, rastreabilidade, zonas de confiança | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:owasp-samm-design-architecture-design:1` | OWASP SAMM | Design → Architecture & Design | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:owasp-samm-design-architecture-design:2` | OWASP SAMM | Design → Architecture & Design | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:owasp-samm-design-architecture-design:3` | OWASP SAMM | Design → Architecture & Design | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Princípios formais, validação e documentação da arquitetura | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:slsa-provenance-isolation:1` | SLSA | Provenance & Isolation | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:slsa-provenance-isolation:2` | SLSA | Provenance & Isolation | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:slsa-provenance-isolation:34` | SLSA | Provenance & Isolation | external | derived |
| MaturityMapping | `04-arquitetura-segura:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Segmentação e isolamento da arquitetura | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Architecture, Requirements, Risk | Segmentação, zonas de confiança, tratamento explícito | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Architecture, Requirements, Risk | Requisitos formais por tipo de componente (ARC-XXX) | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Architecture, Requirements, Risk | Integração com threat modeling e aceitação de risco por exceção | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Requisitos ARC-XXX, rastreabilidade, zonas de confiança | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Architecture & Design | Arquitetura definida informalmente | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Architecture & Design | Documentação com validação proporcional | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Architecture & Design | Integração contínua e revisão automatizada | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Princípios formais, validação e documentação da arquitetura | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Provenance & Isolation | — | Segmentação e zonas de confiança | `achievable-maturity.md` | Explícito |
| Provenance & Isolation | — | Requisitos documentados | `achievable-maturity.md` | Explícito |
| Provenance & Isolation | — | Fora do âmbito (ver Cap. 06 e 08) | `achievable-maturity.md` | Explícito |
| — | — | Segmentação e isolamento da arquitetura | `achievable-maturity.md` | Explícito |

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
- **§26 label rule:** deterministic per `confidence` field (≥0.85 Explícito; ≥0.65 Semântico; ≥0.4 Parcial; <0.4 Gap)
- **§26 §4 discipline applied:** SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity
- **Generated by:** Manual Agent Run 2 (achievable-maturity enrichment)
- **Cycle:** Cycle B Run 2 — last content work pre frozen ceremony
