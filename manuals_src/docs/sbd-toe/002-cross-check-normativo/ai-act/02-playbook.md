---
id: playbook
title: "SbD-ToE 4 AI Act: Playbook de Implementação"
description: Roadmap prático para implementar o SbD-ToE conforme os requisitos do Regulamento (UE) 2024/1689 (AI Act) - mapeamento de artigos para ações, por papel e categoria de risco
tags: [playbook, ai-act, regulamento-ia, implementacao, roadmap, gpai]
sidebar_position: 2
---

# SbD-ToE 4 AI Act: Playbook de Implementação

## Visão Geral

Este playbook mapeia **requisitos do AI Act (Regulamento UE 2024/1689) para ações SbD-ToE práticas**, focando-se nas obrigações técnicas dos sistemas de IA de **alto risco** e dos modelos de **finalidade geral (GPAI)**.

**Princípio:** O SbD-ToE cobre o **núcleo técnico** do AI Act - exatidão, robustez, cibersegurança (Art. 15), logging (Art. 12), gestão de risco (Art. 9), QMS (Art. 17), monitorização pós-mercado (Art. 72) e incidentes (Art. 73). As dimensões de **domínio de IA** (dados/enviesamento, supervisão humana, transparência) e **jurídicas** (classificação de risco, FRIA, avaliação de conformidade, marcação CE) exigem articulação com equipas de ciência de dados, produto, jurídico e compliance.

**Estrutura:** Cada secção mostra:
- AI Act requisito (artigo)
- SbD-ToE capítulo/addon aplicável
- O que fazer (ação concreta)
- Evidência regulatória

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e relatórios de incidentes reutilizáveis para AI Act e outros frameworks.

---

## Passo 0: Determinar papel e categoria de risco (pré-requisito)

Antes de qualquer ação técnica, é necessário estabelecer o enquadramento jurídico - **trabalho de compliance/jurídico, não de AppSec**, mas que condiciona todo o playbook:

1. **Qual é o papel?** Fornecedor (*provider*), utilizador implementador (*deployer*), importador ou distribuidor. O grosso das obrigações técnicas recai sobre o **fornecedor de alto risco**.
2. **Qual a categoria de risco?**
   - **Inaceitável** (Art. 5) → proibido; não há playbook técnico que o legitime.
   - **Alto risco** (Art. 6, Anexos I/III) → aplica-se a generalidade deste playbook.
   - **Risco limitado** (Art. 50) → apenas deveres de transparência.
   - **Risco mínimo** → sem obrigações específicas.
3. **É um modelo GPAI?** Se sim, aplicam-se Art. 53 (todos) e Art. 55 (risco sistémico) - ver Fase 7.

> ⚠️ **Saída do âmbito SbD-ToE:** a classificação de risco e a qualificação de papéis são determinações jurídicas. O SbD-ToE assume o resultado desta análise como input.

---

## Mapa Rápido: AI Act Art. → SbD-ToE

| AI Act Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|---|---|---|---|
| **9** | Gestão de risco | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro) | Classificar; threat model estendido a ATLAS |
| **10** | Dados e governação | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Proveniência de datasets (AI-BOM); *data governance* (IA) |
| **11 / Anexo IV** | Documentação técnica | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | Índice Anexo IV + model card |
| **12 / 19** | Logging e retenção | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Logs de inferência; retenção e imutabilidade |
| **15** | Robustez e cibersegurança | [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | Testes adversariais; AI red teaming; hardening |
| **17** | QMS | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Mapear gates → elementos do QMS |
| **72** | Monitorização pós-mercado | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Plano + dashboards de desempenho/drift |
| **73** | Incidentes graves | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Runbook + esquema c/ prazos do Art. 73 |
| **53 / 55** | GPAI | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) | Proteção de pesos; AI red teaming contínuo |

---

## Como Implementar (Ordem Lógica)

### Fase 1: Governação e QMS (M0–M3)
**AI Act Art. 17** - Estabelecer sistema de gestão da qualidade

1. **Definir governação de IA**
   - Membros: CISO, responsável de IA/ML, GRC, jurídico, produto
   - **Evidência:** Atas, política de IA aprovada
   - Referência: [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

2. **Mapear gates SbD-ToE para os elementos do QMS (Art. 17)**
   - Procedimentos de desenvolvimento → [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)
   - Controlo de qualidade e validação → [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)
   - Reaproveitar **ISO/IEC 42001** se já existir
   - 📄 **Template:** [RACI e Governance](../exemplo-playbook/exemplo-raci-governance)

3. **Definir RACI de IA**
   - Quem aprova release de modelo, quem assina exceções, quem comunica incidentes (Art. 73)

---

### Fase 2: Classificação e gestão de risco (M2–M5)
**AI Act Art. 9** - Sistema de gestão de risco contínuo

1. **Inventariar sistemas de IA**
   - Finalidade, dados processados, modelo(s), serviço de inferência, dependências
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar criticidade (L1–L3) e alinhar com categoria AI Act**
   - Sistema de alto risco (Anexo III) → tipicamente L3
   - Documentar que a proporcionalidade segue a categoria AI Act

3. **Threat model estendido ao vetor adversarial**
   - Base: STRIDE / MITRE ATT&CK ([Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro))
   - Extensão: **MITRE ATLAS** e **OWASP ML/LLM Top 10**
   - Cobrir (Art. 15.º, n.º 5): *data poisoning*, *model poisoning*, *adversarial examples* / *model evasion*, ataques à confidencialidade, *model flaws*
   - **Evidência:** Threat model documentado, risco residual e medidas (Art. 9)

---

### Fase 3: Dados e documentação (M3–M6)
**AI Act Art. 10, 11, Anexo IV**

1. **Proveniência e integridade de dados e modelos (AI-BOM)**
   - Estender o inventário do [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) a *datasets*, *checkpoints* e modelos
   - Verificação de integridade (mitiga *poisoning* e modelos comprometidos de repositórios públicos)

2. **Data governance de IA (delegado à equipa de dados)**
   - Representatividade, deteção de enviesamento, qualidade estatística (Art. 10)
   - *Datasheets for datasets* / *data cards*
   - **Fora do âmbito AppSec** - SbD-ToE garante integridade/proveniência, não fairness

3. **Documentação técnica (Anexo IV)**
   - Construir "índice Anexo IV" apontando para artefactos SbD-ToE (arquitetura, requisitos, threat model, evidência de pipeline/testes) + **model card**
   - Referência: [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)

---

### Fase 4: Segurança técnica e robustez (M5–M10) — NÚCLEO
**AI Act Art. 15** - Exatidão, robustez e cibersegurança

#### 4.1 Arquitetura defensiva
- **O que:** Fronteiras de confiança, validação de input, isolamento do serviço de inferência, redução de superfície
- **Referência:** [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 09 - Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro)

#### 4.2 Testes de robustez adversarial + AI red teaming (CRÍTICO PARA Art. 15)
- **O que:** Estender o catálogo de testes com robustez adversarial, *fuzzing* de input e *red teaming* de modelo
- **Como:** Cenários do threat model (ATLAS); avaliar *evasion*, *poisoning*, *model inversion*, *membership inference*; para LLM, *prompt injection* e *jailbreak*
- **Referência:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)
- 📄 **Template:** [Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)

#### 4.3 Pipeline seguro de ML
- **O que:** Gates de segurança no pipeline de treino e de release (SAST/SCA, secrets, integridade de artefactos)
- **Referência:** [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 08 - IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro)

#### 4.4 Exatidão (delegado à equipa de IA)
- Declarar métricas de exatidão e limiares aceitáveis - **conteúdo de domínio de IA**, suportado pela evidência de testes

---

### Fase 5: Logging e monitorização pós-mercado (M8–M12)
**AI Act Art. 12, 19, 72**

#### 5.1 Logging de inferência
- **O que:** Estender o esquema de logs com metadados de inferência (id/versão do modelo, *features* relevantes, decisão e confiança, *correlation id*)
- **Retenção:** Alinhada com a vida útil do sistema e com o RGPD; imutabilidade
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 5.2 Plano de monitorização pós-mercado (Art. 72)
- **O que:** Formalizar plano + *dashboards* de desempenho, *model drift* e estado de vulnerabilidades
- **Gatilhos:** Degradação ou *drift* alimentam a reavaliação do Art. 9
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Fase 6: Incidentes graves (M10–M12)
**AI Act Art. 73**

- **O que:** Parametrizar o runbook e o esquema de incidente com a tipologia e prazos do Art. 73 (≤15 dias em regra; ≤10 dias em caso de morte; ≤2 dias em caso de infração generalizada ou perturbação grave e irreversível de infraestrutura crítica)
- **Como:** Exportadores SIEM/ITSM → notificação pronta para a autoridade de fiscalização do mercado
- **Referência:** [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)
- 📄 **Template:** [Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)

---

### Fase 7: GPAI (quando aplicável)
**AI Act Art. 53, 55**

#### 7.1 Proteção do modelo (Art. 55 - cibersegurança)
- **O que:** Tratar pesos, *checkpoints* e *datasets* como ativos críticos: proveniência, integridade, controlo de acesso
- **Referência:** [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 7.2 AI red teaming contínuo (Art. 55)
- **O que:** Programa contínuo de avaliação adversarial alinhado com MITRE ATLAS
- **Referência:** [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 7.3 Hardening de infraestrutura física e lógica (Art. 55)
- **Referência:** [Cap. 08 - IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 09 - Containers/Runtime](/sbd-toe/sbd-manual/containers-imagens/intro)

#### 7.4 Documentação GPAI, copyright e resumo de dados (delegado)
- **Fora do âmbito AppSec** - obrigações de domínio e jurídicas (Art. 53)

---

## Checklist de Conformidade

A lista abaixo permite validar o alinhamento do programa SbD-ToE com os requisitos técnicos do AI Act. Recomenda-se revisão periódica:

- [ ] **Enquadramento:** Papel e categoria de risco determinados (jurídico)
- [ ] **Governação/QMS:** Política de IA aprovada; gates mapeados para Art. 17
- [ ] **Classificação:** Sistemas de IA inventariados e classificados (L1–L3)
- [ ] **Gestão de risco:** Threat model estendido a MITRE ATLAS / OWASP ML/LLM
- [ ] **Dados:** Proveniência de datasets/modelos (AI-BOM); *data governance* de IA em curso
- [ ] **Documentação:** Índice Anexo IV + model card
- [ ] **Robustez (Art. 15):** Testes adversariais e AI red teaming executados
- [ ] **Logging:** Logs de inferência com retenção e imutabilidade
- [ ] **Monitorização:** Plano pós-mercado + dashboards de drift
- [ ] **Incidentes:** Runbook parametrizado com prazos do Art. 73
- [ ] **GPAI (se aplicável):** Proteção de pesos + red teaming contínuo + hardening
- [ ] **Evidência:** Data room com documentação técnica, testes e logs

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida)

| Capítulo | AI Act Artigos | O Que Faz |
|---|---|---|
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 9 | Classificação de criticidade (L1–L3) |
| **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro)** | Art. 9, 15 | Threat modeling (extensível a MITRE ATLAS) |
| **[Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro)** | Art. 14, 15 | Arquitetura defensiva, fronteiras, *stop* técnico |
| **[Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)** | Art. 10, 15, 55 | Proveniência de dados/modelos (AI-BOM), integridade |
| **[Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)** | Art. 15, 17 | Pipeline seguro, gates de qualidade |
| **[Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro)** | Art. 15, 55 | Hardening de runtime/inferência |
| **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Art. 15, 55 | Testes de robustez adversarial, AI red teaming |
| **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 17 | Gate de release, validação pré-produção |
| **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)** | Art. 12, 19, 72, 73 | Logging, monitorização pós-mercado, incidentes |
| **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Art. 17, 73 | Governança, RACI, exceções, escalonamento |

---

## Métrica Simples: Estou Alinhado?

Se consegues responder SIM a isto, estás alinhado com o núcleo técnico do AI Act:

1. **Enquadramento:** Conheço o meu papel e a categoria de risco? ✓
2. **Risk Management:** Tenho threat model que cobre o vetor adversarial (ATLAS)? ✓
3. **Robustez (Art. 15):** Faço testes adversariais / AI red teaming? ✓
4. **Cadeia:** Tenho proveniência e integridade de datasets e modelos? ✓
5. **Logging:** Registo eventos de inferência com retenção adequada? ✓
6. **Monitorização:** Tenho plano pós-mercado com deteção de drift? ✓
7. **Incidentes:** Conseguo comunicar um incidente grave nos prazos do Art. 73? ✓
8. **QMS:** Os meus gates mapeiam para os elementos do Art. 17? ✓
9. **Documentação:** Tenho índice Anexo IV + model card? ✓
10. **Evidência:** Consigo demonstrar tudo isto numa auditoria? ✓

≥8/10 → Boa maturidade técnica face ao AI Act. `<`6 → Priorizar Art. 15 (robustez), logging (Art. 12) e gestão de risco (Art. 9).

> ⚠️ **Nota:** esta métrica cobre o **núcleo técnico**. A conformidade plena exige ainda governação de dados (Art. 10), supervisão humana (Art. 14), transparência (Art. 13/50) e avaliação de conformidade / marcação CE (Art. 43, 47–49) - dimensões fora do âmbito SbD-ToE.

---

## Nota Crítica: Gestão de Exceções no AI Act

O AI Act exige conformidade com os requisitos de alto risco. Exceções (desvios) devem ser formais e auditadas, com trilho documental e aprovação adequada.

O que caracteriza uma exceção em SbD-ToE/AI Act:
- Desvio formal de um requisito (ex.: vetor adversarial mitigado por compensação enquanto se prepara *retraining*)
- Aprovação formal, justificação, TTL (Time-To-Live), plano de remediação

Quem aprova (por nível de criticidade):
- L1 (baixo risco): Tech lead / AppSec Engineer
- L2 (médio risco): CISO / responsável de IA
- L3 (alto risco AI Act): Governação de IA + gestão (accountable)

Implicação regulatória:
- Exceções sem aprovação formal comprometem a evidência de gestão de risco (Art. 9) e do QMS (Art. 17)
- **Algumas situações nunca são exceptuáveis** - desde logo, qualquer uso que recaia nas práticas proibidas do Art. 5
- Trilho auditado é obrigatório para demonstrar controlo à autoridade

**Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (addon de exceções) e [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro) (exceções formalizadas).

---

## Próximos Passos

1. **Enquadramento jurídico:** Determinar papel e categoria de risco (jurídico/compliance)
2. **Audit de conformidade atual:** Verificar [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) contra os requisitos técnicos do AI Act
3. **Definir roadmap:** Sequenciar fases conforme contexto e categoria de risco
4. **Articular com domínio:** Coordenar com ciência de dados, produto e jurídico as dimensões fora do âmbito AppSec
5. **Implementar e validar:** Iterar e demonstrar conformidade em auditoria

Documentação completa: ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências

- **SbD-ToE Manual:** Capítulos 01–14 (detalhe técnico por domínio)
- **Cross-Check AI Act:** [Análise normativa completa](/sbd-toe/cross-check-normativo/ai-act/intro)
- **AI Act:** Regulamento (UE) 2024/1689
- **Frameworks de Referência:** ISO/IEC 42001, ISO/IEC 23894, NIST AI RMF 1.0, MITRE ATLAS, OWASP ML Security Top 10, OWASP Top 10 for LLM Applications

---

**Versão:** 1.0
**Data:** Maio 2026
**Nota:** Este playbook complementa a [análise normativa AI Act](intro) com implementação prática.
