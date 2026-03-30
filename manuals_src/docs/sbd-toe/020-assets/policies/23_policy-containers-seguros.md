---
id: policy-containers-seguros
title: Política de Containers Seguros
description: Política organizacional que define os requisitos de segurança para a construção, scanning, assinatura, configuração de runtime e gestão de imagens de container, incluindo hardening de securityContext, policies de admissão em Kubernetes, isolamento de rede e monitorização de runtime, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, containers, Docker, Kubernetes, imagens, scanning, runtime, securityContext, OPA, Kyverno, assinatura, cap09, L1, L2, L3, governance]
sidebar_position: 23
---

# Política de Containers Seguros

## 1. Objetivo

Esta política define os requisitos de segurança para o **ciclo de vida completo de containers**: desde a escolha da imagem base, passando pela construção, scanning e assinatura, até à configuração de runtime e monitorização em produção.

Containers oferecem isolamento lógico - não isolamento de segurança por defeito. Um container sem restrições de execução (a correr como root, com capabilities excessivas, sem read-only filesystem, sem NetworkPolicy) tem potencial de impacto no nó hospedeiro e em outros workloads que compromete as vantagens de isolamento que a tecnologia poderia oferecer. A segurança em containers não é automática - é o resultado de configuração deliberada e verificação sistemática.

O objetivo desta política é garantir que:

- Imagens são construídas a partir de bases confiáveis, minimalistas e com versão fixada por digest
- Vulnerabilidades em imagens são detetadas e bloqueadas antes de produção
- Imagens em produção são assinadas e a sua integridade é verificada antes do deploy
- Configurações de runtime seguem o princípio de mínimo privilégio e são impostas por policy
- Segredos nunca estão embebidos nas imagens

---

## 2. Âmbito

Esta política aplica-se a todos os containers utilizados em ambientes de desenvolvimento, integração, staging e produção, incluindo containers de aplicação, sidecar containers e containers de infraestrutura (ex: proxies, service mesh).

---

## 3. Construção de imagens

### 3.1 Imagem base

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Imagem base de origem verificada (repositório oficial ou catálogo interno) | Obrigatório | Obrigatório | Obrigatório |
| Versão fixada por digest SHA256 (não por tag flutuante) | Recomendado | Obrigatório | Obrigatório |
| Imagem base minimalista (distroless, alpine, slim) | Recomendado | Obrigatório | Obrigatório |
| Sem ferramentas de debug desnecessárias na imagem final (curl, bash, wget) | Recomendado | Obrigatório | Obrigatório |

### 3.2 Dockerfile seguro

O Dockerfile deve seguir as seguintes práticas obrigatórias:

- [ ] Multi-stage build quando aplicável: separação entre build environment e runtime image
- [ ] `USER` definido como utilizador não-root na instrução final antes de `CMD`/`ENTRYPOINT`
- [ ] Sem `ADD` com URLs remotas (use `COPY` de contexto local)
- [ ] Sem `--privileged` ou `--cap-add` em instruções de build
- [ ] Sem segredos em `ARG`, `ENV` ou `RUN` (incluindo variáveis exportadas)
- [ ] Linter de Dockerfile (`hadolint` ou equivalente) sem findings bloqueantes

### 3.3 Registos de imagens

Em L2/L3, imagens devem ser produzidas e armazenadas em registos internos controlados:

- [ ] Registo interno como fonte de imagens em produção (não pulls directos de Docker Hub)
- [ ] Allowlist de registos externos autorizados (para imagens base)
- [ ] Acesso ao registo controlado por autenticação - sem acesso anónimo

---

## 4. Scanning de imagens

O pipeline deve incluir scanning de vulnerabilidades da imagem produzida:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| Scanner de imagens (Trivy, Grype, Clair) | Alerta | Bloqueia High/Critical | Bloqueia Medium+ |
| SBOM gerado por imagem | Recomendado | Obrigatório | Obrigatório |
| Scan de configurações do Dockerfile (hadolint) | Recomendado | Obrigatório | Obrigatório |
| Scan de segredos embebidos em camadas | Obrigatório | Obrigatório | Obrigatório |

O relatório de scanning deve ser arquivado como artefacto do pipeline, associado ao digest da imagem.

---

## 5. Assinatura e proveniência

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Imagem assinada após build (Cosign ou equivalente) | Opcional | Recomendado | Obrigatório |
| Assinatura verificada antes de deploy | Opcional | Recomendado | Obrigatório |
| Attestation de proveniência (SLSA-like) | Não aplicável | Recomendado | Obrigatório |
| Deploy bloqueado se assinatura ausente ou inválida | Não aplicável | Recomendado | Obrigatório |

Em L3, apenas imagens assinadas pelo pipeline da organização devem ser admitidas em produção. Imagens não assinadas ou com assinatura de origem desconhecida devem ser rejeitadas pelo admission controller.

---

## 6. Configuração de runtime (hardening)

### 6.1 securityContext obrigatório

Todos os containers em execução devem ter o seguinte `securityContext` configurado (Kubernetes) ou equivalente:

| Configuração | L1 | L2 | L3 |
|---|---|---|---|
| `runAsNonRoot: true` | Obrigatório | Obrigatório | Obrigatório |
| `allowPrivilegeEscalation: false` | Obrigatório | Obrigatório | Obrigatório |
| `readOnlyRootFilesystem: true` | Recomendado | Obrigatório | Obrigatório |
| `capabilities: drop: ["ALL"]` | Recomendado | Obrigatório | Obrigatório |
| `privileged: false` | Obrigatório | Obrigatório | Obrigatório |
| `seccompProfile: RuntimeDefault` (ou mais restritivo) | Recomendado | Obrigatório | Obrigatório |

### 6.2 Volumes e montagens

- [ ] Sem montagem de `/var/run/docker.sock` (acesso ao socket Docker pelo container)
- [ ] Volumes montados em modo read-only sempre que possível
- [ ] Sem partilha de namespaces do host (`hostNetwork`, `hostPID`, `hostIPC`) sem justificação formal

### 6.3 Policies de admissão (Kubernetes)

Em L2/L3 com Kubernetes, políticas de admissão devem ser impostas por admission controller (OPA/Gatekeeper, Kyverno, ou PSA):

- [ ] Políticas que enforcem `securityContext` mínimo em todos os namespaces de produção
- [ ] Violações bloqueadas e auditadas com timestamp, actor e detalhes do pod
- [ ] Políticas versionadas e aprovadas por AppSec Engineer

---

## 7. Isolamento de rede

- [ ] NetworkPolicy definida para cada namespace/workload (deny-all por defeito, permit explícito)
- [ ] Sem comunicação irrestrita entre namespaces ou entre pods sem política explícita
- [ ] Egress controlado para serviços externos necessários (whitelist de destinos)

---

## 8. Gestão de segredos em containers

Segredos não devem ser incluídos em imagens de container em nenhuma circunstância:

- [ ] Sem segredos em variáveis `ENV` no Dockerfile
- [ ] Sem segredos em `ARG` de build (persistem nas camadas da imagem)
- [ ] Segredos injectados em runtime via Kubernetes Secrets (com encriptação em repouso) ou cofre externo (Vault, AWS Secrets Manager, etc.)
- [ ] Alternativa preferida em L3: workload identity (IRSA, GKE Workload Identity, Vault Agent) - sem segredos persistidos

---

## 9. Monitorização de runtime

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Logging de eventos de runtime (início, paragem, erros) | Básico | Obrigatório | Obrigatório |
| Deteção de anomalias de runtime (Falco, eBPF-based) | Não aplicável | Recomendado | Obrigatório |
| Alertas em caso de violação de política de runtime | Não aplicável | Obrigatório | Obrigatório |
| Resposta automática a anomalias críticas (kill container) | Não aplicável | Recomendado | Recomendado |

---

## 10. Artefactos esperados

| Artefacto | Descrição | Retenção |
|---|---|---|
| Relatório de scan de imagem (Trivy/Grype) | Vulnerabilidades por build | 90 dias (L2), 1 ano (L3) |
| SBOM da imagem | Inventário por build | Ver Política de SBOM |
| Assinatura da imagem | Por build, no registo de imagens | Enquanto a imagem estiver em uso |
| Attestation de proveniência | Por build | 1 ano (L2), 2 anos (L3) |
| Logs de admissão | Violações de política no cluster | 90 dias (L2), 1 ano (L3) |

---

## 11. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Escrever Dockerfiles seguros; não incluir segredos; usar imagens base aprovadas |
| DevOps / SRE | Configurar pipeline de build e scanning; gerir registo de imagens; configurar runtime policies |
| AppSec Engineer | Definir thresholds de scanning; aprovar policies de admissão; rever configurações de securityContext |
| GRC / Compliance | Auditar relatórios de scanning; verificar conformidade de runtime policies; validar retenção |

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em vulnerabilidade de imagem ou misconfiguration de runtime
- Alteração do orquestrador de containers ou do admission controller
- Publicação de nova versão dos benchmarks CIS Docker ou Kubernetes

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 09 - Containers e Execução Isolada | Construção, scanning, runtime, SBOM, signing |
| Política de Golden Base Images (`24_policy-golden-base-images.md`) | Catálogo de imagens base aprovadas |
| Política de SBOM (`11_policy-sbom.md`) | SBOM por imagem |
| Política de Gestão de Segredos (`18_policy-gestao-segredos.md`) | Segredos em containers |
| CIS Docker Benchmark v1.6 | Controlos de referência para Docker |
| CIS Kubernetes Benchmark | Controlos de referência para Kubernetes |
| NIST SP 800-190 | Application Container Security Guide |
| ENISA Cloud Baseline | Segurança em containers - baseline europeu |
| Cosign / Sigstore | Assinatura e verificação de imagens |
| Falco | Runtime security para containers |
| OPA Gatekeeper / Kyverno | Admission controllers para Kubernetes |
