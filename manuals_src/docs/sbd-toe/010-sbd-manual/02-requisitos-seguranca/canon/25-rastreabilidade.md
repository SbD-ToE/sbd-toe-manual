# 25. Rastreabilidade — Requisitos de Segurança

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

Total: **139 entidades** Manual ontology V2 mapped a este capítulo via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `ACC-001` | Controlo de acesso RBAC | normative | explicit | deterministic |
| Requirement | `ACC-002` | Princípio do menor privilégio | normative | explicit | deterministic |
| Requirement | `ACC-003` | Bloqueio e auditoria de acessos ilegítimos | normative | explicit | deterministic |
| Requirement | `ACC-004` | Separação de perfis | normative | explicit | deterministic |
| Requirement | `ACC-005` | Controlo de acesso a APIs e serviços | normative | explicit | deterministic |
| Requirement | `ACC-006` | Protecção de recursos sensíveis | normative | explicit | deterministic |
| Requirement | `ACC-007` | Validação do modelo de acesso | normative | explicit | deterministic |
| Requirement | `ACC-008` | Revogação em tempo real | normative | explicit | deterministic |
| Requirement | `ACC-009` | Autorização baseada em atributos (ABAC) | normative | explicit | deterministic |
| Requirement | `ACC-010` | Revisão periódica de permissões | normative | explicit | deterministic |
| Requirement | `API-001` | Autenticação e autorização de chamadas API | normative | explicit | deterministic |
| Requirement | `API-002` | Endpoints desnecessários removidos ou ocultos | normative | explicit | deterministic |
| Requirement | `API-003` | Validação de input em APIs | normative | explicit | deterministic |
| Requirement | `API-004` | Rate limiting e detecção de abusos | normative | explicit | deterministic |
| Requirement | `API-005` | Protecção por TLS e certificados actualizados | normative | explicit | deterministic |
| Requirement | `API-006` | Verificação de SDKs e wrappers utilizados | normative | explicit | deterministic |
| Requirement | `API-007` | Logging e auditoria de chamadas externas | normative | explicit | deterministic |
| Requirement | `AUT-001` | MFA obrigatório | normative | explicit | deterministic |
| Requirement | `AUT-002` | Política de passwords | normative | explicit | deterministic |
| Requirement | `AUT-003` | Protecção contra brute force | normative | explicit | deterministic |
| Requirement | `AUT-004` | Revogação activa de sessões | normative | explicit | deterministic |
| Requirement | `AUT-005` | Expiração automática de sessão | normative | explicit | deterministic |
| Requirement | `AUT-006` | Proibição de credenciais em claro | normative | explicit | deterministic |
| Requirement | `AUT-007` | Suporte a autenticação federada | normative | explicit | deterministic |
| Requirement | `AUT-008` | Step-up para acções sensíveis | normative | explicit | deterministic |
| Requirement | `AUT-009` | Reautenticação para alterações críticas | normative | explicit | deterministic |
| Requirement | `AUT-010` | Alerta de acessos suspeitos | normative | explicit | deterministic |
| Requirement | `CFG-001` | Debug e flags desactivados em produção | normative | explicit | deterministic |
| Requirement | `CFG-002` | Separação de ambientes com validação automática | normative | explicit | deterministic |
| Requirement | `CFG-003` | Ausência de parâmetros hardcoded | normative | explicit | deterministic |
| Requirement | `CFG-004` | Configuração externa com permissões controladas | normative | explicit | deterministic |
| Requirement | `CFG-005` | Validação de configuração no arranque | normative | explicit | deterministic |
| Requirement | `CFG-006` | Uso de cofres e gestão segura de segredos | normative | explicit | deterministic |
| Requirement | `CFG-007` | Monitorização de drift de configuração | normative | explicit | deterministic |
| Requirement | `DST-001` | Repositórios autenticados e auditáveis | normative | explicit | deterministic |
| Requirement | `DST-002` | Aprovação para publicação pública | normative | explicit | deterministic |
| Requirement | `DST-003` | Assinatura digital ou checksum | normative | explicit | deterministic |
| Requirement | `DST-004` | Inclusão de SBOM nos artefactos | normative | explicit | deterministic |
| Requirement | `DST-005` | Acesso segregado por role e ambiente | normative | explicit | deterministic |
| Requirement | `DST-006` | Deploy apenas via pipeline validado | normative | explicit | deterministic |
| Requirement | `DST-007` | Revogação e limpeza de artefactos comprometidos | normative | explicit | deterministic |
| Requirement | `ENC-001` | Encriptação de todas as comunicações em trânsito | normative | explicit | deterministic |
| Requirement | `ENC-002` | Encriptação de dados sensíveis em repouso | normative | explicit | deterministic |
| Requirement | `ENC-003` | Algoritmos e configurações criptográficas robustas | normative | explicit | deterministic |
| Requirement | `ENC-004` | Hashing adaptativo de passwords | normative | explicit | deterministic |
| Requirement | `ENC-005` | Mascaramento de dados sensíveis em logs, outputs e respostas API | normative | explicit | deterministic |
| Requirement | `ENC-006` | Detecção e prevenção de segredos expostos em repositórios | normative | explicit | deterministic |
| Requirement | `ENC-007` | Rotação periódica de chaves e segredos | normative | explicit | deterministic |
| Requirement | `ENC-008` | Prevenção de caching de dados sensíveis no cliente | normative | explicit | deterministic |
| Requirement | `ENC-009` | Integridade verificável de dados críticos | normative | explicit | deterministic |
| Requirement | `ERR-001` | Erros não expõem dados sensíveis | normative | explicit | deterministic |
| Requirement | `ERR-002` | Mensagens genéricas no cliente | normative | explicit | deterministic |
| Requirement | `ERR-003` | Não revelar existência de recursos | normative | explicit | deterministic |
| Requirement | `ERR-004` | Mensagens localizadas e seguras | normative | explicit | deterministic |
| Requirement | `ERR-005` | Gestão padronizada e centralizada | normative | explicit | deterministic |
| Requirement | `ERR-006` | Testes automáticos para erros excessivos | normative | explicit | deterministic |
| Requirement | `ERR-007` | Logs de erro com contexto pseudonimizado | normative | explicit | deterministic |
| Requirement | `IDE-001` | Ferramentas e IDEs autorizadas | normative | explicit | deterministic |
| Requirement | `IDE-002` | Actualização e gestão de vulnerabilidades | normative | explicit | deterministic |
| Requirement | `IDE-003` | Auditoria de código gerado por ferramentas | normative | explicit | deterministic |
| Requirement | `IDE-004` | Extensões e plugins de fontes confiáveis | normative | explicit | deterministic |
| Requirement | `IDE-005` | Controlo de permissões de extensões | normative | explicit | deterministic |
| Requirement | `IDE-006` | Limitação de ambientes locais sem controlo | normative | explicit | deterministic |
| Requirement | `INT-001` | Validação de mensagens entre sistemas | normative | explicit | deterministic |
| Requirement | `INT-002` | Autenticação mútua ou tokens seguros | normative | explicit | deterministic |
| Requirement | `INT-003` | Transmissão cifrada com TLS | normative | explicit | deterministic |
| Requirement | `INT-004` | Proibição de protocolos inseguros | normative | explicit | deterministic |
| Requirement | `INT-005` | Assinatura e integridade de mensagens | normative | explicit | deterministic |
| Requirement | `INT-006` | Validação cruzada de origem e destino | normative | explicit | deterministic |
| Requirement | `INT-007` | Monitorização e detecção de padrões anómalos | normative | explicit | deterministic |
| Requirement | `INT-008` | Revisão de segurança e contrato em integrações | normative | explicit | deterministic |
| Requirement | `LOG-001` | Registo de eventos críticos | normative | explicit | deterministic |
| Requirement | `LOG-002` | Atributos mínimos em logs | normative | explicit | deterministic |
| Requirement | `LOG-003` | Protecção de integridade e acesso aos logs | normative | explicit | deterministic |
| Requirement | `LOG-004` | Análise periódica de logs | normative | explicit | deterministic |
| Requirement | `LOG-005` | Retenção mínima dos logs | normative | explicit | deterministic |
| Requirement | `LOG-006` | Envio para sistema centralizado | normative | explicit | deterministic |
| Requirement | `LOG-007` | Classificação e detecção de anomalias | normative | explicit | deterministic |
| Requirement | `LOG-008` | Alarme em falhas do mecanismo de logging | normative | explicit | deterministic |
| Requirement | `LOG-009` | Logs suportam resposta a incidentes | normative | explicit | deterministic |
| Requirement | `LOG-010` | Logging de eventos críticos de negócio | normative | explicit | deterministic |
| Requirement | `REQ-001` | Inclusão de requisitos de segurança | normative | explicit | deterministic |
| Requirement | `REQ-002` | Revisão formal de segurança dos requisitos | normative | explicit | deterministic |
| Requirement | `REQ-003` | Alinhamento com classificação de risco | normative | explicit | deterministic |
| Requirement | `REQ-004` | Versionamento e gestão de requisitos | normative | explicit | deterministic |
| Requirement | `REQ-005` | Nova análise de ameaça após alteração de requisito | normative | explicit | deterministic |
| Requirement | `REQ-006` | Rastreabilidade requisito → ameaça → teste | normative | explicit | deterministic |
| Requirement | `REQ-007` | Revisão iterativa com equipas | normative | explicit | deterministic |
| Requirement | `SES-001` | Expiração automática por inactividade | normative | explicit | deterministic |
| Requirement | `SES-002` | Logout manual e após alteração de credenciais | normative | explicit | deterministic |
| Requirement | `SES-003` | Identificadores de sessão imprevisíveis | normative | explicit | deterministic |
| Requirement | `SES-004` | Transmissão segura dos tokens | normative | explicit | deterministic |
| Requirement | `SES-005` | Ligação da sessão ao contexto do cliente | normative | explicit | deterministic |
| Requirement | `SES-006` | Revogação explícita da sessão | normative | explicit | deterministic |
| Requirement | `SES-007` | Prevenção de sessões long-lived | normative | explicit | deterministic |
| Requirement | `SES-008` | Scope, TTL e revogação de tokens JWT | normative | explicit | deterministic |
| Requirement | `VAL-001` | Validação geral de entradas externas | normative | explicit | deterministic |
| Requirement | `VAL-002` | Uso de whitelists em vez de blacklists | normative | explicit | deterministic |
| Requirement | `VAL-003` | Validadores de esquema (JSON/XML schema) | normative | explicit | deterministic |
| Requirement | `VAL-004` | Sanitização contra injecções | normative | explicit | deterministic |
| Requirement | `VAL-005` | Validação antes do uso interno | normative | explicit | deterministic |
| Requirement | `VAL-006` | Mensagens de erro seguras na validação | normative | explicit | deterministic |
| Requirement | `VAL-007` | Testes automáticos contra entradas maliciosas | normative | explicit | deterministic |
| Control | `CTRL-code-integrity-desenvolvimento-seguro-e-validacao-de-codigo-63dedd7460` | Desenvolvimento seguro e validação de código | normative | explicit | deterministic |
| Control | `CTRL-governance-capacitacao-e-onboarding-de-seguranca-f84db7abdf` | Capacitação e onboarding de segurança | normative | explicit | deterministic |
| Control | `CTRL-governance-classificacao-e-governacao-por-risco-97aceecf29` | Classificação e governação por risco | normative | explicit | deterministic |
| Control | `CTRL-infrastructure-infraestrutura-como-codigo-governada-5228bca905` | Infraestrutura como código governada | normative | explicit | deterministic |
| Control | `CTRL-supply-chain-inventario-e-analise-de-dependencias-6b0fd9f7fb` | Inventário e análise de dependências | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:catalogo-de-requisitos-do-projeto-criacao-e-manutencao` | Catálogo de requisitos do projeto (criação e manutenção) | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:definicao-de-criterios-de-validacao` | Definição de critérios de validação | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:gates-automaticos-em-ci-cd-para-requisitos-de-seguranca` | Gates automáticos em CI/CD para requisitos de segurança | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:geracao-de-sbom-e-assinatura-de-artefactos-de-build` | Geração de SBOM e assinatura de artefactos de build | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:gestao-de-excecoes-com-ttl-e-revalidacao-obrigatoria` | Gestão de Exceções com TTL e Revalidação Obrigatória | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:politica-formacao-e-procedimentos-operacionais` | Política, Formação e Procedimentos Operacionais | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:rastreabilidade-de-requisitos` | Rastreabilidade de requisitos | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:revisao-por-alteracao-relevante` | Revisão por alteração relevante | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:selecao-de-requisitos-por-criticidade` | Seleção de requisitos por criticidade | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-de-cobertura-de-testes` | Validação de cobertura de testes | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-de-tags-sec-lx-e-requisitos-no-pipeline` | Validação de tags `SEC-Lx-*` e requisitos no pipeline | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-e-aprovacao-final` | Validação e aprovação final | normative | explicit | deterministic |
| Practice | `02-requisitos-seguranca:validacao-por-requisito-dominio-req-xxx-evidencia` | Validação por requisito/domínio (REQ-XXX → evidência) | normative | explicit | deterministic |
| Threat | `None` | hybrid | normative | heuristic | bounded |

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
