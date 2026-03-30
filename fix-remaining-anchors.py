#!/usr/bin/env python3
"""
Fix remaining broken anchors detected by Docusaurus build.
Extracts correct anchors from chapter files and updates role pages.
"""

import re
from pathlib import Path
from urllib.parse import quote

def docusaurus_anchor(heading_text):
    """
    Generate Docusaurus/GitHub-flavored markdown anchor.
    Rules:
    - Lowercase
    - Replace spaces with hyphens
    - Remove special chars EXCEPT hyphen and unicode letters/digits
    - Collapse consecutive hyphens to single
    - Strip leading/trailing hyphens
    """
    text = heading_text.lower()
    # Keep only alphanumeric, hyphen, and common punctuation that Docusaurus allows
    # Actually, Docusaurus strips most special chars
    text = re.sub(r'[^\w\s\-]', '', text, flags=re.UNICODE)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text

# Map broken anchors from build output to their corrections
# Format: (chapter, us_number) -> correct_anchor_text
corrections = {
    ('desenvolvimento-seguro', 4): 'us-04---automatizacao-em-cicd-linters--sast',
    ('cicd-seguro', 7): 'us-07---gates-por-risco-separacao-sinaldecisao',
    ('cicd-seguro',8): 'us-08---cobertura-ampliada-containers-e-sbom',
    ('cicd-seguro', 9): 'us-09---rastreabilidade-ponta-a-ponta-commit-pipeline-release',
    ('cicd-seguro', 3): 'us-03---scanners-integrados-validacao-empirica-obrigatoria',
    ('cicd-seguro', 2): 'us-02---design-seguro-dos-pipelines-versionamento-determinismo-e-revisao',
    ('arquitetura-segura', 9): 'us-09---sincronizacao-threat-modeling-arquitetura',
    ('arquitetura-segura', 10): 'us-10---gestao-de-excecoes-arquiteturais-com-controlos-compensatorios',
}

# Manual inspection of actual headings from grep above
headings_by_chapter = {
    'cicd-seguro': {
        2: 'Design seguro dos pipelines (versionamento, determinismo e revisão)',
        3: 'Scanners integrados (validação empírica obrigatória)',
        7: 'Gates por risco (separação sinal/decisão)',
        8: 'Cobertura ampliada (containers e SBOM)',
        9: 'Rastreabilidade ponta-a-ponta (commit→pipeline→release)',
    },
    'desenvolvimento-seguro': {
        4: 'Automatização em CI/CD (Linters & SAST)',
    },
    'arquitetura-segura': {
        9: 'Sincronização Threat Modeling ↔ Arquitetura',
        10: 'Gestão de exceções arquiteturais com controlos compensatórios',
    },
}

print("=" * 70)
print("GENERATED ANCHOR PREDICTIONS")
print("=" * 70)
for chapter, us_map in headings_by_chapter.items():
    for us_num, heading_text in us_map.items():
        anchor = docusaurus_anchor(f'US-{us_num} - {heading_text}')
        print(f"{chapter:25} US-{us_num:2d}: #{anchor}")

# Now read the role pages and count broken refs
repo_root = Path(__file__).parent
role_pages_dir = repo_root / 'manuals_src/docs/sbd-toe/010-sbd-manual/00-fundamentos/roles-responsabilidades'

patterns_to_fix = [
    # From Docusaurus build output
    ('us-04---automatiza%C3%A7%C3%A3o-em-cicd-linters-sast', 'us-04---automatizacao-em-cicd-linters--sast'),  # desenvolvimento-seguro
    ('us-07---gates-por-risco-separa%C3%A7%C3%A3o-sinaldecis%C3%A3o-separa%C3%A7%C3%A3o-sinaldecis%C3%A3o', 'us-07---gates-por-risco-separacao-sinaldecisao'),  # cicd (duplicated suffix)
    ('us-08---cobertura-ampliada-containers-e-sbom-containers-e-sbom', 'us-08---cobertura-ampliada-containers-e-sbom'),  # cicd (duplicated)
    ('us-02---design-seguro-dos-pipelines-versionamento-determinismo-e-revis%C3%A3o-versionamento-determinismo-e-revis%C3%A3o', 'us-02---design-seguro-dos-pipelines-versionamento-determinismo-e-revisao'),  # cicd (duplicated)
    ('us-03---scanners-integrados-valida%C3%A7%C3%A3o-emp%C3%ADrica-obrigat%C3%B3ria-valida%C3%A7%C3%A3o-emp%C3%ADrica-obrigat%C3%B3ria', 'us-03---scanners-integrados-validacao-empirica-obrigatoria'),  # cicd (duplicated)
    ('us-09---rastreabilidade-ponta-a-ponta-commitpipelinerelease-commitpipelinerelease', 'us-09---rastreabilidade-ponta-a-ponta-commit-pipeline-release'),  # cicd (duplicated, different separator format)
    ('us-09---sincroniza%C3%A7%C3%A3o-threat-modeling-arquitetura', 'us-09---sincronizacao-threat-modeling-arquitetura'),  # arquitetura-segura
    ('us-10---gest%C3%A3o-de-exce%C3%A7%C3%B5es-bypass-controlado-arquiteturais-com-controlos-compensat%C3%B3rios', 'us-10---gestao-de-excecoes-bypass-controlado-arquiteturais-com-controlos-compensatorios'),  # arquitetura-segura
    ('us-15---prepara%C3%A7%C3%A3o-t%C3%A9cnica-e-valida%C3%A7%C3%A3o-de-contractors-pr%C3%A9-acesso---prepara%C3%A7%C3%A3o-t%C3%A9cnica-e-valida%C3%A7%C3%A3o-de-contractors-pr%C3%A9-acesso---prepara%C3%A7%C3%A3o-t%C3%A9cnica-e-valida%C3%A7%C3%A3o-de-contractors-pr%C3%A9-acesso---prepara%C3%A7%C3%A3o-t%C3%A9cnica-e-valida%C3%A7%C3%A3o-de-contractors-pr%C3%A9-acesso---prepara%C3%A7%C3%A3o-t%C3%A9cnica-e-valida%C3%A7%C3%A3o-de-contractors-pr%C3%A9-acesso', 'us-15---preparacao-tecnica-e-validacao-de-contractors-pre-acesso'),  # governanca-contratacao (HEAVILY corrupted)
]

print("\n" + "=" * 70)
print("PATTERNS TO SEARCH AND FIX")
print("=" * 70)

for broken, fixed in patterns_to_fix:
    count = 0
    print(f"\nSearching for: {broken[:60]}...")
    for role_file in role_pages_dir.glob('*.md'):
        content = role_file.read_text()
        if broken in content:
            occurrences = len(re.findall(re.escape(broken), content))
            print(f"  {role_file.name}: {occurrences} occurrence(s)")
            count += occurrences
    print(f"  TOTAL: {count}")

print("\n" + "=" * 70)
print("Run with --fix to apply all changes")
print("=" * 70)
