---
id: policy-sbom
title: Política de SBOM (Software Bill of Materials)
description: Política organizacional que define os requisitos de geração, formato, assinatura, proveniência, arquivamento e retenção de SBOMs (Software Bill of Materials) em builds de software, contentor e IaC, proporcional ao nível de criticidade da aplicação (L1, L2, L3).
tags: [policy, SBOM, CycloneDX, SPDX, proveniência, assinatura, supply chain, cap05, cap07, cap09, L1, L2, L3, governance, rastreabilidade]
grupo: supply-chain
sidebar_position: 11
---

# Política de SBOM (Software Bill of Materials)

## 1. Objetivo

Esta política define os requisitos para a **geração, assinatura, arquivamento e retenção de Software Bills of Materials (SBOM)** em todos os builds de software produzidos ou operados pela organização.

Um SBOM é o inventário completo e verificável dos componentes que compõem um artefacto de software - dependências diretas, transitivas, versões, licenças e hashes. Sem SBOM, a resposta a um CVE requer pesquisa manual, a auditoria de supply chain é especulativa e a demonstração de conformidade regulatória torna-se impossível.

O objetivo desta política é garantir que:

- Cada build produz um SBOM completo, em formato normalizado, assinado e rastreável
- O SBOM está associado ao artefacto que inventaria e é verificável antes do deploy
- O inventário de componentes em produção é correlacionável com SBOMs de build
- Os SBOMs são retidos conforme os prazos definidos e acessíveis para auditoria

---

## 2. Âmbito

Esta política aplica-se a todos os builds que produzam artefactos destinados a ambientes de teste, homologação ou produção, incluindo:

- Artefactos de software (binários, packages, JARs, wheels, npm packages, etc.)
- Imagens de container (Docker/OCI)
- Artefactos IaC quando incluam dependências de terceiros (módulos Terraform, Helm charts, etc.)

---

## 3. Formato e conteúdo mínimo

### 3.1 Formatos aceites

| Formato | Versão mínima | Notas |
|---|---|---|
| **CycloneDX** | 1.4 | Formato preferido; suporte nativo em Trivy, Syft, cdxgen |
| **SPDX** | 2.3 | Aceite; interoperável com ferramentas de auditoria |

Os SBOMs devem ser produzidos em formato JSON ou XML. Formatos proprietários não são aceites como substitutos.

### 3.2 Conteúdo mínimo obrigatório

- [ ] Metadados do artefacto: nome, versão, hash do build (SHA-256 ou superior)
- [ ] Referência ao commit SHA que originou o build
- [ ] Lista completa de componentes diretos e transitivos com nome, versão e hash
- [ ] Licença de cada componente (quando disponível)
- [ ] Relações de dependência entre componentes
- [ ] Timestamp de geração e identificador do pipeline

### 3.3 Conteúdo adicional obrigatório em L3

- [ ] Proveniência completa: quem construiu, quando, a partir de que commit, em que pipeline
- [ ] Assinatura criptográfica do SBOM (ver secção 5)
- [ ] Attestation do pipeline (SLSA-like) associada ao SBOM

---

## 4. Obrigatoriedade de geração

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| SBOM gerado em cada build | Obrigatório (básico) | Obrigatório (completo) | Obrigatório (completo + assinado) |
| SBOM inclui dependências transitivas | Recomendado | Obrigatório | Obrigatório |
| SBOM associado ao artefacto de release | Recomendado | Obrigatório | Obrigatório |
| SBOM para imagens de container | Recomendado | Obrigatório | Obrigatório |
| SBOM arquivado como artefacto do pipeline | Recomendado | Obrigatório | Obrigatório |

A geração do SBOM deve ser automatizada no pipeline - não é aceitável geração manual ou ad-hoc como substituto do SBOM de build.

---

## 5. Assinatura e verificação de integridade

### 5.1 Assinatura do SBOM

Em L2 e L3, o SBOM deve ser assinado com uma chave gerida centralmente:

- [ ] SBOM assinado com chave privada gerida pelo DevOps/SRE (ex: Cosign, GPG)
- [ ] Chave pública de verificação publicada e acessível
- [ ] Procedimento de rotação de chaves documentado e executado periodicamente
- [ ] Assinatura armazenada junto ao SBOM ou no registo de artefactos

### 5.2 Verificação antes do deploy

Em L2 e L3, o pipeline de deploy deve verificar a assinatura do SBOM e do artefacto antes de proceder à promoção:

- [ ] Job de verificação de assinatura executado antes do deploy
- [ ] Deploy bloqueado se assinatura ausente ou inválida (L3: obrigatório; L2: recomendado)
- [ ] Resultado da verificação registado no log do pipeline

---

## 6. Proveniência

O SBOM deve ser acompanhado de metadados de proveniência que permitam responder a:

- **Quem construiu**: identidade do sistema de CI (não de uma pessoa individual)
- **Quando**: timestamp com precisão de segundo, em UTC
- **A partir de quê**: commit SHA, repositório, branch/tag de release
- **Como**: pipeline, job e versão das ferramentas de build utilizadas

Em L3, a proveniência deve ser registada em `attestation-<build>.json` em formato SLSA ou equivalente, assinada e arquivada com o SBOM.

---

## 7. Inventário em produção

O SBOM de build não é suficiente para garantir visibilidade completa em produção. É necessário manter um **inventário de componentes efetivamente implantados** por serviço e ambiente:

- [ ] `inventario-runtime-<servico>-<ambiente>.json` gerado e atualizado por cada deploy
- [ ] Correlação entre SBOM de build e inventário de runtime para deteção de drift
- [ ] Alertas configurados quando CVE publicado afeta componente presente no inventário de runtime

O inventário de runtime é a base para a correlação de alertas de CVE pós-deploy (ver Política de Dependências e Política de Exceções a CVEs).

---

## 8. Arquivamento e retenção

### 8.1 Localização

Os SBOMs devem ser arquivados como artefactos do pipeline CI/CD ou em repositório dedicado de evidências, com controlo de acesso adequado:

- Não devem ser armazenados apenas localmente na máquina de build
- Devem ser acessíveis para auditoria sem dependência de ambientes efémeros

### 8.2 Prazos de retenção mínimos

| Artefacto | L1 | L2 | L3 |
|---|---|---|---|
| SBOM por build | Por release | 1 ano | 2 anos |
| SBOM da versão em produção (ativo) | Enquanto em produção | Enquanto em produção | Enquanto em produção |
| Attestation de proveniência | Por release | 1 ano | 2 anos |

:::note
Em contextos regulados (DORA, NIS2, saúde, financeiro), os prazos de retenção podem ser superiores. Prevalecem sempre os requisitos regulatórios aplicáveis.
:::

---

## 9. Ferramentas de referência

| Ferramenta | Uso principal |
|---|---|
| **Syft** | Geração de SBOM a partir de imagens, sistemas de ficheiros, packages |
| **Trivy** | Geração de SBOM + SCA integrado |
| **cdxgen** | Geração de SBOM CycloneDX por ecossistema |
| **Cosign** | Assinatura e verificação de imagens e SBOMs |
| **SLSA** | Framework de proveniência e integridade de build |
| **Grype** | Análise SCA sobre SBOM existente |

A organização pode adotar ferramentas alternativas desde que suportem os formatos CycloneDX ou SPDX e permitam assinatura verificável.

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer | Garantir que o manifesto de dependências está atualizado e completo antes do build |
| DevOps / SRE | Integrar geração de SBOM no pipeline; gerir chaves de assinatura; configurar arquivo e retenção |
| AppSec Engineer | Definir requisitos de conteúdo e formato; verificar completude em auditorias; calibrar alertas de CVE |
| GRC / Compliance | Verificar conformidade com prazos de retenção; disponibilizar SBOMs em auditorias |

---

## 11. Anexo — AI BOM (Bill of Materials para componentes AI)

Quando o sistema inclui componentes AI — modelos, datasets, MCP servers/tools, prompts embebidos — geramos um **AI BOM** em formato standardizado por *build*, ligado ao SBOM principal. Não é um inventário separado em paralelo; é uma extensão do SBOM principal com campos próprios para componentes opacos da supply chain AI.

### 11.1 Formato preferido

**CycloneDX 1.6 com extensão `ml-bom`** (publicada em 2024 pela OWASP). Alternativas reconhecidas: SPDX 3.0 AI Profile; formatos proprietários do *provider* quando consumíveis pelo *pipeline* de governança da organização.

### 11.2 Conteúdo mínimo

Para além dos campos comuns a todos os componentes:

- **Modelos**: `model_id`, `version` (fixa), `sha256`, `provider`, `capabilities`, `license`, `provenance`
- **Datasets**: `dataset_id`, `version`, `source`, `hash`, `curation_process`
- **MCP servers/tools**: `server_id`, `version`, `scopes`, `source`, `audit_log_sink`
- **Prompts embebidos**: `prompt_id`, `version` (commit SHA), `owner`, tipo (`system|rag|skill`)
- **Providers**: lista com `name`, `risk_classification`, `contract_ref`, cláusulas críticas

### 11.3 Obrigatoriedade

| Nível | Geração do AI BOM | Notas |
|---|---|---|
| L1 | Recomendado | Formato simples aceitável |
| L2 | Obrigatório | Formato standard (CycloneDX 1.6 `ml-bom` preferido) |
| L3 | Obrigatório + revisão GRC | Cláusulas contratuais detalhadas no campo `providers`; cross-link com cross-check AI Act quando aplicável |

### 11.4 Operação detalhada

A operação completa do AI BOM — geração, *pinning*, lista de *providers* aprovados, resposta a incidentes *upstream* — vive em [Policy 39 — AI BOM e Supply Chain](./policy-ai-bom-supply-chain). Esta política mantém-se como referência da disciplina SBOM em geral; Policy 39 especializa-se na fatia AI.

> 📌 Em curto: SBOM cobre o que vem do *package manager*; AI BOM cobre o que vem de *model registries*, *dataset hubs* e MCP servers. Disciplina equivalente, formato compatível, processo coerente.

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Publicação de nova versão major do formato CycloneDX ou SPDX
- Publicação de nova versão da especificação CycloneDX `ml-bom` ou SPDX AI Profile
- Alteração regulatória que imponha requisitos adicionais de SBOM (ex: EU Cyber Resilience Act, EU AI Act Art. 25)
- Incidente com origem em componente não inventariado (SBOM ou AI BOM)

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 05 - Dependências, SBOM e SCA | Geração, correlação com SCA, inventário de runtime; **DEP-012 AI BOM**; **US-14** |
| SbD-ToE Cap. 07 - CI/CD Seguro | Integração SBOM no pipeline de build e release |
| SbD-ToE Cap. 09 - Containers e Imagens | SBOM por camada de imagem |
| Política de Dependências (`10_policy-dependencias.md`) | Aprovação e rastreabilidade de componentes; anexo Providers AI |
| Política de AI BOM (`39_policy-ai-bom-supply-chain.md`) | Tratamento específico de modelos, datasets, MCP, prompts |
| Política de Rastreabilidade (`06_policy-rastreabilidade.md`) | Arquivo e retenção de artefactos de build |
| CycloneDX 1.6 `ml-bom` (OWASP, 2024) | Formato preferido para AI BOM |
| SPDX 3.0 AI Profile | Formato alternativo para AI BOM |
| CycloneDX Specification | Formato SBOM preferido |
| SPDX Specification (SPDX 2.3) | Formato SBOM alternativo aceite |
| SLSA Framework | Proveniência e integridade de build |
| NIST SP 800-161 | Supply Chain Risk Management |
| EU Cyber Resilience Act | Requisitos de SBOM para produtos com elementos digitais |
| SSDF PW.8 | Archive and protect each software release |
