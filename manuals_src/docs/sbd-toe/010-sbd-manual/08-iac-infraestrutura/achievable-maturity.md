# Achievable Maturity — IaC e Infraestrutura

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
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:owasp-dsomm-aplicacao-a-projetos-iac:build-test` | OWASP DSOMM | Aplicação a Projetos IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:owasp-dsomm-aplicacao-a-projetos-iac:design-dev` | OWASP DSOMM | Aplicação a Projetos IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:owasp-dsomm-aplicacao-a-projetos-iac:tooling` | OWASP DSOMM | Aplicação a Projetos IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-dsomm:visao-geral-de-alinhamento:owasp-dsomm` | OWASP DSOMM | Validação, segregação de ambientes, controlo de estado | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:owasp-samm-secure-build-para-iac:1` | OWASP SAMM | Secure Build para IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:owasp-samm-secure-build-para-iac:2` | OWASP SAMM | Secure Build para IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:owasp-samm-secure-build-para-iac:3` | OWASP SAMM | Secure Build para IaC | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:owasp-samm:visao-geral-de-alinhamento:owasp-samm-v2-1` | OWASP SAMM | Controlo de pipelines IaC, linting, enforcement | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:1` | SLSA | Fonte, Build e Proveniência | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:2` | SLSA | Fonte, Build e Proveniência | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:3` | SLSA | Fonte, Build e Proveniência | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:slsa-fonte-build-e-proveniencia:4` | SLSA | Fonte, Build e Proveniência | external | derived |
| MaturityMapping | `08-iac-infraestrutura:maturity:slsa:visao-geral-de-alinhamento:slsa-v1-0` | SLSA | Validação de planos, proveniência, segregação, controlo de b | external | derived |

---

## § SAMM v2 / DSOMM maturity progression

Maturity progression per SAMM v2.1 + DSOMM (primary frameworks per §26 §4). §26 methodology label deterministic per `confidence` field do KG canonical mapping.

| Framework | Framework area | Coverage summary | Manual section anchor | Confidence | §26 label |
|---|---|---|---|---|---|
| OWASP DSOMM | Aplicação a Projetos IaC | Linting, validação de planos, pipelines de teste | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Aplicação a Projetos IaC | Requisitos IaC, separação de ambientes, arquitetura segura | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | Aplicação a Projetos IaC | Ferramentas de análise estática e validação automatizada | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP DSOMM | — | Validação, segregação de ambientes, controlo de estado | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Secure Build para IaC | Configuração manual, sem rastreabilidade | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Secure Build para IaC | Uso de linters, controlo automatizado e pipelines | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | Secure Build para IaC | Integração contínua com artefactos rastreáveis | `achievable-maturity.md` | 0.90 | Explícito |
| OWASP SAMM | — | Controlo de pipelines IaC, linting, enforcement | `achievable-maturity.md` | 0.90 | Explícito |

---

## § SLSA build/integrity progression

SLSA progression mapping (per §26 §4: SLSA só onde fizer sentido como progressão de build/integridade — este capítulo qualifica).

| SLSA level | Framework area | Coverage summary | Manual section anchor | §26 label |
|---|---|---|---|---|
| Fonte, Build e Proveniência | — | Validadores e aprovação manual formal | `achievable-maturity.md` | Explícito |
| Fonte, Build e Proveniência | — | Controlo de planos e ambientes | `achievable-maturity.md` | Explícito |
| Fonte, Build e Proveniência | — | Fora do âmbito deste capítulo | `achievable-maturity.md` | Explícito |
| Fonte, Build e Proveniência | — | Fora do âmbito deste capítulo | `achievable-maturity.md` | Explícito |
| — | — | Validação de planos, proveniência, segregação, controlo de builds | `achievable-maturity.md` | Explícito |

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
