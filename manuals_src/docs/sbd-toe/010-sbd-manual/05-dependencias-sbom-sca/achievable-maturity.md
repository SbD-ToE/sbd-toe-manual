# Achievable Maturity — Dependências, SBOM e SCA

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
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:owasp-dsomm-policy-build-deploy-tooling:build-deploy` | OWASP DSOMM | Policy, Build & Deploy, Tooling | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:owasp-dsomm-policy-build-deploy-tooling:policy` | OWASP DSOMM | Policy, Build & Deploy, Tooling | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:owasp-dsomm-policy-build-deploy-tooling:tooling` | OWASP DSOMM | Policy, Build & Deploy, Tooling | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Políticas de risco, hardening, bloqueios CI/CD, rastreabilid | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:owasp-samm-construction-dependency-management:1` | OWASP SAMM | Construction → Dependency Management | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:owasp-samm-construction-dependency-management:2` | OWASP SAMM | Construction → Dependency Management | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:owasp-samm-construction-dependency-management:3` | OWASP SAMM | Construction → Dependency Management | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | SBOM, políticas de aceitação, exceções, validação e bloqueio | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:slsa-provenance-dependency-control:1` | SLSA | Provenance & Dependency Control | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:slsa-provenance-dependency-control:2` | SLSA | Provenance & Dependency Control | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:slsa-provenance-dependency-control:3` | SLSA | Provenance & Dependency Control | external | derived |
| MaturityMapping | `05-dependencias-sbom-sca:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | SBOM, pinning, proveniência de dependências | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Policy, Build & Deploy, Tooling | Geração e publicação de SBOM com integração na pipeline | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Policy, Build & Deploy, Tooling | Definição formal de critérios de aceitação e exceções | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Policy, Build & Deploy, Tooling | Ferramentas recomendadas para SCA, validação de findings | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Políticas de risco, hardening, bloqueios CI/CD, rastreabilidade SCA | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Construction → Dependency Management | Identificação e listagem manual de dependências | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Construction → Dependency Management | Processo formal de aceitação, rastreio e controlo de risco | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Construction → Dependency Management | Automação e integração contínua | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | SBOM, políticas de aceitação, exceções, validação e bloqueio | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Provenance & Dependency Control | — | SBOM gerado por build | `achievable-maturity.md` | Explícito |
| Provenance & Dependency Control | — | Critérios de controlo formal | `achievable-maturity.md` | Explícito |
| Provenance & Dependency Control | — | Fora do âmbito (ver Cap. 06 e 08) | `achievable-maturity.md` | Explícito |
| — | — | SBOM, pinning, proveniência de dependências | `achievable-maturity.md` | Explícito |

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
