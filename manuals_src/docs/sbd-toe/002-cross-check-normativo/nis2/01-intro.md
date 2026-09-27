---
id: intro
title: NIS2 - Cross-check normativo
description: O que o SbD-ToE cobre, as lacunas que declara e o que deixa fora do âmbito face à Diretiva NIS2 (UE 2022/2555)
tags: [cross-check, nis2, diretiva, ciberseguranca, incident-reporting, governance]
sidebar_position: 3
---

# Cross-check normativo - NIS2

## Âmbito {#âmbito}

A **Diretiva (UE) 2022/2555 (NIS2)** (CELEX: [32022L2555](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022L2555)) atualiza o quadro europeu de cibersegurança para entidades essenciais e importantes em 18 setores, reforçando governação, medidas de gestão de risco e obrigação de reporte de incidentes. Os Estados-Membros tinham até 17 de outubro de 2024 para transpor a NIS2; a NIS1 foi revogada a 18 de outubro de 2024.

No espírito da NIS2, não chega "ter controlos" - é preciso demonstrar capacidade operacional e responsabilização da gestão. O SbD-ToE, construído top-down e atento a múltiplas referências, encaixa naturalmente neste ethos: entrega processos, políticas e artefactos técnicos reutilizáveis, deixando propositadamente algumas variáveis em aberto para preservar a universalidade do manual.

Este documento apresenta:

1. **PARTE I: ANÁLISE NORMATIVA** - mapeamento artigo a artigo dos requisitos NIS2 para capítulos SbD-ToE, identificando o que o Manual cobre, as lacunas que declara, o que fica fora do âmbito e os passos de integração.
2. **PARTE II: SÍNTESE E REFERÊNCIAS** - visão consolidada da relação NIS2/SbD-ToE e referências normativas.

## O que este Manual cobre e o que fica de fora {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

O SbD-ToE é centrado na aplicação: requisitos, arquitetura, código, dependências, pipeline, deploy e operação do software. Para cada obrigação da NIS2, o Manual responde numa de três categorias, e nenhuma obrigação fica em silêncio:

- **Cobre**, e diz de que forma: requisito do catálogo, política, piso ou requisito acrescentado pelo regime, ou evidência de engenharia para um dever de outro plano.
- **Lacuna declarada**: o que o Manual não cobre por omissão, com o que falta.
- **Fora de âmbito**: o que o Manual não trata, com a razão.

A lista completa, obrigação a obrigação, é gerada da matriz de cobertura e está em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura). Quando esta página e a lista divergirem, prevalece a lista.

**Fora de âmbito, por decisão do programa:**
- Segurança da entidade como um todo (rede corporativa e canais de administração, EDR, patching de sistemas operativos e equipamentos, inventário e classificação de todos os ativos): o Manual é centrado na aplicação.
- Continuidade do negócio, gestão de crise e BIA da entidade. O Manual cobre as cópias de segurança, o restauro testado e a recuperação da aplicação (OPS-016, OPS-017).

---

## PARTE I: ANÁLISE NORMATIVA {#parte-i-análise-normativa}

### Artigo 20 - Governação e responsabilização {#artigo-20---governação-e-responsabilização}

**Conteúdo normativo**

O Art. 20 coloca o órgão de direção no centro: aprova as medidas de gestão dos riscos de cibersegurança, supervisiona a sua aplicação e pode ser responsabilizado por infrações. Exige ainda formação para os membros do órgão de direção (e incentiva formação regular dos trabalhadores).

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Aprovação de medidas pelo órgão de gestão | Cap. 14, Cap. 02 | Aprovação formal do modelo de governação e das políticas pela direção (GOV-001); a aprovação das medidas do art. 21.º pelo órgão de direção é lacuna declarada |
| Supervisão da execução | Cap. 12, Cap. 14 | Métricas, evidências operacionais, monitorização e escalonamento |
| Formação do órgão de direção | Cap. 13 | Parcial: a Política 37 prevê só «Awareness executivo» em L1; a formação obrigatória do órgão de direção e a formação regular do pessoal não técnico ficam como lacuna declarada |

**O que o SbD-ToE cobre**

- Define base técnica de requisitos e políticas (Cap. 02) e a cadeia de governança/aprovação aplicável (Cap. 14).
- Estabelece ciclos de supervisão, monitorização e evidência operacional (Cap. 12), articuláveis com a accountability de gestão.
- Prescreve formação e onboarding para funções técnicas e terceiros com acesso (Cap. 13); a formação do órgão de direção é lacuna declarada.

**Lacunas declaradas**

O Manual exige a aprovação formal, pela direção, do modelo de governação e das políticas (GOV-001), mas não atribui ao órgão de direção a aprovação das medidas do art. 21.º como um todo, a supervisão da sua aplicação nem a responsabilização pessoal. Também não exige que se designe uma pessoa que responda diretamente perante o órgão de direção, e a aceitação do risco residual sobe, no máximo, ao CISO. A forma jurídica da cadeia de aprovação fica, por opção, com a organização.

**Como cumprir**

Sugere-se registar, no Cap. 14, como a cadeia de aprovação e supervisão da gestão foi formalizada, usando o catálogo do Cap. 02 como base técnica e guardando evidência da formação periódica do órgão de direção, que a organização assegura para além do Manual (Art. 20).

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
| Higiene cibernética/treino | Cap. 13 | Formação de funções técnicas e de terceiros com acesso (TRN-002, TRN-007); ciber-higiene e sensibilização de todo o pessoal e do órgão de direção ficam como lacuna declarada |
| IAM, contas privilegiadas, criptografia | Cap. 02, Cap. 04, Cap. 14 | MFA (AUT-001); revisão de acessos (ACC-010, GOV-014); contas privilegiadas e de administração (GOV-016, GOV-017); ciclo de vida das chaves e inventário de certificados (ENC-007); agilidade criptográfica (ENC-003); nas entidades pertinentes, obrigatórios em qualquer nível (CTX-NIS2-P12, P13, P18 a P21) |
| Gestão de ativos e segurança dos RH | Cap. 01, Cap. 13 | Inventário de aplicações e componentes (CLA-008, DEP-001); o inventário de todos os ativos é segurança da entidade, fora do âmbito, e a política de tratamento de ativos é lacuna declarada; a segurança dos RH fica fora do âmbito (gestão de pessoal), salvo onboarding e offboarding |
| Tratamento e divulgação de vulnerabilidades | Cap. 05, Cap. 10, Cap. 14 | Dependências, SCA, testes; divulgação coordenada e tratamento das comunicações externas (GOV-015; CTX-NIS2-P14, P15). A correção de sistemas operativos, equipamentos de rede e software de prateleira é segurança da entidade, fora do âmbito do Manual |
| Logging e monitorização | Cap. 12 | Observabilidade, SIEM, alertas; nas entidades pertinentes são obrigatórios a análise regular, os alarmes com limiares e a cópia de segurança dos registos (LOG-004, LOG-007, OPS-005, LOG-005; CTX-NIS2-P03 a P06); o tráfego de rede e a redundância da monitorização ficam como lacuna declarada |

**O que o SbD-ToE cobre**

- **Políticas e controlos técnicos** (Cap. 02 - Requisitos de Segurança).
- **Classificação de criticidade** e risco proporcional (Cap. 01 - Classificação de Aplicações).
- **Threat modeling** (Cap. 03).
- **Cadeia de fornecimento**: SBOM/SCA, dependências (Cap. 05).
- **CI/CD & IaC** seguros (Cap. 07, Cap. 08); containers/runtime (Cap. 09).
- **Testes** (Cap. 10) e deploy seguro (Cap. 11).
- **Monitorização, logging, resposta e melhoria contínua** (Cap. 12).
- **Governança & contratação** (Cap. 14), incluindo avaliação de terceiros.

**Lacunas declaradas e fora do âmbito**

O Manual é centrado na aplicação. Ficam fora do âmbito, com razão registada, a segurança física e ambiental, os postos de trabalho e os suportes amovíveis, a gestão de recursos humanos, a continuidade do negócio e a gestão de crises, e a segurança da entidade como um todo (inventário de todos os ativos, EDR, correção de sistemas operativos). Entre as lacunas declaradas estão a ciber-higiene de todo o pessoal, a política de tratamento de ativos e a certificação europeia na aquisição (art. 24.º). Os formatos «fechados», como campos de logs e modelos de políticas, continuam deliberadamente genéricos. O detalhe, requisito a requisito, está em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura).

**Como cumprir**

Sugere-se usar o catálogo do Cap. 02 como base de SoA técnica, complementado por `01/03/05/10/12/14`, e alinhar as evidências com o guia técnico da ENISA (exemplos de evidência e mapeamentos). O contexto NIS2 declara-se por entidade e é herdado por todas as aplicações; nas entidades pertinentes do Reg. de Execução (UE) 2024/2690 aplica-se também o grau PERTINENTE. Os níveis L1–L3 continuam a resultar da classificação de cada aplicação (Cap. 01) e não correspondem às categorias essencial e importante.

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
| Processo de resposta obrigatório | Cap. 12 | IRP obrigatório em qualquer nível no contexto NIS2 (CTX-NIS2-P01), com post-mortem dos incidentes significativos e revisão dos artefactos afetados (Política 32 §4.6) |

**O que o SbD-ToE cobre**

- Processo de deteção e resposta, com pós-incidente (Cap. 12).
- Papéis de escalonamento e responsabilidades (Cap. 14).
- Critérios de impacto (Cap. 01) que suportam a classificação de severidade.

**Cobertura e lacunas declaradas**

O registo do incidente recolhe os dados de impacto (Política 32 §4.3). O critério de incidente significativo (CTX-NIS2-R02) e, nas entidades pertinentes, os limiares e a agregação dos incidentes recorrentes do Reg. de Execução (UE) 2024/2690 (CTX-NIS2-R03) decidem se o incidente é notificável. Os prazos e o conteúdo mínimo de cada etapa estão na Política 32 §6 e §6.1. A escala P1–P4 é interna e não substitui estes critérios. O Manual não substitui os formulários nem os canais da CSIRT. Ficam como lacuna declarada a notificação aos destinatários do serviço (art. 23.º, n.º 1), a comunicação aos destinatários das ciberameaças significativas (n.º 2) e a informação ao público quando a CSIRT o exija (n.º 7).

**Como cumprir**

Sugere-se partir dos dados de impacto da Política 32 §4.3 e do conteúdo mínimo da §6.1 e ligar os exportadores do SIEM/ITSM aos formulários da CSIRT nacional, nos prazos de 24 h, 72 h e 1 mês.

---

### Segurança da cadeia de fornecimento e terceiros {#segurança-da-cadeia-de-fornecimento-e-terceiros}

**Conteúdo normativo**

A NIS2 enfatiza segurança da cadeia de fornecimento e de aquisição/desenvolvimento/manutenção (Art. 21), incluindo verificação dos fornecedores críticos e medidas técnicas verificáveis.

**Cobertura SbD-ToE**

| Requisito NIS2 | Capítulo SbD-ToE | Cobertura |
|---|---|---|
| Inventário de dependências e SBOM | Cap. 05 | SBOM, SCA, políticas de atualização |
| Requisitos contratuais técnicos | Cap. 14 | Governança e contratação, práticas de avaliação (GOV-006, GOV-007); nas entidades pertinentes, política da cadeia de abastecimento em qualquer nível (Política 33; CTX-NIS2-P07 a P09) |
| Saída de fornecedores | Cap. 14 | Offboarding com revogação de acessos e eliminação ou devolução dos dados (Política 33 §7.1) |

**O que o SbD-ToE cobre**

- Inventário de dependências e SBOM, SCA, políticas de atualização (Cap. 05).
- Requisitos contratuais técnicos (Cap. 14) e práticas de avaliação.
- Offboarding de fornecedores, com revogação de acessos e eliminação ou devolução dos dados (Política 33 §7.1).

**Fora do âmbito e lacunas declaradas**

O registo junto da autoridade, a designação de representante e o conteúdo jurídico dos contratos pertencem ao plano jurídico-administrativo e ficam fora do âmbito. São lacunas declaradas a exigência de produtos TIC certificados ao abrigo do CSA quando o Estado-Membro o imponha (art. 24.º, n.º 1), as avaliações coordenadas de riscos da UE nos critérios de seleção (art. 22.º), a qualidade global dos produtos e os procedimentos de desenvolvimento seguro do fornecedor como critério explícito, as atualizações de segurança durante toda a vida útil e a verificação de antecedentes do pessoal do fornecedor.

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

**Cobertura e fora do âmbito**

Os atributos mínimos dos registos (LOG-002), o catálogo de eventos (OPS-002) e a retenção por tipo de registo (LOG-005; Política 29 §7) estão prescritos; nas entidades pertinentes, a análise regular, os alarmes com limiares e a cópia de segurança dos registos são obrigatórios (CTX-NIS2-P03 a P06). Os prazos da Política 29 §7 são escolha do Manual: prevalece o mais exigente de entre a lei, a legislação nacional, os supervisores e o setor. A continuidade do negócio, o BCM corporativo e a gestão de crises da entidade ficam fora do âmbito do Manual, que é centrado na aplicação: a war room P1 da Política 32 é resposta a incidentes, não gestão de crises.

**Redundância e continuidade**

As cópias de segurança e o restauro testado (OPS-016) e a recuperação da aplicação (OPS-017) estão prescritos. A redundância pelo menos parcial dos sistemas (Reg. de Execução (UE) 2024/2690, anexo, ponto 4.2.4) entra só para as entidades pertinentes, como requisito do contexto NIS2 (ver [Requisitos aplicáveis](/sbd-toe/cross-check-normativo/nis2/requisitos-aplicaveis)). A continuidade do negócio e a gestão de crise da entidade ficam fora do Manual.

**Como cumprir**

Sugere-se alinhar com as orientações da ENISA as fontes que o Manual cobre (aplicação, IAM, cloud audit) e a retenção, colhendo exemplos de evidência para auditoria. As fontes da entidade, como a rede e o EDR, vêm da segurança da entidade, fora do âmbito do Manual.

---

## PARTE II: SÍNTESE E REFERÊNCIAS {#parte-ii-síntese-e-referências}

### Síntese da cobertura NIS2/SbD-ToE {#síntese-da-cobertura-nis2sbd-toe}

A NIS2 pede gestão com responsabilidade, medidas com substância e reportes com prazos. O SbD-ToE oferece o coração técnico-operacional: políticas, processos, testes, inventários, automação e evidências.

A resposta do Manual à NIS2 tem três partes. Cobre, com a forma indicada em cada requisito, a base técnico-operacional. Declara lacunas onde fica aquém, como a formação do órgão de direção, a ciber-higiene de todo o pessoal ou a gestão de ativos para além das aplicações. E deixa fora do âmbito, com razão, a segurança da entidade como um todo, a continuidade do negócio e a relação administrativa com as autoridades. Os modelos de submissão e os pormenores jurídicos dos contratos continuam deliberadamente configuráveis.

O resultado é estável:

- **Hoje**, o SbD-ToE oferece uma base técnico-operacional forte para práticas compatíveis com NIS2.
- **Depois**, quando a organização quiser defender conformidade NIS2, o trabalho incremental principal passa por formalizar a aprovação e a supervisão pelo órgão de direção, fechar as lacunas declaradas que lhe interessem, assegurar o que fica fora do âmbito do Manual e ligar o conteúdo mínimo da Política 32 §6.1 aos formulários nacionais, sobre essa base já existente.

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

A NIS2, tal como a DORA, beneficia de um processo formal de exceções à conformidade. Casos em que um requisito não se aplica, ou em que se aceita um risco temporário, são documentados e revistos periodicamente (GOV-004; Políticas 03 e 05). No Manual, a alçada de aprovação sobe, no máximo, ao CISO. São lacunas declaradas a aceitação do risco residual pelo órgão de direção e a fundamentação, requisito a requisito, das isenções por nível que o Reg. de Execução (UE) 2024/2690 pede (art. 2.º).

O Cap. 14 (Governança e Contratação) do SbD-ToE fornece os artefactos: registo de exceções, critérios de aceitação de risco, alçadas de aprovação e plano de remediação. A existência deste processo não é sinal de fragilidade - é evidência de governação madura e de controlo consciente sobre o perfil de risco da organização.

:::
