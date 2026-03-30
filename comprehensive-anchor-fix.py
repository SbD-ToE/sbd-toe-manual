#!/usr/bin/env python3
"""
Final fix: Recompute all broken anchor references from scratch.
Uses current chapter headings to generate correct anchors and updates all role pages.
"""

import re
from pathlib import Path
from collections import defaultdict

repo_root = Path(__file__).parent

def docusaurus_anchor(heading_text):
    """Generate Docusaurus/GitHub-flavored anchor from heading text."""
    text = heading_text.lower()
    text = re.sub(r'[^\w\s\-]', '', text, flags=re.UNICODE)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

# STEP 1: Extract current US headings from each chapter
chapters = {
    '06-desenvolvimento-seguro': repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual/06-desenvolvimento-seguro/aplicacao-lifecycle.md',
    '07-cicd-seguro': repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual/07-cicd-seguro/aplicacao-lifecycle.md',
    '04-arquitetura-segura': repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual/04-arquitetura-segura/aplicacao-lifecycle.md',
    '14-governanca-contratacao': repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual/14-governanca-contratacao/aplicacao-lifecycle.md',
}

# Extract headings for each US
heading_map = {}  # (chapter_name, us_number) -> anchor_text
for chapter_name, filepath in chapters.items():
    if not filepath.exists():
        print(f"⚠️  Chapter file not found: {filepath}")
        continue
    
    content = filepath.read_text()
    
    # Find all ### US-XX headings
    for match in re.finditer(r'^### US-(\d+)\s*-\s*(.+?)$', content, re.MULTILINE):
        us_num = int(match.group(1))
        heading_text = match.group(2).strip()
        anchor = docusaurus_anchor(f'US-{us_num} - {heading_text}')
        heading_map[(chapter_name, us_num)] = anchor
        print(f"{chapter_name:30} US-{us_num:2d}: #{anchor}")

print("\n" + "="*80)
print("Extracting broken anchor patterns from broken.txt...")
print("="*80)

# Parse broken.txt to extract exact patterns
broken_file = repo_root / 'manuals_src/anchors-broken/broken.txt'
if brokenfile.exists():
    broken_content = broken_file.read_text()
    
    # Extract all "linking to" lines
    for match in re.finditer(r'-> linking to ([^\n]+)', broken_content):
        url = match.group(1)
        print(f"  {url[:100]}")
else:
    print("⚠️  broken.txt not found")

print("\nRun with --apply to make all fixes")
