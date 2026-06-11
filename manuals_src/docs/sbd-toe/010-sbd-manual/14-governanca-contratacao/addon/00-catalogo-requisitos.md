---
id: catalogo-requisitos-governanca
title: Catálogo de Requisitos de Governação e Contratação
description: Catálogo canónico de requisitos de governação organizacional de segurança (GOV-001 a GOV-014), com aplicabilidade por nível de risco e critérios de aceitação para ownership, excepções, contratação, rastreabilidade, validação contínua, maturidade, onboarding técnico de terceiros e revisão de acesso.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:governanca, GOV, ownership, excecoes, contratacao, rastreabilidade, maturidade, L1, L2, L3, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Governação e Contratação

## Âmbito: governação como requisito verificável

Este catálogo cobre os **requisitos de governação organizacional de segurança** - os controlos que asseguram que as práticas prescritas nos capítulos técnicos do SbD-ToE são aplicadas, rastreadas, auditadas e evoluídas de forma sustentável.

Governação não é uma camada administrativa: é a estrutura que dá autoridade, visibilidade e continuidade à segurança. Sem estes requisitos, os controlos técnicos dos outros capítulos ficam dependentes de indivíduos, invisíveis à gestão e irrastreáveis em auditoria.

Os requisitos GOV são verificáveis: a existência de um modelo de governação aprovado, de um processo de excepções activo, de cláusulas contratuais aplicadas ou de KPIs reportados é factual e auditável. A ausência de evidência equivale a ausência de controlo.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de OWASP SAMM v2.1 (Governance, Policy & Compliance), NIST SSDF (PO.1, PO.3, RV.1, RV.2), ISO/IEC 27001 (A.5, A.15, A.18), OWASP DSOMM (Governance, Third-Party, Metrics), BSIMM13 (SM, CP) e DORA (governance of ICT risk). Deve ser adaptado ao contexto regulatório e revisto com cada ciclo de maturidade organizacional.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-GOV-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo GOV - Governação e Contratação

Requisitos que garantem que a segurança é aplicada com autoridade formal, rastreabilidade completa e capacidade de evolução organizacional sustentada.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| GOV-001 | Modelo formal de governação de segurança aprovado | ✔ | ✔ | ✔ | Modelo documentado e aprovado formalmente pela direcção, com papéis, responsabilidades e ciclo de decisão definidos; acessível e comunicado às equipas relevantes; revisto pelo menos anualmente ou após alteração organizacional significativa. |
| GOV-002 | Ownership de segurança atribuído por aplicação ou projecto | ✔ | ✔ | ✔ | Cada aplicação ou projecto tem um owner de segurança formalmente designado e registado; o owner tem competência e autoridade para tomar decisões de segurança no âmbito do projecto; designação actualizada em mudanças de equipa ou responsabilidade. |
| GOV-003 | Alçadas de aprovação definidas e conhecidas por nível de risco | - | ✔ | ✔ | Alçadas de aprovação para decisões de risco, excepções e compensações estão documentadas por nível (L1/L2/L3); a cadeia de autoridade é conhecida pelos decisores; decisões fora de alçada são escaladas de forma definida e rastreável. |
| GOV-004 | Processo formal de gestão de excepções activo | ✔ | ✔ | ✔ | Existe processo formal de excepções documentado e em uso; toda a não-aplicação de um controlo é registada com justificação, compensação, aprovador e prazo; excepções sem registo são tratadas como não conformidade activa; o processo cobre a cadeia de autoridade completa. |
| GOV-005 | Excepções com validade, monitorização e revalidação obrigatória | - | ✔ | ✔ | Todas as excepções activas têm data de expiração definida; existe mecanismo de alerta antes de expiração; excepções expiradas sem renovação são tratadas como não conformidade; a lista de excepções activas é revista em cada ciclo de auditoria. |
| GOV-006 | Cláusulas de segurança proporcionais ao risco em contratos com terceiros | ✔ | ✔ | ✔ | Contratos com fornecedores, outsourcing e contratados incluem cláusulas de segurança proporcionais ao nível de risco; cláusulas revistas em renovações; evidência de cláusulas aplicadas disponível por contrato activo. |
| GOV-007 | Validação formal de fornecedores antes de onboarding | ✔ | ✔ | ✔ | Fornecedores com acesso a dados, código ou pipelines são validados com questionário ou checklist antes de onboarding; validação proporcional ao risco (L3: SBOM, SLA de incidentes, direito de auditoria formal); registo de validação retido e rastreável. |
| GOV-008 | Rastreabilidade organizacional de decisões de segurança por aplicação | - | ✔ | ✔ | Existe registo consolidado por aplicação que liga: classificação de risco → requisitos aplicados → excepções aprovadas → fornecedores validados → owner de segurança; registo actualizado em cada release relevante ou mudança de risco; disponível para auditoria. |
| GOV-009 | Evidência de decisões rastreável, referenciável e retida | ✔ | ✔ | ✔ | Toda a decisão de risco ou excepção tem artefactos de evidência referenciáveis (ticket, nota, registo GRC, ADR ou equivalente); a cadeia de autoridade - quem pediu, quem avaliou, quem aprovou - é verificável; evidência retida pelo período definido em política. |
| GOV-010 | Ciclo de validação contínua e revisão periódica de conformidade | - | ✔ | ✔ | Ciclo de revisão periódica definido por tipo de activo (aplicações L3: trimestral; L2: semestral; fornecedores críticos: anual); revisões produzem evidência rastreável; desvios identificados geram acções correctivas com owner e prazo definidos. |
| GOV-011 | KPIs de governação definidos, recolhidos e reportados | - | ✔ | ✔ | KPIs de governação estão definidos, são recolhidos periodicamente e reportados à gestão; desvios face a thresholds definidos geram acção correctiva; KPIs incluem pelo menos: excepções activas por domínio, % aplicações com owner atribuído, % contratos com cláusulas de segurança. |
| GOV-012 | Modelo de maturidade activo com evolução medida e planeada | - | - | ✔ | Avaliação de maturidade de segurança activa (SAMM, DSOMM ou equivalente); realizada pelo menos anualmente; resultados documentados com plano de evolução e metas definidas; evolução comparada com ciclo anterior e reportada à gestão. |
| GOV-013 | Onboarding técnico e formação obrigatória pré-acesso de terceiros | rec. | ✔ | ✔ | Contractors e terceiros completam preparação técnica estruturada **antes de acesso real** a sistemas: formação de segurança por perfil (Dev, DevOps, QA, Arquitetura), quiz de compreensão com score mínimo (tipicamente 80%), ambiente sandbox para prática e NDA/confidentiality agreement assinados; o acesso só é concedido após *sign-off* de conclusão validado (Security Champion/AppSec + Tech Lead); o registo é rastreável (GRC/LMS) com datas, scores e validador, e mantido conforme retenção regulatória aplicável (DORA, NIS2). Em L1 é recomendado; em L2/L3 é obrigatório, com quiz validado em L3. |
| GOV-014 | Revisão periódica de acesso de terceiros (least privilege) | ✔ | ✔ | ✔ | O acesso de contractors activos a sistemas (repositórios, CI/CD, bases de dados, cloud IAM, VPN) é revisto periodicamente — semestral em L1, trimestral em L2/L3 — validando, por terceiro, que cada acesso permanece necessário ao projeto; acesso excessivo ou obsoleto é removido no próprio dia; a revisão é assinada (Tech Lead + Security Champion), as mudanças ficam em *audit trail* e um relatório consolidado (% mantido / % removido) é entregue. Triggers adicionais: mudança de projeto, incidente. |

---

## Notas explicativas

- **GOV-001**: A aprovação formal pela direcção não é formalismo - é o mecanismo que confere autoridade ao modelo. Um modelo de governação não aprovado pela direcção não tem força para exigir conformidade nem para sustentar auditorias externas.
- **GOV-002**: O owner de segurança é o ponto de responsabilização de cada aplicação. Sem owner definido, excepções não têm aprovador, desvios não têm destinatário, e auditorias não têm interlocutor. A rotatividade de equipas é o principal trigger de ownership não actualizado.
- **GOV-003**: As alçadas não definem quem decide tudo - definem quem decide *o quê*, com que autoridade, e quando escalar. Para L1 é suficiente um responsável técnico; para L3, o CISO ou equivalente deve estar na cadeia. A ausência de alçadas formais gera inconsistência e concentração informal de poder.
- **GOV-004 e GOV-005**: A distinção é intencional. GOV-004 verifica se o processo existe e é usado; GOV-005 verifica se as excepções activas estão controladas no tempo. É possível ter um processo formal (GOV-004 cumprido) com excepções cronicamente expiradas (GOV-005 não cumprido).
- **GOV-006**: A proporcionalidade ao risco é determinante: exigir o mesmo nível de cláusulas a um fornecedor de L1 e a um de L3 é ineficiente; não exigir cláusulas adequadas a um fornecedor de L3 é uma lacuna de controlo. A referência é a classificação de risco da aplicação ou serviço integrado.
- **GOV-008**: A rastreabilidade organizacional não é um spreadsheet estático - é um registo vivo que reflecte o estado de segurança de cada aplicação num dado momento. O seu valor para auditoria depende directamente da sua actualidade.
- **GOV-011**: KPIs sem thresholds e sem acção correctiva são apenas métricas decorativas. O critério não exige um dashboard sofisticado - exige que os números produzam decisões.
- **GOV-012**: A avaliação de maturidade só tem valor se comparada com ciclos anteriores e se gerar um plano com metas concretas. Uma avaliação que não muda nada não é um controlo - é um exercício.
- **GOV-013**: O risco de um terceiro não preparado não é má-fé - é erro involuntário: credenciais expostas, acesso a dados não autorizados, práticas inseguras por desconhecimento. O *sign-off* antes do acesso é o ponto onde a preparação se torna pré-condição e não formalidade posterior. Liga o Cap. 13 (Formação) ao Cap. 14 (Governação): a formação fornece o conteúdo, a governação fornece o *gate* de acesso e a rastreabilidade.
- **GOV-014**: O *access creep* é silencioso - permissões acumulam-se ao longo do tempo e ninguém as remove sem um ciclo que o force. A revisão periódica é o mecanismo que mantém o *least privilege* vivo em vez de declarado. A diferença face à revisão de acesso interno é o perfil de risco do terceiro e a frequência: para um contractor de L3, o trimestre é o limite aceitável entre o fim de uma necessidade e a remoção do acesso correspondente.

---

> Para o modelo de governação e ciclo de decisão, consultar [Modelo de Governação](./modelo-governancao).
> Para o processo canónico de excepções, consultar [Processo Canónico de Gestão de Excepções](./processo-excecoes).
> Para cláusulas contratuais, consultar [Cláusulas Contratuais de Segurança](./clausulas-contratuais).
> Para validação de fornecedores, consultar [Modelo de Validação de Fornecedores](./modelo-validacao-fornecedores).
> Para rastreabilidade organizacional, consultar [Rastreabilidade Organizacional](./rastreabilidade-organizacional).
> Para validação contínua, consultar [Validação Contínua](./validacao-continuada).
