# 25. Rastreabilidade — Classificação de Aplicações

## Sumário

Este capítulo **não é âncora primária** de nenhuma slice AppSec Core V1. As referências externas relevantes para este domínio encontram-se nos capítulos onde cada slice ancora primariamente.

| Slice | Descrição | Anchored em |
|---|---|---|
| `ACO-ATB` | Arquitetura segura e fronteiras de confiança | Cap. 04 (04-arquitetura-segura) |
| `ACO-IAT` | Identidade, autenticação e gestão de sessões | Cap. 04 (04-arquitetura-segura) |
| `ACO-ITS` | Integração e segurança service-to-service | Cap. 04 (04-arquitetura-segura) |
| `ACO-IVF` | Validação de input, parsing seguro e tratamento controlado de erros | Cap. 06 (06-desenvolvimento-seguro) |
| `ACO-RPR` | Release promotion, rollout controlado e readiness para rollback | Cap. 11 (11-deploy-seguro) |
| `ACO-SCBI` | Integridade da supply chain de software e do build | Cap. 05 (05-dependencias-sbom-sca) |
| `ACO-SLG` | Logging de eventos de segurança e audit trail | Cap. 12 (12-monitorizacao-operacoes) |
| `ACO-SPC` | Gestão de segredos, configuração protegida e identidades operacionais | Cap. 06 (06-desenvolvimento-seguro) |
| `ACO-TMR` | Threat modeling, gestão de risco e rastreabilidade de mitigações | Cap. 03 (03-threat-modeling) |
| `ACO-TSV` | Testes de segurança e validação empírica | Cap. 10 (10-testes-seguranca) |

---

## § Manual ontology V2 — entities canónicas deste capítulo

Total: **59 entidades** Manual ontology V2 mapped a este capítulo via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `CLA-001` | Classificação formal segundo o modelo de eixos de risco | normative | explicit | deterministic |
| Requirement | `CLA-002` | Aprovação proporcional ao nível de risco atribuído | normative | explicit | deterministic |
| Requirement | `CLA-003` | Activação de controlos base determinada pela classificação | normative | explicit | deterministic |
| Requirement | `CLA-004` | Critérios de reclassificação documentados e monitorizados | normative | explicit | deterministic |
| Requirement | `CLA-005` | Ciclo periódico de revisão de classificação diferenciado por nível | normative | explicit | deterministic |
| Requirement | `CLA-006` | Reavaliação de classificação após evento de mudança significativa | normative | explicit | deterministic |
| Requirement | `CLA-007` | Risco residual com compensação formalizada, owner e TTL | normative | explicit | deterministic |
| Requirement | `CLA-008` | Inventário de aplicações actualizado e acessível para auditoria | normative | explicit | deterministic |
| Control | `CTRL-governance-classificacao-e-governacao-por-risco-97aceecf29` | Classificação e governação por risco | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:analise-de-risco-residual` | Análise de risco residual | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:aplicacao-da-matriz-de-controlo` | Aplicação da matriz de controlo | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:classificacao-inicial-da-aplicacao` | Classificação inicial da aplicação | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:mapeamento-de-ameacas-por-nivel-de-risco` | Mapeamento de ameaças por nível de risco | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:revisao-por-alteracao-relevante-event-based` | Revisão por alteração relevante (event-based) | normative | explicit | deterministic |
| Practice | `01-classificacao-aplicacoes:validacao-antes-do-go-live` | Validação antes do go-live | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |
| Concept | `sem:concept:aceitacao-de-risco` | aceitação de risco | semantic | scored | bounded |
| Concept | `sem:concept:atributos-do-risco` | atributos do risco | semantic | scored | bounded |
| Concept | `sem:concept:ciclo-de-desenvolvimento` | ciclo de desenvolvimento | semantic | scored | bounded |
| Concept | `sem:concept:ciclo-de-vida-do-risco` | ciclo de vida do risco | semantic | scored | bounded |
| Concept | `sem:concept:classificacao-de-criticidade` | classificação de criticidade | semantic | scored | bounded |
| Concept | `sem:concept:ferramentas-de-automacao-e-apoio-a-decisao` | ferramentas de automação e apoio à decisão | semantic | scored | bounded |
| Concept | `sem:concept:gates-explicitos-de-validacao-de-risco` | gates explícitos de validação de risco | semantic | scored | bounded |
| Concept | `sem:concept:impacto-residual` | impacto residual | semantic | scored | bounded |
| Concept | `sem:concept:modelo-de-classificacao-simples` | modelo de classificação simples | semantic | scored | bounded |
| Concept | `sem:concept:modelo-e-d-i` | modelo E/D/I | semantic | scored | bounded |
| Concept | `sem:concept:risco` | risco | semantic | scored | bounded |
| Mechanism | `sem:mechanism:dashboards-de-risco` | dashboards de risco | semantic | scored | bounded |
| Mechanism | `sem:mechanism:evidencia-da-eficacia` | evidência da eficácia | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-em-ferramentas-de-backlog` | integração em ferramentas de backlog | semantic | scored | bounded |
| Mechanism | `sem:mechanism:mecanismo` | mecanismo | semantic | scored | bounded |
| Mechanism | `sem:mechanism:mecanismos-claros-rapidos-e-rastreaveis` | mecanismos claros, rápidos e rastreáveis | semantic | scored | bounded |
| Mechanism | `sem:mechanism:modelo-de-classificacao-simples-direto-e-economicamente-viavel` | modelo de classificação simples, direto e economicamente viável | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pipelines-ci-cd` | Pipelines CI/CD | semantic | scored | bounded |
| Mechanism | `sem:mechanism:registo-versionado-em-git` | registo versionado em Git | semantic | scored | bounded |
| Mechanism | `sem:mechanism:verificacao-dos-controlos-aplicados` | verificação dos controlos aplicados | semantic | scored | bounded |
| Pattern | `sem:pattern:user-stories-reutilizaveis` | user stories reutilizáveis | semantic | scored | bounded |
| Pattern | `sem:pattern:uso-de-modelo-alternativo-de-classificacao` | uso de modelo alternativo de classificação | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:aceitacao-de-risco-invalida` | aceitação de risco inválida | semantic | scored | bounded |
| Signal | `sem:signal:alteracao-na-exposicao-dados-impacto-ou-forma-de-decisoes-e-validacoes` | alteração na exposição, dados, impacto ou forma de decisões e validações | semantic | scored | bounded |

> Authority class / source mode / confidence model: per Manual ontology V2 definition (`sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml`, `meta.version: '2.0'`).

---

## Generation provenance

- **Manual ontology V2 canonical:** `sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml` (`meta.version: '2.0'`)
- **KG canonical state:** sbd-toe-knowledge-graph master @ `5550a74` (`kg-v1-cycle-b-iter-3-aligned-2026-05-11`)
- **Substrate version:** v7 (SUPPLIER sha256 `596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04`)
- **V1 entity index:** `ontology-v1.1-fair-baseline` @ `84fe8bf` em sbd-toe-ontology
- **Per-entity source map:** `data/p8_inputs/per_entity_source_map.json` @ ESI commit `aa3c13c`
- **Phase 2/3 gap analysis:** `phase2_3_per_entity_classification.json` @ ESI commit `b8cd401`
- **Generated by:** Manual Agent Run 1 (Iter 4 baseline @ `16dfa5ae` + Manual ontology V2 vocab layer injection)
- **Format:** 5-section (Manual V2 entities + Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11
- **§26 methodology labels:** per `00-fundamentos/canon/26-metodologia-validacao-claims.md` (post Run 1 Step 0 refresh)
- **Cycle:** Cycle B Run 1 (post Iter 4)
