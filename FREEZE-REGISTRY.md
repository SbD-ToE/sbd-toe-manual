# FREEZE REGISTRY - SbD-ToE-Manual

**Repository:** `SbD-ToE-Manual` - `git@github.com:SbD-ToE/sbd-toe-manual.git`
**Part of programme:** SbD-ToE / AppSec Core (P0 DOI 10.17605/OSF.IO/7T849)
**Governed by:** `PROGRAMME-PRESERVATION-PROTOCOL.md` v1.0
**Last updated:** 2026-05-29

**Role in programme:** authoritative SbD-ToE Manual content; primary substrate for Knowledge Graph generation, Curator paper authoring, and canonical evidence base.

---

## Published states

Public release tags under `PROGRAMME-PRESERVATION-PROTOCOL.md` v1.0:

| Tag | Date | Description |
|---|---|---|
| `v1.3.0` | 2026-05-25 | AI Act cross-check (Reg. (UE) 2024/1689) added under `002-cross-check-normativo/ai-act/` - article-by-article analysis, implementation playbook, and AI Act / CRA convergence note. Docusaurus upgraded 3.9.2 -> 3.10.1; transitive dependency hardening (npm audit 46 -> 18). Authorized by programme lead; shipped via PR #43; additive only, canon chapters 01-14 untouched. |
| `v1.4.0` | 2026-05-29 | MCP server mini-site added under `020-assets/mcp/` - 12 pages covering install per client, skills/agents configuration, tools reference, resources & prompts, six use-case recipes (PR audit, grounded codegen, threat modeling, governance bootstrap, role-based onboarding, normative cross-check), advanced patterns, epistemic discipline, troubleshooting/FAQ and versioning/roadmap. Adds reusable `UseCaseCard` / `UseCaseGrid` components and sidebar + footer integration. Content grounded in canonical MCP sources (`sbd://toe/agent-guide`, `sbd://toe/grounded-codegen-guide`); KG coverage verified directly via `inspect_sbd_toe_retrieval`. Authorized by programme lead; shipped via PR #44; additive only, canon chapters 01-14 untouched. |

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
