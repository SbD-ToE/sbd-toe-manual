---
# Proveniência da geração: não se mostra ao leitor (extraída do corpo na v1.17.1).
sbdtoe_provenance:
  ontology_v2: 'sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml (meta.version: ''2.0'')'
  kg_state: sbd-toe-knowledge-graph master @ 5550a743bb9de205676c503da5e81863ed62ab54 (2026-05-11; commit de governação imediatamente a seguir à tag kg-v1-cycle-b-iter-3-aligned-2026-05-11 @ 482ece916cc254126894019432ebd113695365d9)
  generated_by: Manual Agent Run 2 (achievable-maturity enrichment)
  cycle: Cycle B Run 2 — last content work pre frozen ceremony
  notes:
  - 'Maturity mappings: data/entities/maturity_mappings.json (168 items)'
  - '§26 methodology layer: 00-fundamentos/canon/26-metodologia-validacao-claims.md (Run 1 state @ a9e70c98937d41587e86712199fab46854a8d6aa)'
  - '§26 label rule: deterministic per confidence field (≥0.85 Explícito; ≥0.65 Semântico; ≥0.4 Parcial; <0.4 Gap)'
  - '§26 §4 discipline applied: SAMM/DSOMM primary; SLSA conditional; regulatory ≠ maturity'
---

# Achievable Maturity — CI/CD Seguro

## Sumário {#sumário}

Postura de maturidade credível atingível se este capítulo for implementado as written. Análise segue **§26 canon §4 discipline**: SAMM v2.1 + DSOMM são fontes primárias; SLSA só onde fizer sentido como progressão de build/integridade; **alinhamento regulatório NÃO é maturity score** e é registado em § Out-of-Maturity scope.

Cinco secções:

- **§ Manual ontology V2 entities** — MaturityMapping + Practice + Control entities relevantes
- **§ SAMM v2 / DSOMM maturity progression** — primary maturity sources per §26 §4
- **§ SLSA build/integrity progression** — onde aplicável a este capítulo
- **§ Out-of-Maturity scope** — regulatory alignment (NÃO maturity score)
- **§ Future-work register** — maturity gaps registered para P8 §10

---

## § Manual ontology V2 — entities relevantes para maturity {#-manual-ontology-v2--entities-relevantes-para-maturity}

Total: **14 MaturityMapping entities** mapped a este capítulo.

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:build` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:operate` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:release` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:owasp-dsomm-build-test-release-operate:test` | OWASP DSOMM | Build, Test, Release, Operate | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Execução segura, validação de artefactos, assinaturas, rastreabilidade | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:owasp-samm-build-deployment-automation:1` | OWASP SAMM | Build & Deployment Automation | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:owasp-samm-build-deployment-automation:2` | OWASP SAMM | Build & Deployment Automation | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:owasp-samm-build-deployment-automation:3` | OWASP SAMM | Build & Deployment Automation | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Segurança integrada no pipeline, segregação de ambientes | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:1` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:2` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:3` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:slsa-provenance-ci-cd-control:4` | SLSA | Provenance & CI/CD Control | external | derived |
| MaturityMapping | `07-cicd-seguro:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Proveniência, trusted builders, controlo de execução, hardening de pipelines | external | derived |

---

## § SAMM v2 / DSOMM maturity progression {#-samm-v2--dsomm-maturity-progression}

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Build, Test, Release, Operate | Execução autenticada, trusted runners, proveniência | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Build, Test, Release, Operate | Logs, auditoria e controlo de fluxo CI/CD | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Build, Test, Release, Operate | Assinatura e integridade do artefacto | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Build, Test, Release, Operate | Validação e rastreabilidade contínua dos resultados | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Execução segura, validação de artefactos, assinaturas, rastreabilidade | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Build & Deployment Automation | Formalização mínima exigida | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Build & Deployment Automation | Execução autenticada e validada | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Build & Deployment Automation | Parcial - depende de controlo externo à pipeline | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Segurança integrada no pipeline, segregação de ambientes | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression {#-slsa-buildintegrity-progression}

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Provenance & CI/CD Control | — | Execução autenticada com logs | `achievable-maturity.md` | Explícito |
| Provenance & CI/CD Control | — | Validação e assinatura de artefactos | `achievable-maturity.md` | Explícito |
| Provenance & CI/CD Control | — | Trusted environments e runners | `achievable-maturity.md` | Explícito |
| Provenance & CI/CD Control | — | Fora do âmbito do capítulo (ver Cap. 08 e 09) | `achievable-maturity.md` | Explícito |
| — | — | Proveniência, trusted builders, controlo de execução, hardening de pipelines | `achievable-maturity.md` | Explícito |

---

## § Out-of-Maturity scope (regulatory alignment NÃO maturity) {#-out-of-maturity-scope-regulatory-alignment-não-maturity}

Per §26 §4 discipline: alinhamento regulatório (PCI DSS, GDPR, NIS2, DORA, CRA, HIPAA) **NÃO deve ser tratado como maturity score**. Items regulatórios são registados aqui para visibility editorial; conformance vive em obrigações separadas, não em maturity progression.

_(Regulatory alignment para este capítulo é tratado via Manual ontology V2 ExternalObligation entities + capítulos de governança (Cap. 14); não enumerado aqui para evitar conflation com maturity claim.)_

---

## § Future-work register (maturity gaps) {#-future-work-register-maturity-gaps}

_(Nenhuma maturity claim em gap state para este capítulo.)_
