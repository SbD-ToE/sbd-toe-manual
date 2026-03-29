---
id: policy-cicd-seguro
title: Política de CI/CD Seguro
description: Política organizacional que define os requisitos de segurança para pipelines de integração e entrega contínua, incluindo gates obrigatórios, scanners integrados, separação de ambientes, assinatura de artefactos, gestão de segredos no pipeline e aprovações de promoção, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, CI/CD, pipeline, SAST, SCA, secret detection, gates, assinatura, artefactos, separação de ambientes, cap07, L1, L2, L3, governance, DevSecOps]
sidebar_position: 17
---

# Política de CI/CD Seguro

## 1. Objetivo

Esta política define os requisitos de segurança aplicáveis ao **design, configuração e operação de pipelines de integração e entrega contínua (CI/CD)** para aplicações classificadas como L1, L2 ou L3.

O pipeline CI/CD é um componente crítico da postura de segurança de uma organização: é o caminho pelo qual o código chega a produção. Um pipeline comprometido, mal configurado ou sem controlos adequados é equivalente a uma porta de serviço sem cadeado — pode ser usado para introduzir código malicioso, escalar privilégios, ou exfiltrar segredos sem que o processo de revisão de código seja relevante.

O objetivo desta política é garantir que:

- Os pipelines são configurados com segurança e versionados como código
- Os gates de segurança são automatizados, com thresholds documentados e bloqueantes
- Os segredos usados no pipeline são geridos de forma centralizada e nunca expostos em logs
- A promoção entre ambientes é controlada e requer aprovação proporcional ao risco
- Os artefactos produzidos são assinados e verificados antes de qualquer deploy

---

## 2. Âmbito

Esta política aplica-se a todos os pipelines CI/CD que produzam artefactos destinados a ambientes de teste, homologação ou produção, incluindo pipelines de build, teste, análise, empacotamento, containerização e deploy.

---

## 3. Pipeline como código versionado

O pipeline deve ser definido como código, versionado no repositório da aplicação, sujeito a revisão de código e com alterações rastreáveis:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Pipeline definido como código (`ci-pipeline.yml` ou equivalente) | Obrigatório | Obrigatório | Obrigatório |
| Alterações ao pipeline sujeitas a revisão de código e aprovação | Recomendado | Obrigatório | Obrigatório + AppSec |
| Pipeline versionado no mesmo repositório da aplicação (ou monorepo controlado) | Obrigatório | Obrigatório | Obrigatório |
| Sem edição direta do pipeline em ambiente de execução (sem manual override) | Recomendado | Obrigatório | Obrigatório |

---

## 4. Gates de segurança obrigatórios

Os seguintes gates devem ser configurados no pipeline, com thresholds documentados e comportamento bloqueante conforme a tabela de proporcionalidade:

### 4.1 Gates de análise de código e dependências

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| **Secret detection** (TruffleHog, Gitleaks, detect-secrets) | Alerta | Bloqueia qualquer finding | Bloqueia qualquer finding |
| **SAST** (Semgrep, CodeQL, SonarQube, Bandit) | Alerta | Bloqueia High/Critical | Bloqueia Medium+ |
| **Linters de segurança** por stack | Recomendado | Obrigatório | Obrigatório |
| **SCA** (Dependency-Check, Trivy, Grype) | Alerta | Bloqueia High/Critical | Bloqueia Medium+ |
| **Validação de licenças** | Recomendado | Obrigatório | Obrigatório |

### 4.2 Gates de build e artefactos

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| **Geração de SBOM** por build | Obrigatório (básico) | Obrigatório (completo) | Obrigatório (completo + assinado) |
| **Assinatura de artefactos** (Cosign ou equivalente) | Recomendado | Obrigatório | Obrigatório |
| **Verificação de assinatura** antes de promoção | Não aplicável | Obrigatório | Obrigatório |
| **Scan de vulnerabilidades em imagens container** | Recomendado | Obrigatório | Obrigatório |

### 4.3 Regras gerais de gates

- Os thresholds (severidade mínima de bloqueio) devem ser documentados e versionados (`gates-config.yaml` ou equivalente)
- A alteração de um threshold requer aprovação de AppSec Engineer
- Um gate desativado ou com threshold reduzido temporariamente deve ser registado como exceção formal

:::warning
Gates configurados em modo "warn-only" (sem bloqueio) em L2/L3 não cumprem esta política, exceto durante período de exceção formalmente aprovado com data de expiração definida.
:::

---

## 5. Gestão de segredos no pipeline

Segredos usados no pipeline (tokens de CI, chaves de deploy, credenciais de registo, etc.) devem ser geridos de acordo com a Política de Gestão de Segredos. Os princípios específicos para o contexto do pipeline são:

- [ ] Segredos injetados por variáveis de ambiente geridas pelo sistema de CI, nunca hardcoded no ficheiro de pipeline
- [ ] Segredos nunca impressos em logs (configuração de masking obrigatória)
- [ ] Acesso a segredos de produção restrito a jobs que genuinamente necessitam (princípio de mínimo privilégio)
- [ ] Segredos rotacionados conforme política; rotação verificável sem alteração do pipeline
- [ ] Sem segredos em artefactos de build (imagens, JARs, pacotes)

---

## 6. Separação de ambientes e promoção controlada

O pipeline deve implementar separação física ou lógica entre ambientes (desenvolvimento, integração, staging, produção), com promoção controlada:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Ambientes separados com credenciais distintas | Recomendado | Obrigatório | Obrigatório |
| Promoção a staging requer CI verde + gates OK | Recomendado | Obrigatório | Obrigatório |
| Promoção a produção requer aprovação humana | Recomendado | Obrigatório | Obrigatório (dupla aprovação) |
| Promoção a produção usa artefacto imutável do build (não rebuild) | Recomendado | Obrigatório | Obrigatório |
| Rollback automático disponível em caso de falha de health check | Recomendado | Obrigatório | Obrigatório |

A identidade que executa o deploy em produção deve ter permissões mínimas — o pipeline nunca deve ter acesso de escrita em infraestrutura de desenvolvimento e produção simultaneamente.

---

## 7. Identidade e permissões do pipeline

O sistema de CI/CD opera com identidades próprias (service accounts, tokens de CI) que devem seguir o princípio do mínimo privilégio:

- [ ] Cada pipeline tem identidade dedicada; sem uso de credenciais pessoais de developers
- [ ] Permissões do pipeline limitadas ao necessário para cada job (leitura de código, escrita em registo de imagens, deploy em ambiente específico)
- [ ] Tokens de CI com TTL curto; rotação automatizada
- [ ] Auditoria de acessos do pipeline ativa em L3
- [ ] Sem permissão de aprovação de PRs pela identidade do pipeline (evita self-merge automatizado)

---

## 8. Reprodutibilidade e rastreabilidade

Cada execução de pipeline deve ser rastreável:

- [ ] Logs de execução retidos conforme Política de Rastreabilidade (mínimo 90 dias em L2, 1 ano em L3)
- [ ] Artefactos de build associados ao commit SHA que os originou
- [ ] SBOM associado ao artefacto produzido
- [ ] Resultados de scanners arquivados como artefactos da execução
- [ ] Aprovações de promoção registadas com identidade do aprovador, timestamp e referência ao artefacto aprovado

---

## 9. Integridade do pipeline

O próprio pipeline é um vector de ataque — deve ser tratado com o mesmo rigor que o código de aplicação:

- [ ] Dependências do pipeline (actions, plugins, steps externos) fixadas a versões específicas com hash (ex: `uses: actions/checkout@sha256:abc...`)
- [ ] Sem uso de `latest` em steps de pipeline em L2/L3
- [ ] Actions ou plugins externos avaliados antes de adoção (origem, manutenção, permissões requeridas)
- [ ] Pipeline não executa código arbitrário a partir de input de PRs externos sem sandbox adequado

---

## 10. Artefactos esperados

| Artefacto | Descrição | Retenção |
|---|---|---|
| `ci-pipeline.yml` | Definição do pipeline versionada | Histórico de versões |
| Logs de execução | Output completo de cada run | 90 dias (L2), 1 ano (L3) |
| Relatórios de scanners (SAST, SCA, secrets) | Resultados por run, ligados ao commit | 90 dias (L2), 1 ano (L3) |
| SBOM por build | Ver Política de SBOM | Ver Política de SBOM |
| Registos de aprovação de promoção | Identidade, timestamp, artefacto aprovado | 1 ano (L2), 2 anos (L3) |
| Configuração de gates/thresholds | Thresholds documentados e versionados | Histórico de versões |

---

## 11. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Manter pipeline como código; submeter alterações ao pipeline a revisão |
| DevOps / SRE | Configurar e operar a plataforma CI/CD; gerir identidades do pipeline; configurar separação de ambientes |
| AppSec Engineer | Definir thresholds de gates; aprovar alterações a configurações de segurança do pipeline; rever uso de actions externas |
| Tech Lead | Aprovar promoções a produção conforme requisitos do nível |
| GRC / Compliance | Auditar logs e registos de aprovação; verificar conformidade com thresholds definidos |

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem no pipeline (comprometimento, promoção de código vulnerável)
- Adoção de nova plataforma de CI/CD
- Alteração significativa nas ferramentas de análise integradas

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 07 — CI/CD Seguro | Gates, scanners, artefactos, separação de ambientes |
| SbD-ToE Cap. 05 — Dependências, SBOM e SCA | SCA e SBOM no pipeline |
| SbD-ToE Cap. 11 — Deploy Seguro | Gates de aprovação de promoção |
| Política de Gestão de Segredos (`18_policy-gestao-segredos.md`) | Segredos no pipeline |
| Política de SBOM (`11_policy-sbom.md`) | Geração e arquivo de SBOM por build |
| SLSA Framework | Níveis de integridade de supply chain do pipeline |
| OWASP CI/CD Security Top 10 | Riscos de segurança em pipelines CI/CD |
| CIS Software Supply Chain Security Guide | Controlos de referência para pipelines seguros |
| NIST SP 800-218 (SSDF) | PO.3, PW.8: infraestrutura segura e proteção de builds |
