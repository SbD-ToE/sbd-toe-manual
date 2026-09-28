---
id: intro
title: Introdução - Cross-Check Normativo
description: Enquadramento do capítulo de análise normativa, que demonstra como o SbD-ToE se cruza com diferentes normativos e regulações
tags: [cross-check, normativos, compliance, dora, nis2, ai-act, cra, gdpr, enisa-csa]
sidebar_position: 0
---



# Introdução - Cross-Check Normativo

A segurança do software não acontece num vácuo técnico.  
Organizações de diferentes setores estão sujeitas a **regulações, normas e frameworks** que estabelecem requisitos explícitos para garantir proteção adequada de sistemas, dados e operações.  
Neste contexto, o **Security by Design - Theory of Everything (SbD-ToE)** não é apenas um manual prescritivo de boas práticas: é também um **instrumento de convergência normativa**, permitindo alinhar práticas de desenvolvimento e operação segura com as múltiplas exigências externas.

O **Capítulo 002 - Cross-Check Normativo** tem precisamente este papel:  
- Demonstrar, de forma clara e verificável, **como o SbD-ToE responde a requisitos regulatórios e normativos**.  
- Identificar onde o modelo cobre requisitos, onde há **lacunas declaradas** e o que fica **fora de âmbito**, com a razão; as lacunas e o que fica fora exigem complementaridade com processos legais, organizacionais ou contratuais.  
- Apoiar **equipas de GRC, auditores, equipas técnicas e de gestão** na tarefa de articular segurança operacional com conformidade formal.
- Para **organizações que possuem ou contratam desenvolvimento de software**, oferecer **playbooks práticos** para implementar requisitos normativos de forma coerente com a disciplina de segurança aplicacional.

---

## Contexto e Justificação {#contexto-e-justificação}

Historicamente, o panorama normativo de segurança evoluiu de forma fragmentada:  
- **Há duas décadas**, poucas normas existiam, muitas vezes limitadas a requisitos de gestão de risco genéricos.  
- **Com a digitalização**, assistimos a uma explosão de normativos setoriais e regulamentares: **HIPAA** para saúde, **PCI-DSS** para pagamentos, **GDPR** para proteção de dados pessoais, **NIS2** e **DORA** para ciber-resiliência europeia, entre muitos outros.  
- Hoje, o desafio não é a falta de normativos, mas sim o **excesso de sobreposição** e a consequente dificuldade de aplicação prática coerente.

O SbD-ToE foi concebido como resposta a este problema.  
Ao ser construído **top-down**, com base em múltiplas referências normativas, frameworks técnicas e modelos de maturidade (ISO, ENISA, NIST, OWASP SAMM, BSIMM, SSDF, DSOMM, SLSA, etc.), o manual assegura que:  

- **As exigências normativas são incorporadas desde a raiz**, não tratadas como camadas externas ou aditivas.  
- **A conformidade não é um objetivo isolado**: aplicar práticas seguras em todo o ciclo de vida produz a evidência técnica que os regulamentos pedem, e o Manual declara o que fica por fazer.  
- **Cada área de conhecimento** (requisitos, arquitetura, CI/CD, containers, governança, etc.) contribui com requisitos e evidência para essa resposta.

---

## Objetivos deste capítulo {#objetivos-deste-capítulo}

1. **Mostrar a correspondência** entre práticas do SbD-ToE e requisitos de normativos internacionais e europeus.  
2. **Evidenciar as áreas cobertas**, onde a adoção do Manual fornece a evidência técnica que o regulamento pede.  
3. **Declarar as lacunas e o que fica fora de âmbito**, sem zonas cinzentas, ajudando as organizações a perceberem onde necessitam de medidas adicionais (jurídicas, processuais ou técnicas).  
4. **Fornecer um repositório comparativo**, que possa ser reutilizado em auditorias, certificações ou relatórios de conformidade.
5. **Oferecer playbooks de implementação** para organizações que contratam ou desenvolvem software, garantindo que a aquisição/desenvolvimento seja coerente com requisitos normativos específicos.

---

## Metodologia adotada {#metodologia-adotada}

A análise segue uma estrutura sistemática, comum a todos os normativos:  

- **Enquadramento** → breve descrição do normativo, âmbito e objetivos.  
- **Matriz de cobertura** → cada obrigação do regulamento, verificada contra o texto consolidado, tem uma de três respostas, e nenhuma fica sem resposta:  
  - **Cobre**, com a forma: requisito do catálogo, política, piso ou requisito acrescentado pelo regime, ou evidência de engenharia para um dever de outro plano (esta última nunca conta como cobertura do dever em si).  
  - **Lacuna declarada**, com o que falta; quando a lacuna depende de uma ronda futura do AppSec Core, a ronda fica indicada.  
  - **Fora de âmbito**, com a razão.  
  As páginas «Requisitos aplicáveis» (e, para o CSA, «Cobertura») são geradas desta matriz e prevalecem sobre o texto escrito à mão.  
- **Contextos regulatórios** → o núcleo do Manual é agnóstico à regulação. Quando uma aplicação está sujeita a um regime, declara o contexto correspondente (`CTX-<regime>`), que eleva requisitos do catálogo a obrigatórios (pisos) e acrescenta requisitos que só fazem sentido sob o regime. Um contexto nunca remove nem baixa um mínimo do Manual. Os níveis L1–L3 medem o risco da aplicação e não equivalem às classes de risco de nenhum regulamento.  
- **Notas Críticas** → observações sobre interpretação, sobreposição ou complementaridade.  
- **Conclusão** → o que o SbD-ToE cobre nesse normativo, o que fica como lacuna declarada e o que fica fora de âmbito.
- **Playbook Prático** (quando aplicável) → roadmap de implementação para organizações com disciplina de desenvolvimento/AppSec, orientando como integrar requisitos normativos na aquisição ou desenvolvimento de software.

O Manual é centrado na aplicação: requisitos, arquitetura, código, dependências, pipeline, deploy e operação do software. A IA entra como qualquer outro tema do Manual; não há um manual de IA à parte. A resposta obrigação a obrigação de cada regulamento está em:

- [DORA — Requisitos aplicáveis](dora/requisitos-aplicaveis#cobertura)
- [NIS2 — Requisitos aplicáveis](nis2/requisitos-aplicaveis#cobertura)
- [CRA — Requisitos aplicáveis](cra/requisitos-aplicaveis#cobertura)
- [RGPD — Requisitos aplicáveis](gdpr/requisitos-aplicaveis#cobertura)
- [AI Act — Requisitos aplicáveis](ai-act/requisitos-aplicaveis#cobertura)
- [ENISA/CSA — Cobertura](enisa-csa/cobertura#cobertura)

---

## Filosofia de Conformidade Integrada {#filosofia-de-conformidade-integrada}

O **SbD-ToE não é uma norma**, mas foi desenhado para **dialogar com todas as normas**.  
Isto acontece porque:  

- **Normas e regulamentos focam-se em dimensões específicas** (governação, risco, reporte, proteção de dados, etc.), e o SbD-ToE prescreve práticas **abrangentes e integradas** do lado da aplicação.  
- A relação entre os dois não se presume pela abrangência: demonstra-se obrigação a obrigação, e pode ser sobreposição, contribuição, cobertura parcial, satisfação condicionada, lacuna ou fora de âmbito. As matrizes de cobertura registam-na nas três categorias (cobre, lacuna declarada, fora de âmbito).  
- A conformidade continua a ser juízo da organização. O Manual fornece a evidência técnica e diz com clareza o que fica por fazer e o que não lhe cabe, sem um esforço paralelo ou burocrático para cada regulamento.  

Esta visão **mitiga a fragmentação regulatória** e oferece às organizações um **modelo unificado de aplicação prática**, onde segurança, risco e conformidade convergem.

---

## Nota Importante: Normativos e Desenvolvimento Aplicacional {#nota-importante-normativos-e-desenvolvimento-aplicacional}

Muitos normativos (ex.: **DORA**, **NIS2**, **ISO 27001**) **não são específicos de desenvolvimento de software**, mas cobrem a **gestão integral de risco TIC** em organizações.

No entanto, quando uma organização **possui ou contrata desenvolvimento de software**, a disciplina de **segurança aplicacional (AppSec)** torna-se um **componente crítico** para demonstrar conformidade com esses normativos.

**Consequência prática:**  
- O normativo exige "gestão de risco TIC" (âmbito amplo)
- A organização implementa isso através de múltiplos controles (arquitetura, operações, contratos, etc.)
- Se existe desenvolvimento/aquisição de software, os playbooks deste capítulo orientam **como integrar práticas de AppSec** de forma **coerente e proporcional** com o regulamento

**Perímetro do Manual.** O Manual é centrado na aplicação. Ficam fora de âmbito, com a razão registada na matriz de cada regulamento: a segurança da entidade como um todo (rede corporativa e canais de administração, EDR, patching de sistemas operativos e equipamentos, inventário e classificação de todos os ativos), a continuidade de negócio, a gestão de crise e a BIA da entidade, a avaliação da conformidade, a marcação CE e as declarações de conformidade, e o lado jurídico do RGPD (bases legais, resposta formal ao titular e prazos). A IA trata-se como qualquer outro tema do Manual, sem manual à parte.

**Exemplo:** **DORA** é regulação financeira, mas se uma entidade financeira desenvolve software internamente, deve aplicar os princípios do SbD-ToE para demonstrar que a sua **postura de ciber-resiliência** (DORA Art. 5) inclui **development security practices**.

---

## Estrutura do Capítulo {#estrutura-do-capítulo}

Este capítulo está organizado por **framework/normativo**, cada um numa pasta dedicada com introdução, playbook de implementação e a página de cobertura gerada da matriz:

### Frameworks Atualmente Cobertos {#frameworks-atualmente-cobertos}

#### **[DORA](dora/intro)** (Digital Operational Resilience Act) {#dora-digital-operational-resilience-act}
- 📂 `dora/`
  - [Enquadramento do regulamento](dora/intro)
  - [Playbook de implementação prática](dora/playbook)
  - [Análise de convergência com NIS2](dora/convergencia-dora)
  - [Requisitos aplicáveis (gerada da matriz)](dora/requisitos-aplicaveis)

#### **[NIS2](nis2/intro)** (Network and Information Security Directive) {#nis2-network-and-information-security-directive}
- 📂 `nis2/`
  - [Enquadramento da diretiva](nis2/intro)
  - [Playbook de implementação prática](nis2/playbook)
  - [Análise de convergência com DORA](nis2/convergencia-dora)
  - [Requisitos aplicáveis (gerada da matriz)](nis2/requisitos-aplicaveis)

#### **[CRA](cra/intro)** (Cyber Resilience Act) {#cra-cyber-resilience-act}
- 📂 `cra/`
  - [Enquadramento do regulamento](cra/intro)
  - [Playbook de implementação prática](cra/playbook)
  - [Requisitos aplicáveis (gerada da matriz)](cra/requisitos-aplicaveis)

#### **[GDPR](gdpr/intro)** (General Data Protection Regulation) {#gdpr-general-data-protection-regulation}
- 📂 `gdpr/`
  - [Enquadramento do regulamento](gdpr/intro)
  - [Playbook de implementação prática](gdpr/playbook)
  - [Requisitos aplicáveis (gerada da matriz)](gdpr/requisitos-aplicaveis)

#### **[AI Act](ai-act/intro)** (Regulamento de Inteligência Artificial) {#ai-act-regulamento-de-inteligência-artificial}
- 📂 `ai-act/`
  - [Enquadramento do regulamento](ai-act/intro)
  - [Playbook de implementação prática](ai-act/playbook)
  - [Análise de convergência com o CRA](ai-act/convergencia-cra)
  - [Requisitos aplicáveis (gerada da matriz)](ai-act/requisitos-aplicaveis)

#### **[ENISA / CSA](enisa-csa/intro)** (Regulamento Cibersegurança — certificação europeia da cibersegurança) {#enisa-csa-cloud-security-alliance-certification}
- 📂 `enisa-csa/`
  - [Enquadramento do esquema de certificação](enisa-csa/intro)
  - [Cobertura obrigação a obrigação (gerada da matriz)](enisa-csa/cobertura)

### Exemplos e Templates de Suporte {#exemplos-e-templates-de-suporte}

#### **[Exemplo-Playbook](exemplo-playbook/exemplo-toolchain-options)** {#exemplo-playbook}
- 📂 [`exemplo-playbook/`](exemplo-playbook/exemplo-toolchain-options)
  - Templates e exemplos reutilizáveis para implementação de qualquer framework
  - Ferramentas, KPIs, governance, relatórios, políticas, contratos
  - [Ver índice completo](exemplo-playbook/exemplo-toolchain-options) para detalhes

---

### Frameworks a Incluir (Roadmap) {#frameworks-a-incluir-roadmap}

Os seguintes frameworks estão no roadmap para adição futura:

- **ISO 27001** → Norma de Gestão de Segurança da Informação
- **HIPAA** → Health Insurance Portability and Accountability Act
- **PCI-DSS** → Payment Card Industry Data Security Standard
- **SOC2** → Service Organization Control 2
- **FedRAMP** → Federal Risk and Authorization Management Program
- **CSA STAR** → Cloud Security Alliance Security Trust Assurance and Risk

---

### Estrutura Comum de Cada Framework {#estrutura-comum-de-cada-framework}

Cada pasta de framework segue esta estrutura consistente:

1. **Introdução**
   - Enquadramento legal/regulatório
   - Âmbito de aplicação
   - Objetivos principais

2. **Playbook de Implementação**
   - Cross-check: Requisitos vs. SbD-ToE
   - Roadmap de implementação
   - Fases e milestones
   - Checklists práticas

3. **Análises de Convergência** (quando aplicável)
   - Sobreposição entre frameworks
   - Princípio *lex specialis*
   - Estratégias de implementação harmonizada

4. **Requisitos aplicáveis / Cobertura** (gerada da matriz)
   - Obrigação a obrigação: coberta, lacuna declarada ou fora de âmbito
   - Pisos e requisitos acrescentados pelo contexto regulatório, quando existe

---

## Leitura recomendada {#leitura-recomendada}

- Este capítulo deve ser lido **em articulação com o [Capítulo 00 - Theory of Everything](/sbd-toe/teory-of-everything/intro)**, que explica a filosofia global do manual.  
- Para organizações **com desenvolvimento/aquisição de software**, recomenda-se começar pelos playbooks (ex.: [DORA](dora/playbook), [NIS2](nis2/playbook)), que orientam implementação coerente.
- Pode também ser utilizado como **documento autónomo**, servindo de guia de referência rápida para quem procura verificar alinhamento do SbD-ToE com exigências específicas.  

---
