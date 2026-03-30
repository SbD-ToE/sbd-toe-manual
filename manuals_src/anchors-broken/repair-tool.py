#!/usr/bin/env python3
"""
Broken Anchor Repair Tool
Automatically fixes broken anchor references in role pages based on mapping.

Usage:
  python3 repair-tool.py governanca-contratacao  # Fix one chapter
  python3 repair-tool.py all                      # Fix all chapters
  python3 repair-tool.py --dry-run governanca-contratacao  # Preview changes
"""

import re
import urllib.parse
import sys
from pathlib import Path
from collections import defaultdict

def normalize_anchor(text):
    """Convert heading text to markdown anchor format"""
    anchor = text.lower()
    anchor = re.sub(r'[^\w\s\-àáâãäèéêëìíîïòóôõöùúûüç]', '', anchor)
    anchor = re.sub(r'\s+', '-', anchor)
    anchor = re.sub(r'-+', '-', anchor)
    return anchor.strip('-')

def extract_broken_refs(broken_file):
    """Extract all broken references from broken.txt"""
    broken_refs = defaultdict(list)
    
    with open(broken_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find each "Broken anchor" block and extract source page + target chapter
    blocks = re.split(r'- Broken anchor on source page path', content)
    
    for block in blocks[1:]:
        # Extract source page
        source_match = re.match(r' = ([^:]+):', block)
        if not source_match:
            continue
        source_page = source_match.group(1)
        
        # Extract all target refs in this block
        pattern = r'linking to /sbd-toe/sbd-manual/([^/]+)/aplicacao-lifecycle#([^\s\n]+)'
        matches = re.findall(pattern, block)
        
        for chapter, encoded_anchor in matches:
            anchor = urllib.parse.unquote(encoded_anchor)
            broken_refs[(source_page, chapter)].append(anchor)
    
    return broken_refs

def extract_actual_headings(chapter_file):
    """Extract actual US headings from a chapter's aplicacao-lifecycle.md"""
    headings = {}
    
    with open(chapter_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all ### US-XX - Text patterns
    pattern = r'^### (US-\d+)\s*-\s*(.+?)$'
    matches = re.findall(pattern, content, re.MULTILINE)
    
    for us_num, heading_text in matches:
        anchor = normalize_anchor(heading_text)
        full_anchor = f"{us_num.lower()}---{anchor}"
        headings[full_anchor] = f"{us_num} - {heading_text}"
    
    return headings

def find_best_match(broken_anchor, actual_headings):
    """Find the best matching actual heading for a broken anchor"""
    # Extract US number
    match = re.match(r'us-(\d+)', broken_anchor)
    if not match:
        return None
    
    us_num = match.group(1)
    
    # Find first heading with this US number
    for heading in sorted(actual_headings.keys()):
        if f"us-{us_num}---" in heading:
            return heading
    
    # If not found, try broader match  
    return None

def generate_repair_mapping(repo_root, chapter_name):
    """Generate mapping of broken → correct anchors for a chapter"""
    broken_file = repo_root / 'manuals_src/anchors-broken/broken.txt'
    chapters_dir = repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual'
    
    # Find chapter directory
    chapter_dir = None
    for d in chapters_dir.iterdir():
        if d.is_dir() and chapter_name in d.name:
            chapter_dir = d
            break
    
    if not chapter_dir:
        return None
    
    lifecycle_file = chapter_dir / 'aplicacao-lifecycle.md'
    if not lifecycle_file.exists():
        return None
    
    # Get actual headings
    actual_headings = extract_actual_headings(str(lifecycle_file))
    
    # Get all broken refs
    all_broken = extract_broken_refs(str(broken_file))
    
    # Build mapping for this chapter
    mapping = {}
    for (source_page, chapter), anchors in all_broken.items():
        if chapter == chapter_name:
            for broken_anchor in anchors:
                best_match = find_best_match(broken_anchor, actual_headings)
                if best_match:
                    mapping[broken_anchor] = best_match
    
    return mapping

def repair_file(file_path, mapping, dry_run=False):
    """Repair broken anchors in a single file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    for broken, correct in mapping.items():
        # Replace both URL-encoded and decoded versions
        encoded_broken = urllib.parse.quote(broken, safe='')
        encoded_correct = urllib.parse.quote(correct, safe='')
        
        # Pattern: [text](#anchor) or just #anchor
        patterns = [
            (f'#{encoded_broken}', f'#{encoded_correct}'),
            (f'#{broken}', f'#{correct}'),
        ]
        
        for old_pattern, new_pattern in patterns:
            if old_pattern in content:
                count = content.count(old_pattern)
                content = content.replace(old_pattern, new_pattern)
                changes.append((old_pattern, new_pattern, count))
    
    if not dry_run and content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

def repair_chapter(repo_root, chapter_name, dry_run=False):
    """Repair all broken anchors for a chapter"""
    mapping = generate_repair_mapping(repo_root, chapter_name)
    
    if not mapping:
        print(f"❌ Could not generate mapping for chapter: {chapter_name}")
        return 0
    
    print(f"\n📋 Repair mapping for '{chapter_name}' ({len(mapping)} fixes):")
    print("-" * 70)
    for broken, correct in sorted(mapping.items()):
        print(f"  {broken}")
        print(f"    → {correct}\n")
    
    # Find and repair role pages
    roles_dir = repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual/00-fundamentos/roles-responsabilidades'
    total_changes = 0
    
    if not roles_dir.exists():
        print(f"❌ Roles directory not found: {roles_dir}")
        return 0
    
    print(f"\n🔧 Repairing files in {roles_dir}...")
    print("-" * 70)
    
    for role_file in sorted(roles_dir.glob('*.md')):
        if role_file.name.startswith('intro') or role_file.name.startswith('_'):
            continue
        
        changes = repair_file(str(role_file), mapping, dry_run)
        
        if changes:
            mode = "[DRY RUN] " if dry_run else ""
            print(f"\n{mode}✓ {role_file.name}")
            for old, new, count in changes:
                print(f"  {count}x replacements: {old[:50]}... → ...{new[-30:]}")
            total_changes += len(changes)
    
    # Also check addon files that might have broken refs (e.g., checklist-offboarding)
    addon_file = repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual/14-governanca-contratacao/addon/checklist-offboarding.md'
    if addon_file.exists():
        changes = repair_file(str(addon_file), mapping, dry_run)
        if changes:
            mode = "[DRY RUN] " if dry_run else ""
            print(f"\n{mode}✓ {addon_file.name}")
            for old, new, count in changes:
                print(f"  {count}x replacements: {old[:50]}... → ...{new[-30:]}")
            total_changes += len(changes)
    
    return total_changes

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    dry_run = False
    arg_start = 1
    
    if sys.argv[1] == '--dry-run':
        dry_run = True
        arg_start = 2
    
    if len(sys.argv) <= arg_start:
        print(__doc__)
        sys.exit(1)
    
    repo_root = Path(__file__).parent.parent.parent
    chapter_name = sys.argv[arg_start]
    
    print(f"\n{'='*70}")
    print(f"BROKEN ANCHOR REPAIR TOOL {'[DRY RUN]' if dry_run else '[LIVE]'}")
    print(f"{'='*70}")
    
    if chapter_name == 'all':
        print("\n⚠️  Repairing ALL chapters...")
        chapters = [
            'classificacao-aplicacoes', 'requisitos-seguranca', 'threat-modeling',
            'arquitetura-segura', 'desenvolvimento-seguro', 'cicd-seguro',
            'deploy-seguro', 'monitorizacao-operacoes', 'formacao-onboarding',
            'containers-imagens', 'testes-seguranca', 'governanca-contratacao'
        ]
        total = 0
        for ch in chapters:
            total += repair_chapter(repo_root, ch, dry_run)
        print(f"\n{'='*70}")
        print(f"Total changes: {total}")
        print(f"Status: {'Review and commit changes' if total > 0 else 'No changes needed'}")
    else:
        total = repair_chapter(repo_root, chapter_name, dry_run)
        print(f"\n{'='*70}")
        print(f"Total changes: {total}")
        if dry_run and total > 0:
            print(f"✓ Preview complete. Run without --dry-run to apply changes.")
        elif total > 0:
            print(f"✓ Changes applied! Verify with: make -C src/publish web")
        else:
            print(f"ℹ️  No changes needed for this chapter.")

if __name__ == '__main__':
    main()
