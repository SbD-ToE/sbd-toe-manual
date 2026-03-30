---
id: policy-aprovacao-plan-iac
title: Política de Aprovação de Plan IaC
description: Política organizacional que define o processo formal de revisão e aprovação de planos de execução de IaC (terraform plan ou equivalente) antes de qualquer apply em ambientes de staging ou produção, incluindo separação de funções, assinatura de planos, dupla aprovação e janelas de execução, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, IaC, plan, apply, aprovação, separação de funções, assinatura, janela de mudança, cap08, L1, L2, L3, governance, infraestrutura]
sidebar_position: 22
---

# Política de Aprovação de Plan IaC

## 1. Objetivo

Esta política define o processo formal de **revisão e aprovação de planos de execução de Infraestrutura como Código (IaC)** - `terraform plan`, `pulumi preview`, `cdk diff` ou equivalente - antes de qualquer operação de apply em ambientes de staging ou produção.

O `apply` é a operação de maior impacto em IaC: cria, altera ou destrói recursos reais de infraestrutura. Um apply não revisto pode eliminar bases de dados, expor recursos à internet, remover grupos de segurança ou reconfigurabilidade políticas de acesso de forma irreversível no curto prazo. A aprovação formal do plan não é burocracia - é o mecanismo de controlo que separa automação eficiente de automação descontrolada.

O objetivo desta política é garantir que:

- Nenhum apply é executado em staging/produção sem que o plan tenha sido revisto e aprovado
- O plan é gerado no pipeline (não localmente), garantindo reprodutibilidade e rastreabilidade
- A separação de funções impede que o mesmo indivíduo escreva, reveja e execute o apply
- Em L3, os plans são assinados para garantir que o apply usa exactamente o plan aprovado

---

## 2. Âmbito e obrigatoriedade

| Ambiente | L1 | L2 | L3 |
|---|---|---|---|
| Desenvolvimento | Recomendado | Recomendado | Obrigatório (registo mínimo) |
| Staging | Recomendado | Obrigatório | Obrigatório + dupla aprovação |
| Produção | Obrigatório | Obrigatório + aprovação formal | Obrigatório + dupla aprovação + assinatura |

---

## 3. Geração do plan

### 3.1 Origem do plan

O plan deve ser gerado exclusivamente pelo pipeline CI/CD - não por execução manual local:

- [ ] Job de plan executado a partir do commit revisto no PR
- [ ] Credenciais de acesso ao provider injectadas pelo pipeline (OIDC/workload identity)
- [ ] Output do plan exportado como artefacto do pipeline, com timestamp e referência ao commit SHA

A geração local de plans para fins de revisão prévia é aceite durante o desenvolvimento, mas o plan que fundamenta a aprovação formal e o apply subsequente deve ser sempre gerado pelo pipeline.

### 3.2 Conteúdo do output do plan

O output do plan deve ser apresentado de forma legível no PR (comentário automático ou link para artefacto), incluindo:

- [ ] Recursos a criar, alterar e destruir - com contagem e identificação
- [ ] Detalhes das alterações em recursos de segurança (grupos de segurança, IAM, políticas, encriptação)
- [ ] Alertas de alterações destrutivas (recursos a ser eliminados ou substituídos)
- [ ] Metadados: timestamp, autor do PR, commit SHA, ambiente alvo

---

## 4. Revisão do plan

### 4.1 Checklist de revisão

Antes de aprovar um plan, o reviewer deve verificar:

- [ ] As alterações correspondem ao âmbito do PR - sem alterações não previstas
- [ ] Nenhum recurso crítico é destruído ou substituído inesperadamente
- [ ] Sem alterações a grupos de segurança, IAM roles ou políticas não documentadas no PR
- [ ] Sem recursos expostos ao exterior sem justificação
- [ ] Sem segredos hardcoded nos valores do plan
- [ ] Alterações de encriptação ou configurações de backup não removidas inadvertidamente
- [ ] Tags obrigatórias presentes em novos recursos

### 4.2 Reviewers obrigatórios

| Ambiente | L1 | L2 | L3 |
|---|---|---|---|
| Staging | Tech Lead | DevOps/SRE | DevOps/SRE + AppSec Engineer |
| Produção | Tech Lead + DevOps/SRE | DevOps/SRE + AppSec Engineer | DevOps/SRE + AppSec Engineer (dupla aprovação) |

A self-approval (o mesmo indivíduo que submeteu o PR aprova o plan) é proibida em qualquer ambiente.

---

## 5. Separação de funções (SoD)

Em L2/L3, o processo de apply deve implementar separação de funções:

| Função | Responsável | Não pode acumular com |
|---|---|---|
| Escrever e submeter o IaC (PR autor) | Developer / DevOps | Aprovar o seu próprio plan |
| Rever e aprovar o plan | DevOps/SRE sénior + AppSec | Ser o autor do PR |
| Executar o apply em produção | Pipeline (automatizado) | Ser o mesmo que aprovou |

Em L3, nenhuma pessoa individual deve ter permissão de executar unilateralmente um apply em produção - a execução deve ser feita pelo pipeline, condicionada à aprovação registada de pelo menos dois papéis distintos.

---

## 6. Assinatura do plan (L3)

Em L3, o plan aprovado deve ser assinado antes de ser utilizado pelo job de apply:

- [ ] Plan serializado e assinado com chave gerida pelo pipeline (ex: Cosign, GPG)
- [ ] Attestation do pipeline associada ao plan (proveniência: quem gerou, quando, a partir de que commit)
- [ ] O job de apply verifica a assinatura antes de executar - rejeita plans sem assinatura válida ou com assinatura de plan diferente do aprovado
- [ ] Logs de verificação de assinatura arquivados como evidência

---

## 7. Janelas de execução de apply

Em L3, o apply em produção deve ser executado dentro de uma janela de mudança definida:

- [ ] Janela de mudança comunicada e registada antes da execução
- [ ] Apply não executado fora da janela sem aprovação de emergência explícita
- [ ] Aprovações de emergência registadas com justificação e notificação ao responsável de segurança

---

## 8. Rastreabilidade do apply

Toda a operação de apply deve produzir evidência rastreável:

- [ ] Logs completos do apply arquivados como artefacto do pipeline
- [ ] Log inclui: timestamp de início e fim, recursos afectados, resultado (sucesso/falha), identidade do pipeline
- [ ] Referência ao PR e ao plan aprovado
- [ ] Referência às aprovações formais (identidade e timestamp dos aprovadores)

Em L3, os logs de apply devem ser imutáveis (WORM) e retidos conforme a Política de Rastreabilidade.

---

## 9. Apply de emergência

Em situações de incidente com impacto em produção, pode ser necessário executar um apply fora do processo normal. Neste caso:

- [ ] Aprovação de emergência registada com identidade, justificação e timestamp (antes da execução sempre que possível)
- [ ] Apply executado pelo pipeline com o mínimo de alterações necessárias para mitigar o incidente
- [ ] Post-mortem realizado após resolução, com análise do desvio ao processo e medidas correctivas

:::warning
O apply manual directo ao provider (fora do pipeline) em produção é proibido em L2/L3, incluindo em situações de emergência. A excepção deve ser documentada e reportada ao responsável de segurança.
:::

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer / DevOps (autor) | Submeter PR com descrição clara do impacto; não executar apply antes de aprovação |
| DevOps/SRE (reviewer) | Rever o output do plan com checklist; aprovar apenas quando os critérios são cumpridos |
| AppSec Engineer | Rever planos com impacto de segurança; aprovar em L2/L3; definir critérios de assinatura |
| GRC / Compliance | Auditar registos de aprovação; verificar separação de funções; validar janelas de mudança |

---

## 11. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em apply não revisto ou não aprovado
- Alteração das ferramentas IaC com impacto no processo de geração e assinatura de plans
- Alteração de política de janelas de mudança da organização

---

## 12. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 08 - IaC e Infraestrutura | US-06 (revisão formal de plan), US-09 (assinatura), US-15 (SoD) |
| Política de IaC Seguro (`21_policy-iac-seguro.md`) | Requisitos gerais de IaC seguro |
| Política de Gestão de Segredos (`18_policy-gestao-segredos.md`) | Credenciais de pipeline para apply |
| Política de Rastreabilidade (`06_policy-rastreabilidade.md`) | Arquivo de logs de apply |
| ITIL Change Management | Framework de gestão de mudanças e janelas de execução |
| SLSA Framework | Proveniência e integridade de artefactos IaC |
| Cosign | Assinatura de artefactos (incluindo plans IaC) |
