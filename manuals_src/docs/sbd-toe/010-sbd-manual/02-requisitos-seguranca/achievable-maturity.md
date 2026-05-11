# Achievable Maturity — Requisitos de Segurança

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
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:architecture` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:requirements` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:owasp-dsomm-requirements-architecture-verification:verification` | OWASP DSOMM | Requirements, Architecture, Verification | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Catálogo validado, derivação por risco, critérios de aceitaç | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:1` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:2` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:owasp-samm-design-security-requirements:3` | OWASP SAMM | Design → Security Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Requisitos proporcionais, rastreáveis, com validação formal | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:1` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:2` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:slsa-build-verification-requirements:3` | SLSA | Build & Verification Requirements | external | derived |
| MaturityMapping | `02-requisitos-seguranca:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Definição de critérios de aceitação com base em requisitos | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Requirements, Architecture, Verification | Mapeamento por risco e dependência com arquitetura | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Requirements, Architecture, Verification | Requisitos testáveis, rastreáveis e validados | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Requirements, Architecture, Verification | Critérios definidos para validação dos requisitos | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Catálogo validado, derivação por risco, critérios de aceitação | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Security Requirements | Definir requisitos de segurança mínimos | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Security Requirements | Requisitos definidos com base em riscos | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Security Requirements | Requisitos ligados a métricas e controlos de eficácia | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Requisitos proporcionais, rastreáveis, com validação formal | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build & Verification Requirements | — | Aplicação explícita de critérios | `achievable-maturity.md` | Explícito |
| Build & Verification Requirements | — | Fora do âmbito | `achievable-maturity.md` | Explícito |
| Build & Verification Requirements | — | Implementado noutros capítulos | `achievable-maturity.md` | Explícito |
| — | — | Definição de critérios de aceitação com base em requisitos | `achievable-maturity.md` | Explícito |

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
