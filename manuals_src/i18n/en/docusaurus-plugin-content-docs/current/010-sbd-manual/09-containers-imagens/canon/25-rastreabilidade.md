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
translation:
  source_locale: pt
  source_path: 010-sbd-manual/09-containers-imagens/canon/25-rastreabilidade.md
  source_sha256: 6bfd0cee00508e3f8298874f9fc2cc3c83785d9b1a1e483f66bf87e630ad0c06
  source_commit: b1ef4e10cdccc51fc470937a9a2504a7d2f12142
  target_sha256: 2355028503b83be70d06e49e43527dfb30ce1610bcf4b57de43bffb0c5e18df3
  engine: claude-opus-5-5
  prompt_sha256: 08d32de4a4f6d574fc1f0eafc6b83ac308535546bb6b11a18a339b25053005c0
  terms_sha256: 153599a2c96a49fbaadae86b2e07971761ed2be92b9effb3351f1cbec07dcc99
  glossary_keys: [appsec_core, audit_trail, chapter_role, practitioner_manual, provenance, slice, slug_threat_modeling, traceability, validation_evaluation, verificacao_check, verification_taxonomy]
  glossary_sha256: ca11032db817b35c89b411f41e24147f8f6face065c251192d124b526ea3a0bb
  translated_at: 2026-09-28T09:12:13Z
  stamped_at: 2026-09-28T09:12:13Z
  reviewed_by: null
---

# 25. Traceability — Containers and Images

## Summary {#sumário}

This chapter **is not the primary anchor** of any AppSec Core V1 slice. The external references relevant to this domain are found in the chapters where each slice is primarily anchored.

| Slice | Description | Anchored in |
|---|---|---|
| `ACO-ATB` | Secure architecture and trust boundaries | Ch. 04 (04-arquitetura-segura) |
| `ACO-IAT` | Identity, authentication and session management | Ch. 04 (04-arquitetura-segura) |
| `ACO-ITS` | Integration and service-to-service security | Ch. 04 (04-arquitetura-segura) |
| `ACO-IVF` | Input validation, secure parsing and controlled error handling | Ch. 06 (06-desenvolvimento-seguro) |
| `ACO-RPR` | Release promotion, controlled rollout and rollback readiness | Ch. 11 (11-deploy-seguro) |
| `ACO-SCBI` | Software supply chain and build integrity | Ch. 05 (05-dependencias-sbom-sca) |
| `ACO-SLG` | Security event logging and audit trail | Ch. 12 (12-monitorizacao-operacoes) |
| `ACO-SPC` | Secrets management, protected configuration and operational identities | Ch. 06 (06-desenvolvimento-seguro) |
| `ACO-TMR` | Threat modelling, risk management and mitigation traceability | Ch. 03 (03-threat-modeling) |
| `ACO-TSV` | Security testing and empirical validation | Ch. 10 (10-testes-seguranca) |

---

## § Manual ontology V2 — canonical entities of this chapter {#-manual-ontology-v2--entities-canónicas-deste-capítulo}

Total: **67 entities** of Manual ontology V2 mapped to this chapter.

| Entity type | ID | Label | Authority class | Source mode | Confidence |
|---|---|---|---|---|---|
| Requirement | `CNT-001` | Base images from a trusted and approved origin | normative | explicit | deterministic |
| Requirement | `CNT-002` | Vulnerability scanning of images in CI/CD | normative | explicit | deterministic |
| Requirement | `CNT-003` | Minimalist images - absence of unnecessary components | normative | explicit | deterministic |
| Requirement | `CNT-004` | Execution as a non-root user | normative | explicit | deterministic |
| Requirement | `CNT-005` | Read-only file system at runtime | normative | explicit | deterministic |
| Requirement | `CNT-006` | Restriction of kernel capabilities and syscall profiles | normative | explicit | deterministic |
| Requirement | `CNT-007` | Signing and provenance verification of images | normative | explicit | deterministic |
| Requirement | `CNT-008` | SBOM per published image | normative | explicit | deterministic |
| Requirement | `CNT-009` | Active admission control policies | normative | explicit | deterministic |
| Requirement | `CNT-010` | Periodic renewal of base images | normative | explicit | deterministic |
| Requirement | `CNT-011` | Registry access with authentication and traceability | normative | explicit | deterministic |
| Requirement | `CNT-012` | Namespace isolation and network policies in Kubernetes | normative | explicit | deterministic |
| Control | `CTRL-identity-gestao-de-identidades-acessos-e-ownership-d0919c69af` | Management of identities, access and ownership | normative | explicit | deterministic |
| Control | `CTRL-secrets-gestao-de-segredos-e-identidades-operacionais-e2c86cdfe9` | Management of secrets and operational identities | normative | explicit | deterministic |
| Control | `CTRL-supply-chain-supply-chain-segura-de-imagens-e-containers-8a8af25a4d` | Secure supply chain of images and containers | normative | explicit | deterministic |
| Practice | `09-containers-imagens:aplicacao-de-politicas-formais-de-seguranca-no-runtime-com-opa-kyverno` | Application of formal security policies at runtime with OPA/Kyverno | normative | explicit | deterministic |
| Practice | `09-containers-imagens:aprovacao-depreciacao-e-revogacao-de-golden-base-images-catalogo-organizacional` | Approval, deprecation and revocation of Golden Base Images (organisational catalogue) | normative | explicit | deterministic |
| Practice | `09-containers-imagens:assinatura-e-verificacao-de-proveniencia-de-imagens-com-cosign-e-rekor` | Signing and provenance verification of images with Cosign and Rekor | normative | explicit | deterministic |
| Practice | `09-containers-imagens:builders-e-runners-ephemerais-assinados-e-com-auditoria` | Ephemeral, Signed and Audited Builders and Runners | normative | explicit | deterministic |
| Practice | `09-containers-imagens:construcao-de-imagens-a-partir-de-bases-seguras-minimalistas-e-pinned-por-digest` | Building images from secure, minimalist bases pinned by digest | normative | explicit | deterministic |
| Practice | `09-containers-imagens:enforcement-centralizado-e-auditavel-de-politicas-no-runtime` | Centralised and Auditable Enforcement of Policies at Runtime | normative | explicit | deterministic |
| Practice | `09-containers-imagens:excecoes-temporarias-a-findings-policies-com-ttl-compensacoes-e-revalidacao` | Temporary exceptions to findings/policies with TTL, compensations and revalidation | normative | explicit | deterministic |
| Practice | `09-containers-imagens:geracao-e-rastreabilidade-de-sbom-em-imagens` | Generation and Traceability of SBOM in Images | normative | explicit | deterministic |
| Practice | `09-containers-imagens:gestao-de-segredos-fora-da-imagem-com-oidc-e-workload-identity` | Secrets Management Outside the Image with OIDC and Workload Identity | normative | explicit | deterministic |
| Practice | `09-containers-imagens:golden-base-images-com-patching-automatico` | Golden Base Images with Automatic Patching | normative | explicit | deterministic |
| Practice | `09-containers-imagens:governacao-de-registries-com-allowlist-e-digest-only` | Registry Governance with Allowlist and Digest-Only | normative | explicit | deterministic |
| Practice | `09-containers-imagens:monitorizacao-e-resposta-a-incidentes-em-runtime` | Runtime Monitoring and Incident Response | normative | explicit | deterministic |
| Practice | `09-containers-imagens:promocao-por-estagios-com-aprovacao-explicita-e-revalidacao-por-ambiente` | Staged promotion with explicit approval and revalidation per environment | normative | explicit | deterministic |
| Practice | `09-containers-imagens:rbac-minimo-e-serviceaccounts-dedicadas` | Minimal RBAC and Dedicated ServiceAccounts | normative | explicit | deterministic |
| Practice | `09-containers-imagens:sandboxing-avancado-com-gvisor-kata-para-workloads-criticas` | Advanced Sandboxing with gVisor/Kata for Critical Workloads | normative | explicit | deterministic |
| Practice | `09-containers-imagens:segmentacao-de-rede-e-networkpolicy` | Network Segmentation and NetworkPolicy | normative | explicit | deterministic |
| Practice | `09-containers-imagens:validacao-automatica-de-vulnerabilidades-em-imagens-no-pipeline-ci-cd` | Automatic validation of vulnerabilities in images in the CI/CD pipeline | normative | explicit | deterministic |
| Threat | `MT-149` | Vulnerable/obsolete base images | normative | heuristic | bounded |
| Threat | `MT-150` | Inclusion of insecure dependencies in the build | normative | heuristic | bounded |
| Threat | `MT-151` | Unexpected content in the build _context_ | normative | heuristic | bounded |
| Threat | `MT-152` | Insecure configurations in the Dockerfile | normative | heuristic | bounded |
| Threat | `MT-153` | Unsigned images / without verification | normative | heuristic | bounded |
| Threat | `MT-154` | Malicious substitution in the registry | normative | heuristic | bounded |
| Threat | `MT-155` | Lack of an audit trail (who built what) | normative | heuristic | bounded |
| Threat | `MT-156` | Execution as root / excessive capabilities | normative | heuristic | bounded |
| Threat | `MT-157` | Insecure mounts and volumes | normative | heuristic | bounded |
| Threat | `MT-158` | Lack of network policies | normative | heuristic | bounded |
| Threat | `MT-159` | Permissive _admission_ | normative | heuristic | bounded |
| Threat | `MT-160` | Secrets embedded in the image | normative | heuristic | bounded |
| Threat | `MT-161` | Exposure in environment variables | normative | heuristic | bounded |
| Threat | `MT-162` | Insecure manifests approved | normative | heuristic | bounded |
| Threat | `MT-163` | Image↔manifest misalignment | normative | heuristic | bounded |
| Threat | `MT-164` | Lack of traceability of deploys | normative | heuristic | bounded |
| Threat | `MT-165` | _Shadow containers_ outside the pipeline | normative | heuristic | bounded |
| Threat | `MT-166` | Configuration _drift_ | normative | heuristic | bounded |

> Authority class / source mode / confidence model: as defined by the Manual ontology (v2).
