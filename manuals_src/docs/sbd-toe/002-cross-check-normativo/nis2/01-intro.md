---
id: intro
title: NIS2 - Cross-check normativo
description: Como o SbD-ToE cobre, deixa em aberto deliberadamente e pode integrar rapidamente os requisitos da Diretiva NIS2 (UE 2022/2555)
tags: [cross-check, nis2, diretiva, ciberseguranca, incident-reporting, governance]
sidebar_position: 3
---

# Cross-check normativo - NIS2

## Âmbito {#âmbito}

A **Diretiva (UE) 2022/2555 (NIS2)** (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022L2555)) atualiza o quadro europeu de cibersegurança para entidades essenciais e importantes em 18 setores, reforçando governação, medidas de gestão de risco e obrigação de reporte de incidentes. Os Estados-Membros tinham até 17 de outubro de 2024 para transpor a NIS2; a NIS1 foi revogada a 18 de outubro de 2024.

No espírito da NIS2, não chega "ter controlos" - é preciso demonstrar capacidade operacional e responsabilização da gestão. O SbD-ToE, construído top-down e atento a múltiplas referências, encaixa naturalmente neste ethos: entrega processos, políticas e artefactos técnicos reutilizáveis, deixando propositadamente algumas variáveis em aberto para preservar a universalidade do manual.

Este documento apresenta:

1. **PARTE I: ANÁLISE NORMATIVA** - mapeamento artigo a artigo dos requisitos NIS2 para capítulos SbD-ToE, identificando cobertura existente, lacunas intencionais e passos de integração.
2. **PARTE II: SÍNTESE E REFERÊNCIAS** - visão consolidada da relação NIS2/SbD-ToE e referências normativas.

---

## PARTE I: ANÁLISE NORMATIVA {#parte-i-análise-normativa}

### Artigo 20 - Governação e responsabilização {#artigo-20---governação-e-responsabilização}

**Conteúdo normativo**

O Art. 20 coloca o órgão de direção no centro: aprova as medidas de gestão dos riscos de cibersegurança, supervisiona a sua aplicação e pode ser responsabilizado por infrações. Exige ainda formação para os membros do órgão de direção (e incentiva formação regular dos trabalhadores).

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Aprovação de medidas pelo órgão de gestão | Cap. 14, Cap. 02 | Governança, cadeia de aprovação e base técnica de suporte |
| Supervisão da execução | Cap. 12, Cap. 14 | Métricas, evidências operacionais, monitorização e escalonamento |
| Formação regular da gestão | Cap. 13 | Programa de formação e onboarding |

**O que o SbD-ToE cobre**

- Define base técnica de requisitos e políticas (Cap. 02) e a cadeia de governança/aprovação aplicável (Cap. 14).
- Estabelece ciclos de supervisão, monitorização e evidência operacional (Cap. 12), articuláveis com a accountability de gestão.
- Prescreve programa de formação e onboarding (Cap. 13).

**Lacunas intencionais**

Quem assina as políticas: o manual exige aprovação formal, mas não fixa ex ante a forma jurídica exata da cadeia de aprovação. Isto é propositado: em contextos puramente técnicos, aprovação operacional pode bastar; para leitura NIS2, a accountability do órgão de gestão tem de ficar explicitamente formalizada.

**Como cumprir**

Sugere-se registar, no Cap. 14, como a cadeia de aprovação e supervisão da gestão foi formalizada, usando o catálogo do Cap. 02 como base técnica e guardando evidência de formação periódica à gestão (conforme Art. 20).

---

### Artigo 21 - Medidas de gestão de risco de cibersegurança {#artigo-21---medidas-de-gestão-de-risco-de-cibersegurança}

**Conteúdo normativo**

O Art. 21, n.º 2, pede medidas que, numa abordagem que abranja todos os riscos, cubram pelo menos: políticas de análise dos riscos e de segurança dos sistemas de informação; tratamento de incidentes; continuidade das atividades (cópias de segurança, recuperação de desastres) e gestão de crises; segurança da cadeia de abastecimento; segurança na aquisição, desenvolvimento e manutenção dos sistemas, incluindo o tratamento e a divulgação de vulnerabilidades; avaliação da eficácia das medidas; práticas básicas de ciber-higiene e formação em cibersegurança; criptografia e cifragem; segurança dos recursos humanos, controlo do acesso e gestão de ativos; autenticação multifatores e comunicações seguras. Para os prestadores de DNS, registos de TLD, computação em nuvem, centros de dados, CDN, serviços geridos e de segurança geridos, mercados em linha, motores de pesquisa, redes sociais e prestadores de serviços de confiança, o Reg. de Execução (UE) 2024/2690 concretiza estas medidas, incluindo monitorização e registo (anexo, ponto 3.2).

Em 2024/2025, a Comissão e a ENISA publicaram orientações técnicas e mapeamentos práticos com exemplos de evidência para implementar estas medidas - utilíssimos para auditoria.

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Políticas de análise de risco | Cap. 02, Cap. 03 | Requisitos de segurança, threat modeling |
| Gestão de incidentes | Cap. 12 | Deteção, resposta, pós-incidente |
| Continuidade/crise (backups, DR) | Cap. 11, Cap. 12 | Runbooks e exercícios de resposta; cópias de segurança com restauro testado (OPS-016); objectivos e procedimento de recuperação da aplicação (OPS-017, L2/L3); BCM e gestão de crise da entidade fora do Manual |
| Segurança da cadeia de fornecimento | Cap. 05, Cap. 14 | SBOM/SCA, dependências, requisitos contratuais |
| Segurança em desenvolvimento | Cap. 06, Cap. 07, Cap. 08 | Desenvolvimento seguro, CI/CD, IaC |
| Avaliação da eficácia | Cap. 10, Cap. 12 | Testes de segurança, monitorização contínua |
| Higiene cibernética/treino | Cap. 13 | Formação e onboarding |
| IAM, criptografia | Cap. 02, Cap. 04 | Requisitos de segurança, arquitetura segura |
| Gestão de vulnerabilidades/patching | Cap. 05, Cap. 10 | Dependências, SCA, testes |
| Logging e monitorização | Cap. 12 | Observabilidade, SIEM, alertas |

**O que o SbD-ToE cobre**

- **Políticas e controlos técnicos** (Cap. 02 - Requisitos de Segurança).
- **Classificação de criticidade** e risco proporcional (Cap. 01 - Classificação de Aplicações).
- **Threat modeling** (Cap. 03).
- **Cadeia de fornecimento**: SBOM/SCA, dependências (Cap. 05).
- **CI/CD & IaC** seguros (Cap. 07, Cap. 08); containers/runtime (Cap. 09).
- **Testes** (Cap. 10) e deploy seguro (Cap. 11).
- **Monitorização, logging, resposta e melhoria contínua** (Cap. 12).
- **Governança & contratação** (Cap. 14), incluindo avaliação de terceiros.

**Lacunas intencionais**

Taxonomias/formatos "fechados": a NIS2 detalha tópicos, mas o detalhe (p. ex., lista exata de campos de logs ou templates de políticas) pode variar entre jurisdições e setores. O SbD-ToE mantém modelos genéricos, para que possam ser "plugados" aos requisitos nacionais/setoriais.

**Como cumprir**

Sugere-se usar o catálogo do Cap. 02 como base de SoA técnica, complementado por `01/03/05/10/12/14`, e alinhar as evidências com o guia técnico da ENISA (exemplos de evidência e mapeamentos). Declarar, no Cap. 01, que a proporcionalidade segue as classes NIS2 (essencial/importante) e o impacto nos serviços.

---

### Artigo 23 - Reporte de incidentes {#artigo-23---reporte-de-incidentes}

**Conteúdo normativo**

A NIS2 define um trilho de reporte para incidentes significativos:

- **Alerta rápido** (*early warning*), à CSIRT ou, se aplicável, à autoridade competente, sem demora injustificada e até 24 h após o conhecimento do incidente significativo.
- **Notificação de incidente**, com avaliação inicial, até 72 h após o conhecimento.
- **Relatório final** até 1 mês após a notificação de incidente (72h), com relatórios intercalares a pedido da CSIRT/autoridade.

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Deteção e resposta | Cap. 12 | Processo de deteção, resposta, pós-incidente |
| Escalonamento e responsabilidades | Cap. 14 | Papéis e responsabilidades |
| Classificação de severidade | Cap. 01, Cap. 12 | Critérios de impacto, classificação de incidentes |

**O que o SbD-ToE cobre**

- Processo de deteção e resposta, com pós-incidente (Cap. 12).
- Papéis de escalonamento e responsabilidades (Cap. 14).
- Critérios de impacto (Cap. 01) que suportam a classificação de severidade.

**Lacunas intencionais**

O SbD-ToE não fixa um modelo canónico de dados para incidentes, nem uma taxonomia de severidade "oficial" (a escala P1–P4 da Política 31 é interna), nem os templates de submissão. Isto é intencional: DORA, NIS2, HIPAA pedem conjuntos diferentes de campos e formatos. O manual diz "registar o incidente com campos obrigatórios", e o conjunto final de campos vem do normativo aplicável (no caso NIS2, das orientações nacionais e do Art. 23).

**Como cumprir**

Sugere-se, no Cap. 12, adotar um schema mínimo (`incident.json/csv`) e parametrizar os campos em função da NIS2 (p. ex., causa provável, severidade, consequências, IOCs, medidas; cf. guias ENISA). Configurar exportadores do SIEM/ITSM → ficheiros prontos a submeter nos prazos (24h/72h/1 mês).

---

### Segurança da cadeia de fornecimento e terceiros {#segurança-da-cadeia-de-fornecimento-e-terceiros}

**Conteúdo normativo**

A NIS2 enfatiza segurança da cadeia de fornecimento e de aquisição/desenvolvimento/manutenção (Art. 21), incluindo verificação dos fornecedores críticos e medidas técnicas verificáveis.

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Inventário de dependências e SBOM | Cap. 05 | SBOM, SCA, políticas de atualização |
| Requisitos contratuais técnicos | Cap. 14 | Governança e contratação, práticas de avaliação |
| Arquiteturas portáveis e planos de saída | Cap. 04, Cap. 08 | Arquitetura segura, IaC |

**O que o SbD-ToE cobre**

- Inventário de dependências e SBOM, SCA, políticas de atualização (Cap. 05).
- Requisitos contratuais técnicos (Cap. 14) e práticas de avaliação.
- Arquiteturas portáveis e planos de saída (técnicos).

**Lacunas intencionais**

Listas nacionais de entidades a registar, procedimentos de designação e requisitos jurídicos de contrato (variam entre Estados-Membros). Campos normativos específicos de registos nacionais.

**Como cumprir**

Sugere-se estender o registo de fornecedores do Cap. 05 com os campos exigidos pela autoridade nacional (seguindo guias/portais locais e as notas da ENISA).

---

### Continuidade, crise e operação {#continuidade-crise-e-operação}

**Conteúdo normativo**

A NIS2 pede continuidade de negócio, gestão de crise, backups e DR testados, e monitorização/logging eficazes (Art. 21).

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Runbooks e exercícios de resposta/recuperação | Cap. 12 | Runbooks, exercícios, testes |
| Backups com testes de restauração | Cap. 12 | Cópias de segurança com restauro testado ([`OPS-016`](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/catalogo-requisitos-operacoes#catálogo-ops---monitorização-e-operações)), com cadência por nível |
| Logging/observabilidade "by design" | Cap. 12 | Logging, observabilidade, retenção |

**O que o SbD-ToE cobre**

- Runbooks e exercícios de resposta/recuperação (Cap. 12).
- Cópias de segurança com restauro testado (OPS-016) e objectivos e procedimento de recuperação da aplicação (OPS-017).
- Logging/observabilidade "by design" (Cap. 12), com orientação para retenção alinhável a normas.

**Lacunas intencionais**

Períodos de retenção e campos exactos de logs: variam entre NIS2, DORA e regimes setoriais; o manual define "logs com campos obrigatórios" e deixa os campos finais para serem plugados segundo o normativo aplicável (NIS2 aqui). Continuidade empresarial ampla, BCM corporativo e gestão de crise institucional também podem exigir artefactos fora do manual base.

**Redundância e continuidade**

As cópias de segurança e o restauro testado (OPS-016) e a recuperação da aplicação (OPS-017) estão prescritos. A redundância pelo menos parcial dos sistemas (Reg. de Execução (UE) 2024/2690, anexo, ponto 4.2.4) entra só para as entidades pertinentes, como requisito do contexto NIS2 (ver [Requisitos aplicáveis](/sbd-toe/cross-check-normativo/nis2/requisitos-aplicaveis)). A continuidade do negócio e a gestão de crise da entidade ficam fora do Manual.

**Como cumprir**

Sugere-se alinhar a matriz de fontes (app, IAM, rede, cloud audit, EDR) e retenção com as orientações ENISA, colhendo exemplos de evidência para auditoria.

---

## PARTE II: SÍNTESE E REFERÊNCIAS {#parte-ii-síntese-e-referências}

### Síntese da cobertura NIS2/SbD-ToE {#síntese-da-cobertura-nis2sbd-toe}

A NIS2 pede gestão com responsabilidade, medidas com substância e reportes com prazos. O SbD-ToE oferece o coração técnico-operacional: políticas, processos, testes, inventários, automação e evidências.

As aparentes lacunas do manual - quem aprova políticas, campos rígidos de logs/incidentes, templates e formatos de submissão, pormenores jurídicos de contratos - são lacunas deliberadas: detalhes específicos que mudam entre normas e países e que, por isso, o SbD-ToE deixa configuráveis.

O resultado é estável:

- **Hoje**, o SbD-ToE oferece uma base técnico-operacional forte para práticas compatíveis com NIS2.
- **Depois**, quando a organização quiser defender conformidade NIS2, o trabalho incremental principal passa por formalizar aprovação e supervisão da gestão, esquemas de reporte externo e requisitos nacionais ou setoriais sobre essa base já existente.

Assim, o SbD-ToE mantém-se útil na prática diária, e a NIS2 acrescenta a camada de formalidade regulatória e supervisão. Juntos, oferecem um percurso de conformidade mais sustentável do que uma leitura puramente checklist.

### Setor, âmbito e sanções {#setor-âmbito-e-sanções}

A NIS2 alarga o âmbito para 18 setores (Anexos I/II) e reforça a distinção entre essenciais e importantes. Em muitos países, há registos nacionais e prazos de autoregisto para entidades abrangidas; acompanhar trackers oficiais ajuda a implementar as especificidades locais.

Em termos sancionatórios, a Diretiva obriga os Estados-Membros a prever, por violação dos art. 21.º ou 23.º, coimas com um montante máximo de, pelo menos, 10 M€ ou 2 % do volume de negócios anual mundial para entidades essenciais e de, pelo menos, 7 M€ ou 1,4 % para importantes (o que for mais elevado).

### Referências {#referências}

- **Diretiva NIS2**: Diretiva (UE) 2022/2555 (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022L2555))
- **Art. 20** - Responsabilidade do órgão de gestão e obrigação de formação.
- **Art. 21** - Medidas mínimas de gestão de risco (abordagem "all-hazards").
- **Art. 23** - Prazos de reporte de incidentes (24h/72h/1 mês) e relatórios intermédios.
- **Art. 34** - Sanções administrativas máximas (10M€ ou 2%; 7M€ ou 1,4%).
- **ENISA & Comissão Europeia (2024/2025)** - Orientações técnicas e mapeamentos práticos com exemplos de evidência para Art. 21.
- **ENISA** - *Technical implementation guidance for NIS2 risk-management measures* (exemplos de evidência e mapeamentos).
- **Autoridades nacionais NIS2** - Guias/portais de registo e requisitos locais (exemplos: NCSC nacionais).

---

:::note Exceções e evidência de controlo

A NIS2, tal como a DORA, beneficia de um processo formal de exceções à conformidade. Casos onde um requisito específico não é aplicável ou onde se aceita um risco temporário devem ser documentados, aprovados pelo órgão de gestão e revistos periodicamente.

O Cap. 14 (Governança e Contratação) do SbD-ToE fornece os artefactos necessários: registo de exceções, critérios de aceitação de risco, cadeia de aprovação e plano de remediação. A existência deste processo não é sinal de fragilidade - é evidência de governação madura e de controlo consciente sobre o perfil de risco da organização.

:::
