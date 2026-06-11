# FREEZE REGISTRY - SbD-ToE-Manual

**Repository:** `SbD-ToE-Manual` - `git@github.com:SbD-ToE/sbd-toe-manual.git`
**Part of programme:** SbD-ToE / AppSec Core (P0 DOI 10.17605/OSF.IO/7T849)
**Governed by:** `PROGRAMME-PRESERVATION-PROTOCOL.md` v1.0
**Last updated:** 2026-06-11

**Role in programme:** authoritative SbD-ToE Manual content; primary substrate for Knowledge Graph generation, Curator paper authoring, and canonical evidence base.

---

## Published states

Public release tags under `PROGRAMME-PRESERVATION-PROTOCOL.md` v1.0:

| Tag | Date | Description |
|---|---|---|
| `v1.3.0` | 2026-05-25 | AI Act cross-check (Reg. (UE) 2024/1689) added under `002-cross-check-normativo/ai-act/` - article-by-article analysis, implementation playbook, and AI Act / CRA convergence note. Docusaurus upgraded 3.9.2 -> 3.10.1; transitive dependency hardening (npm audit 46 -> 18). Authorized by programme lead; shipped via PR #43; additive only, canon chapters 01-14 untouched. |
| `v1.4.0` | 2026-05-29 | MCP server mini-site added under `020-assets/mcp/` - 12 pages covering install per client, skills/agents configuration, tools reference, resources & prompts, six use-case recipes (PR audit, grounded codegen, threat modeling, governance bootstrap, role-based onboarding, normative cross-check), advanced patterns, epistemic discipline, troubleshooting/FAQ and versioning/roadmap. Adds reusable `UseCaseCard` / `UseCaseGrid` components and sidebar + footer integration. Content grounded in canonical MCP sources (`sbd://toe/agent-guide`, `sbd://toe/grounded-codegen-guide`); KG coverage verified directly via `inspect_sbd_toe_retrieval`. Authorized by programme lead; shipped via PR #44; additive only, canon chapters 01-14 untouched. |
| `v1.5.0` | 2026-06-01 | Comprehensive agentic SDLC coverage — A0-A4 autonomy model, REQ-AGN-001..004 (Cap 02), threat modeling agentic playbook with MITRE ATLAS (Cap 03), ARC-015 agent-as-principal + Cap 04 patterns, US-14 AI BOM with DEP-011..014 (Cap 05), prompts-as-code + structured outputs (Cap 06), US-19 agents as pipeline principals (Cap 07), self-hosted inference runtime addon (Cap 09), C5 eval suites (Cap 10), US-18 release gates with model rollback + canary (Cap 11), US-13 telemetry + OPS-011..014 (Cap 12), US-21 AI provider contracting (Cap 14), composed AI Reliability Engineer note (Cap 00). RAG patterns added to Cap 04. AI Act cross-check refreshed with 3 new sections (Art 4, 25, 26) and Art 14 reframe. New Policies 38 (mandates-agentes) and 39 (ai-bom-supply-chain); Policies 10, 11, 15, 16, 18, 19, 30, 33, 37 extended. Cross-check exemplar + MCP use case for end-to-end agentic SDLC. Editorial pass: H1/title emoji strip + 206 internal navigation links + depersonalized prose. Grounded in NIST AI RMF 1.0, ISO/IEC 42001, NIST SP 800-207, MITRE ATLAS, OWASP LLM Top 10 (2025), CycloneDX 1.6 ml-bom, AI Act + NIS2 + DORA + CRA + RGPD. Authorized by programme lead; shipped via PR #45 (17 commits); additive only, canon chapters 01-14 retained with extensions, 13 canonical roles untouched. |
| `v1.6.0` | 2026-06-11 | **Balde B — enriquecimento editorial.** 5 frameworks integrados como **método/referência ancorada** (não autoridade family-blind, AGENTS.md §3): EPSS + CISA KEV como camada de priorização sobre os SLAs CVSS (Cap 12); MITRE ATT&CK como vocabulário de detection engineering com cobertura threat-informed (Cap 12); método OWASP de abuse/misuse cases (Cap 03, xref backlog Cap 02); metodologia LINDDUN de threat modeling de privacidade (Cap 03); 7 fases PTES de profundidade de pentest (Cap 10). Inclui norma de voz editorial `guia-voz.md` + wiring de descoberta (CONTRIB, copilot-instructions, CODEOWNERS). Taxonomias LINDDUN/ATT&CK/PTES verificadas na fonte; `make web` limpo (0 broken-link warnings nos ficheiros novos). Autorizado por programme lead; sob dispatcher do Orchestrator `2026-06-11-orchestrator-manual-agent-balde-b-editorial-enrichment`; **additive only**, canon 01-14 intocado, wave-notes preservadas. WSTG/SLSA fora de scope (lane do Cartographer). Merge `--no-ff` `0edfa2af`; commits `7edbc1d2`, `b06e741f`, `1502033b`. |
| `v1.6.1` | 2026-06-11 | **Correção editorial cross-check.** Re-authoria do trabalho editorial de abril recuperado (flag Codex `2026-06-11-codex-flag-manual-uncommitted-april-edits`): delimitação (*bounded*) dos claims de conformidade DORA/NIS2/CRA e correção das citações de artigos DORA — testes de resiliência **Art. 24-27** (não 19-20), incidentes **17-23**, terceiros **28-30**, partilha de ameaças **Art. 45** (não 16) — verificadas contra o Regulamento (UE) 2022/2554 (EUR-Lex). NIS2: accountability do órgão de gestão. CRA: fronteiras de conformidade + datas verificadas (Art. 14 a partir de 11-set-2026; aplicação geral 11-dez-2027). `faq.md` reaponta link inbound para a âncora DORA renomeada. Apenas Cluster B recuperado; Cluster A (4× achievable-maturity) excluído (regenerado/machine-facing). `make web` limpo (0 broken links/anchors novos). Autorizado por programme lead; correção aditiva, canon 01-14 intocado. Commit `b1788989`; merge `--no-ff` `76672144`. |

Manual content also has historical release tags that predate the protocol. They are retained under "Pre-protocol tags" for continuity.

---

## Frozen states

None yet at this repository granularity under `PROGRAMME-PRESERVATION-PROTOCOL.md` v1.0.

---

## Pre-protocol tags

These tags predate `PROGRAMME-PRESERVATION-PROTOCOL.md` v1.0 (2026-04-17). Per protocol §10.3, states tagged under earlier conventions remain valid and recoverable.

| Tag | Description |
|---|---|
| `0.2.3` | Pre-protocol release |
| `initial-preview` | Initial preview state |
| `manual-pre-round-1` | Manual baseline pre-Round-1 (P2-v2 reference) |
| `only_chap1_reviewed` | Early review state |
| `post_all_chapters_rescope` | Post-rescope state |
| `pre-release-beta` | Pre-release beta |
| `pre-us-review` | Pre US review |
| `release/2026-04-06` | Release 2026-04-06 |
| `v0.1.1` | Sequential version tag |
| `v0.1.2` | Sequential version tag |
| `v0.1.3` | Sequential version tag |
| `v0.1.4` | Sequential version tag |
| `v0.1.5` | Sequential version tag |
| `v0.1.6` | Sequential version tag |
| `v0.1.7` | Sequential version tag |
| `v0.2.0` | Sequential version tag |
| `v0.2.1` | Sequential version tag |
| `v0.2.2` | Sequential version tag |
| `v0.2.3` | Sequential version tag |
| `v0.2.4` | Sequential version tag |
| `v0.2.5` | Sequential version tag |
| `v0.2.6` | Sequential version tag |
| `v0.2.7` | Sequential version tag |
| `v0.2.8` | Sequential version tag |

---

## Lab Track B Wave-Notes Injection

Lab Cartographer-Mapping-Lab Track B closed on 2026-04-25 and shipped wave-note constraints into the Manual branch `phase-c-methodology-revision`.

Known Phase C wave-note freeze commits on this branch:

| Commit | Description |
|---|---|
| `c273cf0e` | Clarify bounded Wave 1 ACO-SPC translation surfaces |
| `b77080e8` | Clarify bounded Wave 2 ACO-IAT translation surfaces |
| `8762f223` | Clarify bounded Wave 2 ACO-ITS translation surfaces |
| `dfcd98b1` | Clarify bounded Wave 2 ACO-IVF translation surfaces |
| `30f99b87` | Freeze Wave 3 ACO-RPR upstream execution |
| `68b58cf1` | Freeze Wave 3 ACO-ATB upstream execution |
| `7d559d71` | Freeze Wave 3 ACO-SLG upstream execution |
| `4e3ced4f` | Freeze Wave 3 ACO-TSV upstream execution |
| `2828e8c1` | Freeze Wave 4 ACO-SCBI upstream execution |

These wave-notes are contractual constraints for subsequent Manual agent edits. They must not be modified except by explicit programme-lead authorization.

---

## Protected tags

Per `PROGRAMME-PRESERVATION-PROTOCOL.md` §3.2 and §10.3 backward compatibility, all tags listed under "Pre-protocol tags" are permanently immutable.

Bundle F internal milestone tags are also immutable once created:

- `p7-v2-bundle-f-canon-substitution-shipped`

---

## Current working state

**Current branch:** `phase-c-methodology-revision`
**Most recent state before Step 1:** Manual canon files at chapters `04`, `06`, `12`, and `14` include Lab Track B wave-notes and Pedro's two preserved UPDATE commits:

- `67a1a272` - SP800-53-SI-8 in chapter `12-monitorizacao-operacoes`
- `f2efe7aa` - CIS-13.5 in chapter `04-arquitetura-segura`

**Expected next freeze event:** P2-v2 Phase C complete close (`p2v2-phase-c-complete` tag) after Manual agent waves complete and Round 2 DSR close is documented.

---

## Phase C Step 1 Ship Records

Phase C Step 1 was authorized by Orchestrator dispatcher `2026-04-26-orchestrator-manual-agent-phase-c-step-1-governance-plus-revert.md` under programme-lead authority dated 2026-04-26.

| Commit | Bundle | Description |
|---|---|---|
| `d1f694f8` | Bundle A - governance scaffolding | Authored `AGENTS.md`, authored this `FREEZE-REGISTRY.md`, tracked `PROGRAMME-PRESERVATION-PROTOCOL.md`, and ignored local `resume` pointer |
| `fd8577f0` | Bundle B - REVERT cleanup | Removed 21 canon entries classified `REVERT` by v3.2 measure-sync; wave-notes and Pedro's two UPDATE commits preserved |

---

## Bundle F Canon Substitution Ship Record

Bundle F was authorized by Orchestrator dispatcher `2026-04-28-orchestrator-manual-agent-bundle-f-canon-substitution.md` under programme-lead Gate E approval dated 2026-04-28.

| Field | Value |
|---|---|
| Upstream staging tag | `p7-v2-bundle-e-canon-generator-v4-2-shipped` |
| Upstream staging commit | `3d0424ed` |
| Manual substitution commit | `a23c1dbb` |
| Ship tag | `p7-v2-bundle-f-canon-substitution-shipped` |
| Scope | 15 × `manuals_src/docs/sbd-toe/010-sbd-manual/<chapter>/canon/25-rastreabilidade.md` substituted from Bundle E v4.2 staging |
| Verification | 15/15 byte-equivalent to staging; 37 wave-notes preserved as `<!-- WAVE-NOTE: ... -->`; all other `manuals_src` files preserved |

---

## Cross-references

This repository is referenced by:

- **Paper P2-v2** (in preparation; corpus DSR cycle empirical demonstration)
- **Paper P7 v2** (in preparation; corrected pipeline outputs feed P7 §10 substrate via v3.2 supplier)
- **Paper P4/P5** downstream surfaces after Manual plus Knowledge Graph freeze

This repository depends on:

- `ExternalSourcesInventory` v3.2 supplier, post P7 v2 corrected pipeline merge to main on 2026-04-26 at commit `ae5d329`
- `ExternalSourcesInventory` measure-sync output at commit `106ac6b`
- `sbd-toe-ontology` AppSec Core v1 ontology (`ontology-v1-release` at `0b44ac9`)
- `Cartographer-Mapping-Lab` Track A and Track B frozen references

---

## Change log for this registry

| Date | Change | Author |
|---|---|---|
| 2026-04-26 | `FREEZE-REGISTRY.md` created at root per Programme Preservation Protocol §5; 24 pre-protocol tags inventoried; Lab Track B wave-note commit chain documented | Manual agent under Orchestrator dispatcher |
| 2026-04-26 | Phase C Step 1 Bundle A and Bundle B commits recorded in registry | Manual agent under Orchestrator dispatcher |
| 2026-04-28 | Bundle F canon substitution milestone recorded; protected tag `p7-v2-bundle-f-canon-substitution-shipped` declared | Manual agent under Orchestrator dispatcher |
| 2026-05-25 | Public release `v1.3.0` recorded: AI Act cross-check section (analysis + playbook + CRA convergence), Docusaurus 3.10.1 upgrade, dependency hardening; shipped via PR #43 (commits `bbdae891`, `5cc6ceb6`, `5cc547bc`) | Manual agent under programme-lead authorization (Pedro Farinha) |
| 2026-05-29 | Public release `v1.4.0` recorded: MCP server mini-site under `020-assets/mcp/` (12 pages + 6 use cases + 2 React components), sidebar + footer integration; shipped via PR #44 (commits `ca05f0ed`, `facc3ef4`, `2f83b83d`) | Manual agent under programme-lead authorization (Pedro Farinha) |
| 2026-06-01 | Public release `v1.5.0` recorded: comprehensive agentic SDLC coverage across Cap 00-14 + 2 new policies (38, 39) + 9 policies extended + AI Act cross-check refresh + end-to-end agentic SDLC overview (cross-check exemplar + MCP use case) + RAG patterns + self-hosted inference runtime + editorial pass (emoji strip, navigation links, depersonalized prose); shipped via PR #45 (17 commits, head `6a60a82d`) | Manual agent under programme-lead authorization (Pedro Farinha) |
| 2026-06-11 | Public release `v1.6.0` recorded: Balde B editorial enrichment — 5 frameworks como referência ancorada (EPSS/KEV + ATT&CK Cap 12; abuse/misuse cases + LINDDUN Cap 03; PTES Cap 10) + norma de voz editorial `guia-voz.md` + wiring; additive only, canon 01-14 intocado, wave-notes preservadas; `make web` verde; merge `--no-ff` `0edfa2af` de `balde-b-editorial-enrichment` (commits `7edbc1d2`, `b06e741f`, `1502033b`) | Manual agent under programme-lead authorization (Pedro Farinha) |
| 2026-06-11 | Public release `v1.6.1` recorded: correção editorial cross-check — claims DORA/NIS2/CRA delimitados + citações de artigos DORA corrigidas (testes 24-27, incidentes 17-23, terceiros 28-30, partilha Art. 45) vs Reg. (UE) 2022/2554; CRA datas verificadas; re-authorado do flag Codex de trabalho de abril; Cluster A (achievable-maturity) excluído; `faq.md` reapontado; `make web` verde; merge `--no-ff` `76672144` (commit `b1788989`) | Manual agent under programme-lead authorization (Pedro Farinha) |
