---
id: catalogo-requisitos-formacao
title: Catálogo de Requisitos de Formação e Onboarding
description: Catálogo canónico de requisitos de formação e onboarding de segurança (TRN-001 a TRN-009), com aplicabilidade por nível de risco e critérios de aceitação para trilhos formativos, onboarding verificável, Security Champions e eficácia formativa.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:formacao, TRN, onboarding, champions, trilhos, capacitacao, terceiros, formacao-continua, L1, L2, L3, auditoria]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Formação e Onboarding

## Âmbito: capacitação como controlo organizacional verificável

Este catálogo cobre os **requisitos de formação e onboarding de segurança** — os controlos que garantem que as pessoas que constroem, operam e mantêm sistemas têm a competência necessária para fazê-lo com segurança, e que essa competência é verificável.

A formação não é um benefício opcional: é um controlo organizacional com impacto directo na superfície de ataque. As vulnerabilidades mais prevalentes — injecção, autenticação fraca, gestão de segredos, configuração insegura — são, em grande parte, consequência de lacunas de competência rastreáveis a ausência de formação proporcional ao risco.

Os requisitos TRN são verificáveis: a existência de trilhos formativos definidos, de evidência de onboarding validado, de conteúdo actualizado e de KPIs recolhidos são factos auditáveis. A ausência de evidência equivale a ausência de controlo.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de NIST SSDF, NIST SP 800-30, ISO/IEC 27001, ISO/IEC 27005, OWASP SAMM v2.1, OWASP DSOMM, BSIMM13 e práticas de governação aplicacional orientadas a risco. Deve ser adaptado ao modelo organizacional de risco, mas sem perder a rastreabilidade para L1, L2 e L3.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-TRN-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo TRN - Formação e Onboarding

Requisitos que garantem que a competência de segurança das equipas é proporcional ao risco, verificável por evidência objectiva e mantida ao longo do ciclo de vida do projecto.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| TRN-001 | Trilhos de formação de segurança definidos por perfil e nível de criticidade | ✔ | ✔ | ✔ | Existem trilhos de formação de segurança definidos por perfil de colaborador (developer, ops, PO, QA, tech lead) e por nível de criticidade do projecto (L1, L2, L3); os trilhos especificam módulos obrigatórios, duração estimada e periodicidade de renovação; os trilhos são documentados e acessíveis. |
| TRN-002 | Onboarding de segurança obrigatório antes de trabalho autónomo | ✔ | ✔ | ✔ | Todo o colaborador com acesso a código, pipelines ou ambientes de produção completa o onboarding de segurança antes de operar de forma autónoma; o onboarding inclui: políticas e boas práticas relevantes ao perfil, manuseamento de segredos, processo de incidentes e controlos básicos de desenvolvimento seguro ou operações seguras conforme o papel. |
| TRN-003 | Validação objectiva do onboarding com critério de aceitação definido | ✔ | ✔ | ✔ | A conclusão do onboarding é verificada com critério objectivo — quiz, exercício prático ou outra forma de avaliação com taxa de aceitação mínima definida; o resultado é registado e rastreável ao colaborador e à versão do conteúdo administrada; resultados abaixo do limiar têm caminho de remediação definido. |
| TRN-004 | Acesso a ambientes críticos condicionado a onboarding validado | ✔ | ✔ | ✔ | O acesso a repositórios, pipelines de produção ou ambientes classificados como L2+ é condicionado à evidência de onboarding de segurança válido; a condição é verificável — o registo de onboarding é verificado no processo de onboarding de acesso; acesso sem onboarding válido é bloqueado ou escalado ao owner de segurança. |
| TRN-005 | Formação de segurança contínua para equipas em projectos L2 e L3 | - | ✔ | ✔ | Colaboradores em projectos L2+ recebem formação de segurança contínua — no mínimo uma sessão ou módulo relevante por semestre (L2) ou trimestre (L3); a formação contínua cobre evolução de ameaças, novas técnicas de ataque relevantes ao contexto e actualizações de políticas; a participação é registada e rastreável. |
| TRN-006 | Conteúdo formativo versionado e actualizado após triggers definidos | - | ✔ | ✔ | O conteúdo de formação e onboarding tem controlo de versão explícito; é revisto e actualizado após incidentes de segurança relevantes, alterações de política ou identificação de novas classes de vulnerabilidades no contexto do projecto; a versão do conteúdo administrada é rastreável ao registo de formação de cada colaborador. |
| TRN-007 | Onboarding de segurança equivalente para terceiros e contratados | ✔ | ✔ | ✔ | Terceiros, contratados e parceiros com acesso a código, pipelines ou dados sensíveis completam um onboarding de segurança equivalente ao dos colaboradores internos, proporcional ao seu perfil de acesso; o processo de validação e registo é o mesmo; ausência de onboarding válido bloqueia o acesso. |
| TRN-008 | Programa formal de Security Champions em equipas L3 | - | - | ✔ | Equipas em projectos L3 têm um ou mais Security Champions formalmente designados — com papel documentado, responsabilidades definidas, acesso a recursos AppSec e participação em comunidade de prática ou equivalente; o Champion não substitui o AppSec centralizado, mas amplifica a competência de segurança na equipa; a designação é rastreável e actualizada. |
| TRN-009 | KPIs de formação definidos, recolhidos e accionados | - | ✔ | ✔ | KPIs de eficácia formativa são definidos, recolhidos periodicamente e analisados — incluindo pelo menos: % cobertura de onboarding por equipa, taxa de aprovação em validações objectivas, tempo médio de onboarding e taxa de actualização de conteúdo; desvios face a thresholds definidos geram acção correctiva com owner e prazo. |

---

## Notas explicativas

- **TRN-001**: A definição de trilhos por perfil é determinante — um onboarding genérico que cobre todos os papéis superficialmente é menos eficaz do que trilhos diferenciados com menos volume mas maior relevância contextual. Um PO não precisa de saber configurar SAST; precisa de entender threat modeling light e critérios de aceitação de risco.
- **TRN-002 e TRN-003**: A distinção é operacionalmente importante: TRN-002 verifica se o onboarding acontece antes de trabalho autónomo (timing e cobertura); TRN-003 verifica se a conclusão tem evidência verificável (validade objectiva). É possível ter onboarding realizado (TRN-002 cumprido) sem validação rastreável (TRN-003 não cumprido).
- **TRN-004**: A condição de acesso é o mecanismo de enforcement de TRN-002 e TRN-003 — sem ela, o onboarding é recomendado mas não obrigatório na prática. Para L3, o enforcement deve ser automatizado ou verificado por processo formal de onboarding de acesso.
- **TRN-005**: A frequência diferenciada por nível (semestral L2, trimestral L3) reflecte a maior velocidade de evolução do contexto de ameaças em sistemas de maior criticidade. Para L1, formação anual ou em ciclos de performance é suficiente e recomendada mesmo sem obrigatoriedade formal.
- **TRN-006**: O versionamento do conteúdo formativo serve dois propósitos: permite rastrear o que cada colaborador aprendeu em que momento (relevante em incidentes — "a boa prática estava a ser ensinada?") e garante que o conteúdo reflecte o estado actual das ameaças e políticas.
- **TRN-007**: A equivalência de onboarding para terceiros é frequentemente negligenciada em favor da velocidade de onboarding. O critério de proporcionalidade ao perfil de acesso é o calibrador correcto: um contratado com acesso de leitura a repositórios não críticos não requer o mesmo nível de onboarding que um parceiro com acesso a pipelines de produção L3.
- **TRN-008**: O programa de Security Champions é o mecanismo de escala de AppSec sem a necessidade de crescer a equipa centralizada proporcionalmente ao número de projectos. O Champion é um multiplicador — mas a sua eficácia depende directamente de ter tempo formal dedicado, acesso a formação especializada e ligação à comunidade AppSec da organização. Um Champion sem tempo e sem suporte é apenas um título.
- **TRN-009**: KPIs sem thresholds e sem acção correctiva são métricas decorativas. O critério de aceitação de TRN-009 exige explicitamente que os KPIs produzam decisões. A taxa de aprovação em validações objectivas é o KPI mais predictivo de eficácia formativa real.

---

> Para o catálogo formativo detalhado por módulo e perfil, consultar [Catálogo Formativo](./catalogo-formativo).
> Para os trilhos formativos por perfil e nível de criticidade, consultar [Trilhos Formativos](./trilho-formativo).
> Para o programa de Security Champions, consultar [Programa de Security Champions](./programa-champions).
> Para a checklist canónica de onboarding, consultar [Checklist de Onboarding](./checklist-onboarding).
> Para o modelo de inclusão de terceiros e contratados, consultar [Modelo de Inclusão de Terceiros](./modelo-inclusao-terceiros).
> Para KPIs e métricas de eficácia formativa, consultar [KPIs e Métricas de Formação](./kpis-metricas).
