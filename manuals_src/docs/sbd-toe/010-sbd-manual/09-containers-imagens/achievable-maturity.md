# Achievable Maturity — Containers e Imagens

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

Total: **13 MaturityMapping entities** mapped a este capítulo (via `sbd-toe-knowledge-graph/data/entities/maturity_mappings.json`).

| Entity type | ID | Framework | Framework area | Authority class | Source mode |
|---|---|---|---|---|---|
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:build-deploy` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:ops-monitoring` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:owasp-dsomm-build-deploy-supply-chain-ops-monitoring:supply-chain` | OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Construção determinística, proveniência, hardening e observa | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:1` | OWASP SAMM | Deployment, Verification e Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:2` | OWASP SAMM | Deployment, Verification e Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:owasp-samm-deployment-verification-e-governance:3` | OWASP SAMM | Deployment, Verification e Governance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Build seguro, policy-as-code, assinatura, controlo de regist | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:1` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:2` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:3` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:slsa-v1-0-build-integrity-provenance:4` | SLSA | Build Integrity & Provenance | external | derived |
| MaturityMapping | `09-containers-imagens:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Assinaturas, attestations, pipelines confiáveis e digest pin | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | Pipelines determinísticos, verificação de proveniência e attestation. | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | Observabilidade, deteção de drift e shadow containers. | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Build & Deploy / Supply Chain / Ops Monitoring | Assinatura, rastreabilidade e governação de registos e dependências. | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Construção determinística, proveniência, hardening e observabilidade de runtime | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Deployment, Verification e Governance | Governação mínima de imagens e registos | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Deployment, Verification e Governance | Scanning e assinatura no CI/CD | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Deployment, Verification e Governance | Policy-as-code, admission controllers, rastreabilidade auditável | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Build seguro, policy-as-code, assinatura, controlo de registos e validação de ma | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Build Integrity & Provenance | — | Dockerfiles versionados e CI/CD auditável | `achievable-maturity.md` | Explícito |
| Build Integrity & Provenance | — | Digest pinning e attestation de origem | `achievable-maturity.md` | Explícito |
| Build Integrity & Provenance | — | Assinaturas, attestations e verificação automática | `achievable-maturity.md` | Explícito |
| Build Integrity & Provenance | — | Fora do âmbito (nível de integração infraestrutural) | `achievable-maturity.md` | Explícito |
| — | — | Assinaturas, attestations, pipelines confiáveis e digest pinning | `achievable-maturity.md` | Explícito |

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
