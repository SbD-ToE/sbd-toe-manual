# 25. Rastreabilidade — Formação e Onboarding

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

Total: **88 entidades** Manual ontology V2 mapped a este capítulo via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `TRN-001` | Trilhos de formação de segurança definidos por perfil e nível de criticidade | normative | explicit | deterministic |
| Requirement | `TRN-002` | Onboarding de segurança obrigatório antes de trabalho autónomo | normative | explicit | deterministic |
| Requirement | `TRN-003` | Validação objectiva do onboarding com critério de aceitação definido | normative | explicit | deterministic |
| Requirement | `TRN-004` | Acesso a ambientes críticos condicionado a onboarding validado | normative | explicit | deterministic |
| Requirement | `TRN-005` | Formação de segurança contínua para equipas em projectos L2 e L3 | normative | explicit | deterministic |
| Requirement | `TRN-006` | Conteúdo formativo versionado e actualizado após triggers definidos | normative | explicit | deterministic |
| Requirement | `TRN-007` | Onboarding de segurança equivalente para terceiros e contratados | normative | explicit | deterministic |
| Requirement | `TRN-008` | Programa formal de Security Champions em equipas L3 | normative | explicit | deterministic |
| Requirement | `TRN-009` | KPIs de formação definidos, recolhidos e accionados | normative | explicit | deterministic |
| Control | `CTRL-governance-capacitacao-e-onboarding-de-seguranca-f84db7abdf` | Capacitação e onboarding de segurança | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:code-clinics-estruturadas-e-recorrentes` | Code Clinics Estruturadas e Recorrentes | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:exercicios-praticos-e-simulacoes` | Exercícios práticos e simulações | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:formacao-continua-por-perfil` | Formação contínua por perfil | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:formatos-de-entrega-e-dod-por-formato` | Formatos de Entrega e DoD por Formato | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:kpis-de-capacitacao-e-reporte-grc` | KPIs de Capacitação e Reporte (GRC) | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:manutencao-e-atualizacao-de-trilhos-formativos` | Manutenção e Atualização de Trilhos Formativos | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:medicao-de-eficacia-da-formacao` | Medição de eficácia da formação | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:onboarding-seguro-obrigatorio` | Onboarding seguro obrigatório | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:operacionalizacao-de-formacao-de-terceiros` | Operacionalização de Formação de Terceiros | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:programa-de-security-champions` | Programa de Security Champions | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:threat-modeling-peer-led-e-rotativo` | Threat Modeling Peer-led e Rotativo | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:trilhos-formativos-proporcionais-por-risco-l1l3` | Trilhos Formativos Proporcionais por Risco (L1–L3) | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:validacao-de-conhecimento-via-quizzes-estruturados` | Validação de Conhecimento via Quizzes Estruturados | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:validacao-formal-de-onboarding-via-checklist` | Validação Formal de Onboarding via Checklist | normative | explicit | deterministic |
| Practice | `13-formacao-onboarding:war-room-e-simulacoes-de-incidentes` | War Room e Simulações de Incidentes | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |
| Concept | `sem:concept:champion-seguranca` | champions em segurança | semantic | scored | bounded |
| Concept | `sem:concept:champions` | Champions | semantic | scored | bounded |
| Concept | `sem:concept:checklist-de-validacao` | Checklist de Validação | semantic | scored | bounded |
| Concept | `sem:concept:code-clinic` | Code Clinics | semantic | scored | bounded |
| Concept | `sem:concept:contextualizadas` | Contextualizadas | semantic | scored | bounded |
| Concept | `sem:concept:envolventes` | Envolventes | semantic | scored | bounded |
| Concept | `sem:concept:exercicios-praticos` | exercícios práticos | semantic | scored | bounded |
| Concept | `sem:concept:facilitadas` | Facilitadas | semantic | scored | bounded |
| Concept | `sem:concept:formacao-continua` | formação contínua | semantic | scored | bounded |
| Concept | `sem:concept:formacao-e-capacitacao` | Formação e Capacitação | semantic | scored | bounded |
| Concept | `sem:concept:formacao-em-seguranca` | formação em segurança | semantic | scored | bounded |
| Concept | `sem:concept:iterativas` | Iterativas | semantic | scored | bounded |
| Concept | `sem:concept:kpis-de-eficacia-formativa` | KPIs de eficácia formativa | semantic | scored | bounded |
| Concept | `sem:concept:kpis-de-formacao` | KPIs de Formação | semantic | scored | bounded |
| Concept | `sem:concept:onboarding` | Onboarding | semantic | scored | bounded |
| Concept | `sem:concept:papeis-envolvidos` | papéis envolvidos | semantic | scored | bounded |
| Concept | `sem:concept:programas-de-onboarding` | programas de onboarding | semantic | scored | bounded |
| Concept | `sem:concept:quiz-estruturados` | Quizzes Estruturados | semantic | scored | bounded |
| Concept | `sem:concept:sandbox` | Sandbox | semantic | scored | bounded |
| Concept | `sem:concept:simulacoes-de-incidentes` | Simulações de Incidentes | semantic | scored | bounded |
| Concept | `sem:concept:sla-de-conclusao` | SLA de Conclusão | semantic | scored | bounded |
| Concept | `sem:concept:tecnicas-formativas-avancadas` | Técnicas Formativas Avançadas | semantic | scored | bounded |
| Concept | `sem:concept:threat-modeling` | Threat Modeling | semantic | scored | bounded |
| Concept | `sem:concept:trilho-formacao` | Trilho de Formação | semantic | scored | bounded |
| Concept | `sem:concept:trilhos-proporcionais-por-risco` | Trilhos Proporcionais por Risco | semantic | scored | bounded |
| Mechanism | `sem:mechanism:apoio-de-champions` | Apoio de Champions | semantic | scored | bounded |
| Mechanism | `sem:mechanism:checklist-formal` | Checklist Formal | semantic | scored | bounded |
| Mechanism | `sem:mechanism:clinics` | Clinics | semantic | scored | bounded |
| Mechanism | `sem:mechanism:code-clinic-estruturadas` | Code Clinics Estruturadas | semantic | scored | bounded |
| Mechanism | `sem:mechanism:exercicios-praticos` | Exercícios Práticos | semantic | scored | bounded |
| Mechanism | `sem:mechanism:formacao-continua` | formação contínua | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-em-backlog-e-planos-individuais-de-desenvolvimento` | integração em backlog e planos individuais de desenvolvimento | semantic | scored | bounded |
| Mechanism | `sem:mechanism:kpis-de-eficacia-formativa` | KPIs de eficácia formativa | semantic | scored | bounded |
| Mechanism | `sem:mechanism:labs` | Labs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:lms` | LMS | semantic | scored | bounded |
| Mechanism | `sem:mechanism:medicao-de-kpis` | Medição de KPIs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:onboarding` | Onboarding | semantic | scored | bounded |
| Mechanism | `sem:mechanism:programas-de-champion-seguranca` | programas de champions em segurança | semantic | scored | bounded |
| Mechanism | `sem:mechanism:programas-de-onboarding` | programas de onboarding | semantic | scored | bounded |
| Mechanism | `sem:mechanism:quiz` | Quizzes | semantic | scored | bounded |
| Mechanism | `sem:mechanism:sessoes-peer-led` | Sessões peer-led | semantic | scored | bounded |
| Mechanism | `sem:mechanism:simulacoes` | Simulações | semantic | scored | bounded |
| Mechanism | `sem:mechanism:simulacoes-de-incidentes` | Simulações de Incidentes | semantic | scored | bounded |
| Pattern | `sem:pattern:champion-seguranca` | Champions de Segurança | semantic | scored | bounded |
| Pattern | `sem:pattern:formacao-continua` | Formação Contínua | semantic | scored | bounded |
| Pattern | `sem:pattern:pessoas-como-vetor-de-resiliencia` | pessoas como vetor de resiliência | semantic | scored | bounded |
| Pattern | `sem:pattern:trilho-formacao-proporcionais` | Trilhos de Formação Proporcionais | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:dependencia-exclusiva-de-ferramentas-automatizadas` | dependência exclusiva de ferramentas automatizadas | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:falta-de-onboarding` | Falta de Onboarding | semantic | scored | bounded |
| Signal | `sem:signal:checklist-completo` | Checklist Completo | semantic | scored | bounded |
| Signal | `sem:signal:kpis-de-eficacia-formativa` | KPIs de eficácia formativa | semantic | scored | bounded |
| Signal | `sem:signal:kpis-de-formacao` | KPIs de Formação | semantic | scored | bounded |
| Signal | `sem:signal:resultados-de-quiz` | Resultados de Quizzes | semantic | scored | bounded |

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
