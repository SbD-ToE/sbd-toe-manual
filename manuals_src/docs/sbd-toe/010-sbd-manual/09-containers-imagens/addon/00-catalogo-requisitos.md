---
id: catalogo-requisitos-containers
title: Catálogo de Requisitos de Containers e Imagens
description: Catálogo canónico de requisitos de segurança para containers e imagens (CNT-001 a CNT-012), com aplicabilidade por nível de risco e critérios de aceitação para selecção de imagens base, hardening, assinatura, scanning, políticas de runtime e acesso a registries.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:containers, CNT, imagens, hardening, runtime, rastreabilidade, L1, L2, L3, kubernetes, admission-control, supply-chain, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Containers e Imagens

## Âmbito: o container como artefacto de software sujeito a governação

Este catálogo cobre **requisitos de segurança aplicáveis ao ciclo de vida de containers e imagens** - desde a selecção da imagem base, passando pelo hardening e scanning, até à assinatura, verificação de proveniência, políticas de runtime e acesso a registries.

Containers são artefactos de software completos que encapsulam código, dependências e configuração de runtime. A sua ubiquidade em pipelines e em produção introduz vectores de risco específicos: imagens base vulneráveis, configurações permissivas, falta de proveniência verificável e ausência de políticas de execução. Estes requisitos estabelecem os controlos mínimos para que containers sejam **construídos, promovidos e executados de forma confiável e auditável**.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de OWASP Top 10 (A06), CAPEC-310, CWE-1104, CIS Benchmarks for Docker e Kubernetes, NSA/CISA Kubernetes Hardening Guide, SLSA e práticas estabelecidas para Kubernetes, Docker e registries OCI. Deve ser adaptado ao contexto de orquestração em uso e revisto com cada actualização de política de segurança de containers.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-CNT-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo CNT - Containers e Imagens

Requisitos que garantem que containers são construídos, validados, promovidos e executados com controlos de segurança proporcionais ao risco dos workloads que encapsulam.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| CNT-001 | Imagens base de origem confiável e aprovada | ✔ | ✔ | ✔ | Imagens base provenientes de lista de origens aprovadas e mantida; imagens de origem não aprovada rejeitadas em pipeline ou por admission control; decisão de selecção documentada com justificação técnica. |
| CNT-002 | Scanning de vulnerabilidades em imagens no CI/CD | ✔ | ✔ | ✔ | Scanner de containers activo em pipeline (ex: Trivy, Grype); CVEs de severidade crítica bloqueiam a promoção da imagem; relatório de scan disponível e ligado ao build. |
| CNT-003 | Imagens minimalistas - ausência de componentes não necessários | ✔ | ✔ | ✔ | Ausência de binários interactivos (curl, bash, wget, ping) não justificados; imagem distroless, scratch ou alpine como base sempre que possível; verificável por análise de layers do artefacto. |
| CNT-004 | Execução como utilizador não-root | ✔ | ✔ | ✔ | Directiva `USER` com utilizador não-root no Dockerfile ou equivalente; política de admission que rejeita containers a executar como root; evidência de enforcement activo. |
| CNT-005 | Sistema de ficheiros em modo de leitura em runtime | - | ✔ | ✔ | `readOnlyRootFilesystem: true` ou equivalente configurado; volumes com permissão de escrita limitados ao estritamente necessário e explicitamente declarados; verificável por inspecção de configuração. |
| CNT-006 | Restrição de capabilities do kernel e perfis de syscall | - | ✔ | ✔ | `drop: ALL` como padrão com capabilities adicionadas explicitamente e justificadas; seccomp profile activo (runtime default ou personalizado); ausência de `--privileged` ou `hostPID`/`hostNetwork` não justificados. |
| CNT-007 | Assinatura e verificação de proveniência de imagens | - | ✔ | ✔ | Imagens assinadas (ex: Sigstore/Cosign, Notary v2) antes de publicação em registry; verificação de assinatura enforced por admission controller antes de deploy; imagens sem assinatura válida rejeitadas. |
| CNT-008 | SBOM por imagem publicada | - | ✔ | ✔ | SBOM gerado e anexado a cada imagem publicada no registry; formato CycloneDX ou SPDX; acessível para auditoria e resposta a incidentes sem necessidade de rebuild. |
| CNT-009 | Políticas de admission control activas | - | ✔ | ✔ | Admission controller activo (OPA/Gatekeeper, Kyverno ou equivalente); políticas que bloqueiam containers privilegiados, sem user definido, com host networking ou volumes sensíveis não autorizados; logs de admissão e rejeição disponíveis. |
| CNT-010 | Renovação periódica de imagens base | ✔ | ✔ | ✔ | Rebuild periódico ou trigger automático por actualização da imagem base para incorporar patches de segurança; imagens com mais de X dias sem rebuild sinalizadas; política de renovação definida, documentada e cumprida. |
| CNT-011 | Acesso ao registry com autenticação e rastreabilidade | ✔ | ✔ | ✔ | Push e pull requerem autenticação; logs de acesso retidos pelo período definido; publicação em registries públicos requer aprovação explícita; credenciais de registry com âmbito mínimo e rotação definida. |
| CNT-012 | Isolamento de namespace e políticas de rede em Kubernetes | - | - | ✔ | Network policies activas por namespace; sem acesso inter-namespace por omissão; workloads críticos em namespaces dedicados com políticas de rede explícitas; evidência de enforcement activo. |

---

## Notas explicativas

- **CNT-001**: A selecção da imagem base deve ser uma **decisão humana explícita e documentada** - não uma herança implícita de template ou gerador de código. Imagens de bases como `ubuntu:latest` ou imagens sem maintainer verificável são insuficientes para L2/L3.
- **CNT-003**: A minimalidade da imagem reduz a superfície de ataque em caso de comprometimento de runtime. Ferramentas como `dive` ou análise de layers permitem verificar quais binários estão presentes e justificá-los.
- **CNT-006**: A restrição de capabilities é um controlo preventivo fundamental: um container com `CAP_SYS_ADMIN` ou `--privileged` tem efectivamente controlo do nó host em Kubernetes.
- **CNT-007**: A cadeia de confiança de assinatura deve ser verificada downstream no ponto de deploy - gerar a assinatura sem a verificar antes da execução não constitui controlo efectivo.
- **CNT-009**: O admission controller deve ser configurado em modo `Enforce`, não apenas `Audit`, para ser considerado um controlo efectivo. Modo audit sem enforcement é apenas observabilidade, não protecção.
- **CNT-010**: O intervalo de renovação deve ser proporcional ao risco: para workloads L3, um ciclo máximo de 30 dias é razoável; para L1, 90 dias. O critério relevante é a cobertura de patches críticos, não apenas o calendário.

---

> Para selecção e validação de imagens base, consultar [Imagens Base Seguras](./imagens-base).
> Para hardening e restrições de execução, consultar [Hardening de Containers](./hardening-containers).
> Para assinatura e cadeia de confiança, consultar [Assinatura e Cadeia de Confiança](./assinatura-cadeia-trust).
> Para políticas de runtime com OPA/Kyverno, consultar [Policies de Runtime](./policies-runtime-opa).
> Para scanning de vulnerabilidades em imagens, consultar [Vulnerabilidades em Imagens](./vulnerabilidades-imagens).
> Para SBOM de containers, consultar [Inventário SBOM de Containers](./sbom-containers).
