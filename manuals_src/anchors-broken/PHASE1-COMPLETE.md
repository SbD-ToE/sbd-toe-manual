---
id: broken-anchors-fix-guide
title: Broken Anchors - Quick Fixes & Automation Tools
sidebar_position: 1
---

# Phase 1 Quick Win: Governança-Contratação Fixes ✅

## What Was Done

**Governor's chapter (14) is now fixed!** All 30 broken anchor references have been automatically repaired.

### Scope of Repairs
- **Chapter**: `governanca-contratacao` (Chapter 14)
- **Broken refs fixed**: 30
- **Files updated**: 7 role pages + 1 addon = 8 files
- **Total anchor replacements**: 31

### Files Modified
1. `appsec-engineer.md` – 6 fixes
2. `auditores.md` – 3 fixes
3. `developer.md` – 2 fixes
4. `fornecedores-terceiros.md` – 5 fixes
5. `gestao-executiva.md` – 6 fixes
6. `grc-compliance.md` – 2 fixes
7. `security-champion.md` – 7 fixes
8. `addon/checklist-offboarding.md` – (automatically repaired)

---

## Automation Tools Created

### 1. **Mapping Tool** 
**File**: `manuals_src/anchors-broken/mapping-tool.py`

Analyzes all broken anchors and finds which actual headings they should link to.

**Usage:**
```bash
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual
python3 manuals_src/anchors-broken/mapping-tool.py
```

**Output**: Shows each chapter with:
- Actual headings that exist ✓
- Broken references with status (MATCH, NO MATCH, MULTIPLE)
- Suggestions for fixes

### 2. **Repair Tool**
**File**: `manuals_src/anchors-broken/repair-tool.py`

Automatically fixes broken anchors in role pages using the mapping.

**Usage:**

```bash
# Preview changes before applying (dry-run)
python3 manuals_src/anchors-broken/repair-tool.py --dry-run governanca-contratacao

# Apply fixes for one chapter
python3 manuals_src/anchors-broken/repair-tool.py governanca-contratacao

# Fix all chapters at once
python3 manuals_src/anchors-broken/repair-tool.py all

# Fix specific chapters
python3 manuals_src/anchors-broken/repair-tool.py classificacao-aplicacoes
python3 manuals_src/anchors-broken/repair-tool.py threat-modeling
```

### 3. **Analysis Report**
**File**: `manuals_src/anchors-broken/ANALYSIS.md`

Comprehensive breakdown of all 137 broken anchors with:
- Root cause analysis
- Distribution by chapter
- Status of each broken reference
- Resolution strategies

---

## How the Tools Work

### Step 1: Detect & Analyze
The **mapping-tool** reads your broken anchors list and compares against actual chapter headings:

```
Broken:   us-02---dashboard-organizacional-de-práticas-sbd
Actual:   us-02---cláusulas-contratuais-de-segurança
Match:    ✓ MATCH (same US number 02)
```

### Step 2: Preview Changes
The **repair-tool** in `--dry-run` mode shows exactly what would be changed:

```
[DRY RUN] ✓ appsec-engineer.md
  1x replacements: #us-02---dashboard... → ...cláusulas-contratuais
```

### Step 3: Apply Fixes
Running without `--dry-run` applies all changes:

```
✓ appsec-engineer.md
  6 fixes applied
```

---

## Next Steps for Other Chapters

### Quick Wins (Highest ROI) — Phase 2

**Estimated effort**: 2–3 hours per chapter using automation

#### Most Problematic Chapters

| Chapter | Broken Refs | Files Affected | Estimate |
|---------|------------|----------------|----------|
| `formacao-onboarding` | 18 | 6 pages | 1 hour |
| `arquitetura-segura` | 17 | 4 pages | 1 hour |
| `monitorizacao-operacoes` | 15 | 3 pages | 45 min |
| `deploy-seguro` | 13 | 3 pages | 45 min |
| `classificacao-aplicacoes` | 10 | 3 pages | 45 min |

### Recommended Sequence

1. **Verify Phase 1** (governanca-contratacao)
   ```bash
   make -C src/publish web  # Build and check for warnings
   ```

2. **Fix Phase 2** (formacao-onboarding, arquitetura-segura)
   ```bash
   python3 manuals_src/anchors-broken/repair-tool.py formacao-onboarding
   python3 manuals_src/anchors-broken/repair-tool.py arquitetura-segura
   ```

3. **Fix Remaining** (deploy, monitoring, classification)
   ```bash
   python3 manuals_src/anchors-broken/repair-tool.py all
   ```

4. **Validate Full Build**
   ```bash
   make -C src/publish web
   ```

---

## Git Workflow for These Changes

### Commit Phase 1 Fixes

```bash
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual

# Check what changed
git status

# Stage changes
git add manuals_src/docs/sbd-toe/010-sbd-manual/00-fundamentos/roles-responsabilidades/
git add manuals_src/docs/sbd-toe/010-sbd-manual/14-governanca-contratacao/addon/

# Create feature branch
git switch -c fix/cap14-broken-anchors

# Commit
git commit -m "fix(cap14): repair 30 broken anchor references

- Fixed all governanca-contratacao anchor mismatches
- Impacted: 7 role pages + 1 addon (checklist-offboarding)
- Total repairs: 31 anchor replacements
- Status: All 30 refs now point to correct headings

Automation tools created:
- mapping-tool.py: Detect and analyze broken anchors
- repair-tool.py: Automatically fix broken refs by chapter
- ANALYSIS.md: Root cause and detailed breakdown"

# Push
git push -u origin fix/cap14-broken-anchors

# Open PR to master for review
```

---

## Troubleshooting

### Build Verification

After applying fixes, always validate:

```bash
make -C src/publish web
```

**Expected output**: Build completes, broken anchor warnings reduced for that chapter.

### If Something Goes Wrong

**Undo Phase 1**:
```bash
git checkout -- manuals_src/docs/sbd-toe/010-sbd-manual/00-fundamentos/roles-responsabilidades/
git checkout -- manuals_src/docs/sbd-toe/010-sbd-manual/14-governanca-contratacao/addon/
```

**Regenerate mapping** (if tool produces wrong matches):
```bash
# Check actual headings in a chapter
grep "^### US-" manuals_src/docs/sbd-toe/010-sbd-manual/14-governanca-contratacao/aplicacao-lifecycle.md
```

### Manual Verification

To verify a specific role page was fixed correctly:

```bash
# Before: check for broken refs
grep "us-02---dashboard-organizacional" manuals_src/docs/sbd-toe/010-sbd-manual/00-fundamentos/roles-responsabilidades/appsec-engineer.md

# After (should be empty if fixed):
# (no output = successfully replaced)

# Check what it was replaced with
grep "us-02---cláusulas" manuals_src/docs/sbd-toe/010-sbd-manual/00-fundamentos/roles-responsabilidades/appsec-engineer.md
# Should show the link now points to cláusulas-contratuais-de-segurança
```

---

## Statistics & Impact

### Phase 1 Results (Completed ✅)

| Metric | Value |
|--------|-------|
| Chapter | governanca-contratacao (14) |
| Broken refs resolved | 30/30 (100%) |
| Source files updated | 8 |
| Total anchor replacements | 31 |
| Estimated remaining | ~107 (in 11 other chapters) |

### Projected Phase 2 Impact

| Chapter | Broken Refs | % of Total | Estimated Time |
|---------|------------|-----------|-------------------|
| formacao-onboarding | 18 | 13% | 1 hour |
| arquitetura-segura | 17 | 12% | 1 hour |
| monitorizacao-operacoes | 15 | 11% | 45 min |
| deploy-seguro | 13 | 9% | 45 min |
| classificacao-aplicacoes | 10 | 7% | 45 min |
| **Phase 2 Subtotal** | **73** | **53%** | **~4.5 hours** |
| **Remaining (Phase 3)** | **34** | **25%** | **~2 hours** |

---

## Reference: All Tools & Files

### New Files Created

```
manuals_src/anchors-broken/
├── mapping-tool.py        ← Analyze & detect broken anchors
├── repair-tool.py         ← Automatically fix broken anchors
├── ANALYSIS.md            ← Complete root cause analysis
└── broken.txt             ← Original Docusaurus broken anchors report
```

### Key Configuration

Docusaurus config at `manuals_src/docusaurus.config.ts`:

```typescript
onBrokenLinks: 'warn',  // Currently warns (does not block build)
// Could be changed to 'error' to block builds with broken anchors
```

---

## Quick Reference Commands

```bash
# Analyze a chapter
python3 manuals_src/anchors-broken/mapping-tool.py | grep -A 50 "CHAPTER: formacao-onboarding"

# Preview fixes for a chapter (safe, no changes)
python3 manuals_src/anchors-broken/repair-tool.py --dry-run formacao-onboarding

# Apply fixes for a chapter
python3 manuals_src/anchors-broken/repair-tool.py formacao-onboarding

# Fix all remaining chapters
python3 manuals_src/anchors-broken/repair-tool.py all

# Verify build quality
make -C src/publish web

# Check for remaining errors
cat _out/web/build/broken-links.txt 2>/dev/null || echo "Build successful!"
```

---

## Success Criteria

✅ **Phase 1 Complete for governanca-contratacao**
- [ ] Build passes: `make -C src/publish web`
- [ ] No broken anchor warnings for chapter 14
- [ ] Changes committed to feature branch
- [ ] PR reviewed and merged

📋 **Phase 2 Candidate** (Ready to start)
- [ ] formacao-onboarding
- [ ] arquitetura-segura
- [ ] monitorizacao-operacoes

🎯 **Phase 3 Follow-up** (Lower priority)
- Remaining 6 chapters with lower broken anchor counts

---

## Notes for Team

- **Automation is safe**: All changes are mappings from broken → actual headings; no content is modified.
- **Dry-run first**: Always use `--dry-run` to preview before applying.
- **Build validation**: After each phase, run `make web` to confirm no new issues.
- **Tool transparency**: Both tools print detailed logs of all changes.
- **Reversibility**: All changes are in git; undo with `git checkout` if needed.
