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

Fornecedores e terceiros são **parte da cadeia de responsabilidade e estão fora do domínio de prescrição do manual**.  
O manual diz à organização o que tem de exigir, verificar e registar; não diz ao fornecedor como trabalhar — o que se exige dele vive no contrato. Um fornecedor que adote o SbD-ToE passa a encontrar aqui as suas próprias práticas.

A fronteira desloca-se com o processo, não com o contrato: quem é contratado para trabalhar dentro dos repositórios, pipelines e ambientes da organização opera dentro do processo dela, e as práticas aplicam-se-lhe como a qualquer equipa (Cap. 14, US-15 a US-20).

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

O que a organização exige, verifica e regista, por capítulo:

### Cap. 05 - Dependências e SBOM
A organização exige **SBOM atualizado** dos componentes entregues e verifica-o na aceitação, para manter rastreabilidade completa da cadeia.

### Cap. 08-09 - IaC e Containers
A organização exige **validação de vulnerabilidades e assinatura digital** nos módulos IaC e imagens fornecidos, e verifica-as antes da promoção.

### Cap. 13 - Formação e Onboarding
A organização exige e regista a **formação mínima obrigatória** antes de conceder acesso a sistemas ou dados (NIS2/DORA compliance).

**Requisitos associados:**
- [US-12: Formação mínima para terceiros](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12---validação-de-conhecimento-via-quizzes-estruturados) - Receber formação obrigatória (GRC / Compliance / Gestão Executiva responsável por garantir)
- [US-13: Trilho formativo para contractors](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-13---operacionalização-de-formação-de-terceiros) - SLA antes de acesso técnico (CISO / Security Champion (formação) responsável por executar)

### Cap. 14 - Governança e Contratação
A organização fixa as **cláusulas contratuais de segurança**, valida o fornecedor antes do onboarding, monitoriza a conformidade ao longo do contrato e executa o offboarding formal no fim.

**Requisitos associados:**
- [US-03: Validação contínua de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-03---validação-contínua-de-fornecedores) - GRC valida conformidade
- [US-15: Preparação técnica de contractors](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-15---preparação-técnica-e-validação-de-contractors-pré-acesso) - Security Champion (RH) executam preparação
- [US-17: Offboarding seguro](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-17---offboarding-seguro-de-contractors-e-rescisão-de-fornecedores) - Security Champion (RH) / DevOps / SRE executam offboarding
- [US-14: Reavaliação periódica de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-14---reavaliação-contínua-e-rotação-de-fornecedores-pós-onboarding) - Submeter-se a reavaliação
- [US-18: Monitorização contínua de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-18---monitorização-contínua-de-conformidade-de-fornecedores-alertas-e-escalação) - Permitir monitorização (AppSec Engineer / Operações (Ops) executam)

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 05 - Dependências e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Cap. 08 - IaC e Infraestrutura](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
