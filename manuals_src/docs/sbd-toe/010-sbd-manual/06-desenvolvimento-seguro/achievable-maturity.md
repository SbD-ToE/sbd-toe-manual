# Achievable Maturity — Desenvolvimento Seguro

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
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:owasp-dsomm-design-development-tooling-metrics:design-dev` | OWASP DSOMM | Design & Development, Tooling, Metrics | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:owasp-dsomm-design-development-tooling-metrics:metrics` | OWASP DSOMM | Design & Development, Tooling, Metrics | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:owasp-dsomm-design-development-tooling-metrics:tooling` | OWASP DSOMM | Design & Development, Tooling, Metrics | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Práticas estruturadas, validações automáticas, evidência e o | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:owasp-samm-implementation:1` | OWASP SAMM | Implementation | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:owasp-samm-implementation:2` | OWASP SAMM | Implementation | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:owasp-samm-implementation:3` | OWASP SAMM | Implementation | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Linters, validação automática, rastreabilidade, PR validatio | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:slsa-build-validation-provenance:1` | SLSA | Build Validation & Provenance | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:slsa-build-validation-provenance:2` | SLSA | Build Validation & Provenance | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:slsa-build-validation-provenance:34` | SLSA | Build Validation & Provenance | external | derived |
| MaturityMapping | `06-desenvolvimento-seguro:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Integração de validações e proveniência no build | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Design & Development, Tooling, Metrics | Práticas estruturadas de desenvolvimento seguro | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Design & Development, Tooling, Metrics | Rastreabilidade, evidência, ownership e tratamento de exceções | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Design & Development, Tooling, Metrics | Linters, validações automáticas integráveis | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Práticas estruturadas, validações automáticas, evidência e ownership | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Implementation | Práticas básicas de verificação manual | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Implementation | Integração de validações automatizadas no pipeline | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Implementation | Integração contínua e testes estruturados | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Linters, validação automática, rastreabilidade, PR validation | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build Validation & Provenance | — | Linters e PR validation | `achievable-maturity.md` | Explícito |
| Build Validation & Provenance | — | Tracking de alterações e ownership | `achievable-maturity.md` | Explícito |
| Build Validation & Provenance | — | Fora do âmbito deste capítulo | `achievable-maturity.md` | Explícito |
| — | — | Integração de validações e proveniência no build | `achievable-maturity.md` | Explícito |

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
