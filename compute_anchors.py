import re
import urllib.parse

def compute_anchor(heading):
    """Compute Docusaurus anchor from heading"""
    text = heading.lower()
    text = re.sub(r'[^\w\s\-]', '', text, flags=re.UNICODE)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

headings = [
    ('US-04 - Automatização em CI/CD (Linters & SAST)', 'desenvolvimento-seguro'),
    ('US-02 - Design seguro dos pipelines (versionamento, determinismo e revisão)', 'cicd-seguro'),
    ('US-03 - Scanners integrados (validação empírica obrigatória)', 'cicd-seguro'),
    ('US-07 - Gates por risco (separação sinal/decisão)', 'cicd-seguro'),
    ('US-08 - Cobertura ampliada (containers e SBOM)', 'cicd-seguro'),
    ('US-09 - Rastreabilidade ponta-a-ponta (commit→pipeline→release)', 'cicd-seguro'),
    ('US-09 - Sincronização Threat Modeling ↔ Arquitetura', 'arquitetura-segura'),
    ('US-10 - Gestão de exceções arquiteturais com controlos compensatórios', 'arquitetura-segura'),
    ('US-15 - Preparação Técnica e Validação de Contractors pré-Acesso', 'governanca-contratacao'),
]

for heading, chapter in headings:
    anchor = compute_anchor(heading.lstrip('US-').strip().split(' - ', 1)[0] + ' - ' + heading.split(' - ', 1)[1] if ' - ' in heading else heading)
    # No wait, simplify
    anchor = compute_anchor(heading)
    encoded = urllib.parse.quote(anchor.encode('utf-8'), safe='')
    print(f"{chapter:25} {heading[:50]:50} => #{anchor}")
