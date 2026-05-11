# 25. Rastreabilidade — Containers e Imagens

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

Total: **50 entidades** Manual ontology V2 mapped a este capítulo via `sbd-toe-knowledge-graph` canonical data (post-merge 5550a74).

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `CNT-001` | Imagens base de origem confiável e aprovada | normative | explicit | deterministic |
| Requirement | `CNT-002` | Scanning de vulnerabilidades em imagens no CI/CD | normative | explicit | deterministic |
| Requirement | `CNT-003` | Imagens minimalistas - ausência de componentes não necessários | normative | explicit | deterministic |
| Requirement | `CNT-004` | Execução como utilizador não-root | normative | explicit | deterministic |
| Requirement | `CNT-005` | Sistema de ficheiros em modo de leitura em runtime | normative | explicit | deterministic |
| Requirement | `CNT-006` | Restrição de capabilities do kernel e perfis de syscall | normative | explicit | deterministic |
| Requirement | `CNT-007` | Assinatura e verificação de proveniência de imagens | normative | explicit | deterministic |
| Requirement | `CNT-008` | SBOM por imagem publicada | normative | explicit | deterministic |
| Requirement | `CNT-009` | Políticas de admission control activas | normative | explicit | deterministic |
| Requirement | `CNT-010` | Renovação periódica de imagens base | normative | explicit | deterministic |
| Requirement | `CNT-011` | Acesso ao registry com autenticação e rastreabilidade | normative | explicit | deterministic |
| Requirement | `CNT-012` | Isolamento de namespace e políticas de rede em Kubernetes | normative | explicit | deterministic |
| Control | `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af` | Gestão de identidades, acessos e ownership | normative | explicit | deterministic |
| Control | `CTRL-secrets-gestao-de-segredos-e-identidades-operacionais-e2c86cdfe9` | Gestão de segredos e identidades operacionais | normative | explicit | deterministic |
| Control | `CTRL-supply-chain-supply-chain-segura-de-imagens-e-containers-8a8af25a4d` | Supply chain segura de imagens e containers | normative | explicit | deterministic |
| Practice | `09-containers-imagens:aplicacao-de-politicas-formais-de-seguranca-no-runtime-com-opa-kyverno` | Aplicação de políticas formais de segurança no runtime com OPA/Kyverno | normative | explicit | deterministic |
| Practice | `09-containers-imagens:aprovacao-depreciacao-e-revogacao-de-golden-base-images-catalogo-organizacional` | Aprovação, depreciação e revogação de Golden Base Images (catálogo organizaciona | normative | explicit | deterministic |
| Practice | `09-containers-imagens:assinatura-e-verificacao-de-proveniencia-de-imagens-com-cosign-e-rekor` | Assinatura e verificação de proveniência de imagens com Cosign e Rekor | normative | explicit | deterministic |
| Practice | `09-containers-imagens:builders-e-runners-ephemerais-assinados-e-com-auditoria` | Builders e Runners Ephemerais, Assinados e com Auditoria | normative | explicit | deterministic |
| Practice | `09-containers-imagens:construcao-de-imagens-a-partir-de-bases-seguras-minimalistas-e-pinned-por-digest` | Construção de imagens a partir de bases seguras, minimalistas e pinned por diges | normative | explicit | deterministic |
| Practice | `09-containers-imagens:enforcement-centralizado-e-auditavel-de-politicas-no-runtime` | Enforcement Centralizado e Auditável de Políticas no Runtime | normative | explicit | deterministic |
| Practice | `09-containers-imagens:excecoes-temporarias-a-findings-policies-com-ttl-compensacoes-e-revalidacao` | Exceções temporárias a findings/policies com TTL, compensações e revalidação | normative | explicit | deterministic |
| Practice | `09-containers-imagens:geracao-e-rastreabilidade-de-sbom-em-imagens` | Geração e Rastreabilidade de SBOM em Imagens | normative | explicit | deterministic |
| Practice | `09-containers-imagens:gestao-de-segredos-fora-da-imagem-com-oidc-e-workload-identity` | Gestão de Segredos Fora da Imagem com OIDC e Workload Identity | normative | explicit | deterministic |
| Practice | `09-containers-imagens:golden-base-images-com-patching-automatico` | Golden Base Images com Patching Automático | normative | explicit | deterministic |
| Practice | `09-containers-imagens:governacao-de-registries-com-allowlist-e-digest-only` | Governação de Registries com Allowlist e Digest-Only | normative | explicit | deterministic |
| Practice | `09-containers-imagens:monitorizacao-e-resposta-a-incidentes-em-runtime` | Monitorização e Resposta a Incidentes em Runtime | normative | explicit | deterministic |
| Practice | `09-containers-imagens:promocao-por-estagios-com-aprovacao-explicita-e-revalidacao-por-ambiente` | Promoção por estágios com aprovação explícita e revalidação por ambiente | normative | explicit | deterministic |
| Practice | `09-containers-imagens:rbac-minimo-e-serviceaccounts-dedicadas` | RBAC Mínimo e ServiceAccounts Dedicadas | normative | explicit | deterministic |
| Practice | `09-containers-imagens:sandboxing-avancado-com-gvisor-kata-para-workloads-criticas` | Sandboxing Avançado com gVisor/Kata para Workloads Críticas | normative | explicit | deterministic |
| Practice | `09-containers-imagens:segmentacao-de-rede-e-networkpolicy` | Segmentação de Rede e NetworkPolicy | normative | explicit | deterministic |
| Practice | `09-containers-imagens:validacao-automatica-de-vulnerabilidades-em-imagens-no-pipeline-ci-cd` | Validação automática de vulnerabilidades em imagens no pipeline CI/CD | normative | explicit | deterministic |
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
