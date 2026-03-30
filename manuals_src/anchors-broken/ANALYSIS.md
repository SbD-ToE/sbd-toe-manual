---
id: broken-anchors-analysis
title: Broken Anchors Analysis & Resolution Strategy
tags:
  - diagnostics
  - documentation
  - build-validation
---

# Broken Anchors Analysis Report

**Generated**: 30 March 2026  
**Total Issues**: 137 broken anchor references  
**Source Pages Affected**: 15  
**Build Status**: Warnings only (not blocking, but affects user experience)

---

## 📊 Summary

| Metric | Value |
|--------|-------|
| **Broken anchor references** | 137 |
| **Source pages with issues** | 15 |
| **Target chapters affected** | 12 |
| **Primary source** | Role pages (`fundamentos/roles-responsabilidades/*.md`) |
| **Severity** | Medium (documentation quality, not build-blocking) |

---

## 🔍 Root Cause Analysis

### Pattern Identified

**Role pages are linking to User Story (US) anchors with text that does not match the actual chapter headings.**

**Example:**
```
❌ Linked in role page:
   #us-02---dashboard-organizacional-de-práticas-sbd

✅ Actual heading in chapter:
   ### US-02 - Cláusulas contratuais de segurança
   
   (generates anchor: #us-02---cláusulas-contratuais-de-segurança)
```

### Why This Happens

1. **Heading text mismatch**: Role pages were written with expected US descriptions that differ from actual chapter content
2. **Timing mismatch**: Chapter headings may have been renamed after role pages were created
3. **Content drift**: US descriptions evolved in chapters but were not updated in role page links
4. **No synchronization**: No automated process ensures role page links match chapter heading text

---

## 📍 Affected Components

### Source Pages (11 role pages + 2 other pages)

| Source Page | Issue Count | Primary Targets |
|-------------|-------------|-----------------|
| `appsec-engineer` | 30 | governanca-contratacao (8), formacao-onboarding (4), deploy-seguro (4) |
| `arquitetos-software` | 13 | arquitetura-segura (14), threat-modeling (yes) |
| `auditores` | 8 | monitorizacao-operacoes (3), governanca-contratacao (3) |
| `developer` | 8 | Various |
| `devops-sre` | 15 | deployments, cicd, monitoring |
| `fornecedores-terceiros` | 6 | governanca-contratacao (5) |
| `gestao-executiva` | 9 | Multi-chapter |
| `grc-compliance` | 8 | Governance, monitoring, training |
| `operacoes` | 4 | monitorizacao-operacoes |
| `product-owner` | 5 | requisitos, ameaças, arquitetura |
| `qa` | 4 | arquitetura, deploy, training |
| `scrum-master` | 3 | requisitos, threat-modeling, dev |
| `security-champion` | 5 | governanca-contratacao, training |
| `/faq` | 1 | cross-check-normativo/dora |
| `checklist-offboarding` (addon) | 3 | governanca-contratacao |

### Target Chapters (12 affected chapters)

| Chapter | Broken Ref Count | Status |
|---------|------------------|--------|
| governanca-contratacao | 30 | Most problematic |
| formacao-onboarding | 18 | High impact |
| arquitetura-segura | 17 | High impact |
| monitorizacao-operacoes | 15 | High impact |
| deploy-seguro | 13 | High impact |
| classificacao-aplicacoes | 10 | Medium |
| threat-modeling | 9 | Medium |
| cicd-seguro | 8 | Medium |
| requisitos-seguranca | 7 | Medium |
| desenvolvimento-seguro | 6 | Low-medium |
| testes-seguranca | 2 | Low |
| containers-imagens | 2 | Low |

---

## 🛠️ Resolution Strategies

### Strategy A: Audit & Fix (Manual, High-Impact)

**Approach**: For each broken reference, verify if the US exists and update the anchor text or add missing headings.

**Steps**:
1. Extract all broken references from `broken.txt`
2. For each target chapter's `aplicacao-lifecycle.md`:
   - List actual US headings
   - Map to role page references
   - Identify mismatches
3. For each mismatch, choose:
   - **Option A1**: Update role page link to match actual heading
   - **Option A2**: Add missing US heading to chapter (content authoring)

**Pros**: 
- ✅ Fixes broken links permanently
- ✅ Ensures role pages accurately reflect chapter content
- ✅ Improves content coherence

**Cons**:
- ❌ Requires manual review of 137+ links
- ❌ Requires chapter author knowledge
- ❌ Time-intensive
- ❌ Risk of introducing editorial inconsistencies

**Effort**: High (2–3 days for thorough audit + fixes)

---

### Strategy B: Normalize Heading Format (Systematic)

**Approach**: Standardize how all `aplikacao-lifecycle.md` files structure their US headings, then regenerate role page links programmatically.

**Steps**:
1. Define canonical US heading format: `### US-XX - [description text]`
2. Audit all 14 `aplicacao-lifecycle.md` files for format consistency
3. Fix any non-compliant headings
4. Identify which role page links should map to which US (by number + business logic)
5. Regenerate all role page US links programmatically

**Pros**:
- ✅ Solves root cause (format consistency)
- ✅ Prevents future broken anchors
- ✅ Enables automation

**Cons**:
- ❌ Requires defining mapping rules (which role sees which US?)
- ❌ May require restructuring chapters
- ❌ Assumes all 14 chapters follow same structure

**Effort**: High upfront (rules definition), medium ongoing (implementation)

---

### Strategy C: Accept & Document (Minimal)

**Approach**: Configure Docusaurus to ignore broken anchors and document the issue as technical debt.

**Steps**:
1. Update `docusaurus.config.ts` to set `onBrokenAnchors: 'ignore'` instead of `'warn'`
2. Create issue tracker entry with root cause analysis + prioritized fix list
3. Plan gradual fixes in future sprints

**Pros**:
- ✅ Immediate build pass (no warnings)
- ✅ No rework needed now
- ✅ Allows prioritized fixes later

**Cons**:
- ❌ Broken links remain visible to end users
- ❌ Defers problem indefinitely
- ❌ Hurts site documentation quality

**Effort**: Low (< 1 hour)

---

## 📋 Recommended Action Plan

### Phase 1: Quick Wins (Week 1)

**Target**: `governanca-contratacao` chapter (30 broken refs, single source)

1. Extract all 30 references from that chapter
2. Compare against actual `14-governanca-contratacao/aplicacao-lifecycle.md` headings
3. Update role page links to match reality OR add missing US sections
4. Validate with `make web`

**Expected result**: ~22% of broken anchors resolved

---

### Phase 2: Cross-Check High-Impact (Week 2)

**Target**: `formacao-onboarding` (18), `arquitetura-segura` (17)

1. Repeat Phase 1 process
2. Identify patterns (e.g., roles consistently link to non-existent US-XX)
3. Propose content additions or link corrections

**Expected result**: ~60% of broken anchors resolved

---

### Phase 3: Remaining & Standards (Week 3+)

**Target**: Remaining 6 chapters with lower issue counts

1. Systematic audit + fixes
2. Define heading standard for all future `aplicacao-lifecycle.md` files
3. Document in `guia-editorial.md`

---

## 📝 Next Steps

**Choose one**:

- [ ] **Option 1**: Run Phase 1 (governanca-contratacao audit) immediately
- [ ] **Option 2**: Full systematic audit (all chapters, all links)
- [ ] **Option 3**: Accept & document as technical debt (minimal effort)
- [ ] **Option 4**: Request detailed guide with automation tools

---

## 📚 Related Files

- Broken anchors list: [manuals_src/anchors-broken/broken.txt](../../../manuals_src/anchors-broken/broken.txt)
- Docusaurus config: [manuals_src/docusaurus.config.ts](../../../manuals_src/docusaurus.config.ts)
- Editorial guide: [guia-editorial.md](../../../guia-editorial.md)
- Build commands: [src/publish/Makefile](../../../src/publish/Makefile)
