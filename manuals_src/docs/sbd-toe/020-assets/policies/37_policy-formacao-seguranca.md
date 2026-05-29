---
id: policy-formacao-seguranca
title: Política de Formação e Capacitação em Segurança
description: Política organizacional que define os requisitos para o programa de formação e capacitação em segurança, incluindo onboarding obrigatório, trilhos formativos por perfil e nível de risco, programa de Security Champions, exercícios práticos, actualização de conteúdos, KPIs de eficácia e integração com os objectivos de performance individuais, proporcional ao nível de criticidade (L1, L2, L3).
tags: [policy, formação, capacitação, onboarding, Security Champions, trilhos formativos, labs, CTF, KPIs formação, cap13, L1, L2, L3, governance, SSDF, SAMM]
grupo: governacao
sidebar_position: 37
---

# Política de Formação e Capacitação em Segurança

## 1. Objetivo

Esta política define os requisitos para o **programa de formação e capacitação em segurança** da organização, cobrindo o onboarding de novos colaboradores, os trilhos formativos contínuos por perfil e nível de risco, o programa de Security Champions, os exercícios práticos e os mecanismos de avaliação de eficácia.

Políticas, ferramentas e processos de segurança são ineficazes sem as pessoas que os operam. A formação em segurança não é um exercício de compliance anual - é o mecanismo que transforma prescrições técnicas em prática operacional diária. Um developer que compreende as implicações de segurança das decisões de código toma melhores decisões em cada pull request. Um DevOps que compreende o modelo de ameaça da sua infraestrutura configura-a de forma mais segura. Um Security Champion que tem autoridade, conhecimento e suporte institucional consegue disseminar e sustentar a cultura de segurança na sua equipa. Sem investimento deliberado em capacitação, o risco humano permanece o vector mais difícil de mitigar.

O objetivo desta política é garantir que:

- Todos os colaboradores com responsabilidades técnicas recebem formação em segurança proporcional ao seu perfil e ao nível de risco das aplicações em que trabalham
- O onboarding de novos colaboradores inclui formação em segurança antes de acesso técnico pleno
- Os trilhos formativos são mantidos actualizados e reflectem os riscos e tecnologias relevantes
- O programa de Security Champions está operacional e tem suporte institucional
- Exercícios práticos substituem ou complementam formação exclusivamente teórica
- A eficácia da formação é medida com KPIs definidos

---

## 2. Âmbito e obrigatoriedade

Esta política aplica-se a todos os colaboradores com funções técnicas que participam no desenvolvimento, operação, teste, arquitectura ou governação de sistemas da organização. Inclui colaboradores internos, contractors e fornecedores com acesso técnico continuado.

| Nível | Obrigatoriedade |
|---|---|
| L1 | Formação básica de onboarding; awareness de segurança; acesso a recursos formativos |
| L2 | Obrigatório; trilhos formativos por perfil; onboarding estruturado; Security Champion designado; revisão anual de conteúdos |
| L3 | Obrigatório; trilhos completos com exercícios práticos obrigatórios; Security Champion com formação avançada; simulações periódicas; KPIs de eficácia acompanhados |

---

## 3. Onboarding de novos colaboradores

Todo o novo colaborador com funções técnicas deve completar o processo de onboarding de segurança antes de receber acesso técnico pleno:

### 3.1 Conteúdos mínimos de onboarding

| Tópico | Descrição | Obrigatoriedade |
|---|---|---|
| Políticas de segurança da organização | Apresentação das políticas aplicáveis à função (gestão de segredos, acesso a dados, gestão de credenciais, IRP) | Todos os níveis |
| Gestão segura de credenciais | Uso de vault, proibição de hardcoding, rotação de credenciais pessoais | Todos os níveis |
| Classificação de dados e acesso mínimo | Princípio do menor privilégio; categorias de dados; o que pode e não pode ser partilhado | L2/L3 |
| Reporte de incidentes e anomalias | Canal de reporte, o que reportar, responsabilidade individual | Todos os níveis |
| Práticas de desenvolvimento seguro (baseline) | Fundamentos relevantes para a função | L2/L3 |
| Ferramentas e processo de segurança da organização | SAST, SCA, gestão de segredos, pipeline de segurança | L2/L3 |

### 3.2 Validação de onboarding

- [ ] Conclusão documentada no LMS ou sistema de RH
- [ ] Quiz ou avaliação com nota mínima de 80%
- [ ] Registo arquivado e associado à identidade do colaborador
- [ ] Acesso técnico pleno condicionado à conclusão do onboarding (L2/L3)

---

## 4. Trilhos formativos por perfil e nível de risco

Os trilhos formativos são o conjunto de módulos obrigatórios e opcionais recomendados para cada perfil técnico, calibrados pelo nível de risco da aplicação em que o colaborador trabalha.

### 4.1 Matriz de trilhos por perfil e nível de risco

| Função | L1 | L2 | L3 |
|---|---|---|---|
| **Developer** | Secure coding básico; gestão de dependências | Threat modeling leve; SCA; revisão de código segura | Threat modeling formal; arquitectura segura; labs em aplicações vulneráveis |
| **QA / Testes** | Testes de segurança básicos | Critérios de aceitação de segurança; fuzzing leve | Fuzzing avançado; validação de excepções; SAST/DAST |
| **DevOps / SRE** | Gestão de segredos; configuração de ambientes | Integração segura em CI/CD; pipelines com gates de segurança | SLSA; proveniência; monitorização contínua; IaC seguro |
| **Product Owner** | Requisitos mínimos de segurança; backlog seguro | Classificação de risco; gestão de excepções | Processo formal de aceitação de risco; revisão com AppSec |
| **AppSec Engineer** | - | Facilitação de threat modeling; revisão de PRs; operação de ferramentas | Threat modeling avançado; análise de SBOM; gestão de programa |
| **Security Champion** | Awareness geral | Políticas e práticas SbD-ToE; mentoria básica | Trilho avançado; threat modeling; liderança de CTFs; participação em war rooms |
| **Gestão / Tech Lead** | Awareness executivo | Classificação de risco; exceções e aprovações | Métricas de maturidade; reporting executivo; pós-mortems |

### 4.2 Módulos obrigatórios vs. opcionais

Cada trilho formativo deve identificar explicitamente:

- **Módulos obrigatórios**: condição de acesso a sistemas (onboarding) ou de manutenção de acesso (renovação anual)
- **Módulos recomendados**: aprofundamento proporcional ao nível de risco e à função
- **Módulos opcionais**: capacitação avançada voluntária ou para progressão para Security Champion

---

## 5. Programa de Security Champions

O programa de Security Champions tem como objectivo distribuir competências de segurança pelas equipas de desenvolvimento, criando pontos de responsabilização e disseminação que não dependem de centralização no AppSec Engineer.

### 5.1 Requisitos do programa

| Requisito | Descrição |
|---|---|
| Designação formal | Security Champion designado por aplicação L2/L3 (ver Política de Rastreabilidade Organizacional) |
| Trilho formativo específico | Formação adicional além do trilho base da função - threat modeling, gestão de excepções, liderança de exercícios |
| Responsabilidades documentadas | Mentoria da equipa; participação em revisões de código; coordenação com AppSec; submissão de excepções; manutenção do repositório de conformidade |
| Comunidade de Champions | Reuniões regulares entre todos os Champions activos (mínimo mensal em L3); canal de comunicação dedicado; partilha de boas práticas e antipadrões |
| Reconhecimento institucional | A função de Security Champion deve ter visibilidade e reconhecimento formal (ex: referência em avaliações de desempenho, participação em conferências de segurança) |

### 5.2 Renovação e actualização

A formação do Security Champion deve ser renovada anualmente. Um Security Champion com formação expirada deve concluir a renovação no prazo de 60 dias, durante o qual as responsabilidades podem ser partilhadas com o AppSec Engineer enquanto a actualização é concluída.

---

## 6. Exercícios práticos e simulações

A formação exclusivamente teórica tem baixa taxa de retenção e não desenvolve capacidade de resposta em cenários reais. Os exercícios práticos são componente obrigatória dos trilhos L3 e recomendada em L2:

| Tipo de exercício | Descrição | L2 | L3 |
|---|---|---|---|
| Labs em aplicações vulneráveis | Ambientes controlados com vulnerabilidades reais para identificação e exploração (ex: OWASP WebGoat, Juice Shop, DVWA) | Recomendado | Obrigatório |
| CTF (Capture the Flag) | Competições ou exercícios estruturados com desafios de segurança por categoria | Recomendado | Obrigatório (mínimo 1/ano) |
| Simulação de threat modeling | Sessão prática de threat modeling sobre arquitectura real ou fictícia, com resultado documentado | Recomendado | Obrigatório |
| Tabletop de resposta a incidentes | Exercício de simulação de incidente sem activação real de sistemas (ver Política de IRP) | Recomendado | Obrigatório (semestral) |
| Code review de segurança guiado | Revisão de código com antipadrões injectados, em contexto de formação | Recomendado | Obrigatório |

Os resultados dos exercícios devem ser registados com data, participantes, tipo de exercício e métricas de desempenho (quando aplicável).

---

## 7. Actualização de conteúdos formativos

Os trilhos formativos reflectem o estado da arte em determinado momento - sem actualização, tornam-se obsoletos e criam falsa confiança. Os conteúdos devem ser revistos:

| Cadência | Âmbito |
|---|---|
| Anual (mínimo) | Revisão completa de todos os módulos; remoção de conteúdo obsoleto; adição de novos riscos identificados |
| Após incidente de segurança | Revisão dos módulos relevantes para a causa raiz; adição de lição aprendida ao trilho |
| Após alteração tecnológica significativa | Actualização dos módulos afectados (ex: nova plataforma, novo framework, nova regulação) |
| Após feedback de Security Champions | Incorporação de antipadrões identificados em contexto real |

A revisão de conteúdos deve ser coordenada pelo AppSec Engineer com input dos Security Champions e do GRC. As alterações são comunicadas às equipas e ao sistema de RH para actualização de registos de conclusão onde aplicável.

---

## 8. KPIs de eficácia formativa

A eficácia da formação deve ser medida com base em indicadores que vão além da taxa de conclusão:

| KPI | Descrição | Target |
|---|---|---|
| Taxa de conclusão de formação obrigatória | % de colaboradores com trilho obrigatório concluído | > 90% |
| Taxa de aprovação em quiz | % de participantes com nota ≥ 80% | > 85% |
| Tempo médio para completar trilho | Indicador de acessibilidade e adequação da carga formativa | Referência interna |
| % de Security Champions com formação válida | Champions com formação não expirada | 100% |
| Taxa de reincidência de findings do mesmo tipo | Redução de vulnerabilidades recorrentes atribuíveis a lacunas de conhecimento | Trend descendente |
| Tempo médio de resolução em exercícios | MTTR em simulações de incidente - melhoria ao longo do tempo | Trend descendente |
| % de tópicos falhados no quiz | Identificação de áreas de conhecimento com maior lacuna - informa revisão de conteúdos | Trend descendente por tópico |

Os KPIs de formação devem ser reportados trimestralmente ao GRC e integrados nos relatórios de governação de segurança.

---

## 9. Integração com objectivos de performance individuais

Em L3, a participação activa no programa de segurança deve ser reconhecida formalmente:

- [ ] Conclusão de formação obrigatória integrada como critério de avaliação de desempenho
- [ ] Papel de Security Champion reconhecido nas avaliações de desempenho do colaborador
- [ ] Participação em exercícios práticos registada como desenvolvimento profissional
- [ ] Budget para formação externa e certificações de segurança disponibilizado para perfis técnicos com responsabilidades de segurança

---

## 10. Responsabilidades

| Role | Responsabilidade |
|---|---|
| AppSec Engineer | Definir e manter os trilhos formativos; coordenar o programa de Security Champions; facilitar exercícios práticos; analisar KPIs de eficácia |
| GRC / Compliance | Gerir o LMS ou sistema de registo de formação; acompanhar KPIs; produzir relatórios periódicos; auditar conformidade |
| RH | Integrar formação obrigatória no processo de onboarding; registar conclusão; integrar métricas em avaliações de performance |
| Security Champion | Completar o trilho formativo específico; mentorar a equipa; participar em exercícios; reportar lacunas de conhecimento identificadas |
| Tech Lead | Garantir que a equipa tem tempo alocado para formação; promover participação em exercícios; escalar lacunas identificadas |
| Gestão / CISO | Garantir budget e recursos para o programa formativo; reconhecer institucionalmente o papel de Security Champion; analisar relatórios de eficácia |

---

## 11. Formação em agentes AI e tooling pervasivo (módulo obrigatório)

Quando a organização adopta agentes AI com *tool-use* no SDLC (Policy 38), todos os *roles* directamente envolvidos passam a ter formação mínima obrigatória sobre o tema. Não é formação optativa — é parte do *baseline* de competências, ao nível do que exigimos sobre OWASP Top 10 ou *secure coding* básico.

### 11.1 Cobertura mínima por *role*

| Role | Conteúdos mínimos | Cadência |
|---|---|---|
| **Developer** | Uso assistido seguro (revisão obrigatória do output, *secret scanning*, licenças); prompts e *skill files* como código; anti-padrões; quando escalar para `appsec` | Onboarding + actualização anual |
| **AppSec Engineer** | Modelo A0–A4 + `REQ-AGN-*`; threat modeling agentic (playbook Cap. 03); MITRE ATLAS + OWASP LLM Top 10; eval suites; resposta a *off-policy actions* e *intent-action divergence* | Onboarding + actualização semestral |
| **DevOps / SRE** | Identidade *workload* para agentes (OIDC); *scoping* per-tool; *kill-switch* operacional + exercícios; telemetria agentic (OPS-012/013/014) | Onboarding + actualização semestral |
| **GRC / Compliance** | Policy 38 (mandates); cláusulas contratuais AI (Policy 33 §10); AI Act Art. 14 + 26 + 53 + 55; revisão organizacional de mandates | Onboarding + actualização semestral |
| **Tech Lead / Software Architect** | Padrões `ARC-015`; arquitetura agentic (intent declaration, out-of-band approval, kill-switch); supply chain AI (`DEP-011..014`) | Onboarding + actualização anual |
| **Product Owner / Scrum Master** | Implicações dos níveis A0–A4 nos requisitos e *acceptance criteria*; quando uma feature exige *mandate* novo | Onboarding + actualização anual |
| **CISO / Executive Management** | Risco operacional e regulatório de agentes; aprovação A4; revisão periódica do registo de mandates | Anual |

### 11.2 Exercícios práticos recomendados

- **Tabletop**: simulação de *off-policy action* em produção — quem dispara *kill-switch*, quem comunica, quem escala (cross-link Cap. 12 IRP).
- **Hands-on**: exercício de revisão de PR com output GenAI — identificar padrões problemáticos.
- **Red team**: tentar *prompt injection* contra um agente em sandbox; observar deteção em OPS-014.
- **Exercício de mandate**: receber escopo realista, classificar nível A0–A4, escrever mandate.

### 11.3 Onde aterra

Esta formação é parte do trilho do Cap. 13 ([addon 12 — Formação em Uso Seguro de IA e Tooling Pervasivo](/sbd-toe/sbd-manual/formacao-onboarding/addon/formacao-uso-seguro-ia-tooling)). Esta política torna-a **obrigatória** (em vez de recomendada) quando há agentes AI em A1+ no SDLC da organização.

### 11.4 Proporcionalidade

| Nível de risco organizacional | Cobertura obrigatória |
|---|---|
| L1 | Developer + AppSec + DevOps (essenciais) |
| L2 | + GRC + Tech Lead/SWA + PO/SM |
| L3 | Todos os *roles* da tabela 11.1 + exercícios práticos semestrais |

---

## 12. Revisão e auditoria desta política

Esta política deve ser **revista anualmente** ou após qualquer um dos seguintes eventos:

- Incidente de segurança em que uma causa raiz foi lacuna de conhecimento ou prática inadequada de um colaborador
- Alteração significativa do portfólio tecnológico que introduza novos requisitos de competência
- Alteração regulatória que imponha novos requisitos de formação (ex: DORA, NIS2, AI Act Art. 4)
- KPI de eficácia formativa que indique degradação sistemática
- Adopção operacional de agentes AI em A1+ que active a secção 11

---

## 13. Referências normativas e técnicas

| Referência | Relevância |
|---|---|
| SbD-ToE Cap. 13 - Formação e Capacitação | US-03: Security Champions; US-04: exercícios práticos; US-09: actualização de trilhos; US-10: trilhos proporcionais por risco; US-14: KPIs de capacitação |
| SbD-ToE Cap. 13 (addon 12) — Formação em Uso Seguro de IA e Tooling Pervasivo | Conteúdo detalhado do módulo agentic |
| Política de Mandates de Agentes AI (`38_policy-mandates-agentes.md`) | Activação da secção 11 |
| Política de Uso de Ferramentas de Apoio (`16_policy-uso-ferramentas-apoio.md`) | Regras de uso A0–A4 |
| Política de Rastreabilidade Organizacional (`34_policy-rastreabilidade-organizacional.md`) | Designação formal de Security Champions |
| Política de Contratação Segura (`33_policy-contratacao-segura.md`) | Formação mínima para contractors e fornecedores |
| Política de IRP (`32_policy-irp.md`) | Tabletops e simulações de resposta a incidentes |
| NIST SSDF - PO.3, PO.7 | Training requirements for secure software development |
| NIST AI RMF 1.0 — GOVERN-3.x | AI workforce education |
| OWASP SAMM - Education and Guidance | Security training and awareness practices |
| OWASP Top 10 for LLM Applications (2025) | Conteúdo programático para AppSec |
| MITRE ATLAS | Catálogo de tactics/techniques adversariais para AppSec / red team |
| OWASP WebGoat / Juice Shop / DVWA | Plataformas de referência para labs em aplicações vulneráveis |
| DORA - Art. 15 | ICT-related training requirements for financial entities |
| NIS2 - Art. 21 | Cybersecurity training obligations |
| ISO/IEC 27001 - A.7.2.2 | Information security awareness, education and training |
| ISO/IEC 42001:2023 | AI Management System — workforce competence |
| EU AI Act (Reg. (UE) 2024/1689) - Art. 4 (AI literacy) | Obrigação geral de literacia em AI |
