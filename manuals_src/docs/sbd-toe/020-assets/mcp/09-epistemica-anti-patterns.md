---
id: epistemica-anti-patterns
title: Disciplina epistémica e anti-patterns
description: Como rotular respostas geradas com o MCP — manual-grounded vs observed vs inferred vs not verified — e os erros mais comuns a evitar.
sidebar_label: Epistémica & anti-patterns
sidebar_position: 9
tags:
  - mcp
  - epistemica
  - anti-patterns
  - rigor
---

# Disciplina epistémica e anti-patterns

O servidor MCP devolve **dados estruturados**; o LLM **gera conteúdo a partir deles**. A junção dos dois cria uma tentação: apresentar *inferências do LLM* como se fossem *factos do manual*. Para que o output mereça a confiança dos auditores, *legal counsel*, *security champions* — toda afirmação deve ser **rotulável**.

## Os 4 rótulos epistémicos

| Rótulo | Definição | Sinal verde para o utilizador |
|---|---|---|
| **manual-grounded** | Recuperado via MCP — citar `chapterId` ou ID (`CTRL-*`, `<CAT>-NNN`, `MT-*`, `ART-*`) | "O manual diz: `AUT-001` (MFA obrigatório). `<texto verbatim ou parafraseado fielmente>`." |
| **observed** | Visível directamente no repositório / codebase | "No ficheiro `src/auth/login.ts:42`, observo: `<…>`." |
| **inferred** | Conclusão lógica a partir de *grounded* + *observed* — marcar explicitamente | "Inferência: dado que `AUT-001` exige MFA, e o código só valida password, falta o segundo factor." |
| **not verified** | Não confirmado | "Não verificado: `<…>`. Recomenda-se inspeção humana / teste / log." |

### Regra de ouro

> **Em dúvida, preferir `not verified` a apresentar como facto.**
>
> Marcar como `not verified` permite ao utilizador agir; marcar erradamente como `manual-grounded` cria *false positives* que custam revisão e credibilidade.

---

## Onde aplicar cada rótulo

### `manual-grounded`

Permitido apenas quando:
- Devolvido por uma tool MCP (`consult_*`, `get_*`, `query_*`, `resolve_*`, `prepare_*`)
- ID citado existe no output da chamada
- Texto reflete o que o output diz (não amplifica nem reduz)

❌ **Não** marcar como *grounded*:
- Resultados de `search_sbd_toe_manual` que **não foram lidos** (apenas vistos como *snippet*) — esses são pista, não evidência
- Síntese cross-tool (ex.: "`AUT-001` + `LOG-003` implicam X") — isso é `inferred`

### `observed`

Permitido apenas quando:
- O ficheiro/linha foi lido (não inferido do nome do ficheiro)
- A observação é literalmente verificável

❌ **Não** marcar como *observed*:
- "Provavelmente o sistema faz X" — sem ter lido o código
- Comportamento esperado por causa do *framework* — isso é `inferred`

### `inferred`

Sempre marcar explicitamente quando:
- Combinas `manual-grounded` + `observed` para chegar a uma conclusão
- Aplicas conhecimento geral de segurança a um contexto específico
- Estendes uma `mitigation_confidence: "heuristic"` a outra situação

Forma recomendada: **"Inferência: `<conclusão>`. Baseado em: `<grounded ID>` + `<observação>`."**

### `not verified`

Usar generosamente. Casos:
- A tool devolveu lista vazia (`controls: []`, `threats: []`, `assignments: []`)
- O *risk level* não foi confirmado pelo utilizador
- O resultado precisa de teste / scan / log que ainda não correu
- A pergunta toca em regulamento que o MCP **não indexa** (AI Act, CRA, …)

---

## Confidence flags específicos do MCP

Algumas tools devolvem campos próprios de confiança. Traduzi-los para rótulos:

| Campo do MCP | Tradução |
|---|---|
| `mitigation_confidence: "derived"` | `manual-grounded` (ligação estrutural) |
| `mitigation_confidence: "heuristic"` | `inferred` — flag explicitamente |
| `completeness_report.m_recall < 1.0` | sinalizar **cobertura parcial** — o que falta é `not verified` |
| `coverage.hasMore: true` / `coverage_gaps` | resultado **paginado / com lacunas declaradas** — continuar via `nextOffset`; o servidor é *coverage-preserving* (nada truncado em silêncio), mas "página 1" ≠ "tudo" |
| `rule_trace` sem `CONCERNS_FILTER_*` quando concerns foram passadas | sinal de problema — pode estar a devolver mais do que se filtrou |

---

## Anti-patterns gerais

### 1. Inventar IDs

❌ "O controlo `CTRL-09-99` cobre isto."
✅ Verificar via `query_sbd_toe_entities({query: "CTRL-09-99"})` antes de citar. Se não existe, dizer: *"Nenhum controlo aplicável encontrado no manual para este caso — flag para revisão humana."*

### 2. Declarar conformidade regulatória

❌ "Este código é compliant com NIS2 Art. 21."
✅ "O cross-check NIS2 do manual mapeia Art. 21 ↔ capítulos N e M. Não declaração de conformidade — requer avaliação de *legal counsel* + evidência operacional."

### 3. Tratar código como evidência

❌ "Implementei o lockout, logo o controlo está coberto."
✅ "Implementação proposta. **Evidência esperada:** teste em `test/auth/lockout.spec.ts` + log entry `auth.lockout.activated` com schema X."

### 4. Fundir manual-grounded com inferred

❌ "O manual diz que rate limiting + monitoring previnem credential stuffing."
✅ "Manual-grounded: o output liga `MT-NNN` (credential stuffing) a `CTRL-<domain>-<slug>-<hash>` com `mitigation_confidence: derived`. Inferência (minha): aplicados juntos cobrem o threat — marcado como inferência, não como facto do manual."

### 5. Saltar gate `needs_clarification` / `needs_decomposition`

❌ Re-chamar `prepare_sbd_toe_codegen_context` com o mesmo payload para "tentar de novo".
✅ Parar, dialogar com o utilizador, **re-chamar só após inputs novos**.

### 6. Mostrar `mitigation_confidence: "heuristic"` como certeza

❌ "`CTRL-…` mitiga `MT-NNN`."
✅ "`CTRL-…` mitiga `MT-NNN` — ligação **inferida** (*fallback* sem confidence `derived`); validar com teste / revisão humana."

### 7. Confiar no MCP para o **AI Act** (não indexado na versão actual)

❌ `search_sbd_toe_manual("AI Act Art 15")` → resposta directa via MCP.
✅ Reconhecer que o MCP `@0.10.0` foi publicado antes da v1.3.0 do manual — **CRA / DORA / NIS2 / GDPR / ENISA-CSA estão indexados** e podem ser consultados via MCP, mas o cross-check do **AI Act** vive **apenas** no manual web. Consultar [`/sbd-toe/cross-check-normativo/ai-act/intro`](/sbd-toe/cross-check-normativo/ai-act/intro) directamente. Quando em dúvida, validar com `inspect_sbd_toe_retrieval` se o framework aparece nos top-ranked records.

### 8. Confundir *concerns* (ontológicos) com domínios STRIDE

❌ `concerns: ["spoofing", "tampering"]`
✅ `concerns: ["auth", "integrity"]` — o vocabulário ontológico é fechado e mapeia para domínios STRIDE indirectamente.

### 9. Saltar `setup_sbd_toe_agent` no início da sessão

❌ Começar a chamar tools sem inicializar.
✅ Primeira mensagem da sessão de segurança: `setup_sbd_toe_agent(riskLevel, projectRole)` — carrega os capítulos activos e as regras do *role*.

### 10. Re-gerar a skill no início de cada sessão

❌ Chamar `generate_sbd_toe_skill()` cada vez.
✅ Gerar uma vez, guardar no caminho canónico (`.claude/skills/sbd-toe.md`, etc.), re-gerar **apenas após upgrade do MCP**.

### 11. Confundir "consumir MCP" com "expor MCP server" (escopo de segurança distinto)

Este mini-site cobre o uso do MCP server SbD-ToE — o consumo. Quando a organização passa a **expor um MCP server próprio** (não consumir), entra num escopo de segurança adicional que **não é coberto** por este mini-site nem pelo SbD-ToE manual em geral.

❌ Assumir que ler este mini-site cobre a segurança de um MCP server a publicar pela organização.
✅ Para MCP servers expostos, consultar o **OWASP MCP Top 10 (2025)** — catálogo dedicado que cobre prompt injection em contexto MCP, *tool poisoning*, *excessive permissions*, autenticação/autorização inadequadas, transporte inseguro, validação de input, *output handling*, monitorização insuficiente, defaults inseguros. Os controlos SbD-ToE relevantes (`ARC-015`, `REQ-AGN-001..004`, `OPS-011..014`, Policy 38, Policy 39) aplicam-se directamente — o OWASP MCP Top 10 funciona como *checklist de cobertura específica*, complementar ao threat modeling do [Cap. 03 §playbook-agentic](/sbd-toe/sbd-manual/threat-modeling/addon/metodologias-e-ferramentas#playbook-agentic).

---

## Checklist de rigor antes de submeter qualquer output

1. Cada afirmação tem um dos 4 rótulos?
2. Todos os IDs citados existem em outputs MCP da sessão?
3. *Heuristic confidence* está marcado como tal?
4. `m_recall < 1.0` foi sinalizado?
5. Não há declaração de conformidade?
6. Código não foi apresentado como evidência?
7. Para perguntas sobre **AI Act** (fora do índice MCP na v0.10.0) — o cross-check web foi consultado?

Se algum check falha → **rever antes de entregar**.

## A seguir

- [Troubleshooting / FAQ](./10-troubleshooting-faq.md) — sintomas vs soluções.
- [Padrões avançados](./08-padroes-avancados.md) — para combinar tools sem perder rigor.
