---
id: kpis-metricas-containers
title: KPIs e Métricas - Containers e Imagens
sidebar_position: 11
description: Indicadores técnicos e operacionais para avaliação da eficácia dos controlos de segurança em imagens de container e ambientes de orquestração, com thresholds por nível de risco e mapeamento para dimensões transversais de governação SbD-ToE.
tags: [kpi, metricas, CNT, containers, imagens, kubernetes, admission-controller, assinatura, L1, L2, L3]
---

<!--template: sbdtoe-addon -->

# KPIs e Métricas - Containers e Imagens

## Âmbito e propósito

Os indicadores deste domínio avaliam a **segurança do ciclo de vida de imagens de container**: desde a composição e ausência de vulnerabilidades conhecidas, até à assinatura e verificação de proveniência, à aplicação de políticas de admissão em runtime, e à velocidade de resposta a CVEs críticos em imagens de produção.

Containers introduzem um desafio específico de medição: a imagem é imutável após build, mas o ecossistema de vulnerabilidades é dinâmico. Uma imagem que era segura no momento do build pode tornar-se vulnerável 48 horas depois. Os indicadores CNT devem reflectir este carácter contínuo, não apenas o estado no momento do deploy.

Os indicadores CNT alimentam as dimensões transversais **T-01 (Cobertura de controlos)**, **T-03 (Velocidade de resolução)** e **T-05 (Cadeia de fornecimento)**.

---

## Denominador e fundação de portfólio

Os indicadores deste domínio usam como denominador **F-02 - aplicações com classificação de risco formal** (Cap. 01, CLA-K01). As percentagens são interpretáveis apenas em relação ao conjunto de aplicações classificadas ao nível de risco relevante - não ao portfólio total ou a subconjuntos ad-hoc.

Ver `kpis-governanca.md` - secção "Fundação de portfólio" - para o funil de adoptabilidade SbD-ToE e a relação entre denominadores.

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Threshold obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |
| ↓ | Indicador inverso - valor menor indica melhor desempenho |

Os thresholds são cumulativos: L3 inclui todas as obrigações de L1 e L2.

**Tipos de indicador:**

| Código | Significado |
|--------|-------------|
| Q% | Quantitativo percentual |
| Q# | Quantitativo contagem |
| Qt | Quantitativo temporal (dias) |

---

## Catálogo de indicadores

| ID | Indicador | Tipo | L1 | L2 | L3 | Dim. T | Período |
|----|-----------|:----:|:--:|:--:|:--:|:------:|---------|
| CNT-K01 | % imagens em produção sem CVEs críticos (CVSS ≥ 9.0) sem excepção formal válida | Q% | ≥ 70% | ≥ 90% | 100% | T-01, T-03 | Semanal |
| CNT-K02 | MTTR - tempo desde identificação de CVE crítico em imagem de produção até substituição/patch | Qt | ≤ 14d | ≤ 7d | ≤ 3d | T-03 | Por evento |
| CNT-K03 | % imagens de produção assinadas digitalmente e com verificação de assinatura antes de deploy | Q% | - | ≥ 70% | 100% | T-01, T-05 | Por release |
| CNT-K04 | % workloads em orquestrador com política de admission controller activa e em modo de bloqueio | Q% | - | ≥ 80% | 100% | T-01 | Mensal |
| CNT-K05 | % imagens base de produção actualizadas dentro do ciclo definido por política (sem tags mutáveis) | Q% | ≥ 70% | ≥ 90% | 100% | T-01, T-05 | Mensal |
| CNT-K06 | % imagens com SBOM associado e acessível no registo ou repositório de artefactos | Q% | ≥ 50% | ≥ 85% | 100% | T-05 | Por release |
| CNT-K07 | # workloads em execução como root (UID 0) sem justificação técnica formal | Q# ↓ | ≤ 5 | = 0 | = 0 | T-01 | Semanal |

---

## Definições complementares

**CNT-K01 - CVE sem excepção formal:** uma imagem está conforme se não tiver CVEs críticos, ou se os CVEs identificados tiverem excepção formal activa (não expirada) com compensação documentada. Imagens com CVEs críticos sem excepção, mesmo que o patch não esteja disponível, não satisfazem este indicador - devem ter excepção formal.

**CNT-K02 - MTTR de container:** conta desde a data de disponibilização da CVE em NVD/OSV (ou detecção pelo scanner, se posterior) até à data de deploy em produção da imagem corrigida. Se o patch não está disponível no upstream, a substituição da imagem base por uma alternativa sem a vulnerabilidade também fecha o indicador.

**CNT-K03 - Verificação de assinatura:** a existência de assinatura sem processo de verificação antes do deploy não satisfaz este indicador. A verificação pode ser implementada via admission controller (Kyverno + verificação Cosign), ou verificação explícita no pipeline de deploy com log rastreável.

**CNT-K04 - Admission controller em modo bloqueio:** policies configuradas em modo `audit` ou `warn` não satisfazem este critério. Apenas `enforce` (Kyverno) ou `Deny` (OPA Gatekeeper) contam. Excepções a políticas devem ser objectos formais no orquestrador (não desactivação global).

**CNT-K05 - Tag mutável:** uma tag mutável (ex: `latest`, `stable`, `main`) aponta para diferentes camadas ao longo do tempo, tornando impossível garantir a reprodutibilidade e a auditabilidade do que está em produção. Tags imutáveis requerem referência por digest (`image@sha256:...`) ou por tag semântica fixada e imutável no registo.

**CNT-K07 - Execução como root:** inclui containers com `securityContext.runAsUser: 0` explícito ou sem `runAsNonRoot: true` definido. Aplicações legadas com justificação formal e compensação activa (ex: seccomp, AppArmor, capacidades restritas) podem ter excepção, mas são contabilizadas neste indicador até à resolução.

---

## Recolha e instrumentação

| Indicador | Fonte primária | Ferramentas de referência | Automação |
|-----------|---------------|--------------------------|-----------|
| CNT-K01 | Scanner de vulnerabilidades de imagens + registo de excepções | Trivy, Grype, Snyk Container + DefectDojo | Sim |
| CNT-K02 | CVE feed + deploy log + scan histórico | NVD/OSV + pipeline timestamps | Parcial |
| CNT-K03 | Registo de imagens + logs de deploy | Cosign, Notary + admission controller logs | Sim |
| CNT-K04 | Configuração do orquestrador (Kubernetes manifests) | Kyverno, OPA Gatekeeper, Polaris | Sim |
| CNT-K05 | Registo de imagens + política de update | Dependabot for containers, Renovate, Trivy advisories | Sim |
| CNT-K06 | Registo de artefactos + processo de build | Syft + registo OCI com suporte a SBOM attach | Sim |
| CNT-K07 | Configuração de workloads no orquestrador | Kube-bench, Polaris, Checkov (Kubernetes) | Sim |

---

## Referências cruzadas

| Documento | Relação |
|-----------|---------|
| `addon/00-catalogo-requisitos.md` | Requisitos CNT-001..012 que fundamentam os indicadores |
| `addon/10-excecoes-containers.md` | Processo de excepção de containers (CNT-K01, CNT-K04) |
| `addon/07-vulnerabilidades-imagens.md` | Gestão de vulnerabilidades que alimenta CNT-K01/K02 |
| Cap. 14 `addon/kpis-governanca.md` | Dimensões transversais T-01, T-03, T-05 |
