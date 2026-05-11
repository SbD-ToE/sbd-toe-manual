# Achievable Maturity — Testes de Segurança

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
| MaturityMapping | `10-testes-seguranca:maturity:owasp-dsomm:owasp-dsomm-dominios-testing-design-development:design-development` | OWASP DSOMM | Domínios Testing + Design & Development | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-dsomm:owasp-dsomm-dominios-testing-design-development:testing` | OWASP DSOMM | Domínios Testing + Design & Development | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-dsomm:visao-geral-de-alinhamento:dsomm` | OWASP DSOMM | Integração contínua, rastreabilidade por release, gates auto | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:owasp-samm-verification-security-testing:1` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:owasp-samm-verification-security-testing:2` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:owasp-samm-verification-security-testing:3` | OWASP SAMM | Verification → Security Testing | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:owasp-samm:visao-geral-de-alinhamento:samm-v2-1` | OWASP SAMM | Testes automatizados, gates de validação, gestão de findings | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:1` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:2` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:3` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:slsa-build-test-coverage:4` | SLSA | Build/Test Coverage | external | derived |
| MaturityMapping | `10-testes-seguranca:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Cobertura limitada, validação de artefactos antes de deploy | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Domínios Testing + Design & Development | Validação por release, controlo de findings, reporting técnico | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Domínios Testing + Design & Development | SAST/DAST integrados, fuzzing, feedback, gates | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Integração contínua, rastreabilidade por release, gates automáticos | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Verification → Security Testing | Testes manuais básicos de segurança | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Verification → Security Testing | Integração de testes automatizados no pipeline | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Verification → Security Testing | Gestão ativa de findings e feedback contínuo | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Testes automatizados, gates de validação, gestão de findings | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build/Test Coverage | — | Cobertura mínima via pipelines | `achievable-maturity.md` | Explícito |
| Build/Test Coverage | — | Evidência e análise rastreável | `achievable-maturity.md` | Explícito |
| Build/Test Coverage | — | Parcial - depende de governance | `achievable-maturity.md` | Explícito |
| Build/Test Coverage | — | Não abrangido pelo capítulo | `achievable-maturity.md` | Explícito |
| — | — | Cobertura limitada, validação de artefactos antes de deploy | `achievable-maturity.md` | Explícito |

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
