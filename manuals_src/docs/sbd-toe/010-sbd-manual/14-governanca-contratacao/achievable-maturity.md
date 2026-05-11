# Achievable Maturity — Governança e Contratação

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
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:3rd-party` | OWASP DSOMM | Validação de fornecedores, requisitos contratuais, rastreabi | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:governance` | OWASP DSOMM | Definição clara de ownership, políticas, controlo contínuo | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:tooling-metrics` | OWASP DSOMM | KPIs de governação e feedback contínuo | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:owasp-dsomm:training` | OWASP DSOMM | Onboarding formal de stakeholders | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Exceções, KPIs, onboarding, validação, maturidade | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:education-guidance` | OWASP SAMM | Governance e Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:governance` | OWASP SAMM | Governance e Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:owasp-samm-governance-e-education:incident-management` | OWASP SAMM | Governance e Education | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Ownership, exceções, rastreabilidade, formação | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:1` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:2` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:3` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:slsa-supply-chain:4` | SLSA | Supply Chain | external | derived |
| MaturityMapping | `14-governanca-contratacao:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Requisitos contratuais, aceitação de risco, rastreabilidade | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | — | Validação de fornecedores, requisitos contratuais, rastreabilidade | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Definição clara de ownership, políticas, controlo contínuo | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | KPIs de governação e feedback contínuo | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Onboarding formal de stakeholders | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Exceções, KPIs, onboarding, validação, maturidade | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Governance e Education | — | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Governance e Education | — | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Governance e Education | — | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Ownership, exceções, rastreabilidade, formação | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Supply Chain | — | Papéis e terceiros registados | `achievable-maturity.md` | Explícito |
| Supply Chain | — | Cláusulas de segurança formais | `achievable-maturity.md` | Explícito |
| Supply Chain | — | Parcial - validações sem atestado externo | `achievable-maturity.md` | Explícito |
| Supply Chain | — | Não aplicável | `achievable-maturity.md` | Explícito |
| — | — | Requisitos contratuais, aceitação de risco, rastreabilidade | `achievable-maturity.md` | Explícito |

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
