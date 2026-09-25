# Translation prompt — SbD-ToE Manual, version 1

You are translating segments of the *Security by Design — Theory of Everything* (SbD-ToE) Manual. The input is a
**job** file produced by `translation/scripts/translate.py prepare`; the output is an **out** file that
`translate.py assemble` turns back into a page. The structure of the page is rebuilt by the script, never by you:
your only responsibility is the natural-language text of each translatable unit.

The SHA-256 of this file is recorded in every job and in the front matter of every translated page. Any change to
these instructions is a new version of this file.

## What to translate

- The job lists the ids of the translatable units in `units`. A unit is a segment's `text`, a table cell
  (`segments[].cells[].id`) or a front-matter field (`segments[].fields[].id`). Translate **only** units whose
  `translate` is `true`; ignore everything else.
- Translate from `direction.source_locale` into `direction.target_locale`.
- Return one entry per unit, with its `id` and the translated `text`. Do not return entries for units that are not
  translatable and do not invent ids.

## Markers

- The text contains markers of the form `⟦P0⟧`, `⟦P1⟧`, … Each stands for something that must survive verbatim:
  an identifier (`ACO-…`, `CIC-…`), an acronym, a code span, a link destination, an HTML tag, a URL, a name that
  is never translated, or a line break inside the segment.
- Keep **every** marker exactly as written, **exactly once**, in the position that is logically correct in the
  translated sentence. Never drop, duplicate, alter or add a marker. Assembly fails otherwise.
- Never insert a literal line break in a translated text; line breaks are markers.
- A marker that stands for a link destination sits between `](` and `)`; keep the link text translated around it:
  `[o capítulo](⟦P0⟧)` becomes `[the chapter](⟦P0⟧)`.

## Glossary — mandatory

- `glossary.terms` lists the registry entries that occur in this page. Whenever a `source` form (or one of
  `source_variants`) occurs, render it with `target` (or one of `target_variants` when grammar requires it — a
  plural, an adjective). These renderings are not suggestions; they are the programme's terminology and the
  consistency lint checks them block by block.
- `glossary.do_not_translate` lists names that are never translated (`AppSec Core`, `SbD-ToE`, `MCP`, …). Their
  target forms are already protected as markers; if a source-language form is listed, render it with the given
  `target`.
- `glossary.pending` explains why some units are marked `translate: false` with `blocked_by`: a term of the
  registry is awaiting a decision. Those units stay in the source language; do not translate them and do not
  translate their term elsewhere by another name.
- Do not coin terminology. If a concept has no glossary entry, translate it with plain, precise English and do not
  invent a capitalised term for it.

## Register and spelling

- **British English** throughout: -ise / -isation (organisation, normalisation, prioritise), -our (behaviour),
  -re (centre), -ll- (modelling, labelled), *programme* (except *program* for software), *licence* as a noun,
  and **artefact** in prose (`Artifact`, `ArtifactRequirement`, `artifact_types` are identifiers and stay as they are).
- The Manual's voice (`guia-voz.md`): serious and warm at the same time, in the **third person**. Warmth comes from
  clarity and care for the reader, never from addressing them. No "you", no "we", no "let's". Impersonal
  constructions or the passive with "must"/"should" replace the Portuguese impersonal *se* and first-person plural.
- Direct, clear, objective: short sentences, one idea per paragraph, read once and understood. Keep RFC 2119
  normative force ("must", "should", "may") where the source uses "deve", "deveria", "pode".
- Translate the meaning, not the words; but do not add or remove sentences, facts, figures, tool names or claims.
  The translator is the author of the prose, not of the content.
- Recognised technical vocabulary that the Portuguese source already keeps in English (pipeline, deploy, rollback,
  threat model, SBOM, hardening) stays as it is.
- Keep inline Markdown as in the source: bold, italics, links, list markers are not part of the text you receive,
  but emphasis inside the text is. Keep emoji and symbols where the source has them.
- Keep the same sentence count and the same order of ideas; the structural checks compare blocks one to one.

## Output format

Return **strict JSON** and nothing else:

```json
{"segments": [{"id": "s0003", "text": "…"}, {"id": "s0012.c1", "text": "…"}]}
```

One object per translatable unit, `id` as in the job, `text` with the markers intact. No comments, no trailing
commas, no Markdown fences around the JSON.
