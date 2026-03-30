---
id: policy-golden-base-images
title: Política de Golden Base Images
description: Política organizacional que define os requisitos para a criação, aprovação, versionamento semântico, patching, depreciação e revogação de imagens base de container aprovadas pela organização (Golden Base Images), incluindo SLAs de patching por criticidade e gestão do catálogo interno, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, golden base images, imagens base, container, catálogo, patching, digest, depreciação, revogação, cap09, L1, L2, L3, governance]
sidebar_position: 24
---

# Política de Golden Base Images

## 1. Objetivo

Esta política define os requisitos para a **gestão do ciclo de vida de imagens base de container aprovadas pela organização** - as designadas Golden Base Images (GBI).

Toda a imagem de container construída pela organização herda as características de segurança da sua imagem base. Uma imagem base não auditada, desactualizada ou de origem não verificada é uma vulnerabilidade estrutural que se propaga a todos os serviços que a utilizam. A centralização e governação das imagens base é, portanto, um controlo multiplicador: uma atualização de base bem gerida corrige vulnerabilidades em todos os serviços simultaneamente; uma base comprometida compromete todos.

O objetivo desta política é garantir que:

- A organização mantém um catálogo controlado de imagens base aprovadas
- Nenhuma imagem de container em produção é construída sobre bases fora do catálogo aprovado
- As Golden Base Images são mantidas atualizadas com SLA de patching definido por criticidade
- Imagens base depreciadas ou revogadas são substituídas de forma controlada
- A integridade de cada imagem base é verificável por digest SHA256

---

## 2. Âmbito e obrigatoriedade

| Nível | Obrigatoriedade |
|---|---|
| L1 | Recomendado; uso de imagens base de fontes oficiais com versão fixada |
| L2 | Obrigatório; catálogo de GBIs mantido; builds com bases fora do catálogo bloqueadas |
| L3 | Obrigatório; catálogo com aprovação formal, changelog, SLA de patching e revogação imediata |

---

## 3. Catálogo de Golden Base Images

### 3.1 Estrutura do catálogo

O catálogo de GBIs (`golden-base-images.yaml` ou equivalente) é o inventário oficial de imagens base aprovadas para uso em builds da organização. Cada entrada deve conter:

- [ ] Identificador único da GBI (ex: `ubuntu-22.04-minimal-v1.3.2`)
- [ ] Imagem upstream de origem (ex: `ubuntu:22.04`) e digest SHA256 da versão upstream referenciada
- [ ] Digest SHA256 da GBI interna (no registo interno da organização)
- [ ] Versão semântica da GBI
- [ ] Data de aprovação e responsável pela aprovação
- [ ] Data da última revisão de segurança
- [ ] Estado: `active` / `deprecated` / `revoked`
- [ ] Data de End-of-Life (EOL) da upstream (quando aplicável)
- [ ] Changelog das versões anteriores

### 3.2 Localização

As GBIs são armazenadas no registo interno de imagens da organização (Artifactory, Harbor, ECR, GCR ou equivalente), com:

- [ ] Acesso controlado por autenticação - sem pull anónimo
- [ ] Imutabilidade dos digests (uma vez publicado, o digest não pode ser alterado)
- [ ] Tags semânticas associadas a digests imutáveis (sem redefinição de tags existentes)

---

## 4. Aprovação de novas GBIs

Antes de uma nova imagem base ser adicionada ao catálogo, deve ser realizada uma avaliação formal:

| Critério de avaliação | Descrição |
|---|---|
| Origem e manutenção | Imagem de repositório oficial ou provedor confiável com histórico de respostas a CVEs |
| Minimalismo | Contém apenas o necessário para o caso de uso; sem ferramentas de diagnóstico desnecessárias |
| CVEs activos | Sem CVEs Critical ou High activos na versão candidata |
| EOL da upstream | Data de EOL conhecida e não iminente (mínimo 12 meses de suporte restante) |
| Licença | Licença compatível com a política da organização |
| Compatibilidade | Testada com as stacks e frameworks utilizadas pela organização |

O resultado da avaliação deve ser registado com:

- [ ] Decisão (aprovada / rejeitada) com justificação
- [ ] Responsável pela aprovação: AppSec Engineer + DevOps/SRE sénior
- [ ] Data de aprovação e versão avaliada

---

## 5. Versionamento semântico

As GBIs devem seguir versionamento semântico (`MAJOR.MINOR.PATCH`):

| Tipo de versão | Quando usar |
|---|---|
| **PATCH** | Atualização de pacotes do OS sem alteração de API ou comportamento; security patches |
| **MINOR** | Adição de componentes; upgrade de runtime (ex: Python 3.11 → 3.12 mantendo compatibilidade) |
| **MAJOR** | Mudança de OS base, breaking changes, substituição de runtime major |

---

## 6. SLA de patching

Quando é publicado um CVE que afecta uma GBI activa, o prazo para publicar uma nova versão corrigida é:

| Severidade CVE | L2 | L3 |
|---|---|---|
| Critical (CVSS ≥ 9.0) | 7 dias | 3 dias |
| High (CVSS 7.0–8.9) | 30 dias | 15 dias |
| Medium (CVSS 4.0–6.9) | 90 dias | 45 dias |
| Low | 180 dias | 90 dias |

O patching consiste em:

1. Actualizar a GBI (nova versão PATCH ou MINOR conforme o caso)
2. Executar o pipeline de build e scanning da nova versão
3. Publicar no registo interno após aprovação automática (CI verde) + revisão manual quando aplicável
4. Notificar as equipas com builds que referenciam a versão afectada
5. Deprecar a versão anterior (ver secção 7)

---

## 7. Depreciação

Uma GBI deve ser marcada como `deprecated` quando:

- Uma nova versão de patching está disponível e estável
- A upstream atingiu EOL
- Existe uma GBI substituta aprovada que cobre o mesmo caso de uso

Uma GBI deprecated:

- [ ] Permanece acessível no registo para builds existentes em transição
- [ ] Não deve ser referenciada em novos Dockerfiles
- [ ] O pipeline emite aviso (warning) quando uma build usa uma GBI deprecated
- [ ] Tem um prazo de remoção definido (máximo 60 dias após depreciação em L2/L3)

---

## 8. Revogação

Uma GBI deve ser marcada como `revoked` e removida imediatamente quando:

- É descoberta uma vulnerabilidade crítica sem fix disponível e com vector de exploração activo
- A integridade da imagem é comprometida (supply chain attack, digest manipulado)
- A upstream foi comprometida

Uma GBI revoked:

- [ ] É removida do registo (ou tornada inacessível para pull) imediatamente
- [ ] O pipeline bloqueia qualquer build que tente usar a GBI revogada
- [ ] As equipas são notificadas de imediato com instruções de substituição
- [ ] Os serviços em produção que usam a GBI revogada são identificados via inventário de runtime e priorizados para substituição

:::warning
A revogação de uma GBI é um evento de segurança que pode requerer activação do processo de resposta a incidentes se existirem serviços em produção expostos. A rastreabilidade de quais serviços usam cada GBI (via SBOM e inventário de runtime) é pré-requisito para uma resposta eficaz.
:::

---

## 9. Validação em pipeline

O pipeline de build de qualquer serviço deve verificar a GBI utilizada:

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| GBI referenciada por digest SHA256 (não por tag) | Recomendado | Obrigatório | Obrigatório |
| GBI no catálogo com estado `active` | Recomendado | Obrigatório | Obrigatório |
| Aviso se GBI `deprecated` | Aviso | Aviso bloqueante | Bloqueante |
| Bloqueio se GBI `revoked` | Bloqueio | Bloqueio | Bloqueio |

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| DevOps / SRE (Plataforma) | Manter o catálogo; construir e publicar GBIs; executar patching dentro de SLA; gerir o registo interno |
| AppSec Engineer | Aprovar novas GBIs; definir SLAs de patching; coordenar revogações; monitorizar CVEs em bases activas |
| Developer | Referenciar GBIs por digest; não usar imagens fora do catálogo; reportar problemas de compatibilidade |
| GRC / Compliance | Auditar o catálogo; verificar conformidade com SLAs; validar rastreabilidade de GBIs em produção |

---

## 11. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em GBI comprometida ou desactualizada
- Adoção de nova plataforma de container (ex: migração de orquestrador)
- Alteração dos critérios de aprovação de imagens base pela comunidade de segurança

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 09 - Containers e Execução Isolada | US-01, US-11, US-15: bases seguras, patching, catálogo |
| Política de Containers Seguros (`23_policy-containers-seguros.md`) | Uso de GBIs em builds e runtime |
| Política de SBOM (`11_policy-sbom.md`) | SBOM por imagem base e rastreabilidade em runtime |
| CIS Docker Benchmark v1.6 | Critérios de segurança de imagens base |
| NIST SP 800-190 | Application Container Security - imagens base |
| Cosign / Sigstore | Assinatura e verificação de GBIs |
| Harbor / Artifactory | Registos internos de referência para gestão de GBIs |
