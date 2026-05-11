# 25. Rastreabilidade — CI/CD Seguro

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

Total: **101 entidades** Manual ontology V2 mapped a este capítulo via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `CIC-001` | Pipelines como código, versionados e sujeitos a revisão | normative | explicit | deterministic |
| Requirement | `CIC-002` | Triggers controlados e restritos a fontes autorizadas | normative | explicit | deterministic |
| Requirement | `CIC-003` | Gestão segura de segredos no pipeline | normative | explicit | deterministic |
| Requirement | `CIC-004` | Gates de segurança obrigatórios antes de promoção entre ambientes | normative | explicit | deterministic |
| Requirement | `CIC-005` | Rastreabilidade completa de cada execução de pipeline | normative | explicit | deterministic |
| Requirement | `CIC-006` | Isolamento de runners e ambientes de execução | normative | explicit | deterministic |
| Requirement | `CIC-007` | Integridade e proveniência verificável dos artefactos produzidos | normative | explicit | deterministic |
| Requirement | `CIC-008` | Separação de responsabilidades entre build, test e deploy | normative | explicit | deterministic |
| Requirement | `CIC-009` | Credenciais do pipeline com âmbito mínimo e rotação definida | normative | explicit | deterministic |
| Requirement | `CIC-010` | Protecção contra execução de código não autorizado em runners | normative | explicit | deterministic |
| Control | `CTRL-code-integrity-integridade-e-governacao-de-pipelines-d5b14eeef2` | Integridade e governação de pipelines | normative | explicit | deterministic |
| Control | `CTRL-secrets-gestao-de-segredos-e-identidades-operacionais-e2c86cdfe9` | Gestão de segredos e identidades operacionais | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:assinatura-e-proveniencia` | Assinatura e proveniência | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:cobertura-ampliada-containers-e-sbom` | Cobertura ampliada (containers e SBOM) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:contencao-de-contexto-e-higiene-de-logs-outputs` | Contenção de contexto e higiene de logs/outputs | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:design-seguro-dos-pipelines-versionamento-determinismo-e-revisao` | Design seguro dos pipelines (versionamento, determinismo e revisão) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:evidencia-empirica-obrigatoria-anti-relatorios-sem-execucao` | Evidência empírica obrigatória (anti-“relatórios sem execução”) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gates-por-risco-separacao-sinal-decisao` | Gates por risco (separação sinal/decisão) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gestao-de-excecoes-bypass-controlado` | Gestão de exceções (bypass controlado) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gestao-de-segredos` | Gestão de segredos | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:gestao-segura-de-codigo-fonte` | Gestão segura de código fonte | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:isolamento-de-runners` | Isolamento de runners | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:metricas-e-conformidade-organizacional` | Métricas e conformidade organizacional | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:nao-repudio-e-ownership-de-promocoes-acoes-irreversiveis` | Não-repúdio e ownership de promoções (ações irreversíveis) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:rastreabilidade-ponta-a-ponta-commitpipelinerelease` | Rastreabilidade ponta-a-ponta (commit→pipeline→release) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:reprodutibilidade-e-determinismo-do-pipeline` | Reprodutibilidade e determinismo do pipeline | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:scanners-integrados-validacao-empirica-obrigatoria` | Scanners integrados (validação empírica obrigatória) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:separacao-formal-entre-sinal-automatico-e-decisao-de-promocao` | Separação formal entre sinal automático e decisão de promoção | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:testes-de-seguranca-dinamicos-dast` | Testes de segurança dinâmicos (DAST) | normative | explicit | deterministic |
| Practice | `07-cicd-seguro:validacao-de-integridade-de-imagens-base` | Validação de integridade de imagens base | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |
| Concept | `sem:concept:ambientes-de-execucao` | Ambientes de execução | semantic | scored | bounded |
| Concept | `sem:concept:appsec` | AppSec | semantic | scored | bounded |
| Concept | `sem:concept:artefact-protection` | Artefact Protection | semantic | scored | bounded |
| Concept | `sem:concept:assinatura-e-proveniencia-de-artefactos` | Assinatura e proveniência de artefactos | semantic | scored | bounded |
| Concept | `sem:concept:auditorias-regulares` | Auditorias regulares | semantic | scored | bounded |
| Concept | `sem:concept:ci-cd-seguro` | CI/CD Seguro | semantic | scored | bounded |
| Concept | `sem:concept:dependencia-externa` | Dependência externa | semantic | scored | bounded |
| Concept | `sem:concept:dev-team` | Dev Team | semantic | scored | bounded |
| Concept | `sem:concept:devops` | DevOps | semantic | scored | bounded |
| Concept | `sem:concept:gates-de-promocao` | gates de promoção | semantic | scored | bounded |
| Concept | `sem:concept:gestao-de-segredos` | Gestão de segredos | semantic | scored | bounded |
| Concept | `sem:concept:grc-auditoria` | GRC/Auditoria | semantic | scored | bounded |
| Concept | `sem:concept:mvp` | MVP | semantic | scored | bounded |
| Concept | `sem:concept:oidc` | OIDC | semantic | scored | bounded |
| Concept | `sem:concept:organizational-trust` | Organizational Trust | semantic | scored | bounded |
| Concept | `sem:concept:pipeline` | Pipeline | semantic | scored | bounded |
| Concept | `sem:concept:proveniencia` | proveniência | semantic | scored | bounded |
| Concept | `sem:concept:rastreabilidade-ponta-a-ponta` | Rastreabilidade ponta-a-ponta | semantic | scored | bounded |
| Concept | `sem:concept:reprodutibilidade-e-determinismo-operacional` | Reprodutibilidade e determinismo operacional | semantic | scored | bounded |
| Concept | `sem:concept:runners` | runners | semantic | scored | bounded |
| Concept | `sem:concept:runners-ephemerais` | Runners ephemerais | semantic | scored | bounded |
| Concept | `sem:concept:runners-tooling-gates-segredos` | Runners, tooling, gates, segredos | semantic | scored | bounded |
| Concept | `sem:concept:scanners-de-seguranca` | Scanners de segurança | semantic | scored | bounded |
| Concept | `sem:concept:secure-release` | Secure Release | semantic | scored | bounded |
| Concept | `sem:concept:slsa` | SLSA | semantic | scored | bounded |
| Concept | `sem:concept:supply-chain-attack` | Supply Chain Attack | semantic | scored | bounded |
| Mechanism | `sem:mechanism:assinatura-de-artefactos` | Assinatura de artefactos | semantic | scored | bounded |
| Mechanism | `sem:mechanism:auditorias-regulares` | Auditorias regulares | semantic | scored | bounded |
| Mechanism | `sem:mechanism:configuracao-de-oidc-e-ttl-curto-para-segredos` | Configuração de OIDC e TTL curto para segredos | semantic | scored | bounded |
| Mechanism | `sem:mechanism:controlo-de-logging-e-debug-com-ativacao-temporaria-e-auditavel` | Controlo de logging e debug com ativação temporária e auditável | semantic | scored | bounded |
| Mechanism | `sem:mechanism:gestao-de-segredos` | Gestão de segredos | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-de-ferramentas-como-semgrep-trivy-cosign-scorecard-e-scanners-de-iac-containers` | Integração de ferramentas como semgrep, trivy, cosign, scorecard e scanners de I | semantic | scored | bounded |
| Mechanism | `sem:mechanism:integracao-de-scanners-servicos-repositorios-registries` | Integração de scanners, serviços, repositórios, registries | semantic | scored | bounded |
| Mechanism | `sem:mechanism:logs-mascarados` | logs mascarados | semantic | scored | bounded |
| Mechanism | `sem:mechanism:oidc` | OIDC | semantic | scored | bounded |
| Mechanism | `sem:mechanism:politicas-de-gates` | Políticas de gates | semantic | scored | bounded |
| Mechanism | `sem:mechanism:promocao-de-releases` | Promoção de releases | semantic | scored | bounded |
| Mechanism | `sem:mechanism:registo-de-configuracao-efetiva` | Registo de configuração efetiva | semantic | scored | bounded |
| Mechanism | `sem:mechanism:retencao-estruturada-de-logs-metadados-e-correlacoes-commit-pipeline-release` | Retenção estruturada de logs, metadados e correlações commit→pipeline→release | semantic | scored | bounded |
| Mechanism | `sem:mechanism:runners-e-agentes` | Runners e agentes | semantic | scored | bounded |
| Mechanism | `sem:mechanism:scanners-automaticos` | scanners automáticos | semantic | scored | bounded |
| Mechanism | `sem:mechanism:scanners-de-seguranca-integrados` | Scanners de segurança integrados | semantic | scored | bounded |
| Mechanism | `sem:mechanism:tokens-de-curta-duracao` | tokens de curta duração | semantic | scored | bounded |
| Mechanism | `sem:mechanism:uso-de-runners-ephemerais-nao-privilegiados-e-segregados` | Uso de runners ephemerais, não privilegiados e segregados | semantic | scored | bounded |
| Mechanism | `sem:mechanism:versionamento-de-pipelines` | Versionamento de pipelines | semantic | scored | bounded |
| Pattern | `sem:pattern:registro-formal-de-excecoes` | registro formal de exceções | semantic | scored | bounded |
| Pattern | `sem:pattern:separacao-entre-sinal-automatico-e-decisao-de-promocao` | separação entre sinal automático e decisão de promoção | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:exposicao-excessiva-de-contexto-em-logs-e-artefactos` | exposição excessiva de contexto em logs e artefactos | semantic | scored | bounded |
| AntiPattern | `sem:antipattern:uso-de-segredos-estaticos` | uso de segredos estáticos | semantic | scored | bounded |
| Signal | `sem:signal:sinal-automatico` | sinal automático | semantic | scored | bounded |

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
