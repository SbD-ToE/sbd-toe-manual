# GitHub Copilot Instructions – SbD-ToE Manual

**Repository**: Security by Design – Theory of Everything (SbD-ToE) Manual  
**Primary Language**: Portuguese (pt-BR)  
**Framework**: Docusaurus with custom build pipeline  
**Purpose**: Authoritative source for secure software engineering manual and operational framework

---

## 🎯 Core Principles

1. **Source of truth is the repository** – Never assume generated output or build artifacts are canonical.
2. **Preserve structure and naming** – This manual uses numbered chapters (`00-`, `01-`, etc.) for ordering; Docusaurus strips numeric prefixes in URLs via `numberPrefixParser: true`.
3. **Respect editorial coherence** – Content must align with existing chapters, style guide, and cross-link patterns.
4. **Build pipeline matters** – Changes to Markdown must not break `make web` or Docusaurus build; validate locally before proposing changes.
5. **Language is technical and prescriptive** – Use third-person impersonal form, normative modals (deve, requer, não deve), and avoid colloquialisms.

---

## 📁 Repository Structure

```
/manuals_src/
  docusaurus.config.ts       ← Main Docusaurus config (routeBasePath: 'sbd-toe')
  sidebars-sbd-toe.ts        ← Sidebar navigation structure
  docs/
    sbd-toe/
      000-teory-of-everything/     ← ToE Overview
      002-cross-check-normativo/   ← Cross-check vs standards
      010-sbd-manual/
        00-fundamentos/            ← Chapter 0: Fundamentals
        01-classificacao-aplicacoes/
        02-requisitos-seguranca/
        ... (chapters 03–14)
        14-governanca-contratacao/ ← Chapter 14: Governance
      020-assets/                  ← Assets (NOT yet in sidebar)
      tldr.md                       ← TLDR index

/src/publish/
  Makefile                   ← Build automation (copy, install, build)

guia-editorial.md           ← Editorial guidelines & style rules
guia-voz.md                 ← Prose voice norm (tone, person, anti-AI-tells)
CONTRIB.md                  ← Git workflow & validation requirements
```

---

## 🔨 Build & Validation

### Build Commands

| Command | Purpose |
|---------|---------|
| `make -C src/publish web` | **Full pipeline**: update-lock → prepare → install → build (produces `_out/web/build/`) |
| `make -C src/publish dev` | Start dev server (hot reload) |
| `make -C src/publish serve` | Serve pre-built (requires `make web` first) |
| `make -C src/publish clean` | Remove build artifacts |

### Pre-Commit Validation

Before submitting changes:

```bash
# From repository root:
make -C src/publish web
```

If build succeeds, the site is valid for merging. Check for:
- ✅ No broken links warnings (Docusaurus `onBrokenLinks: 'warn'`)
- ✅ No Markdown parse errors
- ✅ No broken anchors (currently 300+; see `manuals_src/anchors-broken/broken.txt`)

---

## 📝 When Editing Content

### Naming & Organization

- **Chapters**: Numbered directories (`00-`, `01-`, etc.) under `/010-sbd-manual/`
- **Files**: Use lowercase, hyphens for word separation, meaningful names
- **Prefixes in URLs**: Docusaurus strips numeric prefixes; **use `sbd-manuel/...` not `010-sbd-manual/...` in sidebar references**

### Chapter Structure

Each chapter must follow this template:

```
XX-chapter-name/
  _category_.json              ← Sidebar label & metadata
  intro.md                     ← Main chapter content (required)
  achievable-maturity.md       ← SAMM/SSDF alignment (required)
  aplicacao-lifecycle.md       ← SDLC application (required)
  recomendacoes-avancadas.md  ← Advanced practices (recommended)
  policies-relevantes.md       ← Org policy guidance (recommended)
  addon/
    01-*.md … 09-*.md         ← Supplementary technical docs (numbered)
  canon/
    20-checklist-revisao.md   ← Binary checklist (Yes/No)
    25-rastreabilidade.md     ← Traceability to standards
    50-ameacas-mitigadas.md   ← Threat mitigation list
```

### Frontmatter (YAML)

```yaml
---
id: unique-id
title: Display Title for Menu
tags:
  - type: chapter | addon | canon
  - grupo: base | execucao | validacao | suporte | transversal
  - tema: technical-topic-name
---
```

### Language & Style

| Aspect | Rule | Example |
|--------|------|---------|
| **Perspective** | Third person, impersonal | "Debe ser definido um owner de segurança." ✅ |
| **Modality** | RFC 2119 normatives (deve, pode, não deve) | "A validação **deve** ocorrer antes do deploy." |
| **Tone** | Technical, prescriptive, clear | Avoid "você", "nós", colloquialisms |
| **Structure** | Short sentences & focused paragraphs | 4–5 lines per paragraph, one concept per block |
| **Links** | Use cross-references; avoid duplication | [Link text](../other-chapter/section#anchor) |

---

## 🔗 Key Files to Understand

| File | Purpose | Notes |
|------|---------|-------|
| `guia-editorial.md` | Editorial guidelines & style rules | **Read before creating new content** |
| `guia-voz.md` | Prose voice norm — tone, person discipline, anti-AI-tells | **Read before writing/editing prose** |
| `CONTRIB.md` | Git workflow & validation setup | Requirements for PRs |
| `docusaurus.config.ts` | Docusaurus configuration | `numberPrefixParser: true` is critical |
| `sidebars-sbd-toe.ts` | Sidebar structure & navigation | Maps filesystem paths to URL routes |
| `manuals_src/anchors-broken/broken.txt` | List of currently broken anchors | ~300 references; useful for debugging |

---

## 🚫 Common Pitfalls

1. **Confusing filesystem paths with URL routes**
   - ❌ Linking to `/010-sbd-manual/...` in sidebar configs
   - ✅ Use `sbd-manual/...` (numeric prefix is stripped)

2. **Breaking internal anchors**
   - When renaming sections, check all incoming links
   - Use `grep` or semantic search to find references

3. **Not validating build locally**
   - Always run `make -C src/publish web` before pushing
   - Broken Markdown can block CI/CD

4. **Editing sidebar structure without understanding `numberPrefixParser`**
   - Docusaurus removes `00-`, `01-`, etc. prefixes in URLs
   - Use stripped names in `id` and sidebar references

5. **Inconsistent language or tone**
   - Manual requires technical, prescriptive Portuguese
   - Avoid informal phrases or second-person pronouns

---

## 🔄 Git Workflow

- **Branch model**: Trunk-based; use `feat/`, `fix/`, `chore/`, `docs/` prefixes
- **Commit format**: `type(scope): message` (Portuguese or English)
- **Example**: `feat(cap05): adicionar threat modeling por epic`, `fix(roles): corrigir anchors em AppSec Engineer`
- **Merge strategy**: Squash and merge to `master`
- **Validation**: Mandatory `make -C src/publish web` before PR

---

## 📋 Known Issues & Tracking

### Broken Anchors (300+)

**File**: `manuals_src/anchors-broken/broken.txt`  
**Scope**: Mainly role pages (`fundamentos/roles-responsabilidades/*.md`) linking to non-existent `aplicacao-lifecycle` sections  
**Action**: Cross-check existence of target anchors and either fix links or add missing sections

### Incomplete Integrations

- **`020-assets/`**: Exists but not integrated into `sidebars-sbd-toe.ts`—clarify scope before adding to sidebar

---

## 🔍 Troubleshooting

| Issue | Check | Solution |
|-------|-------|----------|
| Build fails with "cannot find module" | Node.js version (need ≥ 20) | `node --version` then reinstall via Makefile |
| Broken anchors appear after changes | Cross-reference source headings | Ensure heading matches link anchor exactly |
| Sidebar doesn't reflect changes | Did you edit `sidebars-sbd-toe.ts`? | Restart Docusaurus dev server |
| URL route unexpected | Numeric prefix still visible? | Check `numberPrefixParser: true` in config |

---

## 📖 When Asked to Help

### Authoring / Content Review
1. Check `guia-editorial.md` for rules
2. Validate chapter structure matches template
3. Ensure consistent language & tone
4. Verify all cross-references are valid

### Fixing Links / Anchors
1. Inspect `broken.txt` to understand scope
2. Verify target sections exist and have correct heading level
3. Check for multiple spaces or special chars in anchor names
4. Test with `make -C src/publish web`

### Restructuring Content
1. Preserve existing `id` values (used in URLs)
2. Check all incoming references before renaming
3. Update sidebar config if chapter order changes
4. Validate build post-restructure

### Adding New Chapters
1. Follow numbered directory pattern (`XX-name`)
2. Create required files: `_category_.json`, `intro.md`, `achievable-maturity.md`, `aplicacao-lifecycle.md`
3. Add sidebar entry in `sidebars-sbd-toe.ts`
4. Validate language & style vs. existing chapters
5. Run `make -C src/publish web`

---

## 📚 References

- **Project**: https://github.com/Shiftleftpt/SbD-ToE-Manual
- **Published site**: https://www.securitybydesign.dev/sbd-toe/
- **Docusaurus docs**: https://docusaurus.io/
- **RFC 2119** (normative language): https://tools.ietf.org/html/rfc2119
