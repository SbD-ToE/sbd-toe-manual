---
# Proveniência da geração: não se mostra ao leitor (extraída do corpo na v1.17.1).
sbdtoe_provenance:
  ontology_v2: 'sbd-toe-knowledge-graph/ontology/sbdtoe-ontology.yaml (meta.version: ''2.0'')'
  kg_state: sbd-toe-knowledge-graph master @ 5550a743bb9de205676c503da5e81863ed62ab54 (2026-05-11; commit de governação imediatamente a seguir à tag kg-v1-cycle-b-iter-3-aligned-2026-05-11 @ 482ece916cc254126894019432ebd113695365d9)
  substrate: v7 (SUPPLIER sha256 596783ed984d9c0e8c8ef6439a0eaee8fbaf2d863af37138cde8fad55d62be04)
  v1_index: ontology-v1.1-fair-baseline @ 84fe8bf6f5de1443d778f9b2f0555b722540bbff em sbd-toe-ontology
  source_map: data/p8_inputs/per_entity_source_map.json @ ESI commit aa3c13cd39db8277a7066755d692eb37ee5b7ecd
  gap_analysis: phase2_3_per_entity_classification.json @ ESI commit b8cd4016f8876721046953363eee2995bc62a3f0
  generated_by: Manual Agent Run 1 (Iter 4 baseline @ 16dfa5ae1f6aabd811e34dd8f7299453f4f9b786 + Manual ontology V2 vocab layer injection)
  cycle: Cycle B Run 1 (post Iter 4)
  notes:
  - 'Format: 5-section (Manual V2 entities + Core-mapped + Manual-only + Out-of-AppSec + Future-work) per dispatch vision 2026-05-11'
  - '§26 methodology labels: per 00-fundamentos/canon/26-metodologia-validacao-claims.md (post Run 1 Step 0 refresh)'
---

# 25. Rastreabilidade — IaC e Infraestrutura

## Sumário {#sumário}

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

## § Manual ontology V2 — entities canónicas deste capítulo {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **119 entidades** Manual ontology V2 mapped a este capítulo.

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `IAC-001` | Backend remoto autenticado com locking activo | normative | explicit | deterministic |
| Requirement | `IAC-002` | Ambientes segregados e versionados | normative | explicit | deterministic |
| Requirement | `IAC-003` | Validações automáticas obrigatórias em pipeline | normative | explicit | deterministic |
| Requirement | `IAC-004` | Módulos reutilizados com origem confiável e versão imutável | normative | explicit | deterministic |
| Requirement | `IAC-005` | Histórico completo com versionamento, tags e releases | normative | explicit | deterministic |
| Requirement | `IAC-006` | Convenções formais de naming, tagging e layout | normative | explicit | deterministic |
| Requirement | `IAC-007` | Plan rastreável e aprovado antes de qualquer apply | normative | explicit | deterministic |
| Requirement | `IAC-008` | Rastreabilidade ficheiro → recurso → ambiente | normative | explicit | deterministic |
| Requirement | `IAC-009` | Enforcement automático de políticas em pipeline | normative | explicit | deterministic |
| Requirement | `IAC-010` | Artefactos de plan e manifests versionados e com hash | normative | explicit | deterministic |
| Requirement | `IAC-011` | Gestão segura de segredos - proibição de hardcoding | normative | explicit | deterministic |
| Requirement | `IAC-012` | Detecção automatizada de drift entre IaC e estado real | normative | explicit | deterministic |
| Requirement | `IAC-013` | Revisão periódica formal de módulos e templates | normative | explicit | deterministic |
| Control | `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af` | Gestão de identidades, acessos e ownership | normative | explicit | deterministic |
| Control | `CTRL-infrastructure-infraestrutura-como-codigo-governada-5228bca905` | Infraestrutura como código governada | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:assinatura-e-proveniencia-de-artefactos-iac` | Assinatura e Proveniência de artefactos IaC | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:backend-remoto-locking-e-rastreabilidade` | Backend remoto, locking e rastreabilidade | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:detecao-e-correcao-de-drift` | Deteção e correção de *drift* | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:determinismo-e-reprodutibilidade-do-plan` | Determinismo e reprodutibilidade do `plan` | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:enforcement-automatico-de-politicas` | Enforcement automático de políticas | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:excecoes-formais-em-iac` | Exceções formais em IaC | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:gestao-de-segredos-e-identidades-para-iac` | Gestão de segredos e identidades para IaC | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:governanca-e-origem-confiavel-de-modulos` | Governança e origem confiável de módulos | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:janela-de-mudanca-e-aprovacoes-por-papel` | Janela de mudança e aprovações por papel | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:minimizacao-de-contexto-e-protecao-de-informacao-sensivel-em-iac` | Minimização de contexto e proteção de informação sensível em IaC | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:rastreabilidade-ficheiro-recurso-ambiente` | Rastreabilidade ficheiro → recurso → ambiente | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:rastreabilidade-versionamento-e-naming` | Rastreabilidade, versionamento e naming | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:revisao-formal-de-plan-antes-de-apply` | Revisão formal de plan antes de apply | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:rollback-e-salvaguarda-de-destroy` | *Rollback* e salvaguarda de *destroy* | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:segregacao-de-ambientes-tagging-e-permissoes-minimas` | Segregação de ambientes, tagging e permissões mínimas | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:separacao-de-funcoes-sod-e-controlo-de-execucao-de-apply` | Separação de funções (SoD) e controlo de execução de `apply` | normative | explicit | deterministic |
| Practice | `08-iac-infraestrutura:validacoes-automaticas-integradas` | Validações automáticas integradas | normative | explicit | deterministic |
| Threat | `MT-132` | Defaults inseguros ou permissivos | normative | heuristic | bounded |
| Threat | `MT-133` | Configurações sem validação | normative | heuristic | bounded |
| Threat | `MT-134` | Campos críticos deixados em branco ou default | normative | heuristic | bounded |
| Threat | `MT-135` | Ambientes inconsistentes entre execuções | normative | heuristic | bounded |
| Threat | `MT-136` | Uso de módulos inseguros ou sem validação | normative | heuristic | bounded |
| Threat | `MT-137` | Hardcoded de parâmetros críticos | normative | heuristic | bounded |
| Threat | `MT-138` | Ambientes inseguros provisionados por erro | normative | heuristic | bounded |
| Threat | `MT-139` | Provisionamento com permissões excessivas | normative | heuristic | bounded |
| Threat | `MT-140` | Falta de tags de classificação de dados | normative | heuristic | bounded |
| Threat | `MT-141` | Uso de dados reais em ambientes de teste | normative | heuristic | bounded |
| Threat | `MT-142` | Segredos hardcoded ou mal geridos | normative | heuristic | bounded |
| Threat | `MT-143` | Alterações aplicadas sem revisão | normative | heuristic | bounded |
| Threat | `MT-144` | Falta de owner e accountability | normative | heuristic | bounded |
| Threat | `MT-145` | Reutilização de módulos sem tracking | normative | heuristic | bounded |
| Threat | `MT-146` | Aplicação de alterações inseguras por bypass | normative | heuristic | bounded |
| Threat | `MT-147` | Justificações informais ou inexistentes | normative | heuristic | bounded |
| Threat | `MT-148` | Ambientes provisionados com exceções acumuladas | normative | heuristic | bounded |
| Concept | `sem:concept:catalogo-de-modulos-internos-certificados` | Catálogo de módulos internos certificados | semantic | scored | bounded |
| Concept | `sem:concept:dashboards-de-validacao-automatizada` | Dashboards de validação automatizada | semantic | scored | bounded |
| Concept | `sem:concept:drift` | drift | semantic | scored | bounded |
| Concept | `sem:concept:drift-detection` | drift detection | semantic | scored | bounded |
| Concept | `sem:concept:enforcement-automatico` | Enforcement automático | semantic | scored | bounded |
| Concept | `sem:concept:enforcement-de-politicas` | Enforcement de políticas | semantic | scored | bounded |
| Concept | `sem:concept:ferramentas-de-scanning` | Ferramentas de scanning | semantic | scored | bounded |
| Concept | `sem:concept:gestao-centralizada-de-excecoes` | Gestão centralizada de exceções | semantic | scored | bounded |
| Concept | `sem:concept:infraestrutura-como-codigo-iac` | Infraestrutura como Código (IaC) | semantic | scored | bounded |
| Concept | `sem:concept:papel-funcao` | Papel/Função | semantic | scored | bounded |
| Concept | `sem:concept:pipelines-ci-cd` | Pipelines CI/CD | semantic | scored | bounded |
| Concept | `sem:concept:rastreabilidade` | Rastreabilidade | semantic | scored | bounded |
| Concept | `sem:concept:responsabilidade-partilhada` | Responsabilidade partilhada | semantic | scored | bounded |
| Concept | `sem:concept:riscos-em-iac` | Riscos em IaC | semantic | scored | bounded |
| Concept | `sem:concept:seguranca-em-iac` | Segurança em IaC | semantic | scored | bounded |
| Concept | `sem:concept:templates-e-scripts-de-provisionamento` | Templates e scripts de provisionamento | semantic | scored | bounded |
| Mechanism | `sem:mechanism:auditoria` | Auditoria | semantic | scored | bounded |
| Mechanism | `sem:mechanism:auditorias-periodicas` | auditorias periódicas | semantic | scored | bounded |
| Mechanism | `sem:mechanism:checkov` | checkov | semantic | scored | bounded |
| Mechanism | `sem:mechanism:ciclo-de-vida` | Ciclo de vida | semantic | scored | bounded |
| Mechanism | `sem:mechanism:code-review` | code review | semantic | scored | bounded |
| Mechanism | `sem:mechanism:conftest` | Conftest | semantic | scored | bounded |
| Mechanism | `sem:mechanism:detecao-de-mas-praticas-e-permissoes-excessivas` | Deteção de más práticas e permissões excessivas | semantic | scored | bounded |
| Mechanism | `sem:mechanism:enforcement-automatico-de-politicas` | Enforcement automático de políticas | semantic | scored | bounded |
| Mechanism | `sem:mechanism:kics` | kics | semantic | scored | bounded |
| Mechanism | `sem:mechanism:minimizacao-de-informacao-sensivel` | Minimização de informação sensível | semantic | scored | bounded |
| Mechanism | `sem:mechanism:opa` | OPA | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pipelines` | Pipelines | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pipelines-ci-cd` | Pipelines CI/CD | semantic | scored | bounded |
| Mechanism | `sem:mechanism:politicas` | Políticas | semantic | scored | bounded |
| Mechanism | `sem:mechanism:pull-merge-requests` | pull/merge requests | semantic | scored | bounded |
| Mechanism | `sem:mechanism:requisitos` | Requisitos | semantic | scored | bounded |
| Mechanism | `sem:mechanism:scanners-obrigatorios` | Scanners obrigatórios | semantic | scored | bounded |
| Mechanism | `sem:mechanism:sentinel` | Sentinel | semantic | scored | bounded |
| Mechanism | `sem:mechanism:templates-iac` | Templates IaC | semantic | scored | bounded |
| Mechanism | `sem:mechanism:terrascan` | terrascan | semantic | scored | bounded |
| Mechanism | `sem:mechanism:testes` | Testes | semantic | scored | bounded |
| Mechanism | `sem:mechanism:tfsec` | tfsec | semantic | scored | bounded |
| Mechanism | `sem:mechanism:validacao-e-controlo-de-configuracao` | Validação e controlo de configuração | semantic | scored | bounded |
| Mechanism | `sem:mechanism:versionamento-de-modulos-e-dependencias` | Versionamento de módulos e dependências | semantic | scored | bounded |
| Pattern | `sem:pattern:catalogo-de-modulos-certificados-e-versionados` | Catálogo de módulos certificados e versionados | semantic | scored | bounded |
| Pattern | `sem:pattern:gestao-formal-de-excecoes-com-validade-temporal` | Gestão formal de exceções com validade temporal | semantic | scored | bounded |
| Pattern | `sem:pattern:validacao-automatizada-em-pipelines-ci-cd` | Validação automatizada em pipelines CI/CD | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:ambientes-mal-segregados` | Ambientes mal segregados | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:confianca-na-experiencia-individual-sem-automacao` | Confiança na experiência individual sem automação | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:erros-de-configuracao` | Erros de configuração | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:ignorar-momentos-criticos-no-ciclo-de-vida-do-iac` | Ignorar momentos críticos no ciclo de vida do IaC | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:permissoes-excessivas` | Permissões excessivas | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:uso-de-modulos-maliciosos` | Uso de módulos maliciosos | semantic | scored | bounded |
| Signal | `sem:signal:catalogo-de-modulos-certificados` | Catálogo de módulos certificados | semantic | scored | bounded |
| Signal | `sem:signal:dashboards-de-validacao` | Dashboards de validação | semantic | scored | bounded |
| Signal | `sem:signal:gestao-centralizada-de-excecoes` | Gestão centralizada de exceções | semantic | scored | bounded |
| Signal | `sem:signal:pipelines-ci-cd-obrigatorios` | Pipelines CI/CD obrigatórios | semantic | scored | bounded |
| Signal | `sem:signal:uso-de-ferramentas-de-scanning` | Uso de ferramentas de scanning | semantic | scored | bounded |

> Authority class / source mode / confidence model: segundo a definição da ontologia do Manual (v2).
