---
id: threat-modeling
title: Threat modeling
description: Combinar get_threat_landscape + consult_security_requirements por concern para gerar threat models grounded.
sidebar_label: Threat modeling
sidebar_position: 3
tags:
  - mcp
  - casos-uso
  - threat-modeling
  - STRIDE
---

# Caso de uso — Threat modeling

O *threat modelling* tem uma falha previsível em ambientes acelerados — ou se faz cedo demais (e fica desactualizado quando o código chega), ou se faz tarde demais (e vira teatro de conformidade). O MCP ajuda a fazê-lo num momento útil: o agente extrai do manual as *threats* já catalogadas para o *risk level* do projecto e os *concerns* do sistema, e ancora-as nos controlos que as mitigam — com IDs.

O exemplo aqui é uma API pública de gestão de utilizadores (criar conta, autenticar, recuperar password). Em duas chamadas ao servidor, o agente reúne o material para um *threat model* defensável, com confiança explicitamente marcada (`derived` vs `heuristic`) sempre que a ligação entre *threat* e controlo é inferida e não estrutural.

## Pré-requisitos

- MCP instalado, skill carregada.
- *Risk level* do projecto — `L2` no exemplo (API pública, dados de utilizador).

## Fluxo

### 1. Identificar *concerns* do sistema

Da descrição em prosa, mapear para o vocabulário ontológico:

| Aspecto do sistema | Concern |
|---|---|
| Login / autenticação | `auth` |
| Endpoints REST públicos | `api` |
| Validação de input (email, password strength) | `validation` |
| Hash de password, *tokens* | `encryption` |
| *Audit log* de operações sensíveis | `logging` |

→ `concerns = ["auth", "api", "validation", "encryption", "logging"]`

### 2. Threat landscape

**Importante:** `get_threat_landscape` corre `consult` internamente — **não chamar `consult_security_requirements` antes**.

```json
get_threat_landscape({
  "risk_level": "L2",
  "concerns": ["auth", "api", "validation", "encryption", "logging"]
})
```

**Output esperado** (forma real — ameaças `MT-NNN`; cada ligação cita o `control_id`):

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

:::warning Routing dos *concerns*
À data desta versão, os *concerns* de **base** (`auth`, `validation`, `api`) roteiam para o **cap. 02** e devolvem meta-ameaças de **processo** (`MT-021..038`), não as ameaças técnicas do domínio. Para ameaças técnicas, incluir um *concern* de **domínio** (ex.: `architecture` → cap. 04, `MT-055..072`) e cruzar com os requisitos de `consult_security_requirements`. *(Verificar o comportamento ao vivo — há fix em curso no servidor.)*
:::

### 3. Práticas por *role* (opcional, mas útil)

Para o *role* que vai mitigar (ex.: `arquitetos-software` no design, `developer` no implement):

```json
get_guide_by_role({"risk_level": "L2", "role": "arquitetos-software", "phase": "design"})
```

→ devolve *practice assignments* + *user stories* a usar como *acceptance criteria*.

### 4. Estruturar o threat model

Modelo recomendado (STRIDE adaptado ao output):

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

## Disciplina de output

- **`mitigation_confidence: "derived"`** (strength tipicamente `"parcial"`) → ligação estrutural. Apresentar como ligação fiável.
- *Fallback* sem ligação estrutural → tratar como **inferido**; rotular explicitamente, não como certeza.
- Se `threats: []` → escrever *"Sem threats catalogados no manual para este escopo — não confundir com ausência de risco"*. Não inventar.
- Citar IDs `MT-*` e `CTRL-*` exactamente como devolvidos.

## Skill / subagent — Cursor

`.cursorrules`, secção dedicada:

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

## Anti-patterns

- ❌ Chamar `consult_security_requirements` **antes** de `get_threat_landscape` — duplicação desnecessária; a *tool* já corre `consult` internamente.
- ❌ Apresentar uma ligação inferida (sem `mitigation_confidence: "derived"`) como certeza.
- ❌ Inventar `MT-CUSTOM-001` para encaixar uma ameaça que conheces mas não está no output — escrever em secção separada como *threat observada* e marcar `not verified` no manual.
- ❌ Confundir `concerns` técnicos (`auth`) com domínios STRIDE (`Spoofing`).

## Relacionado

- [Codegen grounded](./codegen-grounded) — depois do *threat model*, gerar mitigações com IDs.
- [`get_threat_landscape`](../05-tools-reference.md#get_threat_landscape) na referência.
