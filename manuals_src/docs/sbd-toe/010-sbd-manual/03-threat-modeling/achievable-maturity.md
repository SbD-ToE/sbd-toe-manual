# Achievable Maturity — Threat Modeling

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
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:owasp-dsomm-architecture-risk-analysis-requirements:architecture` | OWASP DSOMM | Architecture, Risk Analysis, Requirements | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:owasp-dsomm-architecture-risk-analysis-requirements:requirements` | OWASP DSOMM | Architecture, Risk Analysis, Requirements | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:owasp-dsomm-architecture-risk-analysis-requirements:risk-analysis` | OWASP DSOMM | Architecture, Risk Analysis, Requirements | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Integração no SDLC, rastreabilidade, threat maps reutilizáve | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:owasp-samm-design-threat-assessment:1` | OWASP SAMM | Design → Threat Assessment | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:owasp-samm-design-threat-assessment:2` | OWASP SAMM | Design → Threat Assessment | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:owasp-samm-design-threat-assessment:3` | OWASP SAMM | Design → Threat Assessment | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Modelação estruturada com STRIDE, DFDs e análise por risco | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:slsa-supply-chain-risk-awareness:1` | SLSA | Supply Chain Risk Awareness | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:slsa-supply-chain-risk-awareness:2` | SLSA | Supply Chain Risk Awareness | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:slsa-supply-chain-risk-awareness:3` | SLSA | Supply Chain Risk Awareness | external | derived |
| MaturityMapping | `03-threat-modeling:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Apoio indireto à definição proporcional de controlos | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Architecture, Risk Analysis, Requirements | Análise de arquitetura e dependências com mapeamento de ameaças | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Architecture, Risk Analysis, Requirements | Geração de requisitos a partir do threat modeling e sua validação | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Architecture, Risk Analysis, Requirements | Integração com classificação e aceitação de risco | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Integração no SDLC, rastreabilidade, threat maps reutilizáveis | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Threat Assessment | Ameaças identificadas de forma sistemática | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Threat Assessment | Análise estruturada com modelos formais e rastreabilidade | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Design → Threat Assessment | Integração contínua e automação organizacional | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Modelação estruturada com STRIDE, DFDs e análise por risco | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Supply Chain Risk Awareness | — | Classificação e threat modeling | `achievable-maturity.md` | Explícito |
| Supply Chain Risk Awareness | — | Fora do âmbito | `achievable-maturity.md` | Explícito |
| Supply Chain Risk Awareness | — | Tratado noutros capítulos (CI/CD) | `achievable-maturity.md` | Explícito |
| — | — | Apoio indireto à definição proporcional de controlos | `achievable-maturity.md` | Explícito |

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
