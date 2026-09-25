# `translation/` — infra-estrutura de tradução do Manual SbD-ToE

**Estado:** Fase 1 da inversão do canon (épico `DevelopmentGovernance/docs/epic-international-english-first.md`).
**Língua canónica nesta fase:** **PT**. O EN é tradução mantida e publicada. O KG e o MCP continuam a ler PT.
**Dono:** Manual agent. **Brief de desenho:** `.work-drafts/BRIEF-i18n-fase1-desenho-2026-09-24.md` (planner).
**Ortografia da prosa EN:** British English (-isation, -our, -re, -ll-), decisão do lead 2026-09-25.

Esta pasta é a infra-estrutura **reutilizável**: corre a cada alteração e, na Fase 2, inverte de direcção
sem mudar código. Nada aqui é uma tradução única.

## Layout

```
translation/
├── README.md                  ← este contrato
├── terms/
│   ├── input/                 ← inputs de outras personas, IMUTÁVEIS (levantamento do Curator, SHA-256 no brief)
│   └── registry.yaml          ← registo de termos (frente 3) — a única fonte de terminologia
├── prompts/translate-v1.md    ← prompt versionado; o seu SHA-256 fica no frontmatter de cada ficheiro EN
├── scripts/                   ← Python 3, sem dependências fora da stdlib + PyYAML
│   ├── anchors_freeze.py      ← frente 2: ids explícitos em cabeçalhos + prova de diff de âncoras vazio
│   ├── fingerprint.py         ← frente 4: impressão digital estrutural de um ficheiro, independente da língua
│   ├── equivalence.py         ← frente 4: compara fonte vs tradução; falha em qualquer divergência não-textual
│   ├── sync_state.py          ← frente 5: deriva estados por hash e escreve state/sync-state.json
│   ├── terms_lint.py          ← frente 3: lint de espécie 3, ortografia en-GB, detector de blocos `pending`
│   └── translate.py           ← frente 6: --source-locale pt --target-locale en --path …
└── state/sync-state.json      ← GERADO por sync_state.py e commitado; o site lê-o (faixa + página de estado)
```

## Regras que nenhum script ou agente viola

1. **Nomes de ficheiro não mudam, nem slugs.** O Docusaurus espelha traduções por caminho.
2. **Caminho espelho:** `manuals_src/i18n/en/docusaurus-plugin-content-docs/current/<caminho relativo a manuals_src/docs/sbd-toe>`.
   O plugin de docs tem `path: 'docs/sbd-toe'`; o espelho é relativo a isso.
3. **Ninguém coina termos da Espécie 1 ou 2.** Espécie 1 revê-se com o levantamento do Curator e ratificação do lead;
   Espécie 2 é do Archon/lead. Termos `pending` bloqueiam a tradução do bloco que os contém.
4. **Identificadores não são inglês, são ids:** `ACO-*`, `ACC-*`, `CIC-*`, `EX-*`, `ArtifactRequirement`, chaves de
   dados, códigos de categoria ficam intactos (`do-not-translate`). A prosa escreve *artefact*.
5. **Direcção é parâmetro.** Todas as ferramentas recebem `--source-locale` e `--target-locale`; nenhuma assume PT→EN.
6. **Estados nunca se declaram à mão.** `sync-state.json` é derivado de hashes; o CI verifica que é reproduzível.
7. **Só o texto natural difere entre línguas.** Ids, âncoras, contagens e formas de tabela são iguais — é o critério
   de aceitação (`equivalence.py`), não «a tradução está boa».

## Contrato do `state/sync-state.json`

```json
{
  "generated_at": "2026-09-25T00:00:00Z",
  "source_locale": "pt",
  "target_locale": "en",
  "terms_sha256": "<sha256 de terms/registry.yaml>",
  "files": {
    "010-sbd-manual/00-fundamentos/index.md": {
      "state": "untranslated",
      "source_sha256": "<sha256 do conteúdo fonte actual>",
      "translated_source_sha256": null,
      "target_sha256": null,
      "terms_sha256_at_translation": null,
      "translated_at": null,
      "pending_blocks": 0
    }
  },
  "totals": {"untranslated": 413, "synced": 0, "partial": 0, "pt-ahead": 0, "en-ahead": 0, "drift": 0, "stale-terms": 0}
}
```

Chaves de `files` são caminhos **relativos a `manuals_src/docs/sbd-toe`**, com separador `/`, ordenadas.
Estados e condições:

| estado | condição |
|---|---|
| `untranslated` | não existe ficheiro no espelho |
| `synced` | `translated_source_sha256` == hash actual da fonte, `pending_blocks` == 0, `terms_sha256_at_translation` == actual |
| `partial` | existe tradução com `pending_blocks` > 0 |
| `pt-ahead` | a fonte mudou depois da tradução (só ela) |
| `en-ahead` | a tradução mudou depois de gerada (só ela); não deve ocorrer na Fase 1 |
| `drift` | ambas mudaram |
| `stale-terms` | o registo mudou numa entrada que ocorre no ficheiro, depois da tradução |

Precedência quando várias condições se verificam: `drift` > `en-ahead` > `pt-ahead` > `stale-terms` > `partial` > `synced`.

## Contrato do frontmatter de um ficheiro traduzido

Gerado por `translate.py`, nunca à mão. Todo o frontmatter estrutural da fonte (`id`, `sidebar_position`, …) é
copiado; `title` e `description` são traduzidos; acrescenta-se:

```yaml
translation:
  source_locale: pt
  source_path: 010-sbd-manual/04-arquitetura-segura/canon/25-rastreabilidade.md
  source_sha256: <hash do conteúdo fonte no momento da tradução>
  source_commit: <sha do commit da fonte>
  target_sha256: <hash do corpo EN gerado, sem este bloco>
  engine: <modelo>
  prompt_sha256: <sha256 de prompts/translate-v1.md>
  terms_sha256: <sha256 de terms/registry.yaml>
  translated_at: <ISO-8601>
  reviewed_by: null
```

Ficheiros fonte **sem frontmatter** (46) recebem no espelho um frontmatter mínimo com `id` igual ao id efectivo
(derivado do nome do ficheiro) mais o bloco `translation`.

## Hashes

`sha256` do **conteúdo do ficheiro** normalizado: UTF-8, `\n`, sem BOM, sem espaço final de linha, com uma
`\n` final. A mesma função (`scripts/common.py: content_sha256`) é usada por todos os scripts.

## Integração das frentes (Fase 1)

Worktrees `wt/i18n-infra`, `wt/i18n-anchors`, `wt/i18n-equivalence` a partir de `feat/i18n-en-phase1`; o Manual agent
(planner) integra por `merge --no-ff`, nesta ordem: infra → âncoras → equivalência+sincronismo. Nenhum sub-agente
faz merge nem toca no ramo de outro.
