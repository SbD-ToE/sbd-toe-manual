---
id: policy-iac-seguro
title: Política de IaC Seguro
description: Política organizacional que define os requisitos de segurança para a definição, validação, execução e manutenção de Infraestrutura como Código (IaC), incluindo scanning de configurações, policy-as-code, separação de ambientes, controlo de drift, módulos aprovados e assinatura de planos, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, IaC, Terraform, Pulumi, tfsec, checkov, OPA, policy-as-code, drift, módulos, assinatura, cap08, L1, L2, L3, governance, infraestrutura]
sidebar_position: 21
---

# Política de IaC Seguro

## 1. Objetivo

Esta política define os requisitos de segurança aplicáveis ao **design, validação, execução e manutenção de Infraestrutura como Código (IaC)** em todos os ambientes geridos pela organização.

O IaC define a base onde o software corre - um erro de configuração em IaC não é um bug de aplicação: é uma vulnerabilidade de infraestrutura com potencial impacto em todos os sistemas que a partilham. Grupos de segurança permissivos, IAM roles com acesso excessivo, buckets públicos, encriptação desactivada - todos estes erros são recorrentes em IaC não revisada e têm consequências proporcionalmente mais graves do que a maioria das vulnerabilidades de código.

O objetivo desta política é garantir que:

- O IaC é tratado como software crítico: revisado, testado, assinado e auditado
- Configurações inseguras são detetadas automaticamente antes de qualquer apply
- Policy-as-code impõe guardrails que não dependem de revisão humana individual
- Alterações manuais ao estado real da infraestrutura (drift) são detetadas e corrigidas
- Módulos IaC externos são avaliados, versionados e aprovados antes de adoção

---

## 2. Âmbito

Esta política aplica-se a toda a infraestrutura definida como código, independentemente da ferramenta utilizada (Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, Ansible, etc.) e do ambiente (cloud pública, privada ou híbrida, Kubernetes, etc.).

---

## 3. Princípios de IaC seguro

| Princípio | Aplicação prática |
|---|---|
| **IaC como código** | Versionado, revisto, testado e auditado com o mesmo rigor que código de aplicação |
| **Princípio do mínimo privilégio** | IAM roles e políticas com permissões mínimas para a função; sem wildcards em prod |
| **Separação de ambientes** | Environments segregados com estado separado e credenciais distintas; sem referências cruzadas entre backends |
| **Imutabilidade de infraestrutura** | Alterações via pipeline - não manual; alterações manuais são drift e devem ser revertidas |
| **Fail secure** | Configurações por defeito são as mais restritivas; permissões explícitas para o necessário |
| **Sem hardcodes** | Segredos, IPs e referências sensíveis nunca hardcoded; passados como variáveis ou via cofre |

---

## 4. Validação automática obrigatória

### 4.1 Linting e validação de sintaxe

Executado em cada PR com alterações IaC, antes de qualquer plan ou apply:

- [ ] Formatação verificada (`terraform fmt`, equivalente por ferramenta)
- [ ] Sintaxe validada (`terraform validate`, equivalente)
- [ ] Linter de boas práticas (`tflint`, equivalente)

### 4.2 Scanning de segurança

| Gate | L1 | L2 | L3 |
|---|---|---|---|
| Scanner de configurações IaC (tfsec, checkov, kics, terrascan) | Alerta | Bloqueia High/Critical | Bloqueia Medium+ |
| Policy-as-code (OPA/Rego, Sentinel, Conftest) | Recomendado | Obrigatório | Obrigatório |
| Validação de permissões IAM mínimas | Recomendado | Obrigatório | Obrigatório |
| Deteção de segredos hardcoded | Obrigatório | Obrigatório | Obrigatório |

### 4.3 Policy-as-code

Em L2/L3, as políticas de segurança de infraestrutura devem ser codificadas em regras verificáveis automaticamente:

- [ ] Políticas cobertas incluem (exemplos): sem buckets públicos, encriptação obrigatória em repouso, grupos de segurança sem acesso 0.0.0.0/0 irrestrito, tags obrigatórias em todos os recursos
- [ ] Políticas versionadas e aprovadas por AppSec Engineer
- [ ] Falha de política bloqueia o apply independentemente da revisão humana
- [ ] Relatórios de conformidade exportados por ambiente

---

## 5. Separação de ambientes

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Ambientes em diretórios/workspaces separados | Recomendado | Obrigatório | Obrigatório |
| Estado remoto separado por ambiente (sem state partilhado dev/prod) | Recomendado | Obrigatório | Obrigatório |
| Credenciais distintas por ambiente | Recomendado | Obrigatório | Obrigatório |
| Sem referências cruzadas entre backends de diferentes ambientes | Recomendado | Obrigatório | Obrigatório |
| Estado encriptado em repouso | Recomendado | Obrigatório | Obrigatório |
| Locking de estado para operações concorrentes | Recomendado | Obrigatório | Obrigatório |

---

## 6. Módulos externos e catálogo interno

### 6.1 Avaliação de módulos externos

Módulos IaC de fontes externas (ex: Terraform Registry, GitHub público) devem ser avaliados antes de adoção:

- [ ] Origem verificada (maintainer reconhecido, repositório activo)
- [ ] Sem vulnerabilidades conhecidas na versão a adoptar
- [ ] Licença compatível
- [ ] Versão fixada (pinning) - sem uso de `latest` ou ranges em prod

### 6.2 Catálogo interno de módulos aprovados

Em L2/L3, a organização deve manter um catálogo de módulos IaC internos aprovados:

- [ ] Módulos versionados com changelog
- [ ] Módulos com outputs documentados e tipados
- [ ] Aprovação formal antes de publicação (AppSec Engineer + DevOps/SRE)
- [ ] Módulos novos ou alterados sujeitos a revisão e scanning antes de publicação
- [ ] Projetos referenciam módulos do catálogo interno - não cópias locais

---

## 7. Revisão e aprovação de plan

Antes de qualquer apply em ambientes de staging ou produção:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Plan gerado no pipeline (não localmente) | Recomendado | Obrigatório | Obrigatório |
| Output do plan legível anexado ao PR | Recomendado | Obrigatório | Obrigatório |
| Plan revisto por DevOps/SRE antes de apply | Recomendado | Obrigatório | Obrigatório |
| Plan revisto por AppSec Engineer (impacto de segurança) | Não aplicável | Recomendado | Obrigatório |
| Plan assinado antes de apply (L3) | Não aplicável | Não aplicável | Obrigatório |
| Apply bloqueado sem aprovação explícita em staging/prod | Recomendado | Obrigatório | Obrigatório (dupla aprovação) |

A revisão do plan deve validar:
- [ ] Sem recursos a ser destruídos inesperadamente
- [ ] Sem alterações a grupos de segurança, IAM roles ou políticas não previstas
- [ ] Alterações confinadas ao âmbito do PR

---

## 8. Deteção e correção de drift

Alterações manuais à infraestrutura real criam divergência (drift) face ao estado definido em IaC. Este estado é inaceitável em L2/L3:

| Requisito | L1 | L2 | L3 |
|---|---|---|---|
| Job agendado de deteção de drift | Recomendado | Obrigatório (mensal) | Obrigatório (quinzenal) |
| Relatório de drift por ambiente gerado e arquivado | Recomendado | Obrigatório | Obrigatório |
| Drift crítico em produção gera alerta imediato | Recomendado | Obrigatório | Obrigatório |
| Correção de drift via PR com aprovação (nunca manual) | Recomendado | Obrigatório | Obrigatório |

:::warning
Alterações manuais directas a infraestrutura de produção, fora do pipeline IaC, são tratadas como não-conformidade em L2/L3 e devem ser registadas como incidente. O drift resultante deve ser corrigido pelo pipeline, não legitimado retroactivamente.
:::

---

## 9. Tagging obrigatório de recursos

Todos os recursos criados por IaC devem ter tags obrigatórias que permitam rastreabilidade:

| Tag | Descrição |
|---|---|
| `Environment` | dev / staging / prod |
| `Owner` | Equipa ou produto responsável |
| `Application` | Identificador da aplicação |
| `Criticality` | L1 / L2 / L3 |
| `ManagedBy` | terraform / pulumi / etc. |

A conformidade de tagging deve ser verificada automaticamente por policy-as-code em L2/L3.

---

## 10. Artefactos esperados

| Artefacto | Descrição | Retenção |
|---|---|---|
| `backend.tf` + logs de locking | Configuração de estado remoto e evidência de locking | Enquanto activo |
| Relatórios de lint e scanning | Output de tfsec, checkov, etc., por PR | 90 dias (L2), 1 ano (L3) |
| Relatórios de policy-as-code | Conformidade de políticas por ambiente | 90 dias (L2), 1 ano (L3) |
| Histórico de plan com metadados | Timestamp, autor, PR/MR ID | 1 ano (L2/L3) |
| Relatórios de drift | Por ambiente, por ciclo de auditoria | 1 ano (L2/L3) |
| Catálogo de módulos aprovados | Versão activa + changelog | Histórico |

---

## 11. Responsabilidades

| Role | Responsabilidade |
|---|---|
| Developer / DevOps | Escrever e submeter IaC a revisão; corrigir findings de scanning; referenciar módulos do catálogo |
| DevOps / SRE | Gerir backends de estado; configurar pipeline IaC; executar deteção de drift; gerir catálogo de módulos |
| AppSec Engineer | Definir policies de policy-as-code; aprovar módulos; rever plans com impacto de segurança; gerir exceções |
| GRC / Compliance | Auditar relatórios de conformidade; verificar drift; validar retenção de artefactos |

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente com origem em configuração IaC insegura ou drift não detectado
- Adoção de nova ferramenta IaC ou nova cloud provider
- Alteração das ferramentas de scanning ou policy-as-code

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 08 - IaC e Infraestrutura | Princípios, user stories, artefactos, ciclo de vida |
| Política de Aprovação de Plan IaC (`22_policy-aprovacao-plan-iac.md`) | Processo detalhado de revisão e aprovação de plans |
| Política de CI/CD Seguro (`17_policy-cicd-seguro.md`) | Pipeline de validação IaC |
| Política de Gestão de Segredos (`18_policy-gestao-segredos.md`) | Segredos em IaC e providers |
| tfsec / checkov / kics | Ferramentas de scanning de IaC |
| OPA / Rego / Sentinel / Conftest | Ferramentas de policy-as-code |
| CIS Benchmarks (AWS, Azure, GCP) | Controlos de referência para infraestrutura cloud |
| NIST SP 800-190 | Application Container Security Guide (aplicável a IaC de containers) |
| SLSA Framework | Integridade de build - aplicável a artefactos IaC |
