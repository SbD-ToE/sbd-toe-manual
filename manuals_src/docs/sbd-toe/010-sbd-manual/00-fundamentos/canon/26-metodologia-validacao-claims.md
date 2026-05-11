---
id: metodologia-validacao-claims
title: Metodologia de Validação de Claims
description: Método usado para validar claims de rastreabilidade, maturidade e ameaças mitigadas no manual SbD-ToE
sidebar_position: 26
tags: [metodologia, rastreabilidade, maturidade, ameacas, ontology, knowledge-graph]
---

# Metodologia de Validação de Claims

Esta nota descreve o método comum usado para sustentar os documentos canónicos de:

- `25-rastreabilidade`
- `achievable-maturity`
- `50-ameacas-mitigadas`

O objetivo não é substituir o juízo técnico dos autores, mas tornar **explícito e auditável** como as claims destes documentos foram revistas, validadas, limitadas quando necessário e corrigidas.

---

## 1. Baseline empírica dos autores

O ponto de partida do manual é uma baseline **empírica e construída pelos autores**.

Isto significa que:

- a estrutura dos capítulos foi construída pelos autores com base em prática real de AppSec, DevSecOps, governance e operações
- os controlos, exemplos, addons e fluxos de aplicação não foram gerados automaticamente a partir de frameworks externos
- a semântica base do manual precede e orienta o mapeamento externo, e não o contrário

Por isso, os documentos canónicos não devem ser lidos como mera conversão mecânica de frameworks para texto editorial.

---

## 2. Validação por chunking semântico e backtrace ontológico

Depois da baseline empírica, as claims foram revistas com apoio do `knowledge-graph` V2.

A Manual ontology V2 canónica vive em `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`, status `current`). Define 15 entity types: Requirement, Control, Practice, PracticeAssignment, Artifact, Threat, Role, SDLCPhase, UserStory, EvidencePattern, Concept, Mechanism, Pattern, AntiPattern, Signal. Para cada entidade, a V2 declara: **authority class** (normative / editorial / semantic / operational / external), **source mode** (explicit / derived / scored / heuristic / runtime) e **confidence model** (deterministic / bounded / probabilistic).

A validação usa, entre outros, estes artefactos:

- Manual ontology V2 canonical: `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`
- `ontology_discovery_units.jsonl`
- `canonical_chunks.jsonl`
- índices semânticos derivados do manual completo
- runtime e overlay publicados no `knowledge-graph`

Na prática, isto permite:

- localizar unidades normativas relevantes por capítulo
- verificar se uma claim editorial tem backtrace para headings, addons, lifecycle stories ou catálogos concretos
- distinguir entre presença explícita, presença semântica, presença parcial e ausência real

---

## 3. Comparação com fontes externas mapeadas

As claims do manual foram ainda confrontadas com pilotos e artefactos do repositório `external-sources-inventory`.

Dependendo do tipo de documento, foram usados outputs como:

- `appsec_core_normalization.json` (canónico AppSec Core V1 substrate v7 grounding; supersedes earlier surface)
- AppSec Core V1 ontology @ `sbd-toe-ontology` tag `ontology-v1.1-fair-baseline` (`84fe8bf`)
- KG runtime @ `sbd-toe-knowledge-graph` master @ `5550a74` (tag `kg-v1-cycle-b-iter-3-aligned-2026-05-11`)
- `ExternalSourcesInventory/data/p8_gap_analysis/coverage_v1_to_manual.json` + `coverage_manual_to_v1.json` (Cartographer Phase 1)
- `ExternalSourcesInventory/data/p8_inputs/per_entity_source_map.json` (Cartographer per-entity source coverage @ commit `aa3c13c`)
- `ExternalSourcesInventory/data/p8_gap_analysis/phase2_3/phase2_3_per_entity_classification.json` (Cartographer Phase 2/3 refined classifications @ commit `b8cd401`)
- comparações publicadas de surface de ameaças
- overlays regulatórios publicados (`DORA`, `NIS2`, `CRA`, `RGPD`)

Este passo não serve para "fazer o manual igual às fontes", mas para:

- validar se a claim editorial é materialmente suportada
- identificar `claim gaps`
- identificar `cross-reference gaps`
- separar `content gap` real de `scope boundary`

---

## 4. Regra de leitura por tipo de documento

### `25-rastreabilidade`

Aqui a pergunta principal é:

- que frameworks ou fontes externas este capítulo suporta
- e com que tipo de cobertura

As claims devem ser classificadas explicitamente, por exemplo como:

- `Explícito`
- `Semântico`
- `Parcial`
- `Reparação`
- `Gap`
- `Scope boundary`, quando aplicável

### `achievable-maturity`

Aqui a pergunta principal é:

- se este capítulo for implementado como escrito, que postura de maturidade é credível atingir

A leitura deve ser limitada e explícita. Em particular:

- `SAMM` e `DSOMM` são fontes primárias
- `SLSA` só deve ser usado onde fizer sentido como progressão de build/integridade
- alinhamento regulatório não deve ser tratado como score de maturidade

### `50-ameacas-mitigadas`

Aqui a pergunta principal é:

- que famílias de ameaça ou attack pattern este capítulo mitiga
- e se a mitigação é forte, parcial ou dependente de outros capítulos

A leitura deve ser feita sobretudo com base em:

- superfícies de ameaça do próprio manual
- `CAPEC`
- `CWE` apenas como suporte limitado, não como substituto de taxonomia de threat

---

## 5. O que o método evita

Este método existe precisamente para evitar quatro erros editoriais frequentes:

1. promover presença semântica fraca a cobertura completa
2. confundir alinhamento regulatório com maturidade
3. confundir frameworks de prática com catálogos de ameaça
4. apagar a baseline empírica dos autores em favor de uma reconstrução puramente framework-driven

---

## 6. Fórmula editorial resumida

A regra usada deve ser lida assim:

1. baseline empírica dos autores
2. revisão por chunking semântico e ontology backtrace
3. confronto com pilotos e fontes externas mapeadas
4. exposição explícita de claims limitadas, parciais ou em reparação

---

## 7. Regra curta para usar nos documentos canónicos

Sempre que um documento `25-rastreabilidade`, `achievable-maturity` ou
`50-ameacas-mitigadas` fizer uma claim material, a leitura correta deve ser:

1. existe uma baseline empírica no manual
2. a claim foi confrontada com os índices semânticos do `knowledge-graph`
3. a claim foi revista face às fontes externas relevantes para esse tipo de documento
4. a claim é exposta como explícita, semântica, parcial, em reparação ou fora de âmbito

---

## 8. Conclusão

Os documentos `25-rastreabilidade`, `achievable-maturity` e `50-ameacas-mitigadas` devem ser lidos como **artefactos editoriais validados**, não como tabelas geradas automaticamente.

O método combina:

- autoria empírica do manual
- validação factual por índices semânticos
- comparação estruturada com fontes externas
- disciplina explícita de boundary e de claim calibration

---

## 9. Pipeline primitive operacional (Cycle B closure 2026-05-11) {#pipeline-primitive}

A partir de Cycle B (closure 2026-05-11), o método foi reframed como **pipeline primitive operacional** — não apenas Editorial Feedback cycle, mas pipeline de produção reutilizável que combina quatro camadas distintas:

1. **Manual ontology V2** (semi-formal YAML; estrutural backbone) — define entity types, authority classes, source modes, confidence model. Canónico em `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`.
2. **AppSec Core V1 overlay** (ES grounding mediation) — fornece per-entity mediation entre Manual ontology V2 entities e substrate externo via `ExternalSourcesInventory/data/p8_inputs/per_entity_source_map.json`. Anchor: `sbd-toe-ontology` tag `ontology-v1.1-fair-baseline`.
3. **Substrate v7** (P7 normalization output) — corpus de fontes externas normalizado por pipeline P7 com classificação GROUNDED / LabDepthPending / out-of-scope. Anchor: `ExternalSourcesInventory` tag `cycle-a-frozen-2026-05-08`.
4. **§26 methodology layer** (claim quality discipline) — esta nota; classifica cada claim como Explícito / Semântico / Parcial / Reparação / Gap / Scope boundary.

Combinadas, as camadas produzem **Manual + KG frozen joint snapshots** por ciclo (e.g., Cycle B 2026-05-11). Cada ciclo é uma **instantiation** do pipeline; futuros ciclos podem re-rodar contra substrate / V1 / Manual states actualizados sem restructure.

**Stream 2 future work** (P8 §10 future-work register): Manual ontology V2 OWL+SHACL formalisation + corpus validation pipeline operacional.
