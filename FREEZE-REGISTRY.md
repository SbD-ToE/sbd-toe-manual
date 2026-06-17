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
| `v1.6.2` | 2026-06-11 | **Patch de cobertura: re-derivação dos checklists + preenchimento de lacunas de US + matriz transversal de verificação + fixes editoriais.** Quatro frentes num só patch (corpo suficiente para release). **(1) Checklists de revisão** — os 14 `canon/20-checklist-revisao.md` (caps 01-14) re-derivados top-down como função do conteúdo de cada capítulo (canon+addon+intro), não das US; granularidade consolidada por requisito (~196 → 230 itens); fecha cobertura agêntica/IA (REQ-AGN, ARC-014/015, DEP-011..014, IAC-011/012/013, self-hosted inference, OPS-011..014, eval suites/TLPT/IAST, prompts-as-code), divide compostos em binários, corrige defeitos (cap12 `☑`→`☐`, cap14 `draft:true`, refs partidas, headers de âmbito, cap03 `sidebar_position`). **(2) User stories** — ~47 novas US autoradas nos 14 capítulos a preencher lacunas do gap report, cada uma ancorada a uma prescrição existente (canon/addon/intro), numeração contígua verificada, links verificados contra `id:` reais; maior densidade: cap09 inferência AI self-hosted, cap13 formação uso seguro de IA + sandbox, cap06 prompts-as-code/structured outputs, cap12 SOAR/kill-switch/EPSS-KEV. **(3) Matriz transversal de verificação** — nova página `10-testes-seguranca/addon/17-matriz-verificacao-transversal.md` (42 linhas): índice único de toda a verificação de segurança (atividade × tipo × oráculo × capítulo × L1/L2/L3 × grounding), distinguindo teste (oráculo comportamental) de análise/scanning (lookup/policy), validação funcional, revisão e deteção runtime; cobre 10 capítulos + verificação AI/agentic. **(4) Fixes editoriais** — cap10 `addon/13` refs US-21/22→US-12/13; cap13 cadência de formação reconciliada a `TRN-005` (L1 anual/L2 semestral/L3 trimestral); cap10 item de fronteira/roll-up + nota teste-vs-análise. **(5) Extensões de canon** — promovidas a requisito as prescrições que só viviam em US (autorizado pelo programme lead; Cartographer assenta a partir da prosa): cap11 `DPL-010` (release gates de sistemas agentic) + `DPL-011` (canary de modelo + demoção de autonomia) → grounding da US-18; cap14 `GOV-013` (onboarding técnico + formação pré-acesso de terceiros) + `GOV-014` (revisão periódica de acesso, least privilege) → grounding das US-15/16/19; US ligadas a citar o código, checklists `canon/20` cap11/cap14 atualizados, matriz +2 linhas. `make web` limpo (0 broken links/anchors novos; baseline pré-existente de 4 inalterado). Encaminhado: cap03 `canon/50` refs stale → Cartographer (substrato gerado); cap11 US-14/15 colocação → nota; KG regen → Codex pós-push. Gap report e plano em `.work-drafts/checklists-v1.6.2-gap-report.md`. `canon/25-rastreabilidade` e wave-notes intocados. Autorizado por programme lead. Checklists: merge `--no-ff` `02b90395` (commits `2d54b799`, `f9c95e13`). US+matriz+editorial: commits `5e87e8fd`, `4aa9d70a`, `b0af50ca`, `d69f3164`, `c4921436`, `33ac4aaa`, `38af279f`. Extensões canon (Bucket B): commit `c40947cd`. Governance: `1e7c1d75`. |
| `v1.6.3` | 2026-06-12 | **Canonicalização dos roles no mini-site MCP.** As duas listas "Roles canónicos" do mini-site (`020-assets/mcp/01-intro.md`, `04-skills-agentes.md`) eram um despejo de 18 tokens que misturava os 13 role_ids canónicos com aliases e tokens não-canónicos (`pentester`, `ir`, `team_lead`, `software_architect`, …) apresentados como canónicos — fonte de confusão no KG/MCP. Substituídas pelos **13 papéis canónicos reais** (= `00-fundamentos/roles-responsabilidades`), com nota de que o servidor aceita aliases e os resolve para estes 13. Contagens "18→13" corrigidas (`05-tools-reference`, `06-resources-prompts`, `07-casos-uso/05-onboarding-formacao`); exemplos com ids não-canónicos canonicalizados em 10 ficheiros (`software_architect`→`arquitetos-software`, `appsec`→`appsec-engineer`, etc.). `make web` limpo (0 broken links/anchors novos; baseline de 4 inalterado). **Encaminhado ao Codex (lane do KG):** o alias-map do runtime bundle colapsa roles canónicos distintos (`software_architect`/`scrum_master`/`team_lead`→`developer`; `product_owner`→`qa`; `ops`→`devops-sre`) e a descrição da tool `get_guide_by_role` está stale (`appsec`→`security-champion`, contradiz os dados) — handover `2026-06-12-manual-agent-mcp-role-alias-conflation-to-codex.md`; a correção do mini-site encaminha os utilizadores para os ids canónicos mas não corrige a resolução no servidor. Autorizado por programme lead; aditivo, canon 01-14 intocado. Commit `2397fdc6`. |
| `v1.6.4` | 2026-06-12 | **Ancoragem de papéis: taxonomia fechada sob os 13 roles canónicos.** Correção da drift nas atribuições de papel das User Stories e tabelas dos 14 capítulos + fundamentos (~450 edições, 34 ficheiros), na sequência da diretriz do programme lead ("os roles têm de estar todos ancorados nos canónicos; se as US usam sinónimos, devem ser corrigidos"). Sinónimos → display name canónico, em **slots, personas "Como X" e tabelas de papéis**: Tech/Dev/Team Lead → Scrum Master / Team Lead; PenTester/AppSec Lead/Manager → AppSec Engineer; Plataforma/Infraestrutura/DevOps Lead/Engineer/DevSecOps → DevOps / SRE; Test Engineer → QA; Gestão de Produto/BA → Product Owner; SOC/IR → Operações (Ops); GRC Analyst → GRC / Compliance; CTO → Gestão Executiva. Atores externos (RH, Procurement, Jurídico, DPO, Training Manager) **ancorados a um role canónico com a função em parênteses** (`Security Champion (RH)`, `GRC / Compliance (Procurement)`) — decisão de não os tratar como 14.º role. Shortforms (AppSec, DevOps, GRC) aceites como **equivalentes canónicas** (resolvem para o role canónico; prosa não slug-ificada por norma de voz). Atores automatizados (pipeline, runner) e placeholder "Owner" ficam fora da taxonomia. Resolve a confusão a montante no KG/MCP (o gerador colapsava roles distintos: software_architect→developer, product_owner→qa, ops→devops-sre). `make web` limpo (0 broken links/anchors novos; baseline de 4 inalterado). Spec de normalização autoritativa + correção do alias-map encaminhadas ao Codex (handovers `2026-06-12-manual-agent-mcp-role-alias-conflation` e `…-role-normalization-spec`). Autorizado por programme lead; aditivo, canon 01-14 intocado. Commit `4a1e70e8`. |
| `v1.6.5` | 2026-06-15 | **Passe editorial ao mini-site MCP (voz, links, tese).** Três frentes editoriais, todas no `020-assets/mcp/` e em fundamentos/roles; **zero canon 01-14 tocado**. **(1) Voz** — mini-site convertido para 3ª pessoa impessoal conforme `guia-voz.md` §2: eliminadas ~14 ocorrências reais de 2ª pessoa (tu/vocês) e imperativos dirigidos ao leitor em 8 ficheiros (`02-quickstart`, `04-skills-agentes`, `08-padroes-avancados`, `07-casos-uso/{01,05,06,index}`, `09-epistemica-anti-patterns`); imperativos dentro de blocos de skill/agent (prompts para a máquina) mantidos. **(2) Links** — 4 links partidos + 1 âncora corrigidos: `arquitetura/intro` ARC-014 → slug `catalogo-requisitos-arquitetura`; `formacao/90-indicadores` → `11-kpis-metricas.md` (91 inexistente); `threat-modeling/metodologias` rastreabilidade + Cap.5 com extensão `.md` (file-link resolvível vs URL-path com prefixo); `roles/arquitetos-software` âncora `us-14`→`us-15` (heading real). **(3) Tese** — reformulada a tese de abertura do `01-intro.md` e o seu seguimento para o eixo *priors/training-time vs grounding no momento da escrita, com IDs citáveis* (sem novos claims). `make web` verde nas três (0 broken links/anchors novos; baseline pré-existente de 4 inalterado). Autorizado por programme lead; aditivo, canon 01-14 intocado. Commits `7b2a1a72` (voz), `70422de9` (links), `98104872` (tese). |
| `v1.6.6` | 2026-06-18 | **Refresh do mini-site MCP para `@shiftleftpt/sbd-toe-mcp@0.10.0`.** Sob dispatch do Orchestrator (`2026-06-17-orchestrator-manual-mcp-minisite-refresh`); programme-lead autorizou avançar com a superfície 0.10.0 (dev-build estável, tag formal a cargo do Codex); diff doc↔servidor revisto e aprovado pelo Orchestrator antes da autoria. **Verify-live** contra o servidor 0.10.0 (resource `sbd://toe/version` + uma chamada a cada tool; zero ids inventados). **(A) Erros factuais** (mesmo para 0.9.0): `query("CTRL-06")→cap.06` é erro de categoria (não é id; *fallback* semântico) → reescrito com `AUT-001` (`match:exact_id`); ids fictícios `CTRL-04-1`/`THR-…`/`REQ-…` → formatos reais (`CTRL-<domain>-<slug>-<hash>`, `MT-NNN`, `<CAT>-NNN`); `mitigation_confidence:"heuristic"` → real `derived`/strength `parcial`; `rule_trace` real (`REQUIREMENT_APPLIES_BY_RISK(L2)`, não `L2_RULESET_LOADED`); enum **fechado** de `concerns` (12) documentado (`monitoring`→`logging`, `supply-chain`→`distribution`); limitação de *routing* do `get_threat_landscape` (concerns base→cap.02 meta-ameaças). Corrigido em `05-tools-reference` + recorrências em `01-intro` (convenções de id), `08-padroes` (Padrões 2/6), `07-casos-uso/{01,03,06,07}`, `09-epistemica`. **(B)** `generate_sbd_toe_skill` reescrito (`role`/`format`/`flavour` + `meta.coverage` declarada) em `05`, `04-skills`, `01-intro`. **(C)** 7 tools novas documentadas (`get_sbd_toe_chapter_implementation_checklist`, `get_sbd_toe_operating_model`, `plan_sbd_toe_rollout`, `get_sbd_toe_verification_matrix`, `assess_sbd_toe_implementation`, `map_sbd_toe_regulatory_activation`, `answer_sbd_toe_manual`) com params + output real + quando-usar (nova secção *Implementation view* em `05`; modo IMPL em `01-intro`). **(D)** vista de implementação V5, *two-band* `next` (`08-padroes`), *coverage-preserving* (`09-epistemica`). **(E)** sweep `0.9.0→0.10.0` (regressão Node `20.9.0` corrigida); 8 resources (+`skill/subagent/{role}`) e `version` com *provenance* em `06-resources`; roadmap atualizado (Entregue 0.10.0 / state-layer Premium no futuro); **content-lag do AI Act reescrito**: o verify-live revelou que o framing antigo ("0.10.0 publicada antes de v1.3.0") estava errado — o *snapshot* é manual `v1.6.4` (posterior), por isso a lacuna é de **indexação KG** do bundle `ai-act/`, não de versão (corrigido em `10-faq` e `11-roadmap`). Achados encaminhados (não-bloqueantes): `assess_implementation` sem paginação (76k chars); AI Act ainda não indexado; `operating_model` ainda serve de `bundle=exemplo-playbook`. **Nota de gate:** o texto descreve `0.10.0` mas o npm `@latest` ainda é `0.9.0` (dev-build) — o *release* público do mini-site pressupõe o *publish* npm real (lane do Pontifex). 14 ficheiros; `make web` verde, 0 broken links/anchors; aditivo, canon 01-14 intocado. Diff de verificação em `.work-drafts/mcp-minisite-0.10.0-diff.md`. Commit `48785cef`. |

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
| 2026-06-11 | Release `v1.6.2` recorded: re-derivação dos 14 `canon/20-checklist-revisao.md` top-down (consolidado por requisito; cobertura agêntica fechada; disciplina binária; defeitos estruturais corrigidos); ~196→230 itens; `make web` verde; merge `--no-ff` `02b90395` de `editorial-checklists-v1.6.2` (commits `2d54b799`, `f9c95e13`) | Manual agent under programme-lead authorization (Pedro Farinha) |
