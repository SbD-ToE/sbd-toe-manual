---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de capacitação e onboarding no ciclo de vida de desenvolvimento
tags: [tipo:aplicacao, ciclo-vida, formacao, capacitacao, onboarding, seguranca]
genia: us-format-normalization
---

# Aplicação de Formação e Capacitação no Ciclo de Vida

## 🧭 Quando aplicar

| Fase | Ação | Evidência |
|------|------|-----------|
| Onboarding | Formação inicial em SbD e práticas seguras | Certificação LMS |
| Desenvolvimento contínuo | Cursos, labs e revisões trimestrais | Relatórios de formação |
| Release/Operações | Exercícios práticos e simulações | Logs de exercícios |
| Auditoria | Verificação de KPIs de capacitação | Relatórios GRC |

---

## 👥 Quem executa cada ação

| Papel | Responsabilidade |
|-------|------------------|
| **Developer** | Participar em formação prática, aplicar no código |
| **Quality Assurance (QA)** | Formação em validação e regressões |
| **AppSec Engineer** | Produzir conteúdos, ministrar formação, facilitar sesões |
| **DevOps / SRE** | Capacitação em CI/CD e monitorização |
| **Security Champion** | Mentorar equipas, facilitar peer-learning |
| **Gestão Executiva** | Apoiar adoção, validar conformidade regulatória |
| **GRC / Compliance** | Gerir rastreabilidade, auditorias, KPIs |
| **RH / PeopleOps** | Operar LMS, gerir onboarding, integrar em PDI |
| **Arquitetos de Software** | Contribuir ao threat modeling e padrões seguros |
| **Operações (Ops)** | Participar em simulações, comunicação em incidentes |
| **Fornecedores / Terceiros** | Receber formação mínima obrigatória |

---

## 📖 User Stories normalizadas

### US-01 - Onboarding seguro obrigatório
**Contexto.** Novos elementos sem formação introduzem riscos básicos.  

:::userstory
**História.**   
Como **RH/PeopleOps**, quero **garantir formação obrigatória de onboarding em SbD**, para **assegurar que todos iniciam alinhados com as práticas**.  

**Critérios de aceitação (BDD).**  
- **Dado** novo colaborador  
  **Quando** inicia funções  
  **Então** só tem acesso completo após completar formação  

**Checklist.**  
- [ ] Curso concluído no LMS  
- [ ] Certificação emitida  
- [ ] Registo arquivado  
- [ ] Acesso técnico bloqueado até conclusão  
- [ ] Bloqueio automático em Git/Azure DevOps/pipelines CI/CD  
- [ ] Exceções documentadas com aprovação AppSec/Gestão  
- [ ] Reautenticação bienal ou por trigger de novo risco  

:::

**Artefactos & evidências.** Certificados LMS, registos de bloqueio em Git/Azure DevOps, documento de exceções.

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Obrigatório | Obrigatório + avaliação prática |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Entrada de novo colaborador | RH + AppSec Engineer | Antes de acesso técnico |

**Ligações úteis.**  
[Checklist de Onboarding Técnico](./addon/checklist-onboarding)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)  

---

### US-02 - Formação contínua por perfil
**Contexto.** Sem atualização contínua, práticas ficam obsoletas.  

:::userstory
**História.**   
Como **AppSec**, quero **fornecer formação contínua por perfil (Dev, QA, DevOps, Gestão)**, para **garantir atualização com práticas mais recentes**.  

**Critérios de aceitação (BDD).**  
- **Dado** ciclo trimestral (L3), semestral (L2), anual (L1)  
  **Quando** LMS disponibiliza cursos  
  **Então** cada perfil completa trilha específica  

**Checklist.**  
- [ ] Cursos definidos por perfil  
- [ ] Registo no LMS  
- [ ] Ciclo definido: trimestral para L3, semestral para L2, anual para L1 (TRN-005)  
- [ ] Triggers adicionais: novo capítulo técnico, novo risco, incidente  
- [ ] Comunicação a equipas (anúncio, deadline, critério de conclusão)  
- [ ] Integração em OKRs individuais ou avaliações de performance  
- [ ] Revisão de eficácia trimestral  

:::

**Artefactos & evidências.** Relatórios LMS, comunicações a equipas, registos de conclusão, OKRs com formação.

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado anual | Obrigatório semestral | Obrigatório trimestral |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Ciclo contínuo | Trimestral (L3) / Semestral (L2) / Anual (L1) | AppSec Engineer + RH | Deadline comunicado com 2 semanas |

**Ligações úteis.**  
[Catálogo de Formação por Perfil Técnico](./addon/catalogo-formativo)  
[Trilhos Formativos por Função e Risco](./addon/trilho-formativo)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)  

---

### US-03 - Programa de Security Champions
**Contexto.** Sem champions, equipas carecem de liderança interna.  

:::userstory
**História.**   
Como **Champion**, quero **mentorar e evangelizar a equipa**, para **assegurar aplicação contínua das práticas SbD**.  

**Critérios de aceitação (BDD).**  
- **Dado** sprint em curso  
  **Quando** surgem dúvidas  
  **Então** champion apoia e orienta equipa  

**Checklist.**  
- [ ] Champion nomeado por equipa  
- [ ] Reuniões mensais registadas  
- [ ] Feedback recolhido  
- [ ] Comunidade de Champions formal (reunião mensal, canal Teams/Slack)  
- [ ] Documentação coletiva de práticas e antipadrões (wiki)  
- [ ] Badges ou reconhecimento institucional (email, quadro, salário)  
- [ ] Budget para eventos ou conferências de segurança (opcional por maturity)  

:::

**Artefactos & evidências.** Registos de reuniões, wiki de práticas, canal de comunidade, lista de reconhecimentos.

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Ciclo contínuo | Mensal | Security Champions + AppSec Engineer | Reunião mensal confirmada |

**Ligações úteis.**  
[Programa de Security Champions](./addon/programa-champions)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)  

---

### US-04 - Exercícios práticos e simulações
**Contexto.** Formação teórica sem prática tem baixa retenção.  

:::userstory
**História.**   
Como **QA/Testes**, quero **realizar exercícios práticos (labs, CTFs, simulações)**, para **garantir que o conhecimento é aplicável**.  

**Critérios de aceitação (BDD).**  
- **Dado** plano de formação  
  **Quando** executo exercício  
  **Então** registo resultado e métricas de desempenho  

**Critérios de aceitação (DoD).**  
- [ ] Labs executados  
- [ ] Resultados registados  
- [ ] Métricas analisadas  

:::

**Artefactos & evidências.** Logs de exercícios  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Ciclo de formação; Resp: QA + AppSec  

---

### US-05 - Medição de eficácia da formação
**Contexto.** Sem medir eficácia, não há melhoria contínua.  

:::userstory
**História.**   
Como **GRC**, quero **medir KPIs de capacitação (taxa de conclusão, eficácia em auditoria)**, para **avaliar impacto real da formação**.  

**Critérios de aceitação (BDD).**  
- **Dado** ciclo de formação  
  **Quando** recolho métricas  
  **Então** KPIs são reportados a gestão  

**Critérios de aceitação (DoD).**  
- [ ] KPIs definidos  
- [ ] Métricas recolhidas  
- [ ] Relatórios trimestrais  

:::

**Artefactos & evidências.** Relatórios GRC  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | KPIs anuais | KPIs trimestrais com metas |

**Integração.** Auditoria; Resp: GRC  

---

### US-06 - Code Clinics Estruturadas e Recorrentes
**Contexto.** Code clinics são sessões regulares de revisão pública de código real, educando sobre padrões seguros. Sem estrutura, tornam-se ad-hoc e perdem impacto.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **executar code clinics estruturadas** (revisão de PR reais, educativas, com checklist de segurança aplicado), para **garantir aprendizagem contínua e aplicação visível de padrões seguros**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma ou mais PRs são selecionadas  
  **Quando** a sessão é conduzida (presencial ou assíncrona)  
  **Então** o checklist de segurança é aplicado publicamente  
- E feedback é registado e compartilhado em canal interno  
- E lições aprendidas são documentadas para reutilização  

**Checklist.**  
- [ ] Cadência definida (semanal ou quinzenal)  
- [ ] Templates de checklist por domínio (Dev, DevOps, IaC)  
- [ ] PRs exemplares arquivadas (boas práticas + falhas)  
- [ ] Sessões registadas (vídeo, sumário, discussão assíncrona)  
- [ ] Participação rotativa (Developers, Security Champions, QA)  

:::

**Artefactos & evidências.**  
- Repositório de PRs exemplares (comentados)  
- Sumários de sessões e feedback  
- Estatísticas de participação  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Ocasional (mensal) | Recorrente (quinzenal) | Recorrente + rotativo (semanal) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Desenvolvimento | Submissão de PRs | AppSec Engineer + Security Champions | Semanal/quinzenal |

**Ligações úteis.**  
[Técnicas Formativas Avançadas](./addon/tecnicas-formativas)  
[Exemplo - Pull Request Seguro](./addon/exemplo-manual-dev-pr)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-07 - Threat Modeling Peer-led e Rotativo
**Contexto.** Threat modeling é prática crítica mas concentrada em AppSec. Operacionalizar como atividade peer-led e rotativa aumenta distribuição de conhecimento.

:::userstory
**História.**  
Como **Developer / Security Champion**, quero **liderar sessões de threat modeling** (por feature, épico ou refactor), para **disseminar conhecimento de análise de risco e aplicar SbD em design**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma feature nova ou refactor é planeado  
  **Quando** a sessão de threat modeling é agendada  
  **Então** é facilitada por Developer ou Champion com apoio de AppSec Engineer  
- E output é documentado (diagrama, matriz de riscos)  
- E decisões de segurança são rastreadas a requisitos do manual  

**Checklist.**  
- [ ] Sessão agendada antes de design finalizador  
- [ ] Template de threat modeling (ex: STRIDE) aplicado  
- [ ] Diagrama de arquitetura/fluxo documentado  
- [ ] Matriz de riscos (ameaça × impacto × controlo)  
- [ ] Decisões e exceções justificadas  
- [ ] Rotação de liderança entre Security Champions  

:::

**Artefactos & evidências.**  
- Diagramas (draw.io, Lucidchart)  
- Atas de sessão  
- Matriz de riscos com rastreabilidade a REQ-XXX  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional / ad-hoc | Recomendado por épico | Obrigatório antes de design finalizador |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Planeamento/Design | Aprovação de feature | Security Champion + AppSec Engineer | Antes do sprint de desenvolvimento |

**Ligações úteis.**  
[Técnicas Formativas Avançadas](./addon/tecnicas-formativas)  
[Integração Transversal com Capítulos Técnicos](./addon/integracao-transversal)  
[Threat Modeling - Capítulo 03](/sbd-toe/sbd-manual/threat-modeling/intro)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-08 - War Room e Simulações de Incidentes
**Contexto.** Simulações de incidentes treinam equipas na resposta sob pressão, validam processos e criam cultura de prontidão.

:::userstory
**História.**  
Como **Gestão Executiva / GRC**, quero **executar simulações de incidentes (war room)** regularmente, para **treinar equipas na resposta e validar processos de comunicação e remediação**.

**Critérios de aceitação (BDD).**  
- **Dado** que um cenário de incidente é simulado  
  **Quando** a resposta é executada em tempo real  
  **Então** todos os papéis (Developer, DevOps, AppSec Engineer, Operações, Gestão) participam  
- E o processo é documentado e analisado num debrief educativo  
- E lições aprendidas são incorporadas em runbooks  

**Checklist.**  
- [ ] Cenários baseados em riscos reais ou históricos  
- [ ] Comunicação (alertas, escalation, comms internas/externas) validadas  
- [ ] Tempos de deteção, resposta e resolução medidos (MTTD/MTTR)  
- [ ] Papel de cada interveniente documentado (playbooks)  
- [ ] Debrief realizado com recomendações  
- [ ] Cadência definida (anual mínimo, trimestral ideal)  

:::

**Artefactos & evidências.**  
- Cenários e scripts de simulação  
- Logs de execução (timelines, comunicações)  
- Relatório de debrief com MTTD/MTTR observados  
- Playbooks e runbooks atualizados  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado anual | Trimestral | Trimestral + rotativo por ameaça |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Operações/Auditoria | Trimestral ou pós-incidente | Gestão Executiva + GRC | Planeado anualmente |

**Ligações úteis.**  
[Técnicas Formativas Avançadas](./addon/tecnicas-formativas)  
[Monitorização e Operações - Capítulo 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-09 - Manutenção e Atualização de Trilhos Formativos
**Contexto.** Trilhos formativos precisam de revisão periódica com base em novos riscos, tecnologias, lições aprendidas.

:::userstory
**História.**  
Como **AppSec Engineer / GRC**, quero **manter e atualizar trilhos formativos por perfil e risco** (anualmente ou por trigger), para **garantir que a formação reflete práticas atuais e lições aprendidas**.

**Critérios de aceitação (BDD).**  
- **Dado** que um ano passou ou um novo risco é identificado  
  **Quando** a revisão de trilhos é agendada  
  **Então** conteúdos são reavaliados contra incidentes, atualizações tecnológicas e feedback de Security Champions  
- E trilhos são atualizados ou novos conteúdos são adicionados  
- E mudanças são comunicadas a RH e às equipas  

**Checklist.**  
- [ ] Revisão anual agendada (ex: Q1 de cada ano)  
- [ ] Feedback de Security Champions recolhido (survey ou reunião)  
- [ ] Lições aprendidas de incidentes integradas  
- [ ] Novos capítulos técnicos ou práticas mapeados  
- [ ] Trilhos atualizados (documento e matriz)  
- [ ] Comunicação a stakeholders (RH, equipas, Gestão Executiva)  

:::

**Artefactos & evidências.**  
- Documento com versão e changelog  
- Survey de feedback de Security Champions  
- Mapeamento de novos conteúdos a capítulos  
- Nota de lançamento com mudanças  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Ocasional | Anual | Anual + contínua por trigger |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Governance/Auditoria | Anual (Q1) ou novo risco | AppSec Engineer + GRC + RH | Antes do ciclo de formação novo |

**Ligações úteis.**  
[Catálogo de Formação por Perfil Técnico](./addon/catalogo-formativo)  
[Trilhos Formativos por Função e Risco](./addon/trilho-formativo)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-10 - Trilhos Formativos Proporcionais por Risco (L1–L3)

**Contexto.**  
Trilhos formativos precisam de ser explicitamente proporcionais ao risco da aplicação. Embora US-02 mencione "por perfil", falta clareza sobre a aplicação L1–L3 e sua integração com matriz de classificação de risco do cap 01.

:::userstory
**História.**  
Como **AppSec Engineer / GRC**, quero **aplicar trilhos formativos de forma explicitamente proporcional ao nível de risco** (L1, L2, L3) da aplicação e ao perfil técnico, para **garantir que cada colaborador recebe formação adequada ao seu contexto e responsabilidade**.

**Critérios de aceitação (BDD).**  
- **Dado** uma aplicação classificada em L1, L2 ou L3  
  **Quando** um novo colaborador é onboarded ou trilho é atualizado  
  **Então** o trilho formativo aplicado corresponde à matriz de proporcionalidade  
- E conteúdo reflete práticas obrigatórias conforme nível de risco  
- E rastreabilidade entre classificação → trilho é documentada  

**Checklist.**  
- [ ] Classificação de risco da aplicação documentada (cap 01)  
- [ ] Matriz de trilhos (addon/02) referenciada no plano de formação  
- [ ] Trilho L1: conteúdos básicos (secure coding, dependências, políticas)  
- [ ] Trilho L2: conteúdos intermédios (threat modeling, SCA, PR seguro, scanners CI/CD)  
- [ ] Trilho L3: conteúdos avançados (arquitetura segura, labs em apps vulneráveis, fuzzing, integração IRP)  
- [ ] Atribuição explícita do trilho por colaborador em LMS ou documento  
- [ ] Rastreabilidade: link entre classificação de aplicação → trilho → RH/LMS  
- [ ] Revisão periódica (anual ou por trigger de reclassificação)  
- 
- [ ] Catálogo → Trilho: existe um artefacto de mapeamento catálogo→trilho (`catalogo_trilhos.csv` ou `catalogo_trilhos.json`) que lista, para cada capítulo/tópico do `addon/01`, o módulo/trilho recomendado e a versão L1/L2/L3 aplicável.  
- 
**Artefactos & evidências adicionais.** `catalogo_trilhos.csv` com colunas mínimas: capitulo, topico, trilho_L1, trilho_L2, trilho_L3, formato_sugerido, exemplo_import_lms. Um exemplo de importação (CSV pequeno) deve acompanhar o plano de formação.  
- 
:::

**Artefactos & evidências.**  
Documento de classificação de risco (cap 01), matriz de trilhos (addon/02) com seleção do trilho aplicado, atribuição em LMS ou documento de plano formativo, rastreabilidade documentada.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Trilho básico (conteúdos essenciais) | Trilho intermédio (conteúdos obrigatórios + labs) | Trilho avançado (conteúdos completos + simulações + auditoria contínua) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding / Governance | Classificação da aplicação | AppSec Engineer + RH | Antes de primeira atribuição técnica |

**Ligações úteis.**  
[Trilhos Formativos por Função e Risco](./addon/trilho-formativo)  
[Gestão de Risco e Classificação - Capítulo 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-11 - Validação Formal de Onboarding via Checklist
**Contexto.** Onboarding sem validação formal deixa lacunas. Um checklist estruturado garante que todos os passos mínimos são cumpridos antes de qualquer acesso técnico.

:::userstory
**História.**  
Como **RH / GRC**, quero **validar formalmente o onboarding de cada colaborador** (via checklist estruturado), para **garantir que todos cumprem requisitos mínimos antes de acesso técnico e criar rastreabilidade auditável**.

**Critérios de aceitação (BDD).**  
- **Dado** que um novo colaborador inicia  
  **Quando** o processo de onboarding é executado  
  **Então** todos os itens do checklist são validados por responsável designado  
- E o registo formal é arquivado  
- E acesso técnico é bloqueado até conclusão  

**Checklist.**  
- [ ] Trilho formativo correto atribuído por função e risco  
- [ ] Conclusão do trilho validada (LMS ou evidência prática)  
- [ ] Validação de conhecimento concluída (quiz, exercício ou PR)  
- [ ] Acesso a repositórios de boas práticas e templates confirmado  
- [ ] Acesso técnico (Git, pipelines, ambientes) condicionado à conclusão  
- [ ] Registo formal arquivado com data e responsável  
- [ ] Contacto de apoio (Champion, SPOC) identificado  
- [ ] Aplicável a internos e externos (fornecedores com acesso técnico)  

:::

**Artefactos & evidências.**  
- Checklist preenchido e assinado (digital ou papel)  
- Registo em LMS, sistema de permissões ou GitHub/ADO  
- Evidência de conclusão (certificado, PDF, issue fechada)  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico (função) | Estruturado (função + risco) | Estruturado + auditoria periódica |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Entrada de novo colaborador | RH + GRC | Antes de acesso técnico |

**Ligações úteis.**  
[Checklist de Onboarding Técnico](./addon/checklist-onboarding)  
[Trilhos Formativos por Função e Risco](./addon/trilho-formativo)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-12 - Validação de Conhecimento via Quizzes Estruturados
**Contexto.** Formação sem validação de retenção de conhecimento é ineficaz. Quizzes estruturados garantem compreensão real e funcionam como rastreabilidade objetiva.

:::userstory
**História.**  
Como **AppSec Engineer / RH**, quero **implementar e executar quizzes de validação** (pós-onboarding, contínuos, por função) para **garantir retenção de conhecimento e criar registro auditável de competência**.

**Critérios de aceitação (BDD).**  
- **Dado** que um colaborador completa formação  
  **Quando** o quiz é aplicado  
  **Então** resultado ≥ 80% é obtido  
- E o registo (pontuação, data, validador) é arquivado  
- E acesso técnico só é desbloqueado com resultado positivo  

**Checklist.**  
- [ ] Quizzes definidos por trilho formativo (onboarding, contínuo, função)  
- [ ] Perguntas adaptadas a conteúdos reais do manual e aplicação  
- [ ] Formato acessível (LMS, formulário, ferramenta online, papel)  
- [ ] Resultado mínimo de aprovação definido (ex: 80%)  
- [ ] Feedback imediato com explicações de respostas  
- [ ] Registo com timestamp, nome, resultado e validador  
- [ ] Reciclagem periódica (ex: anual ou por trigger de novo risco)  
- [ ] Aplicável a internos, fornecedores e terceiros com acesso  

:::

**Artefactos & evidências.**  
- Templates de quiz por trilho e função  
- Registos de submissão com resultados  
- Análise de tendências (taxa de aprovação, tópicos mais falhados)  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Pontual (onboarding) | Periódica (anual) | Periódica + adaptativa (por trigger) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding / Contínuo | Conclusão de trilho ou anualmente | AppSec Engineer + RH | Antes/durante acesso |

**Ligações úteis.**  
[Template de Quiz para Onboarding](./addon/quiz-onboarding)  
[Quiz de Validação para Terceiros](./addon/quiz-terceiros)  
[Catálogo de Formação por Perfil Técnico](./addon/catalogo-formativo)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-13 - Operacionalização de Formação de Terceiros
**Contexto.** Fornecedores e terceiros com acesso técnico precisam de formação mínima obrigatória para reduzir risco de falhas de segurança.

:::userstory
**História.**  
Como **GRC / Gestão Executiva**, quero **garantir que fornecedores e terceiros com acesso recebem formação mínima obrigatória**, para **reduzir risco de falhas de segurança por falta de conhecimento e cumprir obrigações regulatórias (NIS2, DORA)**.

**Critérios de aceitação (BDD).**  
- **Dado** que um fornecedor com acesso técnico é onboarded  
  **Quando** é estabelecido acesso  
  **Então** completa trilho formativo obrigatório (ex: política da organização, canais de apoio, requisitos mínimos)  
- E certificação é registada contratualmente  
- E acesso é bloqueado até conclusão  

**Checklist.**  
- [ ] Categorização de terceiros (acesso nível, sensibilidade de dados)  
- [ ] Trilho mínimo definido por categoria  
- [ ] Quiz ou validação prática com resultado ≥ 80%  
- [ ] Certificado emitido e arquivado  
- [ ] Registo de conformidade em GRC  
- [ ] Acesso condicionado a conclusão  
- [ ] Reciclagem trimestral ou anual  

:::

**Artefactos & evidências.**  
- Trilhos por categoria de terceiro (conforme addon/21)  
- Quizzes e templates de validação (conforme addon/22)  
- Certificados e registos de conclusão  
- Registo de conformidade contratual  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + anual |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Contrato de fornecedor | GRC + RH + AppSec Engineer | Antes de acesso |

**Ligações úteis.**  
[Modelo de Inclusão de Terceiros](./addon/inclusao-terceiros)  
[Plano de Formação de Terceiros](./addon/plano-formacao-terceiros)  
[Quiz de Validação para Terceiros](./addon/quiz-terceiros)  
[Governança e Contratação - Capítulo 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

### US-14 - KPIs de Capacitação e Reporte (GRC)
**Contexto.** KPIs dispersos reduzem a capacidade de avaliar impacto da formação. É necessário formalizar lista, responsáveis e cadência.

:::userstory
**História.**
Como **GRC / Gestão Executiva**, quero **definir e recolher KPIs de capacitação** (taxa de conclusão, taxa de aprovação, eficácia em auditoria, MTTR em exercícios), para **avaliar impacto e reportar conformidade**.

**Critérios de aceitação (BDD).**
- **Dado** ciclo de formação definido
  **Quando** as métricas são recolhidas
  **Então** os KPIs são reportados ao dashboard e enviados trimestralmente para Gestão Executiva

**Checklist.**
- [ ] Lista de KPIs definida (ex: taxa de conclusão, taxa aprovação ≥80%, % tópicos falhados, tempo médio para completar labs)
- [ ] Responsável definido (GRC owner)
- [ ] Cadência de recolha e reporte definida (mensal/trimestral)
- [ ] Dashboard ou relatório automatizado configurado (ex: PowerBI/Looker/Grafana)
- [ ] Evidências arquivadas para auditoria (CSV/relatório PDF)

:::

**Artefactos & evidências.** Documento `KPIs_formacao.md` com definição, owner, cadência; amostra de exportação CSV; link para dashboard.

**Proporcionalidade L1–L3.**
| L1 | L2 | L3 |
|----|----|----|
| KPIs anuais | KPIs trimestrais com metas | KPIs trimestrais + metas por trilho e auditoria prática |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Auditoria/Formação | Monthly/Quarterly | GRC + AppSec Engineer | Report trimestral |

---

### US-15 - Formatos de Entrega e DoD por Formato
**Contexto.** A falta de especificação mínima por formato (labs, code clinics, microlearning, simulações) dificulta replicabilidade e níveis de qualidade.

:::userstory
**História.**
Como **AppSec Engineer / RH**, quero **definir os formatos de entrega e o DoD mínimo por formato** (labs, code clinics, microlearning, quizzes, simulações), para **garantir consistência e qualidade na formação**.

**Critérios de aceitação (BDD).**
- **Dado** um formato escolhido (ex: lab)
  **Quando** a sessão é planeada
  **Então** existe um DoD mínimo (infra + cenário + scoring + registo) e artefactos associados

**Checklist / DoD por formato.**
- Labs: infra provisionada + app vulnerável (ou VM) + guia de exercícios + scoring automático/manual + logs e relatório
- Code clinics: PRs selecionadas + checklist aplicado + gravação/resumo + pacote de lições aprendidas
- Microlearning: micro‑modules ≤15min + quiz de 3–5 perguntas + material de referência
- Simulações: cenário scriptado + playbook atualizado + debrief com MTTD/MTTR e melhorias
- Quizzes: template por trilho + threshold (ex: ≥80%) + registo timestamped

:::

**Artefactos & evidências.** Exemplos: `lab_template.md`, `code_clinic_template.md`, `microlearning_manifest.csv`, `simulation_script.yaml`.

**Proporcionalidade L1–L3.**
| L1 | L2 | L3 |
|----|----|----|
| Formatos básicos (microlearning) | Labs e quizzes estructurados | Labs com scoring + simulações + auditoria |

---

### US-16 - Caminho de Remediação Abaixo do Limiar

Um resultado abaixo do limiar mínimo não pode deixar o onboarding num estado indefinido.  

**Contexto.** `TRN-003` exige que resultados abaixo do limiar de aceitação tenham um caminho de remediação definido. Sem esse trilho, um colaborador que reprova a validação fica num limbo: nem tem acesso bloqueado de forma rastreável, nem tem um percurso claro para recuperar a competência. Operacionalizar a remediação fecha o ciclo entre validação objetiva e desbloqueio de acesso.  

:::userstory
**História.**   
Como **AppSec Engineer / RH**, quero **definir e executar um caminho de remediação para quem fica abaixo do limiar de validação**, para **garantir que a reprovação tem consequência operacional e percurso de recuperação rastreável, sem acesso técnico até aprovação**.  

**Critérios de aceitação (BDD).**  
- **Dado** um colaborador que obtém resultado abaixo do limiar mínimo na validação de onboarding  
  **Quando** o resultado é registado  
  **Então** é acionado automaticamente um plano de remediação (reformação dirigida + nova validação) e o acesso técnico permanece bloqueado até aprovação  

**Checklist.**  
- [ ] Limiar mínimo de aprovação documentado e versionado junto ao conteúdo  
- [ ] Plano de remediação definido por trilho (reformação dirigida aos tópicos falhados)  
- [ ] Número máximo de tentativas e escalonamento a AppSec/gestão após esgotamento  
- [ ] Acesso técnico bloqueado até nova validação aprovada (enforcement de `TRN-004`)  
- [ ] Registo da reprovação, da remediação e da reavaliação rastreável ao colaborador e à versão do conteúdo  

:::

**Artefactos & evidências.** Registo de resultados (pontuação, data, validador, versão do conteúdo); plano de remediação por tópico falhado; registo de bloqueio de acesso até reaprovação; trilha de tentativas e escalonamentos.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Reformação informal + nova tentativa | Plano de remediação documentado + bloqueio de acesso | Plano formal + limite de tentativas + escalonamento a AppSec e auditoria |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Resultado abaixo do limiar | AppSec Engineer + RH | Remediação iniciada antes de qualquer concessão de acesso |

**Ligações úteis.** [Catálogo de Requisitos de Formação (TRN-003)](./addon/catalogo-requisitos-formacao)  
[Checklist de Onboarding Técnico](./addon/checklist-onboarding)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-17 - Termo de Responsabilidade de Terceiros

O onboarding de um terceiro só fica completo quando a responsabilidade está formalmente aceite e registada.  

**Contexto.** `TRN-007` exige que o onboarding de terceiros e contratados tenha um termo de responsabilidade e registo formal (nome, entidade, data, validador). A formação por si só não vincula: sem aceitação explícita das obrigações de segurança e sem registo auditável, falta a evidência de que o terceiro assumiu o compromisso proporcional ao seu perfil de acesso. Este termo é a peça que torna o onboarding de terceiros equivalente — e não apenas semelhante — ao dos internos.  

:::userstory
**História.**   
Como **GRC / Gestão Executiva**, quero **registar um termo de responsabilidade assinado por cada terceiro com acesso técnico**, para **vincular formalmente o terceiro às obrigações de segurança e criar evidência auditável que condiciona o acesso (NIS2, DORA)**.  

**Critérios de aceitação (BDD).**  
- **Dado** um terceiro ou contratado com acesso a código, pipelines ou dados sensíveis  
  **Quando** conclui o onboarding de segurança  
  **Então** assina um termo de responsabilidade e o registo (nome, entidade, data, validador, perfil de acesso) é arquivado antes da concessão de acesso  

**Checklist.**  
- [ ] Termo de responsabilidade definido por perfil de acesso (proporcional)  
- [ ] Campos mínimos do registo: nome, entidade, data, validador, âmbito de acesso  
- [ ] Assinatura (digital ou contratual) recolhida antes da concessão de acesso  
- [ ] Registo arquivado em repositório institucional rastreável  
- [ ] Vinculação ao contrato/conformidade GRC (NIS2, DORA)  
- [ ] Acesso bloqueado na ausência de termo válido  

:::

**Artefactos & evidências.** Termo de responsabilidade assinado por terceiro; registo formal com campos mínimos (nome, entidade, data, validador); ligação contratual em GRC; evidência de bloqueio de acesso sem termo.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Termo simples + registo | Termo por perfil + arquivo rastreável | Termo por perfil + vinculação contratual + auditoria periódica |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Contrato de terceiro com acesso técnico | GRC + RH + AppSec Engineer | Termo registado antes de acesso |

**Ligações úteis.** [Catálogo de Requisitos de Formação (TRN-007)](./addon/catalogo-requisitos-formacao)  
[Modelo de Inclusão de Terceiros](./addon/inclusao-terceiros)  
[Plano de Formação de Terceiros](./addon/plano-formacao-terceiros)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-18 - Ação Corretiva sobre Desvios de KPIs

KPIs sem ação corretiva são métricas decorativas.  

**Contexto.** `TRN-009` exige que desvios de KPIs de formação face a thresholds definidos gerem ação corretiva com owner e prazo. US-14 define e recolhe os KPIs, mas a recolha não fecha o ciclo: falta o mecanismo que transforma um desvio (ex.: cobertura de onboarding abaixo da meta, taxa de aprovação em queda) numa decisão acionável e rastreável. Esta US operacionaliza o accionamento, não a definição dos indicadores.  

:::userstory
**História.**   
Como **GRC / Gestão Executiva**, quero **acionar uma ação corretiva sempre que um KPI de formação desvia do threshold**, para **garantir que os indicadores produzem decisões com owner e prazo, e não apenas relatórios**.  

**Critérios de aceitação (BDD).**  
- **Dado** um KPI de formação com threshold definido  
  **Quando** a recolha periódica revela desvio face ao threshold  
  **Então** é aberta uma ação corretiva com owner e prazo, registada e seguida até fecho  

**Checklist.**  
- [ ] Threshold explícito por KPI (cobertura de onboarding, taxa de aprovação, tempo médio, atualização de conteúdo)  
- [ ] Regra de acionamento documentada (desvio → ação corretiva)  
- [ ] Ação corretiva com owner nomeado e prazo definido  
- [ ] Seguimento até fecho registado (estado, evidência de resolução)  
- [ ] Desvios e ações reportados a Gestão Executiva no ciclo de reporte  

:::

**Artefactos & evidências.** Registo de desvios face a thresholds; ações corretivas com owner e prazo; trilha de seguimento até fecho; secção de desvios no relatório trimestral a Gestão Executiva.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Revisão informal de desvios | Ação corretiva com owner e prazo registados | Ação corretiva + seguimento até fecho + reporte e auditoria |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Auditoria/Formação | Desvio de KPI face ao threshold | GRC owner + AppSec Engineer | Ação aberta no ciclo de recolha; fecho dentro do prazo definido |

**Ligações úteis.** [Catálogo de Requisitos de Formação (TRN-009)](./addon/catalogo-requisitos-formacao)  
[KPIs e Métricas de Formação](./addon/kpis-metricas-formacao)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-19 - Formação em Uso Seguro de IA e Tooling

Ferramentas assistem; humanos decidem. A formação tem de ensinar a fronteira.  

**Contexto.** Com a adoção pervasiva de code assistants, geradores de código/testes, SAST/DAST/SCA e SOAR, é crítico que a formação cubra **quando confiar vs. quando validar** os outputs. O addon/12 define os conteúdos por capítulo técnico — antipadrões (aceitar código gerado sem ler, testes que apenas "provam" a implementação, confiança cega em alertas), os limites de automação (guardrails) e o princípio de que automação não-determinística requer sempre validação. Falta uma US que torne esta formação obrigatória e verificável.  

:::userstory
**História.**   
Como **AppSec Engineer / RH**, quero **tornar obrigatória e verificável a formação em uso seguro de IA e tooling**, para **prevenir vulnerabilidades de código gerado não-revisto, testes tautológicos e decisões automatizadas sem governação em contextos não-determinísticos**.  

**Critérios de aceitação (BDD).**  
- **Dado** um colaborador com acesso a code assistants, geradores ou automação de pipeline/SOAR  
  **Quando** completa o trilho formativo do seu perfil  
  **Então** inclui o módulo de uso seguro de IA/tooling (quando confiar vs. validar, guardrails, validação de código e testes gerados) com validação objetiva aprovada  

**Checklist.**  
- [ ] Módulo de uso seguro de IA/tooling incluído no trilho por perfil (Developer, QA, DevOps, AppSec, IR/Ops, Gestão)  
- [ ] Conteúdo cobre antipadrões, guardrails e validação de outputs (código e testes) do addon/12  
- [ ] Labs práticos: identificar vulnerabilidades em código gerado e testes tautológicos  
- [ ] Validação objetiva (quiz ≥ limiar) específica do módulo  
- [ ] Prompt engineering seguro (requisitos de segurança explícitos) abordado  
- [ ] Revisão do conteúdo anual ou por trigger de novo risco  

:::

**Artefactos & evidências.** Módulos de IA/tooling por perfil; registos de conclusão e validação no LMS; outputs de labs (vulnerabilidades e testes tautológicos identificados); versão do conteúdo formativo.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Microlearning de princípios (assistir vs. decidir) | Módulo por perfil + labs + quiz (≥ semestral) | Módulo por perfil + labs avançados + validação adaptativa (≥ trimestral) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding / Ciclo contínuo | Acesso a tooling de IA/automação ou novo risco | AppSec Engineer + RH | Antes de uso autónomo de tooling de IA |

**Ligações úteis.** [Formação em Uso Seguro de IA e Tooling](./addon/formacao-uso-seguro-ia-tooling)  
[Catálogo de Formação por Perfil Técnico](./addon/catalogo-formativo)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

### US-20 - Sandbox Isolado para Prática de Contractors

Contractors praticam num ambiente isolado antes de tocar em sistemas reais.  

**Contexto.** O guia de preparação de sandbox (addon/13) define um ambiente isolado, controlado e efémero onde contractors praticam ferramentas e procedimentos de segurança antes de acesso a produção — com permissões iniciais read-only, isolamento de rede face a produção, logging de toda a atividade, validação por exercícios (≥70%) e quiz (≥80%), e destruição pós-onboarding. Falta uma US que torne este sandbox um passo verificável do trilho de contractors, com sign-off que condiciona o acesso real.  

:::userstory
**História.**   
Como **DevOps / AppSec Engineer**, quero **provisionar e operar um sandbox isolado para prática de contractors antes do acesso a sistemas reais**, para **reduzir o risco de erro em produção e validar empiricamente a compreensão de políticas antes de conceder acesso**.  

**Critérios de aceitação (BDD).**  
- **Dado** um contractor em onboarding técnico  
  **Quando** o sandbox é provisionado  
  **Então** o contractor pratica num ambiente isolado de produção (read-only inicial, logging ativo) e o acesso real só é concedido após exercícios (≥70%), quiz (≥80%) e sign-off  

**Checklist.**  
- [ ] Sandbox provisionado por perfil (Developer, DevOps, QA) com app de demonstração  
- [ ] Isolamento de rede face a produção e resource limits aplicados  
- [ ] Permissões iniciais read-only, evoluindo só após validação  
- [ ] Logging de toda a atividade (logins, commits, acessos a secrets) ativado  
- [ ] Exercícios práticos (≥70%) e quiz de compreensão (≥80%) concluídos  
- [ ] Sign-off de conclusão (Tech Lead + AppSec) condiciona o acesso real  
- [ ] Destruição do sandbox e revogação de credenciais pós-onboarding; logs arquivados  

:::

**Artefactos & evidências.** Definição de infraestrutura do sandbox (repos, namespace, IaC); registos de logging de atividade; resultados de exercícios e quiz; sign-off de conclusão assinado; evidência de destruição e revogação pós-onboarding.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Sandbox simples opcional | Sandbox isolado por perfil + exercícios + quiz | Sandbox isolado + logging auditado + sign-off formal + destruição rastreável |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Onboarding técnico de contractor | DevOps + AppSec Engineer + Training Manager | Provisão T-5 dias; sign-off antes de acesso real (T+7) |

**Ligações úteis.** [Guia de Preparação Sandbox para Contractors](./addon/guia-preparacao-sandbox)  
[Modelo de Inclusão de Terceiros](./addon/inclusao-terceiros)  
[Governança e Contratação - Capítulo 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)  
[Papéis e Responsabilidades](/sbd-toe/sbd-manual/fundamentos/roles-responsabilidades/intro)

---

## 📦 Artefactos esperados

| Artefacto | Evidência |
|-----------|-----------|
| Certificados LMS | Onboarding concluído |
| Relatórios LMS | Formação contínua |
| Registos de champions | Reuniões + feedback |
| Logs de exercícios | Resultados e métricas |
| Relatórios GRC | KPIs e eficácia |
| **Repositório de PRs exemplares** | **Code clinics registadas** |
| **Diagramas de threat modeling** | **Atas e matriz de riscos** |
| **Cenários e logs de simulações** | **Relatórios de debrief e playbooks** |
| **Documento de trilhos com changelog** | **Survey de Champions + feedback** |
| **Checklist de onboarding validado** | **Registos formais por colaborador** |
| **Registos de quizzes** | **Pontuações, datas e validadores** |
| **Certificados de terceiros** | **Registos GRC de conformidade contratual** |

---

## ⚖️ Matriz de proporcionalidade L1–L3

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Onboarding seguro | Básico | Obrigatório | Obrigatório + avaliação prática |
| Formação contínua | Básico | Anual | Trimestral |
| Champions | Opcional | Recomendado | Obrigatório |
| Exercícios práticos | Opcional | Recomendado | Obrigatório |
| Métricas de eficácia | Básico | Anual | Trimestral com metas |
| **Code Clinics** | **Ocasional** | **Recorrente (quinzenal)** | **Recorrente + rotativo (semanal)** |
| **Threat Modeling** | **Opcional** | **Recomendado por épico** | **Obrigatório antes de design** |
| **Simulações de incidentes** | **Recomendado anual** | **Trimestral** | **Trimestral + rotativo** |
| **Manutenção de trilhos** | **Ocasional** | **Anual** | **Anual + contínua por trigger** |
| **Trilhos proporcionais por risco** | **Trilho básico** | **Trilho intermédio + labs** | **Trilho avançado + simulações + auditoria** |
| **Validação de onboarding (checklist)** | **Básico** | **Estruturado (função + risco)** | **Estruturado + auditoria periódica** |
| **Validação de conhecimento (quizzes)** | **Pontual** | **Periódica (anual)** | **Periódica + adaptativa** |
| **Formação de terceiros** | **Recomendado** | **Obrigatório** | **Obrigatório + anual** |

---

## 🏁 Recomendações finais

- **Onboarding é crítico**: sem formação inicial, erros básicos propagam-se.  
- **Validação formal via checklist** garante que todos os passos mínimos são cumpridos.  
- **Quizzes estruturados** validam retenção de conhecimento de forma auditável.  
- **Formação contínua** mantém práticas atualizadas.  
- **Champions** criam cultura de segurança dentro das equipas.  
- **Exercícios práticos** aumentam retenção e prontidão.  
- **Code Clinics estruturadas** garantem aprendizagem visível e replicável.  
- **Threat Modeling peer-led** distribui conhecimento de análise de risco.  
- **Simulações de incidentes** treinam resposta sob pressão e validam processos.  
- **Manutenção periódica de trilhos** garante relevância contínua da formação.  
- **Trilhos proporcionais por risco** garantem adequação de formação a contexto.  
- **Formação de terceiros** reduz risco de falhas por falta de conhecimento e cumpre obrigações regulatórias.  
- **Medição de KPIs** garante melhoria contínua e ligação a objetivos organizacionais.

```
