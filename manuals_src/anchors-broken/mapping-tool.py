#!/usr/bin/env python3
"""
Broken Anchor Detector & Mapping Tool
Analyzes broken anchor references and generates mapping for fixes.
"""

import re
import urllib.parse
import sys
from pathlib import Path
from collections import defaultdict

def normalize_anchor(text):
    """Convert heading text to markdown anchor format"""
    # Convert to lowercase, replace spaces with hyphens, remove special chars
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
    
    # Pattern to extract: chapter name and anchor
    pattern = r'linking to /sbd-toe/sbd-manual/([^/]+)/aplicacao-lifecycle#([^\s\n]+)'
    matches = re.findall(pattern, content)
    
    for chapter, encoded_anchor in matches:
        anchor = urllib.parse.unquote(encoded_anchor)
        broken_refs[chapter].append(anchor)
    
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

def find_matches(broken_anchor, actual_headings):
    """Try to find which actual heading a broken anchor might refer to"""
    # Extract US number from broken anchor (e.g., 'us-02-...' -> '02')
    match = re.match(r'us-(\d+)', broken_anchor)
    if not match:
        return None
    
    us_num = match.group(1)
    
    # Find all headings with this US number
    candidates = [
        (heading, text) for heading, text in actual_headings.items()
        if f"us-{us_num}" in heading
    ]
    
    return candidates

def main():
    repo_root = Path(__file__).parent.parent.parent
    broken_file = repo_root / 'manuals_src/anchors-broken/broken.txt'
    chapters_dir = repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual'
    
    print("=" * 80)
    print("BROKEN ANCHOR MAPPING TOOL")
    print("=" * 80)
    print()
    
    # Extract broken refs
    broken_refs = extract_broken_refs(broken_file)
    
    # Process each chapter with broken refs
    for chapter_name in sorted(broken_refs.keys()):
        broken_anchors = broken_refs[chapter_name]
        print(f"\n{'='*80}")
        print(f"CHAPTER: {chapter_name}")
        print(f"Total broken refs: {len(broken_anchors)}")
        print(f"{'='*80}")
        
        # Find chapter directory
        chapter_dir = None
        for d in chapters_dir.iterdir():
            if d.is_dir() and chapter_name in d.name:
                chapter_dir = d
                break
        
        if not chapter_dir:
            print(f"  ⚠️  Could not find chapter directory for: {chapter_name}")
            continue
        
        lifecycle_file = chapter_dir / 'aplicacao-lifecycle.md'
        if not lifecycle_file.exists():
            print(f"  ⚠️  No aplicacao-lifecycle.md found in {chapter_dir}")
            continue
        
        # Extract actual headings
        actual_headings = extract_actual_headings(lifecycle_file)
        
        print(f"\n  Actual headings in chapter ({len(actual_headings)}):")
        for anchor, text in sorted(actual_headings.items()):
            print(f"    ✓ {anchor}")
        
        print(f"\n  Broken references ({len(broken_anchors)}):")
        
        # Check each broken anchor
        for broken_anchor in sorted(set(broken_anchors)):
            candidates = find_matches(broken_anchor, actual_headings)
            
            if candidates and len(candidates) == 1:
                match_anchor, match_text = candidates[0]
                status = f"✓ MATCH → {match_anchor}"
            elif candidates and len(candidates) > 1:
                status = f"⚠ MULTIPLE → {len(candidates)} candidates"
            else:
                status = f"✗ NO MATCH"
            
            count = broken_anchors.count(broken_anchor)
            print(f"    [{count}x] {broken_anchor}")
            print(f"       {status}")

if __name__ == '__main__':
    main()
