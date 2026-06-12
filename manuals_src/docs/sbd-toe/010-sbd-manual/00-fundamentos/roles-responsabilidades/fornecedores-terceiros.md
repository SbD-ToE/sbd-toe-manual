---
id: fornecedores-terceiros
title: Fornecedores / Terceiros
sidebar_label: 🤝 Fornecedores / Terceiros
description: Responsabilidades de Fornecedores e Terceiros no SbD-ToE
tags: [fornecedores, terceiros, supply-chain, responsabilidades]
sidebar_position: 13
---

# Fornecedores / Terceiros

## Visão Geral

Fornecedores são **parte da cadeia de responsabilidade**.  
Devem cumprir os mesmos padrões de segurança que equipas internas, garantindo rastreabilidade, formação e conformidade contratual.

### Responsabilidades Principais
- Cumprem cláusulas contratuais de segurança (Cap. 14)
- Entregam SBOM atualizado e evidência de conformidade
- Garantem que componentes externos respeitam requisitos de segurança
- Submetem-se a validação periódica

### Contexto Organizacional
São críticos para **NIS2** e **DORA**, que obrigam a gestão explícita da cadeia de fornecimento digital (Art. 21 NIS2, Art. 28-30 DORA) e avaliação contínua de terceiros.

## Enquadramento Regulatório

Gestão da cadeia de fornecimento é exigência explícita em:
- **NIS2**: Art. 21 - Medidas de gestão de risco de cibersegurança da cadeia de abastecimento
- **DORA**: Art. 28-30 - Gestão do risco de ICT de terceiros

---

## Atividades por Capítulo

### Cap. 05 - Dependências e SBOM
Fornecer **SBOM atualizado** de todos os componentes entregues, garantindo rastreabilidade completa.

### Cap. 08-09 - IaC e Containers
Assegurar **segurança em módulos IaC e imagens** fornecidas, com validação de vulnerabilidades e assinatura digital.

### Cap. 13 - Formação e Onboarding
Receber **formação mínima obrigatória** antes de acesso a sistemas ou dados (NIS2/DORA compliance).

**Requisitos associados:**
- [US-12: Formação mínima para terceiros](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12---validação-de-conhecimento-via-quizzes-estruturados) - Receber formação obrigatória (GRC / Compliance / Gestão Executiva responsável por garantir)
- [US-13: Trilho formativo para contractors](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-13---operacionalização-de-formação-de-terceiros) - SLA antes de acesso técnico (CISO / Security Champion (formação) responsável por executar)

### Cap. 14 - Governança e Contratação
Cumprir **cláusulas contratuais de segurança**, submeter-se a validação periódica de conformidade, permitir monitorização contínua, executar processo de onboarding e offboarding formal.

**Requisitos associados:**
- [US-01: Validação contínua de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-01---processo-formal-de-exceções-com-alçadas-por-nível-de-risco) - GRC valida conformidade
- [US-11: Preparação técnica de contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-11---consolidação-de-kpis-de-governação-e-maturidade) - Security Champion (RH) executam preparação
- [US-12: Offboarding seguro](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-12---formaliza%C3%A7%C3%A3o-de-modelo-de-governa%C3%A7%C3%A3o-por-n%C3%ADvel-de-risco) - Security Champion (RH) / DevOps / SRE executam offboarding
- [US-13: Reavaliação periódica de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-13---controlo-sistemático-e-periódico-por-capítulo-sbd-toe) - Submeter-se a reavaliação
- [US-14: Monitorização contínua de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding) - Permitir monitorização (AppSec Engineer / Operações (Ops) executam)

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 05 - Dependências e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Cap. 08 - IaC e Infraestrutura](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
