---
id: playbook
title: "SbD-ToE 4 DORA: Playbook de Implementação"
description: Roadmap prático para implementar SbD-ToE conforme requisitos DORA - mapeamento direto de artigos para ações
tags: [playbook, dora, implementacao, roadmap]
sidebar_position: 2
---

# SbD-ToE 4 DORA: Playbook de Implementação

## Visão Geral

Este playbook mapeia **requisitos DORA (Regulamento UE 2022/2554) para ações SbD-ToE práticas**.

**Princípio:** Implementar o SbD-ToE cobre grande parte da **base AppSec e operacional** exigida por DORA, mas a conformidade final depende também de **formalização regulatória adicional**, artefactos institucionais e parametrização de reporte que ficam fora do manual base.

**Estrutura:** Cada secção mostra:
- DORA requisito ou bloco normativo
- SbD-ToE capítulo/addon aplicável
- O que fazer
- Que parte fica dentro do manual e que parte continua em `overlay/compliance`

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/exemplo-toolchain-options) com toolchains, KPIs, RACI e relatórios de incidentes reutilizáveis para DORA e outros frameworks.

---

## Mapa Rápido: DORA Art. → SbD-ToE

| DORA Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|----------|-----------|-----------------|----------------|
| **5** | Governação e responsabilidade do órgão de gestão | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Aprovar políticas, supervisionar risco, formalizar cadeia de autoridade |
| **6** | Framework de gestão de risco TIC | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Inventariar, classificar, ligar risco a requisitos, evidência e revisão |
| **8–15** | Proteção, prevenção, deteção, resposta, recuperação, aprendizagem e comunicação | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro) | Implementar controlos técnicos e operacionais com evidência, monitorização e melhoria |
| **17–23** | Gestão, classificação e reporte de incidentes TIC | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Deteção, triagem, escalonamento e parametrização de reporte regulatório |
| **24–27** | Programa de testes de resiliência digital e TLPT | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Testes contínuos, validação pré-deploy e TLPT readiness bounded |
| **28–30** | Gestão de risco de terceiros TIC | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | SBOM, due diligence, cláusulas contratuais, ciclo de vida e saída |

---

## Como Implementar (Ordem Lógica)

### Fase 1: Governação (M0–M2)
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

### Fase 2: Framework de risco TIC (M2–M4)
**DORA Art. 6** - Estruturar a gestão de risco TIC

1. **Inventariar aplicações e serviços**
   - Nome, owner, função suportada, dados, dependências
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar por risco**
   - L3: impacto direto em funções críticas
   - L2: suporta processos importantes
   - L1: ferramentas de suporte
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

### Fase 3: Proteção, prevenção, deteção e recuperação (M4–M12)
**DORA Art. 8–15** - Implementar controlos técnicos e operacionais

#### 3.1 Threat modeling, requisitos e arquitetura
- **O que:** ligar risco, ameaças, requisitos e decisões arquiteturais
- **Como:** threat modeling proporcional; requisitos versionados; arquitetura segura
- **Trilho:** risco → ameaça → requisito → controlo → evidência
- **Referências:** [Cap. 02 - Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.2 Desenvolvimento, CI/CD, IaC e supply chain
- **O que:** endurecer a cadeia de entrega e a composição do software
- **Como:** SAST/SCA; bloqueio de segredos; proveniência; validação pré-deploy; SBOM; scanning de IaC
- **Trilho:** logs auditados, SBOM atualizado, findings, gates e exceções formais
- **Referências:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 08 - IaC](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- 📄 **Template:** [Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)

#### 3.3 Monitorização, resposta, recuperação e aprendizagem
- **O que:** monitorizar, reagir, conter, recuperar e aprender com eventos e desvios
- **Como:** logging estruturado; alertas com SLAs; rollback; runbooks; métricas; formação contínua
- **Trilho:** evidência operacional, post-incident reviews, KPIs e reporting
- **Referências:** [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro), [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Fase 4: Incidentes e reporte regulatório (M8–M12)
**DORA Art. 17–23** - Gerir, classificar e reportar incidentes TIC

#### 4.1 Monitorização centralizada
- **O que:** logs centralizados de aplicações, infraestrutura e acessos
- **Retenção:** conforme política interna e enquadramento regulatório aplicável
- **Proteção:** imutabilidade, integridade e rastreabilidade
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 4.2 Deteção, triagem e resposta
- **O que:** identificar eventos, classificar por impacto e responder
- **Escalação:** conforme criticidade e modelo de governação
- **Documentação:** o quê, quando, ações, aprendizagem
- **Referências:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
- 📄 **Template:** [Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)

#### 4.3 Parametrização de reporte externo
- **O que:** traduzir o processo interno em `initial`, `intermediate` e `final report`
- **Como:** parametrizar campos, templates e exportadores conforme RTS/ITS e autoridade competente
- **Boundary:** esta parte já não fica toda no manual base; exige material regulatório complementar
- **Referências:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Fase 5: Testes de resiliência (M12–M18)
**DORA Art. 24–27** - Validar postura defensiva e preparar TLPT

#### 5.1 Testes contínuos
- **SAST:** análise estática integrada
- **DAST:** análise dinâmica em staging
- **PenTesting:** testes manuais guiados por threat model
- **Referência:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 5.2 Validação pré-deploy
- **O que:** checklist de segurança antes de produção
- **Confirmação:** requisitos e evidência coerentes com o nível de risco
- **Aprovação:** formal quando aplicável
- **Referência:** [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)

#### 5.3 TLPT readiness e boundary regulatório
- **O que:** preparar a base técnica para exercícios TLPT em entidades elegíveis
- **Base:** cenários de threat model, escopo, remediação e evidência
- **Boundary:** elegibilidade, qualificação formal de testers e attestation pertencem à camada regulatória/compliance
- **Referências:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)

---

### Fase 6: Terceiros TIC e fornecedores críticos (M12–M18)
**DORA Art. 28–30** - Gerir risco de terceiros TIC

#### 6.1 Fornecedores de componentes e supply chain de software
- **O que:** SBOM + SCA
- **Como:** gerar SBOM; scan contínuo; atualizar dependências
- **Trilho:** inventário, findings, correções e exceções
- **Referência:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

#### 6.2 Fornecedores contratuais
- **O que:** contractors, outsourcing e parceiros com acesso ou responsabilidade técnica
- **Ciclo de Vida:**
  - **Onboarding:** validação, formação SbD, sandbox
  - **Operação:** acesso controlado, revisão periódica
  - **Offboarding:** revogação de acessos, auditoria de fecho
- **Referência:** [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 6.3 Concentração e saída
- **O que:** avaliar concentração, dependências críticas e estratégia de saída
- **Como:** inventário, revalidação periódica, cláusulas contratuais e planos de transição
- **Boundary:** parte desta leitura é regulatória e portfolio-wide, não apenas AppSec
- **Referências:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

## Checklist de Leitura DORA

A lista abaixo permite validar a maturidade da **base AppSec e operacional** para uma leitura DORA defensável. A conformidade final continua a depender de parametrização regulatória e evidência institucional adicional:

- [ ] **Governação:** Política aprovada; cadeia de autoridade clara; reporting periódico
- [ ] **Framework de risco:** Todas as apps classificadas e ligadas a requisitos por nível
- [ ] **Requisitos:** Catálogo versionado e rastreável
- [ ] **Supply chain técnica:** SBOM gerado e SCA contínuo
- [ ] **Pipeline:** Gates de segurança operacionais
- [ ] **Monitorização:** Logs centralizados, proteção e retenção adequadas
- [ ] **Incidentes:** Processo de deteção, classificação e reporte parametrizável
- [ ] **Fornecedores:** Inventário, due diligence e ciclo de vida operacional
- [ ] **Testes:** SAST/DAST integrados; readiness para TLPT onde aplicável
- [ ] **Evidência:** Data room com políticas, testes, logs, contratos e reporting

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida)

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

---

## Métrica Simples: Estou Bem Preparado?

Se consegues responder SIM a isto, tens uma base AppSec forte para uma implementação DORA defensável:

1. **Governance:** Tenho política aprovada e cadeia de autoridade clara? ✓
2. **Risk Management:** Todas as apps estão classificadas e ligadas a requisitos? ✓
3. **Security by Design:** Meus requisitos e controlos são rastreáveis? ✓
4. **Software Supply:** Tenho SBOM e SCA ativos? ✓
5. **Operations:** Tenho monitorização centralizada com retenção e proteção adequadas? ✓
6. **Incident Response:** Consigo detetar, classificar e parametrizar reporte de incidentes? ✓
7. **Vendor Management:** Tenho ciclo de vida formal de contractors e terceiros críticos? ✓
8. **Testing:** Faço SAST/DAST e tenho readiness para TLPT quando aplicável? ✓
9. **Evidence:** Consigo demonstrar tudo isto em auditoria e reporte regulatório? ✓

**Leitura prática:** quanto mais respostas positivas, mais madura está a tua base AppSec. A passagem para conformidade DORA plena continua a exigir artefactos regulatórios, templates de reporte e formalização institucional que não vivem apenas neste manual.

---

## Nota Crítica: Gestão de Exceções em DORA

DORA exige que desvios e exceções sejam formais, auditáveis e aprovados ao nível adequado.

O que caracteriza uma exceção em SbD-ToE/DORA:
- desvio formal de um requisito;
- justificação técnica e de negócio;
- prazo de validade (`TTL`);
- plano de remediação e owner;
- trilho documental passível de auditoria.

Quem aprova depende da criticidade, do modelo de governação e do enquadramento regulatório aplicável. Em contextos críticos, a leitura DORA tende a exigir elevação clara da decisão ao nível de gestão apropriado.

Leitura prática:
- exceções sem aprovação formal comprometem a supervisão;
- algumas exceções podem ser inaceitáveis em leitura regulatória defensável;
- o manual cobre bem o processo, mas a admissibilidade final continua a depender do contexto regulatório.

**Referências:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) e [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

## Recursos Práticos de Implementação

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Comparação de ferramentas (IaC, logs, SCA, SAST, CI/CD) com exemplos de configuração
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de segurança por perfil organizacional
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Matrizes de responsabilidades e aprovações DORA-compatíveis
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Templates de reporte formal com campos DORA

Estes recursos são reutilizáveis para múltiplos frameworks e mostram como operacionalizar, fora do manual base, os detalhes que dependem de contexto regulatório, supervisor e tooling.

---

## Próximos Passos

1. Fazer um audit de conformidade atual contra a matriz acima
2. Sequenciar o roadmap por criticidade, gap e dependência
3. Implementar por fases, com evidência versionada
4. Parametrizar a camada regulatória de reporte e terceiros
5. Validar periodicamente a prontidão documental e operacional

Documentação completa: ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências

- **SbD-ToE Manual:** Capítulos 01–14
- **Cross-Check DORA:** [Análise normativa completa](/sbd-toe/cross-check-normativo/dora/intro)
- **Regulamento DORA:** UE 2022/2554

---

**Versão:** 1.2 (recalibrado após validação regulatória)  
**Data:** Abril 2026  
**Nota:** Este playbook complementa a [análise normativa DORA](intro) com implementação prática bounded e orientada a evidência.
