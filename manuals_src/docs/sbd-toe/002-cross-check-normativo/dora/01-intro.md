---
id: intro
title: DORA - Cross-Check Normativo
description: Análise de como o SbD-ToE cobre os requisitos técnicos do Regulamento DORA (UE 2022/2554)
tags: [cross-check, dora, regulamentacao, ict-risk, resiliencia, finanças]
sidebar_position: 1
---

# DORA: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 DORA](/sbd-toe/cross-check-normativo/dora/playbook).
> 
> Para exemplos práticos internos, ver pasta `exemplo-playbook/`.

## Enquadramento Geral {#enquadramento-geral}

O **Digital Operational Resilience Act (DORA)** - **Regulamento (UE) 2022/2554** (CELEX: [32022R2554](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32022R2554)) - representa uma viragem histórica na forma como a União Europeia encara a **resiliência digital** no setor financeiro.  
A partir de janeiro de 2025, não basta às entidades financeiras protegerem dados ou cumprirem boas práticas gerais: exige-se que demonstrem, com evidências e mecanismos consistentes, que **sabem identificar, prevenir, detetar, responder e aprender com riscos tecnológicos**.

O SbD-ToE foi concebido como **modelo de segurança aplicacional**. Cobre boa parte da base técnica do DORA do lado da aplicação, declara as lacunas onde fica aquém e deixa fora do âmbito, com razão, o que é da entidade como um todo. Este documento consolida:

1. **Cross-check normativo:** Como o SbD-ToE mapeia para DORA
2. **Playbook prático:** Roadmap de 12–18 meses para implementação

## O que este Manual cobre e o que fica de fora {#o-que-este-manual-cobre-e-o-que-fica-de-fora}

O SbD-ToE é centrado na aplicação: requisitos, arquitetura, código, dependências, pipeline, deploy e operação do software. Para cada obrigação do DORA, o Manual responde numa de três categorias, e nenhuma obrigação fica em silêncio:

- **Cobre**, e diz de que forma: requisito do catálogo, política, piso ou requisito acrescentado pelo regime, ou evidência de engenharia para um dever de outro plano.
- **Lacuna declarada**: o que o Manual não cobre por omissão, com o que falta.
- **Fora de âmbito**: o que o Manual não trata, com a razão.

A lista completa, obrigação a obrigação, é gerada da matriz de cobertura e está em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura). Quando esta página e a lista divergirem, prevalece a lista.

**Fora de âmbito, por decisão do programa:**
- Segurança da entidade como um todo (rede corporativa e canais de administração, EDR, patching de sistemas operativos e equipamentos, inventário e classificação de todos os ativos): o Manual é centrado na aplicação.
- Continuidade do negócio, gestão de crise e BIA da entidade. O Manual cobre as cópias de segurança, o restauro testado e a recuperação da aplicação (OPS-016, OPS-017).

---

## PARTE I: ANÁLISE NORMATIVA {#parte-i-análise-normativa}

### 🔍 O que DORA exige, em termos operacionais {#-o-que-dora-exige-em-termos-operacionais}

> ⚖️ **Nota editorial.**  
> Esta secção é uma **síntese operacional** dos artigos relevantes do DORA, não uma citação literal do regulamento.  
> Baseia-se, em particular, nos Artigos 5.º–6.º (governação e gestão de risco TIC), 8.º–15.º (proteção, prevenção, deteção, resposta e recuperação), 17.º–23.º (incidentes e reporte), 24.º–27.º (testes de resiliência) e 28.º–30.º (fornecedores TIC). A partilha de informação sobre ameaças (Art. 45.º) e o regime simplificado de gestão de risco (Art. 16.º) funcionam como enquadramento complementar, não como blocos principais de aterragem.

De forma prática, o DORA traduz-se em obrigações que impactam diretamente as práticas do SbD-ToE:

- **Órgão de administração com responsabilidade explícita (Art. 5.º).**  
  - O órgão de gestão aprova a estratégia de gestão de risco TIC, acompanha a sua execução e é responsável por garantir que existem políticas, procedimentos, documentação e evidência.  
  - No SbD-ToE isto liga-se à governação global, políticas e à exigência de _accountability_ sobre decisões de risco.

- **Gestão de risco TIC estruturada e documentada (Art. 6.º).**  
  - O regulamento exige identificação de ativos críticos, avaliação de impacto, definição de controlos e monitorização contínua.  
  - O SbD-ToE fornece os blocos técnicos (capítulos 01–14) que podem ser usados como catálogo de controlos para cumprir esta obrigação.

- **Gestão de incidentes, classificação e reporte estruturado (Art. 17.º–23.º).**  
  - DORA define requisitos mínimos para classificação, registo, escalonamento e reporte de incidentes de TIC a autoridades competentes, em prazos definidos.  
  - O manual fornece práticas para deteção, _logging_, evidência técnica e _runbooks_ que suportam estes fluxos.

- **Testes de resiliência operacional digital (Art. 24.º–27.º).**  
  - Exige um programa de testes regulares, proporcional ao risco (incluindo _threat-led penetration testing_ para entidades mais críticas).  
  - No SbD-ToE isto cruza com os testes de segurança aplicacional (Cap. 10), a preparação para o TLPT e a validação contínua de pipelines. Os testes de desempenho, de continuidade e baseados em cenários são lacuna declarada; o TLPT regulado fica fora do âmbito.

- **Gestão de risco de terceiros TIC (Art. 28.º–30.º).**  
  - Impõe um registo de informações sobre todos os acordos contratuais com terceiros prestadores de serviços de TIC (distinguindo os que apoiam funções críticas ou importantes), avaliação de risco, cláusulas contratuais específicas e supervisão contínua.  
  - O Manual cobre a parte técnica: SBOM e SCA, devida diligência e cláusulas de segurança, e ciclo de vida dos fornecedores com acesso. O registo de informações (Reg. de Execução (UE) 2024/2956), o conteúdo contratual específico do DORA e a superintendência dos prestadores críticos ficam fora do âmbito. A devida diligência plena do Reg. Delegado (UE) 2024/1773, o programa de auditorias aos prestadores e os planos de transição são lacunas declaradas.

- **Decisões de exceção e vulnerabilidades não remediadas.**  
  - Embora o regulamento não use exatamente esta formulação, a combinação de exigências sobre gestão de risco, testes, incidentes e terceiros implica que:  
    - **exceções a testes de resiliência**,  
    - **aceitação de vulnerabilidades não remediadas**, e  
    - **desvios às políticas de segurança aprovadas**  
    devem ser **formalmente analisados, contextualizados, aprovados ao nível adequado e documentados** (incluindo justificação, prazo, _owner_ e medidas compensatórias).  
  - O SbD-ToE materializa isto em _playbooks_ de Risk Acceptance, fluxos de aprovação, registos estruturados e KPIs.

Na prática, o DORA fornece o "chapéu regulatório" e os critérios de responsabilização; o SbD-ToE funciona como o **manual técnico** que torna essas obrigações executáveis no ciclo de vida de desenvolvimento e operação.

---

### Governação e Gestão de Risco TIC (Artigos 5–6 DORA) {#governação-e-gestão-de-risco-tic-artigos-56-dora}

**Cobertura SbD-ToE:**
- **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro):** Classificação de criticidade aplicacional (L1–L3)
- **[Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro):** Catálogo de requisitos de segurança por nível
- **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro):** Threat Modeling para identificação de riscos
- **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Deteção, resposta e melhoria contínua
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Governação e aprovação de políticas

**Fora do âmbito:** O SbD-ToE não fixa o nível hierárquico de aprovação acima do CISO: os deveres do órgão de administração e a estrutura de governo interno (art. 5.º; art. 6.º, n.º 4) são da entidade. O Manual exige a aprovação formal do modelo de governação e das políticas pela direção (GOV-001) e fixa as alçadas das exceções e da aceitação de risco (Políticas 03 §7 e 05 §6). Para o DORA, a entidade mapeia estas políticas para a aprovação formal no órgão de administração, com registo documental da decisão.

---

### Proteção, deteção, resposta e recuperação (Artigos 8–16 DORA) {#proteção-deteção-resposta-e-recuperação-artigos-816-dora}

**Cobertura SbD-ToE:**
- Cópias de segurança com restauro testado em sistemas separados (OPS-016; CTX-DORA-P11)
- Objetivos e procedimento de recuperação da aplicação (OPS-017; também em L1 nas funções críticas ou importantes, CTX-DORA-P12)
- Capacidades redundantes e testes de comutação (CTX-DORA-R01)
- Ciclo de vida das chaves e registo de certificados (ENC-007; CTX-DORA-P15, P16); inventário e agilidade criptográfica (ENC-003; CTX-DORA-P17)
- Revisão semestral das regras de filtragem de rede nas funções críticas ou importantes (ARC-006; CTX-DORA-P18)
- Autenticação forte, contas privilegiadas e gestão de identidades (AUT-001, GOV-016, GOV-017; CTX-DORA-P07, P13, P14)
- Revisão dos acessos, anual e semestral nas funções críticas ou importantes (ACC-010; CTX-DORA-P05, P06)
- Divulgação responsável de vulnerabilidades (GOV-015; CTX-DORA-P10) e análise automatizada semanal de vulnerabilidades dos ativos que apoiam funções críticas ou importantes (Política 10 §9; CTX-DORA-P08)
- Testes dinâmicos em qualquer nível (TST-005; CTX-DORA-P03); alarme em falhas do logging (LOG-008; CTX-DORA-P04) e alertas automáticos nas funções críticas ou importantes (OPS-005; CTX-DORA-P09)

**Lacunas declaradas:** a política de gestão dos ativos de TIC para além das aplicações e dos componentes (hardware, rede, licenças, fim de suporte), a gestão de capacidade, a política de segurança das redes da entidade e o plano de administração de rede dedicado, a prevenção de fugas de dados e a proteção dos dados em utilização.

**Fora do âmbito:** a continuidade do negócio e a gestão de crises (arts. 11.º, n.os 1 e 7, e 14.º), a segurança física e dos postos de trabalho e a infraestrutura de rede corporativa: o Manual é centrado na aplicação.

---

### Incidentes, Classificação e Reporte (Artigos 17–23 DORA) {#incidentes-classificação-e-reporte-artigos-1723-dora}

Exige processo ponta-a-ponta: deteção, registo, classificação, reporte formal e integração com templates/campos harmonizados.

**Cobertura SbD-ToE:**
- **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Processos de deteção e resposta de incidentes
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Responsabilidades de reporte e escalonamento

**Cobertura, lacuna declarada e fora do âmbito:** A escala P1–P4 (Política 31) define a severidade interna, mas não a classificação de incidentes do DORA (Reg. Delegado (UE) 2024/1772) nem templates específicos DORA: essas vêm do contexto DORA e da Política 32. O registo do incidente recolhe os dados de impacto (Política 32 §4.3). No contexto DORA, o processo de gestão de incidentes é obrigatório em qualquer nível (CTX-DORA-P01); os incidentes classificam-se com os critérios do art. 18.º, n.º 1, e os limiares do Reg. Delegado (UE) 2024/1772, com avaliação mensal dos recorrentes (CTX-DORA-R02), e as ciberameaças significativas ficam registadas (CTX-DORA-R03). Os prazos e o conteúdo seguem a Política 32 §6 e §6.1, com os modelos do Reg. de Execução (UE) 2025/302. Fica fora do âmbito a relação com a autoridade (canais, submissão, procedimentos). É lacuna declarada o reporte dos incidentes severos ao órgão de administração (art. 17.º, n.º 3, al. e)).

---

### Testes de Resiliência (Artigos 24–27 DORA) {#testes-de-resiliência-artigos-2427-dora}

Exige programa contínuo de testes, culminando em Threat-Led Penetration Testing (TLPT) para entidades elegíveis.

**Cobertura SbD-ToE:**
- **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro):** Threat Modeling (cenários de ataque realistas)
- **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro):** Catálogo de testes (SAST, DAST, fuzzing, etc.)
- **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro):** Validação de segurança pré-produção

**Cobertura parcial - ver [Cap. 10 → addon 14: TLPT Readiness](/sbd-toe/sbd-manual/testes-seguranca/addon/tlpt-readiness):** O SbD-ToE enquadra o que é o TLPT, o que o distingue do PenTest convencional e como a maturidade do programa de testes se relaciona com o exercício. O que permanece fora do âmbito do manual são os critérios de elegibilidade (identificação pela autoridade competente), a qualificação formal de testers e providers segundo o Reg. Delegado (UE) 2025/1190, e o processo de attestation pela autoridade TLPT designada - estes aspectos são da competência das equipas de compliance e da relação com o supervisor.

---

### Gestão de Fornecedores Críticos (Artigos 28–30 DORA) {#gestão-de-fornecedores-críticos-artigos-2830-dora}

Os Artigos 28–30 estabelecem requisitos para inventário formal, avaliação de risco, cláusulas contratuais obrigatórias, supervisão contínua e planos de saída testados.

**Cobertura SbD-ToE (Duas categorias de fornecedores, uma estratégia):**

**Categoria 1: Fornecedores de Componentes de Software ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) - SBOM)**
- **Contexto DORA:** Componentes de software (bibliotecas, frameworks) de terceiros constituem fornecedores implícitos de tecnologia
- **Solução técnica:** a SBOM (Software Bill of Materials) identifica os componentes e a sua origem (projeto, autor ou editor)
- **Característica:** Fornecedores implícitos - os autores de componentes frequentemente desconhecem que integram a cadeia de fornecimento
- **Gestão operacional:** SCA contínuo (análise de vulnerabilidades), gestão de atualizações de segurança, rastreamento de licenças
- **Relação com o DORA:** a SBOM é evidência complementar. Os autores de componentes de código aberto não são, em regra, prestadores terceiros de serviços de TIC com quem a entidade tenha um acordo contratual; o registo de informações do art. 28.º, n.º 3, abrange os acordos contratuais (Reg. de Execução (UE) 2024/2956), e a SBOM não o substitui

**Categoria 2: Fornecedores Contratuais ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) - Governance)**
- Entidades contratadas formalmente: contractors, outsourcing, prestadores de serviços
- **Característica:** Fornecedores explícitos com contratos e responsabilidades formalmente documentadas
- Ciclo de vida estruturado: preparação → onboarding → monitorização → offboarding
- User Stories US-15 a US-20: Processos de gestão de contractors/fornecedores

**Artefactos de suporte (Cap. 14):**
- Template de validação pré-acesso de contractors
- Guia de preparação técnica de sandbox
- Checklist de offboarding seguro

**Conformidade DORA (Art. 28–30):**
- São quatro coisas distintas: o inventário de componentes (SBOM), a proveniência desses componentes, os prestadores terceiros de serviços de TIC e os acordos contratuais com eles
- A SBOM alimenta o inventário de risco técnico de componentes; os prestadores e os acordos contratuais alimentam o registo de informações e a gestão do risco de terceiros, que são da entidade
- **Fora do âmbito:** O SbD-ToE não inclui templates ITS nem fórmulas de análise de concentração DORA. O registo de informações (Reg. de Execução (UE) 2024/2956), a análise do risco de concentração (art. 29.º), o conteúdo contratual específico do DORA e a superintendência dos prestadores terceiros críticos são da entidade e da relação com o supervisor.
- **Lacunas declaradas:** a devida diligência plena do Reg. Delegado (UE) 2024/1773 (capacidade e continuidade do prestador, localização, idoneidade), o programa de auditorias aos prestadores com frequência baseada no risco e os planos de transição e de migração integral dos dados (art. 28.º, n.os 4 a 6 e 8).
- **Base do Manual:** SBOM atualizado ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)), inventário formal de contractors e cláusulas de segurança proporcionais ao risco ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro); GOV-006, GOV-007).

---

### Partilha de Informação sobre Ameaças (Artigo 45 DORA, contexto complementar) {#partilha-de-informação-sobre-ameaças-artigo-45-dora-contexto-complementar}

O Artigo 45 DORA estabelece arranjos de partilha de informação sobre ciberameaças e inteligência de ameaças, promovendo a cooperação entre entidades financeiras e com as autoridades competentes.

**Cobertura SbD-ToE:**
- **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Integração de indicadores de threat intelligence em processos de monitorização
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Estruturas de governança e responsabilidades de reporte

**Fora do âmbito:** O SbD-ToE não prescreve acordos institucionais específicos nem processos de notificação ao supervisor: a participação em acordos de partilha de informação e a sua notificação à autoridade (art. 45.º) são da entidade. No contexto DORA, as ciberameaças significativas ficam registadas (CTX-DORA-R03). A integração de feeds de threat intelligence (ex: STIX/TAXII, MISP) e a formalização de canais de partilha com autoridades competentes seguem as orientações setoriais.

---

### Gestão de Exceções e Desvios (Artigos 5, 17–23, 24–27, 28–30 DORA) {#gestão-de-exceções-e-desvios-artigos-5-1723-2427-2830-dora}

DORA não menciona explicitamente "exceções", porém em **conformidade regulatória**, exceções constituem **desvios formais de requisitos** que exigem:
- Aprovação documentada com autoridade formal designada
- Justificação técnica e de negócio
- Período de validade definido
- Plano de remediação estruturado

**Cobertura SbD-ToE (Parcial):**
- **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro):** Gestão de exceções em testes de segurança com aprovação formal (ex: vulnerabilidades conhecidas com justificação)
- **[Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro):** Rastreamento de exceções de configuração em IaC
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Estrutura RACI para aprovações
- **[Política 05](/sbd-toe/assets/policies/policy-gestao-excecoes):** processo formal de exceções, alçadas de aprovação por nível e severidade (§6) e prazos de validade (§7)

**O que o Manual define e o que fica para a entidade.** O Manual define as alçadas de aprovação por nível e severidade (Política 05 §6), os prazos de validade (Política 05 §7) e os SLA de remediação (Política 19 §4.3), e regista toda a não-aplicação de um controlo com justificação, compensação, aprovador e prazo (GOV-004). Ficam para a entidade a elevação ao órgão de administração, as categorias que o supervisor considere inadmissíveis e o reporte de exceções ao regulador.

**Conformidade DORA:**
- Estabelecer política formal de exceções com estrutura de governança e rastreabilidade
- Documentar cada exceção: justificação, aprovador, data de expiração, plano de correção
- Manter trilho auditado de exceções (passível de inspeção regulatória)
- Validar admissibilidade com supervisor (algumas exceções podem violar Art. 5)

---

### Exceções Formais e Desvios de Conformidade (Artigos 5, 17–23, 24–27, 28–30 DORA) {#exceções-formais-e-desvios-de-conformidade-artigos-5-1723-2427-2830-dora}

#### O Problema: Exceções Informais = Incoerência com DORA {#o-problema-exceções-informais--incoerência-com-dora}

DORA Art. 5 estabelece que a **resiliência digital é responsabilidade última do órgão de gestão** (board), e **supervisão de execução** significa:
- Conhecer **todos os desvios** de políticas de segurança
- Aprovar formalmente exceções a controlos
- Documentar razões, período de validade e plano de remediação
- Manter trilho auditado para demonstrar ao regulador

**Cenário crítico (incoerência com DORA):**
| Situação | Risco | Impacto | Posição DORA |
|----------|-------|--------|-------------|
| **SQLi em produção (L3) sem exceção documentada** | Exploração, violação de dados, incident notificável | Responsabilidade não-atribuída, trilho perdido | ❌ **GRAVE** - Desvio não gerido: sem registo, sem alçada e sem trilho, a entidade não demonstra a supervisão que o art. 5.º pede |
| **CVE crítico ignorado sem justificação** | Exposição contínua, compliance gap | Falha de gestão de risco TIC | ❌ **GRAVE** - Pode contrariar deveres de gestão de risco, validação e remediação contínua em DORA |
| **Exceção aprovada verbalmente (no Teams/email informal)** | Perda de trilho, falta de autoridade formal, re-negociação ad-hoc | Impossível auditar decisões | ❌ **CRÍTICO** - Sem evidência de governance; regulador questiona: "quem aprovou?" |
| **Exceção expirada sem reavaliação** | Risco aceito torna-se risco não-aceito (drift), violação técnica silenciosa | Aplicação continua com risco acima de limite | ❌ **CRÍTICO** - Violação Art. 5 (falta de supervisão contínua) |

---

#### O que DORA Exige Explicitamente {#o-que-dora-exige-explicitamente}

**Art. 5.º (Governação e organização):**
> «O órgão de administração da entidade financeira define, aprova, fiscaliza e é responsável pela aplicação de todas as disposições relacionadas com o quadro de gestão do risco associado às TIC […]» (art. 5.º, n.º 2)

**Tradução operacional:**
- Decisões de aceitação de risco (exceções) exigem aprovação documentada de autoridade formal
- Conhecer uma vulnerabilidade explorada sem decisão documentada deixa a entidade sem evidência de supervisão (leitura do Manual; o regulamento não usa esta formulação)
- Exceções requerem reavaliação periódica - a ausência de reavaliação constitui aprovação tácita indefinida, configurando falha de supervisão

**Art. 17–23 (Incidentes e reporte):**
> Exceções com impacto em incident management, classificação ou reporte devem ser contextualizadas e tratadas com trilho documental compatível com o regime regulatório aplicável.

**Art. 24–27 (Testes):**
> O programa contínuo de testes deve cobrir cenários realistas. Exceções aos testes aplicacionais (ex: componente legado não-testável) exigem compensação documentada. A periodicidade do TLPT não é excecionável internamente: o art. 26.º, n.º 1, fixa-a em pelo menos de três em três anos, e só a autoridade competente pode obrigar a entidade a reduzi-la ou aumentá-la. Uma decisão interna planeia a preparação e o âmbito, mas nunca adia a obrigação.

**Art. 28–30 (Fornecedores):**
> Exceções a SLAs de fornecedores, dependências críticas ou CVEs não mitigados devem ser escaladas conforme o modelo de risco e governação aplicável.

---

#### Cobertura SbD-ToE (Forte, mas com Gaps Explícitos) {#cobertura-sbd-toe-forte-mas-com-gaps-explícitos}

**O que SbD-ToE JÁ PRESCREVE (excelente):**

| Capítulo | O que prescreve | Nível de detalhe |
|----------|-----------------|-----------------|
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Classificação L1–L3 (base para criticidade de exceções) | ✅ Modelo E+D+I claro; criterios de L1/L2/L3 definidos |
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), addon 03** | Critérios de aceitação de risco (limiares por nível) | ✅ L1≤9, L2≤6, L3≤4; em L2, validação formal e registo; em L3, exceção só com aprovação do gestor de risco |
| **[Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), addon 08** | Gestão de exceções a requisitos (processo formal) | ✅ Identificação, justificação, avaliação, compensação, revisão periódica |
| **[Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), addon 03** | Exceções a requisitos arquiteturais | ✅ Modelo de registo com horizonte temporal; responsáveis designados |
| **[Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), addon 09** | Exceções a CVEs (formalização, owner, TTL, impacto) | ✅ Processo completo: identificação → justificação → aceitação → TTL → revalidação |
| **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Exceções a testes de segurança (com aprovação formal) | ✅ Menção explícita: "exceções formais aprovadas" |
| **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Governança de exceções (RACI, approval flow, auditoria) | ⚠️ **PARCIAL** - User Stories definem roles, mas não explicam implicações DORA |
| **[Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Waivers e exceções temporárias (durante formação) | ✅ "Justificação formal documentada, aprovada por AppSec/GRC/gestão" |
| **[Política 05](/sbd-toe/assets/policies/policy-gestao-excecoes)** | Alçadas de aprovação por nível e severidade (§6) e prazos de validade (§7) | ✅ Topo da alçada no CISO; Critical não aceitável como exceção em L3 |

---

#### Gaps Identificados (Incoerências com DORA) {#gaps-identificados-incoerências-com-dora}

**Ponto 1: Alçadas do Manual e elevação ao órgão de administração**

| Nível | SbD-ToE Prescreve | DORA Exige | Estado |
|-------|------------------|-----------|-----|
| **L1** | Tech Lead ou AppSec Engineer, por severidade (Política 05 §6) | Exceções à aplicação das políticas registadas, com a resiliência assegurada (Reg. Delegado (UE) 2024/1774, art. 2.º, n.º 2, al. c)) | ✅ Alçada formal definida |
| **L2** | AppSec Engineer; High com Gestão de Produto; Critical com CISO (Política 05 §6) | Idem | ✅ Alçada formal definida |
| **L3** | AppSec Engineer com GRC (Medium); CISO (High); Critical não aceitável (Política 05 §6) | Aceitação de risco residual acima da tolerância aprovada pelo órgão de administração, por função/responsável formalmente designado, com inventário justificado e revisão anual (RTS 2024/1774, art. 3.º, al. a) e d); DORA art. 5.º, n.º 2, e 6.º, n.º 4) | ✅ Papéis de aceitação, registo e expiração dos riscos residuais aceites estão prescritos (Política 03 §7–§8; CLA-007; GOV-004). A elevação ao órgão de administração é da entidade (DORA art. 5.º; fora do âmbito do Manual). |

**Como manifesta:** se a entidade decidir que as exceções L3 sobem ao órgão de administração, essa elevação e o seu registo são da entidade: no Manual, a alçada para no CISO.

---

**Gap 2: Falta de Descrição de Inaceitabilidade em DORA**

| Exceção | SbD-ToE | DORA |
|---------|---------|------|
| "Não implementar MFA porque é complexo" | No contexto DORA, não é exceção admissível: a autenticação forte é piso em qualquer nível (AUT-001, CTX-DORA-P07, que só admite justificação de não aplicabilidade; acesso remoto e privilegiado: GOV-016, CTX-DORA-P13, sem justificação admitida) | ❌ **Pode contrariar medidas mínimas de autenticação forte e gestão de risco TIC em DORA** |
| "SQLi em endpoint legado, mantém-se" | Segue a Política 05 como qualquer vulnerabilidade: pela severidade e pelo nível, com as alçadas e os prazos da Política 05 §6 e §7 e com compensação (ex: WAF). Uma SQLi explorável de severidade Critical não é aceitável em L3; em L2, só com aprovação do CISO, plano de remediação e TTL de 7 dias | ⚠️ O DORA não enumera vulnerabilidades nem exceções inadmissíveis; a decisão é a da Política 05, e nada se atribui ao regulamento |
| "CVE crítico em runtime, sem plano de fix" | Não aceitável em nenhum nível sem plano de remediação ativo (Política 03 §5); TTL de 7 dias em L1 e L2 e não aceitável em L3 (Política 05 §7) | ❌ **Pode contrariar deveres de remediação, validação e supervisão contínua em DORA** |

**Como manifesta:** Organização registra exceção no SbD-ToE formalmente; regulador rejeita: "esta exceção não é admissível em DORA" → perda de tempo, revisão forçada.

---

**Gap 3: Falta de Rastreamento de TTL vs. Supervisão Contínua**

| Processo | SbD-ToE | DORA Exigência | Gap |
|----------|---------|----------------|-----|
| **Criação de exceção** | Documenta com owner, TTL, critérios | ✅ Bom | ✅ Alinhado |
| **Reavaliação periódica** | Revalidação na data de expiração, com alerta 15 dias antes (Política 05 §7, escolha do Manual); re-aprovação obrigatória | ✅ Bom | ✅ Alinhado |
| **Rastreamento centralizado** | Ferramenta GRC; audit trail por aplicação | ✅ Bom | ⚠️ Manual não descreve formato de reporte a DORA |
| **Escalada ao regulador** | A notificação de incidentes está na Política 32 §6 (DORA art. 19.º); a ligação das exceções relevantes ao relatório do incidente não está prescrita | ⚠️ O DORA exige a comunicação de incidentes de caráter severo relacionados com as TIC (art. 19.º); exceções relacionadas devem constar da documentação de suporte | ⚠️ Lacuna parcial - sem guia para juntar as exceções à documentação do incidente |

**Como manifesta:** Incidente de segurança; regulador pede: "mostre-me exceções relevantes" → organização não tem visão consolidada ou não sabe se deve reportar.

---

**Gap 4: Sem Política Organizacional Formal sobre Inaceitabilidade**

O SbD-ToE descreve **como** gerir exceções e fixa alguns limites (o Critical não é aceitável em L3, Política 05 §6; os pisos do contexto DORA não admitem exceção por conveniência), mas não estabelece **todas as categorias inaceitáveis numa leitura DORA**:

- **Nunca aceitável numa leitura DORA defensável:**
  - Exceções sem aprovação documentada
  - Exceções expiradas sem reavaliação
  - Exceções a obrigações que decorrem diretamente do regulamento (ex: a periodicidade do TLPT, art. 26.º, n.º 1), que uma decisão interna não pode afastar

- **Aceitável com restrições (compatível com DORA):**
  - Exceções com TTL, plano de fix e compensação
  - Exceções aprovadas pela alçada da Política 05 §6 (e, se a entidade o decidir, ratificadas pelo órgão de administração)
  - Exceções com trilho auditado

**Como manifesta:** Organização sem política formal aceita exceção inadmissível; auditoria regulatória identifica achado crítico.

---

#### Como Resolver a Incoerência {#como-resolver-a-incoerência}

**1. Estabelecer Política Formal de Exceções Compatível com DORA**

```
POLÍTICA: Gestão de Exceções e Desvios de Conformidade

Objetivo: Garantir que todas as exceções a requisitos de segurança são aprovadas por autoridade formal, documentadas com trilho auditado, e compatíveis com exigências regulatórias (DORA).

Categorias de exceção:

A. Exceções INACEITÁVEIS (incompatíveis com uma leitura DORA defensável):
   - Exceções sem aprovação documentada
   - Exceções expiradas sem reavaliação
   - Vulnerabilidades fora das alçadas e dos prazos da Política 05 (ex: Critical em L3; Critical em L2 sem CISO, plano e TTL)
   - Exceções a obrigações que decorrem diretamente do regulamento (ex: a periodicidade do TLPT)
   ➜ Ação: REJEITAR; forçar mitigação

B. Exceções ACEITÁVEIS em L3 (alçada da Política 05 §6):
   - Componentes legados sem patch aplicável
   - CVEs com "no fix available" + compensação (ex: isolamento de rede)
   - Arquitetura herdada em transição
   ➜ Ação: APROVAR pela alçada da Política 05 §6 e, se a entidade o exigir, com ratificação do órgão de administração; TTL da Política 05 §7 (L3: 30 dias; High 14 dias; Critical não aceitável); reavaliação obrigatória

C. Exceções ACEITÁVEIS em L2 (alçada da Política 05 §6):
   - Requisitos técnicos com compensação equivalente
   ➜ Ação: APROVAR pela alçada da Política 05 §6 (AppSec Engineer; High com Gestão de Produto; Critical com CISO); TTL da Política 05 §7 (L2: 60 dias; High 30 dias; Critical 7 dias); reavaliação obrigatória

D. Exceções ACEITÁVEIS com aprovação AppSec-level (L1):
   - MVP com funcionalidade reduzida de segurança
   - Prototipagem com dados não-sensíveis
   ➜ Ação: APROVAR pela alçada da Política 05 §6 (Tech Lead ou AppSec Engineer); TTL da Política 05 §7 (L1: 90 dias; Critical 7 dias); reavaliação obrigatória

Rastreamento:
- Ferramenta GRC centralizada (SAP GRC, AuditBoard, ou custom)
- Campos: ID | Aplicação | Nível | Exceção | Justificação | Aprovador | Data | TTL | Status | Observações regulatórias
- Reporte periódico ao CISO e, se a entidade o decidir, ao órgão de administração (periodicidade definida pela entidade)
- Reporte ad-hoc a regulador se incidente relacionado
```

---

**2. O que fica fora do Manual.** As categorias de inadmissibilidade e a elevação ao órgão de administração são decisões da entidade, e o Manual não as prescreve (DORA art. 5.º; fora do âmbito). O reporte ao regulador segue a Política 32 §6; os formulários e os canais são da autoridade.

---

#### Resumo: Por que Ausência de Gestão Formal = Incoerência DORA {#resumo-por-que-ausência-de-gestão-formal--incoerência-dora}

| Aspecto | Sem Gestão Formal | Com Gestão SbD-ToE + DORA Mapping |
|--------|-------------------|----------------------------------|
| **Descoberta regulatória** | Ausência de documentação de exceções ou localização desconhecida ❌ | Processo formal (Política 05) em sistema GRC, com as alçadas definidas ✅ |
| **Trilho auditado** | Exceções em canais informais (Slack/Teams/email) ❌ | Exceções em ferramenta GRC com audit trail completo ✅ |
| **Supervisão do board** | Board desconhece exceções críticas ❌ | O órgão de administração recebe o reporte das exceções L3, pela via e com a periodicidade que a entidade define ✅ |
| **Resposta a incidentes** | Desconhecimento de vulnerabilidade explorada ❌ | Vulnerabilidade registada em exceção aprovada com plano de correção; escalada segundo protocolo ✅ |
| **Achados auditoria** | Achado crítico: falha de governance ❌ | Achado menor: oportunidades de melhoria operacional ✅ |

---

### Conformidade Prática {#conformidade-prática}

**Alinhamento SbD-ToE com DORA:**
1. Aplicar o processo formal de exceções do SbD-ToE (Política 05; [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) addon 09)
2. Manter as alçadas da Política 05 §6 e, onde a entidade o decida, acrescentar a elevação ao órgão de administração para as exceções L3 (decisão da entidade, fora do âmbito do Manual)
3. Definir categorias de inaceitabilidade (política organizacional)
4. Implementar rastreamento centralizado com audit trail (ferramenta GRC)
5. Estabelecer reporte periódico ao órgão de administração (o art. 5.º, n.º 2, al. i), do DORA exige canais de informação; a periodicidade trimestral é opção organizacional)
6. Seguir a Política 32 §6 e §6.1 na notificação de incidentes; os canais e os formulários são da autoridade

---

## CONCLUSÃO DO CROSS-CHECK {#conclusão-do-cross-check}

O SbD-ToE cobre o núcleo técnico do DORA do lado da aplicação. A resposta tem três partes: o que o Manual cobre, com a forma indicada em cada requisito; as lacunas que declara; e o que deixa fora do âmbito, com razão, por ser da entidade como um todo (continuidade do negócio e gestão de crises, segurança física, postos de trabalho, rede corporativa) ou da relação com o supervisor (registo de informações, TLPT regulado, modelos e canais de reporte).

**Requisitos para conformidade plena:**
- Mapeamento de políticas SbD-ToE a aprovações formais de órgão de gestão
- Ligação do conteúdo da Política 32 §6.1 aos canais e formulários da autoridade competente
- Fecho das lacunas declaradas que interessem à entidade (ver [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura))
- Extensão de inventários com dados regulatórios específicos
- Cálculo de métricas DORA de concentração de fornecedores
- Formalização de acordos de partilha de informação sobre ameaças

---

## Referências {#referências}

- SbD-ToE Manual (Capítulos 01–14)
- Regulamento DORA (UE 2022/2554)
- NIST SP 800-53, OWASP SAMM, BSIMM, SSDF
- [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) SbD-ToE: User Stories US-15 a US-20 (fornecedores/contractors)

---

**Versão:** 1.1  
**Data:** Setembro 2026  
**Próxima revisão:** Março 2027
