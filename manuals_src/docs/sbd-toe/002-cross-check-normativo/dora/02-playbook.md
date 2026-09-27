---
id: playbook
title: "SbD-ToE 4 DORA: Playbook de Implementação"
description: Roadmap prático para implementar SbD-ToE conforme requisitos DORA - mapeamento direto de artigos para ações
tags: [playbook, dora, implementacao, roadmap]
sidebar_position: 2
---

# SbD-ToE 4 DORA: Playbook de Implementação

## Visão Geral {#visão-geral}

Este playbook mapeia **requisitos DORA (Regulamento UE 2022/2554) para ações SbD-ToE práticas**.

**Princípio:** Implementar o SbD-ToE cobre grande parte da **base AppSec e operacional** exigida por DORA, mas a conformidade final depende também de **formalização regulatória adicional** e de artefactos institucionais que ficam fora do âmbito do Manual.

O que o Manual cobre, as lacunas que declara e o que fica fora de âmbito, obrigação a obrigação, estão em [Requisitos aplicáveis — O que este Manual cobre e o que fica de fora](./requisitos-aplicaveis#cobertura).

**Estrutura:** Cada secção mostra:
- DORA requisito ou bloco normativo
- SbD-ToE capítulo/addon aplicável
- O que fazer
- Que parte fica dentro do Manual (incluindo os pisos e os requisitos acrescentados pelo contexto DORA, em `_contextos-regulatorios.yaml`) e que parte fica fora do âmbito

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e relatórios de incidentes reutilizáveis para DORA e outros frameworks.

---

## Mapa Rápido: DORA Art. → SbD-ToE {#mapa-rápido-dora-art--sbd-toe}

| DORA Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|----------|-----------|-----------------|----------------|
| **5** | Governação e responsabilidade do órgão de gestão | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Aprovar políticas, supervisionar risco, formalizar cadeia de autoridade |
| **6** | Framework de gestão de risco TIC | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Inventariar, classificar, ligar risco a requisitos, evidência e revisão |
| **8–15** | Proteção, prevenção, deteção, resposta, recuperação, aprendizagem e comunicação | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro) | Implementar controlos técnicos e operacionais com evidência, monitorização e melhoria |
| **17–23** | Gestão, classificação e reporte de incidentes TIC | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Deteção, triagem, escalonamento e parametrização de reporte regulatório |
| **24–27** | Programa de testes de resiliência digital e TLPT | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Testes contínuos, validação pré-deploy e TLPT readiness bounded |
| **28–30** | Gestão de risco de terceiros TIC | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | SBOM, due diligence, cláusulas contratuais, ciclo de vida e saída |

---

## Como Implementar (Ordem Lógica) {#como-implementar-ordem-lógica}

### Fase 1: Governação (M0–M2) {#fase-1-governação-m0m2}
**DORA Art. 5** - Estabelecer supervisão do órgão de gestão

1. **Criar fórum formal de governação de segurança digital**
   - Membros: board sponsor, CISO, CTO, GRC, legal/procurement
   - Frequência: regular e com registo formal
   - **Evidência:** atas, decisões, owners, follow-up

2. **Aprovar política e cadeia de autoridade**
   - Referência: [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
   - **Aprovação:** nível de gestão adequado ao contexto regulatório
   - **Conteúdo:** responsabilidades, escalonamento, exceções, reporting

3. **Definir RACI e critérios de escalada**
   - Quem aprova o quê
   - Quando escalar
   - Como preservar trilho documental
   - 📄 **Template:** [RACI e Governance](../exemplo-playbook/exemplo-raci-governance)

---

### Fase 2: Framework de risco TIC (M2–M4) {#fase-2-framework-de-risco-tic-m2m4}
**DORA Art. 6** - Estruturar a gestão de risco TIC

1. **Inventariar aplicações e serviços**
   - Nome, owner, função suportada, dados, dependências
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar por risco**
   - Nível L1–L3 por aplicação, segundo os eixos de exposição, sensibilidade dos dados e impacto (CLA-001)
   - Marcar, por aplicação, se suporta uma função crítica ou importante (grau FCI do contexto DORA, com remissão para o inventário de funções da entidade): é um eixo separado do nível e acrescenta pisos próprios; L3 não equivale a função crítica ou importante
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

3. **Definir requisitos mínimos por nível**
   - L1: básicos
   - L2: essenciais com validação formal
   - L3: rigor reforçado com maior evidência
   - Referência: [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

4. **Formalizar evidência, revisão e owners**
   - Registar decisões, exceções, owners e ciclos de revisão
   - Garantir reporting periódico a gestão e GRC
   - Referência: [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Fase 3: Proteção, prevenção, deteção e recuperação (M4–M12) {#fase-3-proteção-prevenção-deteção-e-recuperação-m4m12}
**DORA Art. 8–15** - Implementar controlos técnicos e operacionais

#### 3.1 Threat modeling, requisitos e arquitetura {#31-threat-modeling-requisitos-e-arquitetura}
- **O que:** ligar risco, ameaças, requisitos e decisões arquiteturais
- **Como:** threat modeling proporcional; requisitos versionados; arquitetura segura
- **Trilho:** risco → ameaça → requisito → controlo → evidência
- **Referências:** [Cap. 02 - Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.2 Desenvolvimento, CI/CD, IaC e supply chain {#32-desenvolvimento-cicd-iac-e-supply-chain}
- **O que:** endurecer a cadeia de entrega e a composição do software
- **Como:** SAST/SCA; bloqueio de segredos; proveniência; validação pré-deploy; SBOM; scanning de IaC
- **Trilho:** logs auditados, SBOM atualizado, findings, gates e exceções formais
- **Referências:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 08 - IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- 📄 **Template:** [Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)

#### 3.3 Monitorização, resposta, recuperação e aprendizagem {#33-monitorização-resposta-recuperação-e-aprendizagem}
- **O que:** monitorizar, reagir, conter, recuperar e aprender com eventos e desvios
- **Como:** logging estruturado; alertas com SLAs; rollback; runbooks; métricas; formação contínua
- **Trilho:** evidência operacional, post-incident reviews, KPIs e reporting
- **Recuperação:** cópias de segurança com restauro testado (OPS-016) e objetivos e procedimento de recuperação da aplicação (OPS-017); as capacidades redundantes e os testes de comutação são requisito acrescentado pelo contexto DORA (CTX-DORA-R01). Os planos de continuidade da entidade (art. 11.º) ficam fora do Manual.
- **Pisos do contexto DORA:** IRP em qualquer nível (Política 32 §2; CTX-DORA-P01); testes dinâmicos (TST-005; P03); revisão anual dos acessos e semestral nas funções críticas ou importantes (ACC-010; P05, P06); autenticação forte (AUT-001; P07); análise semanal de vulnerabilidades dos ativos que apoiam funções críticas ou importantes (Política 10 §9; P08); divulgação responsável (GOV-015; P10); contas privilegiadas e ciclo de vida das identidades (GOV-016, GOV-017; P13, P14); ciclo de vida das chaves e registo de certificados (ENC-007; P15, P16); agilidade criptográfica (ENC-003; P17); revisão semestral das regras de filtragem de rede (ARC-006; P18). Ver [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura).
- **Referências:** [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro), [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Fase 4: Incidentes e reporte regulatório (M8–M12) {#fase-4-incidentes-e-reporte-regulatório-m8m12}
**DORA Art. 17–23** - Gerir, classificar e reportar incidentes TIC

#### 4.1 Monitorização centralizada {#41-monitorização-centralizada}
- **O que:** logs centralizados de aplicações, infraestrutura e acessos
- **Retenção:** conforme política interna e enquadramento regulatório aplicável
- **Proteção:** imutabilidade, integridade e rastreabilidade
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 4.2 Deteção, triagem e resposta {#42-deteção-triagem-e-resposta}
- **O que:** identificar eventos, classificar por impacto e responder
- **Escalação:** conforme criticidade e modelo de governação
- **Documentação:** o quê, quando, ações, aprendizagem
- **Referências:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
- 📄 **Template:** [Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)

#### 4.3 Parametrização de reporte externo {#43-parametrização-de-reporte-externo}
- **O que:** traduzir o processo interno em `initial`, `intermediate` e `final report`, nos prazos fixados pelas RTS (Reg. Delegado (UE) 2025/301, art. 5.º: notificação inicial ≤ 4 h após a classificação como severo e ≤ 24 h após o conhecimento; relatório intercalar ≤ 72 h após a notificação inicial; relatório final ≤ 1 mês após o último relatório intercalar) e informar os clientes afetados sem demora indevida (art. 19.º, n.º 3)
- **Como:** partir dos dados de impacto (Política 32 §4.3), classificar com os critérios do art. 18.º e os limiares do Reg. Delegado (UE) 2024/1772, com avaliação mensal dos recorrentes (CTX-DORA-R02), e usar o conteúdo da Política 32 §6.1 (modelos do Reg. de Execução (UE) 2025/302)
- **Boundary:** a submissão, os canais e a relação com a autoridade competente ficam fora do âmbito do Manual
- **Referências:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Fase 5: Testes de resiliência (M12–M18) {#fase-5-testes-de-resiliência-m12m18}
**DORA Art. 24–27** - Validar postura defensiva e preparar TLPT

#### 5.1 Testes contínuos {#51-testes-contínuos}
- **SAST:** análise estática integrada
- **DAST:** análise dinâmica em staging, obrigatória em qualquer nível no contexto DORA, com testes aos sistemas e aplicações expostos à Internet (TST-005; CTX-DORA-P03)
- **PenTesting:** testes manuais guiados por threat model
- **Referência:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 5.2 Validação pré-deploy {#52-validação-pré-deploy}
- **O que:** checklist de segurança antes de produção
- **Confirmação:** requisitos e evidência coerentes com o nível de risco
- **Aprovação:** formal quando aplicável
- **Referência:** [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)

#### 5.3 TLPT readiness e boundary regulatório {#53-tlpt-readiness-e-boundary-regulatório}
- **O que:** preparar a base técnica para exercícios TLPT em entidades elegíveis
- **Base:** cenários de threat model, escopo, remediação e evidência
- **Boundary:** elegibilidade, qualificação formal de testers e attestation pertencem à camada regulatória/compliance
- **Referências:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)

---

### Fase 6: Terceiros TIC e fornecedores críticos (M12–M18) {#fase-6-terceiros-tic-e-fornecedores-críticos-m12m18}
**DORA Art. 28–30** - Gerir risco de terceiros TIC

#### 6.1 Fornecedores de componentes e supply chain de software {#61-fornecedores-de-componentes-e-supply-chain-de-software}
- **O que:** SBOM + SCA
- **Como:** gerar SBOM; scan contínuo; atualizar dependências
- **Trilho:** inventário, findings, correções e exceções
- **Referência:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

#### 6.2 Fornecedores contratuais {#62-fornecedores-contratuais}
- **O que:** contractors, outsourcing e parceiros com acesso ou responsabilidade técnica
- **Ciclo de Vida:**
  - **Onboarding:** validação, formação SbD, sandbox
  - **Operação:** acesso controlado, revisão periódica
  - **Offboarding:** revogação de acessos, auditoria de fecho
- **Referência:** [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 6.3 Concentração e saída {#63-concentração-e-saída}
- **O que:** avaliar concentração, dependências críticas e estratégia de saída
- **Como:** inventário, revalidação periódica, cláusulas contratuais e planos de transição
- **Boundary:** o registo de informações (Reg. de Execução (UE) 2024/2956), a análise de concentração e as estratégias de saída da entidade ficam fora do âmbito do Manual (relação com o supervisor e continuidade do negócio); os planos de transição e de migração integral dos dados são lacuna declarada.
- **Referências:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

## Checklist de Leitura DORA {#checklist-de-leitura-dora}

A lista abaixo permite validar a maturidade da **base AppSec e operacional** para uma leitura DORA defensável. A conformidade final continua a depender de parametrização regulatória e evidência institucional adicional:

- [ ] **Governação:** Política aprovada; cadeia de autoridade clara; reporting periódico
- [ ] **Framework de risco:** Todas as apps classificadas e ligadas a requisitos por nível
- [ ] **Requisitos:** Catálogo versionado e rastreável
- [ ] **Supply chain técnica:** SBOM gerado e SCA contínuo
- [ ] **Pipeline:** Gates de segurança operacionais
- [ ] **Monitorização:** Logs centralizados, proteção e retenção adequadas
- [ ] **Incidentes:** IRP em qualquer nível (CTX-DORA-P01); classificação DORA (CTX-DORA-R02) e conteúdo da Política 32 §6.1
- [ ] **Fornecedores:** Inventário, due diligence e ciclo de vida operacional
- [ ] **Testes:** SAST/DAST integrados; readiness para TLPT onde aplicável
- [ ] **Evidência:** Data room com políticas, testes, logs, contratos e reporting

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida) {#o-que-cada-capítulo-sbd-toe-cobre-referência-rápida}

| Capítulo | DORA Artigos | O Que Faz |
|----------|-------------|----------|
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 5, 6 | Classificação de apps por risco e proporcionalidade |
| **[Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)** | Art. 6, 8–15 | Requisitos mínimos, rastreabilidade e validação |
| **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro)** | Art. 8–15, 24–27 | Threat modeling para cenários realistas |
| **[Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)** | Art. 8–15, 28–30 | SBOM, SCA, supply chain de software |
| **[Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)** | Art. 8–15 | CI/CD seguro, gates, trilho auditado |
| **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Art. 24–27 | Testes contínuos, readiness e evidência |
| **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 8–15, 24–27 | Validação pré-deploy, rollback e contenção |
| **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)** | Art. 8–15, 17–23 | Monitorização, incidentes, resposta e reporting interno |
| **[Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 8–15 | Formação e capacitação contínua |
| **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Art. 5, 6, 17–23, 28–30 | Governança, RACI, reporte e ciclo de vida fornecedores |

A coluna indica onde cada capítulo contribui, não que o artigo fique coberto. Nos arts. 28.º–30.º, o Manual cobre partes da devida diligência e das cláusulas e dá apoio à evidência; o registo de informações e a análise de concentração ficam fora do âmbito. No art. 19.º, a Política 32 §6 dá apoio à evidência, e a relação com a autoridade fica fora do âmbito. O detalhe está em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura).

---

## Métrica Simples: Estou Bem Preparado? {#métrica-simples-estou-bem-preparado}

Cada resposta afirmativa conta um ponto e indica a maturidade da base AppSec para uma implementação DORA defensável:

1. **Governance:** Tenho política aprovada e cadeia de autoridade clara?
2. **Risk Management:** Todas as apps estão classificadas e ligadas a requisitos?
3. **Security by Design:** Meus requisitos e controlos são rastreáveis?
4. **Software Supply:** Tenho SBOM e SCA ativos?
5. **Operations:** Tenho monitorização centralizada com retenção e proteção adequadas?
6. **Incident Response:** Consigo detetar, classificar e parametrizar reporte de incidentes?
7. **Vendor Management:** Tenho ciclo de vida formal de contractors e terceiros críticos?
8. **Testing:** Faço SAST/DAST e tenho readiness para TLPT quando aplicável?
9. **Evidence:** Consigo demonstrar tudo isto em auditoria e reporte regulatório?

**Leitura prática:** quanto mais respostas positivas, mais madura está a base AppSec. A passagem para a conformidade DORA plena continua a exigir o que o Manual deixa fora do âmbito, com razão (continuidade do negócio e gestão de crises, segurança física e dos postos de trabalho, registo de informações, TLPT regulado, canais de reporte), a formalização pelo órgão de administração e o fecho das lacunas declaradas em [Requisitos aplicáveis](./requisitos-aplicaveis#cobertura).

---

## Nota Crítica: Gestão de Exceções em DORA {#nota-crítica-gestão-de-exceções-em-dora}

O quadro DORA exige que as exceções à aplicação das políticas de segurança das TIC sejam registadas e que a resiliência seja assegurada nesses casos (Reg. Delegado (UE) 2024/1774, art. 2.º, n.º 2, al. c)); a aceitação de riscos residuais acima da tolerância exige funções atribuídas, inventário justificado e revisão anual (art. 3.º, al. d)). O nível de aprovação concreto é definido pela entidade.

O que caracteriza uma exceção em SbD-ToE/DORA:
- desvio formal de um requisito;
- justificação técnica e de negócio;
- prazo de validade (`TTL`);
- plano de remediação e owner;
- trilho documental passível de auditoria.

Quem aprova depende da criticidade, do modelo de governação e do enquadramento regulatório aplicável. No Manual, a alçada das exceções sobe, no máximo, ao CISO (Política 05 §6), e o Critical não é aceitável como exceção em L3. Em contextos críticos, a leitura DORA tende a exigir a elevação da decisão ao órgão de administração: é decisão da entidade, fora do âmbito do Manual.

Leitura prática:
- exceções sem aprovação formal comprometem a supervisão;
- algumas exceções podem ser inaceitáveis em leitura regulatória defensável;
- o manual cobre bem o processo, mas a admissibilidade final continua a depender do contexto regulatório.

**Referências:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) e [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

## Recursos Práticos de Implementação {#recursos-práticos-de-implementação}

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Comparação de ferramentas (IaC, logs, SCA, SAST, CI/CD) com exemplos de configuração
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de segurança por perfil organizacional
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Matrizes de responsabilidades e aprovações DORA-compatíveis
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Templates de reporte formal com campos DORA

Estes recursos são reutilizáveis para múltiplos frameworks e mostram como operacionalizar, fora do manual base, os detalhes que dependem de contexto regulatório, supervisor e tooling.

---

## Próximos Passos {#próximos-passos}

1. Fazer um audit de conformidade atual contra a matriz acima
2. Sequenciar o roadmap por criticidade, gap e dependência
3. Implementar por fases, com evidência versionada
4. Ligar o conteúdo da Política 32 §6.1 aos canais da autoridade e assegurar o que fica fora do âmbito (registo de informações, concentração, continuidade)
5. Validar periodicamente a prontidão documental e operacional

Documentação completa: ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências {#referências}

- **SbD-ToE Manual:** Capítulos 01–14
- **Cross-Check DORA:** [Análise normativa completa](/sbd-toe/cross-check-normativo/dora/intro)
- **Regulamento DORA:** UE 2022/2554

---

**Versão:** 1.3 (alinhado com a matriz de cobertura e o contexto DORA)  
**Data:** Setembro 2026  
**Nota:** Este playbook complementa a [análise normativa DORA](intro) com implementação prática bounded e orientada a evidência.
