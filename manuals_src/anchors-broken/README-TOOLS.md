# Broken Anchors – Quick Reference

## TL;DR - What Happened

✅ **Phase 1 DONE**: Fixed all 30 broken anchor refs in `governanca-contratacao` chapter (Chapter 14)

- **7 role pages** + **1 addon** were auto-repaired
- **31 anchor replacements** made
- Tools created: `mapping-tool.py`, `repair-tool.py`, analysis reports

**Status**: Ready for Phase 2

---

## One-Minute Usage

### Preview a Chapter's Fixes (Safe)
```bash
cd /Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual
python3 manuals_src/anchors-broken/repair-tool.py --dry-run formacao-onboarding
```

### Apply Fixes
```bash
python3 manuals_src/anchors-broken/repair-tool.py formacao-onboarding
```

### Fix All Remaining Chapters
```bash
python3 manuals_src/anchors-broken/repair-tool.py all
```

### Verify Build
```bash
make -C src/publish web  # Full build test
```

---

## Files You Need

Located in: `manuals_src/anchors-broken/`

| File | Purpose | Run? |
|------|---------|------|
| `mapping-tool.py` | Analyze broken → correct mappings | Read output |
| `repair-tool.py` | Fix broken anchors automatically | Execute |
| `ANALYSIS.md` | Full root cause analysis | Read |
| `PHASE1-COMPLETE.md` | Detailed completion report | Read |
| `broken.txt` | Original Docusaurus report | Reference |

---

## Common Commands

```bash
# Show all broken anchors analysis
python3 manuals_src/anchors-broken/mapping-tool.py

# Dry-run for specific chapter
python3 manuals_src/anchors-broken/repair-tool.py --dry-run classificacao-aplicacoes

# Apply all fixes
python3 manuals_src/anchors-broken/repair-tool.py all

# Build & validate
make -C src/publish web
```

---

## Phase 2 Chapters (Highest Impact)

```bash
# By volume (biggest wins first)
python3 manuals_src/anchors-broken/repair-tool.py formacao-onboarding      # 18 refs
python3 manuals_src/anchors-broken/repair-tool.py arquitetura-segura       # 17 refs
python3 manuals_src/anchors-broken/repair-tool.py monitorizacao-operacoes  # 15 refs
python3 manuals_src/anchors-broken/repair-tool.py deploy-seguro            # 13 refs
```

---

## Git Workflow

```bash
git status                          # See changes
git switch -c fix/broken-anchors    # Create feature branch
git add -A                          # Stage all fixes
git commit -m "fix: repair broken anchor references in [chapter]"
git push -u origin fix/broken-anchors
# Create PR to master
```

---

## How the Tool Works

1. **Reads** `broken.txt` (Docusaurus report)
2. **Extracts** expected anchor text from role page links
3. **Finds** actual headings in chapter files
4. **Maps** old → new anchors by US number matching
5. **Replaces** all broken references in files

✅ = Successfully mapped and fixed  
⚠️ = Multiple candidates (needs review)  
❌ = No match found (may need manual fix)

---

## Before/After Example

**Before** (broken):
```
[AppSec - Tasks](#us-02---dashboard-organizacional-de-práticas-sbd)
```

**After** (fixed):
```
[AppSec - Tasks](#us-02---cláusulas-contratuais-de-segurança)
```

---

## Questions?

See [ANALYSIS.md](ANALYSIS.md) for detailed root cause analysis and strategy options.

See [PHASE1-COMPLETE.md](PHASE1-COMPLETE.md) for full methodology and troubleshooting.

See [../../.github/copilot-instructions.md](../../.github/copilot-instructions.md) for workspace conventions.