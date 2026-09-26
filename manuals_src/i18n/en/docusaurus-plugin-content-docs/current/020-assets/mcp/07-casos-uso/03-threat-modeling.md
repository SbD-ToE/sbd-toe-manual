---
id: threat-modeling
title: Threat modelling
description: Combining get_threat_landscape + consult_security_requirements by concern to produce grounded threat models.
sidebar_label: Threat modelling
sidebar_position: 3
tags:
  - mcp
  - casos-uso
  - threat-modeling
  - STRIDE
translation:
  source_locale: pt
  source_path: 020-assets/mcp/07-casos-uso/03-threat-modeling.md
  source_sha256: cb19c759eafa0dd75075fae1afc7e94fcb83e52fe19b435a18e18d89bf8d7584
  source_commit: 4e04c6c26f9325b8a3515d4ccd3b126f58be3b1e
  target_sha256: c41f6ec369abca1bfd8f0a608464ee2418c2ece4c29cdc945624f18f63ba77f9
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 211df96a27d713b5934d7534d61f1972d877902236e63b858563d206c67ccaa8
  glossary_keys: [chapter_role, discipline, mcp, practitioner_manual, threat, validation_evaluation]
  glossary_sha256: 9295ee4b6fd79121b8c65819b7ad448c6bf8cd7abab799066587082d7b652a05
  translated_at: 2026-09-26T14:55:18Z
  reviewed_by: null
---

# Use case — Threat modelling

*Threat modelling* has a predictable failure in fast-paced environments — either it is done too early (and is out of date by the time the code arrives), or it is done too late (and turns into compliance theatre). The MCP helps to do it at a useful moment: the agent extracts from the manual the *threats* already catalogued for the project's *risk level* and the system's *concerns*, and anchors them in the controls that mitigate them — with IDs.

The example here is a public user-management API (create account, authenticate, recover password). In two calls to the server, the agent gathers the material for a defensible *threat model*, with confidence explicitly marked (`derived` vs `heuristic`) whenever the link between *threat* and control is inferred rather than structural.

## Prior requirements {#pré-requisitos}

- MCP installed, skill loaded.
- Project *risk level* — `L2` in the example (public API, user data).

## Flow {#fluxo}

### 1. Identify the system's *concerns* {#1-identificar-concerns-do-sistema}

From the prose description, map to the ontological vocabulary:

| System aspect | Concern |
|---|---|
| Login / authentication | `auth` |
| Public REST endpoints | `api` |
| Input validation (email, password strength) | `validation` |
| Password hashing, *tokens* | `encryption` |
| *Audit log* of sensitive operations | `logging` |

→ `concerns = ["auth", "api", "validation", "encryption", "logging"]`

### 2. Threat landscape {#2-threat-landscape}

**Important:** `get_threat_landscape` runs `consult` internally — **do not call `consult_security_requirements` beforehand**.

```json
get_threat_landscape({
  "risk_level": "L2",
  "concerns": ["auth", "api", "validation", "encryption", "logging"]
})
```

**Expected output** (real shape — threats `MT-NNN`; each link cites the `control_id`):

```json
{
  "threats": [
    {
      "id": "MT-055", "name": "Interfaces expostas sem isolamento",
      "chapter_id": "04-arquitetura-segura", "threat_category": "STRIDE",
      "mitigation_confidence": "derived", "mitigation_strength": "parcial",
      "mitigated_by": [
        {"control_id": "CTRL-infrastructure-segmentacao-e-controlo-arquitetural-dceb3c1f0b", "domain": "infrastructure"}
      ]
    }
  ]
}
```

:::info *Concern* routing — `routing_basis`
The response declares, for each *concern*, the basis of the *routing* in `routing_basis`: `domain_chapter` when the *concern* has a threat chapter of its own, `activated_controls` when the threats arrive through the chapters that define the activated controls. Reading `routing_basis` before structuring the *threat model* tells where each threat came from — and, with that, how to present it.
:::

### 3. Practices by *role* (optional, but useful) {#3-práticas-por-role-opcional-mas-útil}

For the *role* that will mitigate (e.g.: `arquitetos-software` in design, `developer` in implement):

```json
get_guide_by_role({"risk_level": "L2", "role": "arquitetos-software", "phase": "design"})
```

→ returns *practice assignments* + *user stories* to use as *acceptance criteria*.

### 4. Structure the threat model {#4-estruturar-o-threat-model}

Recommended model (STRIDE adapted to the output):

```markdown
## Threat Model — <componente>

### Componente em análise
- Surface: <endpoint, módulo, dataflow>
- Risk level: L2
- Concerns: auth, api, validation, encryption, logging

### Data flow (DFD)
<diagrama mermaid ou descrição>

### Threats (manual-grounded)

#### MT-NNN — <título da ameaça do output>
- **Descrição:** <`name` do output do MCP>
- **STRIDE:** <`threat_category`>
- **Mitigated by:** `CTRL-<domain>-<slug>-<hash>` (do `mitigated_by`)
- **Mitigation confidence:** derived · strength parcial ✅
- **Acceptance criteria:** <user stories de get_guide_by_role>

#### MT-NNN — <outra ameaça, ligação fraca>
- **Mitigation confidence:** *fallback* sem ligação estrutural → rotular como **inferido** ⚠️
- **Nota:** validar com revisão humana / testes.

### Threats sem mitigação no manual
- <`MT-*` devolvidos sem `mitigated_by`> — flag para revisão humana

### Resíduo
<o que não foi endereçado>
```

## Output discipline {#disciplina-de-output}

- **`mitigation_confidence: "derived"`** (strength typically `"parcial"`) → structural link. Present it as a reliable link.
- *Fallback* without a structural link → treat as **inferred**; label it explicitly, not as a certainty.
- If `threats: []` → write *"No threats catalogued in the manual for this scope — not to be confused with absence of risk"*. Do not invent.
- Cite `MT-*` and `CTRL-*` IDs exactly as returned.

## Skill / subagent — Cursor {#skill--subagent--cursor}

`.cursorrules`, dedicated section:

```markdown
## Threat modeling com SbD-ToE

Quando for pedido threat model ou análise de ameaças:

1. Identificar concerns aplicáveis a partir do escopo do sistema.
2. Chamar mcp__sbd-toe__get_threat_landscape(risk_level, concerns).
3. Chamar mcp__sbd-toe__get_guide_by_role(risk_level, role, phase) para acceptance criteria.
4. Estruturar relatório STRIDE-adaptado citando MT-* e CTRL-* exactos.
5. Rotular mitigation_confidence (derived/parcial); ligação fraca → inferido.
6. Não inventar threats nem ligações. Threats vazios → flag para revisão humana.
```

## Anti-patterns {#anti-patterns}

- ❌ Calling `consult_security_requirements` **before** `get_threat_landscape` — unnecessary duplication; the *tool* already runs `consult` internally.
- ❌ Presenting an inferred link (without `mitigation_confidence: "derived"`) as a certainty.
- ❌ Inventing `MT-CUSTOM-001` to fit a threat that is known but not in the output — write it in a separate section as an *observed threat* and mark it `not verified` in the manual.
- ❌ Confusing technical `concerns` (`auth`) with STRIDE domains (`Spoofing`).

## Related {#relacionado}

- [Grounded codegen](./codegen-grounded) — after the *threat model*, generate mitigations with IDs.
- [`get_threat_landscape`](../05-tools-reference.md#get_threat_landscape) in the reference.
