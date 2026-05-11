# 25. Rastreabilidade — Governança e Contratação

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

Total: **87 entidades** Manual ontology V2 mapped a este capítulo via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `GOV-001` | Modelo formal de governação de segurança aprovado | normative | explicit | deterministic |
| Requirement | `GOV-002` | Ownership de segurança atribuído por aplicação ou projecto | normative | explicit | deterministic |
| Requirement | `GOV-003` | Alçadas de aprovação definidas e conhecidas por nível de risco | normative | explicit | deterministic |
| Requirement | `GOV-004` | Processo formal de gestão de excepções activo | normative | explicit | deterministic |
| Requirement | `GOV-005` | Excepções com validade, monitorização e revalidação obrigatória | normative | explicit | deterministic |
| Requirement | `GOV-006` | Cláusulas de segurança proporcionais ao risco em contratos com terceiros | normative | explicit | deterministic |
| Requirement | `GOV-007` | Validação formal de fornecedores antes de onboarding | normative | explicit | deterministic |
| Requirement | `GOV-008` | Rastreabilidade organizacional de decisões de segurança por aplicação | normative | explicit | deterministic |
| Requirement | `GOV-009` | Evidência de decisões rastreável, referenciável e retida | normative | explicit | deterministic |
| Requirement | `GOV-010` | Ciclo de validação contínua e revisão periódica de conformidade | normative | explicit | deterministic |
| Requirement | `GOV-011` | KPIs de governação definidos, recolhidos e reportados | normative | explicit | deterministic |
| Requirement | `GOV-012` | Modelo de maturidade activo com evolução medida e planeada | normative | explicit | deterministic |
| Control | `CTRL-governance-governacao-de-fornecedores-e-excecoes-a9a9ab3628` | Governação de fornecedores e exceções | normative | explicit | deterministic |
| Control | `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af` | Gestão de identidades, acessos e ownership | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:ciclo-continuo-de-revisao-e-reavaliacao-de-excecoes` | Ciclo contínuo de revisão e reavaliação de exceções | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:clausulas-contratuais-de-seguranca` | Cláusulas contratuais de segurança | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:consolidacao-de-kpis-de-governacao-e-maturidade` | Consolidação de KPIs de governação e maturidade | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:controlo-sistematico-e-periodico-por-capitulo-sbd-toe` | Controlo sistemático e periódico por capítulo SbD-ToE | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:designacao-formal-de-owners-de-seguranca-por-aplicacao` | Designação formal de owners de segurança por aplicação | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:execucao-de-fluxo-formal-de-validacao-de-fornecedores` | Execução de fluxo formal de validação de fornecedores | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:feedback-pos-projeto-e-rating-de-contractors` | Feedback Pós-Projeto e Rating de Contractors | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:formalizacao-de-modelo-de-governacao-por-nivel-de-risco` | Formalização de modelo de governação por nível de risco | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:kpis-de-governacao` | KPIs de governação | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:monitorizacao-continua-de-conformidade-de-fornecedores-alertas-e-escalacao` | Monitorização Contínua de Conformidade de Fornecedores (Alertas e Escalação) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:offboarding-seguro-de-contractors-e-rescisao-de-fornecedores` | Offboarding Seguro de Contractors e Rescisão de Fornecedores | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:preparacao-tecnica-e-validacao-de-contractors-pre-acesso` | Preparação Técnica e Validação de Contractors pré-Acesso | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:processo-formal-de-excecoes-com-alcadas-por-nivel-de-risco` | Processo formal de exceções com alçadas por nível de risco | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:rastreabilidade-organizacional` | Rastreabilidade organizacional | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:reavaliacao-continua-e-rotacao-de-fornecedores-pos-onboarding` | Reavaliação contínua e rotação de fornecedores pós-onboarding | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:repositorio-de-conformidade-por-aplicacao-controlo-sistematico` | Repositório de conformidade por aplicação (controlo sistemático) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:revisao-trimestral-de-acesso-de-contractors-least-privilege` | Revisão Trimestral de Acesso de Contractors (Least Privilege) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:trilho-de-formacao-obrigatoria-pre-acesso-contractors` | Trilho de Formação Obrigatória pré-Acesso (Contractors) | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:validacao-continua-de-fornecedores` | Validação contínua de fornecedores | normative | explicit | deterministic |
| Practice | `14-governanca-contratacao:validacao-periodica-de-aplicacoes-ciclo-de-conformidade` | Validação periódica de aplicações (ciclo de conformidade) | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |
| Concept | `sem:concept:ciclo-sbd-toe` | ciclo SbD-ToE | semantic | scored | bounded |
| Concept | `sem:concept:clausulas-contratuais-de-sbd-toe` | cláusulas contratuais de SbD-ToE | semantic | scored | bounded |
| Concept | `sem:concept:clausulas-contratuais-de-seguranca` | cláusulas contratuais de segurança | semantic | scored | bounded |
| Concept | `sem:concept:excecoes` | exceções | semantic | scored | bounded |
| Concept | `sem:concept:fluxo-explicito-de-excecoes-e-aceitacao-de-risco` | fluxo explícito de exceções e aceitação de risco | semantic | scored | bounded |
| Concept | `sem:concept:frameworks-normativos` | Frameworks normativos | semantic | scored | bounded |
| Concept | `sem:concept:governacao` | governação | semantic | scored | bounded |
| Concept | `sem:concept:governanca-organizacional` | governança organizacional | semantic | scored | bounded |
| Concept | `sem:concept:kpis-consolidados` | KPIs consolidados | semantic | scored | bounded |
| Concept | `sem:concept:kpis-de-governacao` | KPIs de governação | semantic | scored | bounded |
| Concept | `sem:concept:modelo-de-governacao-e-autoridade` | modelo de governação e autoridade | semantic | scored | bounded |
| Concept | `sem:concept:modelo-formal-e-aprovado-de-governacao` | modelo formal e aprovado de governação | semantic | scored | bounded |
| Concept | `sem:concept:papeis-envolvidos` | papéis envolvidos | semantic | scored | bounded |
| Concept | `sem:concept:rastreabilidade-organizacional` | rastreabilidade organizacional | semantic | scored | bounded |
| Concept | `sem:concept:sbd-toe` | SbD-ToE | semantic | scored | bounded |
| Concept | `sem:concept:validacao-continua-de-terceiros` | validação contínua de terceiros | semantic | scored | bounded |
| Mechanism | `sem:mechanism:dashboard-organizacional` | Dashboard organizacional | semantic | scored | bounded |
| Mechanism | `sem:mechanism:definicao-e-analise-de-kpis-de-governacao` | definição e análise de KPIs de governação | semantic | scored | bounded |
| Mechanism | `sem:mechanism:documentos-de-governacao-aprovados-pela-direcao` | documentos de governação aprovados pela direção | semantic | scored | bounded |
| Mechanism | `sem:mechanism:ferramenta-de-grc` | ferramenta de GRC | semantic | scored | bounded |
| Mechanism | `sem:mechanism:gestao-de-excecoes-e-aceitacao-de-risco` | gestão de exceções e aceitação de risco | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-de-clausulas-contratuais-de-seguranca` | integração de cláusulas contratuais de segurança | semantic | scored | bounded |
| Mechanism | `sem:mechanism:kpis` | KPIs | semantic | scored | bounded |
| Mechanism | `sem:mechanism:mecanismos-tecnicos-automatizados` | mecanismos técnicos automatizados | semantic | scored | bounded |
| Mechanism | `sem:mechanism:rastreabilidade-organizacional` | rastreabilidade organizacional | semantic | scored | bounded |
| Mechanism | `sem:mechanism:reporting-periodico` | reporting periódico | semantic | scored | bounded |
| Mechanism | `sem:mechanism:validacao-continua-de-fornecedores` | validação contínua de fornecedores | semantic | scored | bounded |
| Pattern | `sem:pattern:delegacao-consciente-e-documentada` | delegação consciente e documentada | semantic | scored | bounded |
| Pattern | `sem:pattern:integracao-explicita-de-seguranca-em-fornecedores-e-contratos` | integração explícita de segurança em fornecedores e contratos | semantic | scored | bounded |
| Pattern | `sem:pattern:integracao-juridico-e-procurement` | integração jurídico e procurement | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:confianca-exclusiva-em-mecanismos-tecnicos-automatizados` | confiança exclusiva em mecanismos técnicos automatizados | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:limitacao-do-sbd-toe-a-pratica-tecnica-local` | limitação do SbD-ToE à prática técnica local | semantic | scored | bounded |
| Signal | `sem:signal:clausulas-contratuais-rastreadas` | Cláusulas contratuais rastreadas | semantic | scored | bounded |
| Signal | `sem:signal:excecoes-as-praticas-prescritas` | exceções às práticas prescritas | semantic | scored | bounded |
| Signal | `sem:signal:excecoes-registadas-e-aprovadas` | Exceções registadas e aprovadas | semantic | scored | bounded |
| Signal | `sem:signal:kpis-consolidados` | KPIs consolidados | semantic | scored | bounded |
| Signal | `sem:signal:kpis-de-governacao` | KPIs de governação | semantic | scored | bounded |
| Signal | `sem:signal:ligacao-explicita-a-frameworks-normativos` | Ligação explícita a frameworks normativos | semantic | scored | bounded |
| Signal | `sem:signal:registo-e-aprovacao-de-excecoes` | registo e aprovação de exceções | semantic | scored | bounded |
| Signal | `sem:signal:reporting-periodico-a-gestao` | reporting periódico à gestão | semantic | scored | bounded |
| Signal | `sem:signal:validacao-continua-de-fornecedores` | validação contínua de fornecedores | semantic | scored | bounded |

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
