---
id: catalogo-requisitos-testes
title: Catálogo de Requisitos de Testes de Segurança
description: Catálogo canónico de requisitos do programa de testes de segurança (TST-001 a TST-010), com aplicabilidade por nível de risco e critérios de aceitação para estratégia de testes, SAST, DAST, gestão de findings, regressão, pentesting e evidência auditável.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:testes, TST, SAST, DAST, IAST, fuzzing, pentesting, findings, rastreabilidade, L1, L2, L3, auditoria, evidencia]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Testes de Segurança

## Âmbito: o programa de testes como requisito de processo

Este catálogo cobre **requisitos do programa de testes de segurança** - os controlos de processo que definem como os testes de segurança são planeados, executados, geridos e evidenciados ao longo do ciclo de vida. Distingue-se dos requisitos aplicacionais de validação de input (Cap. 02, VAL-) por se focar no *programa* de testes em si, não nas propriedades que o software deve ter.

O âmbito inclui: estratégia formal de testes proporcional ao risco, SAST como gate programático com cobertura gerida, DAST em ambiente de staging, gestão de findings com SLA, testes de regressão para vulnerabilidades corrigidas, fuzzing e IAST para casos de risco elevado, pentesting periódico e produção de evidência auditável e reproduzível.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de OWASP SAMM (Practice: Security Testing), NIST SSDF (RV.1), OWASP ASVS (verificação programática), DSOMM, NIST SP 800-115 (Technical Guide to Information Security Testing) e boas práticas de integração de testes de segurança em SDLC. Deve ser adaptado ao contexto tecnológico e revisto com cada ciclo de actualização da estratégia de testes.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-TST-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo TST - Testes de Segurança

Requisitos que garantem que o programa de testes de segurança é planeado, executado, gerido e evidenciado de forma proporcional ao risco e auditável.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| TST-001 | Estratégia formal de testes de segurança por nível de risco | ✔ | ✔ | ✔ | Documento de estratégia com tipologias de teste, frequência, responsáveis e critérios de aceitação por nível de risco; revisto pelo menos anualmente ou após alteração significativa de risco ou arquitectura. |
| TST-002 | SAST com perfil de cobertura gerido e baseline de falsos positivos | ✔ | ✔ | ✔ | Scanner SAST com perfil de regras documentado e versionado; baseline de falsos positivos aprovada por AppSec; evidência de cobertura de componentes críticos; taxa de falsos positivos revista periodicamente. |
| TST-003 | Gestão formal de findings com SLA de correcção por severidade | ✔ | ✔ | ✔ | SLA de correcção definido por severidade (ex: crítico ≤ 7 dias, elevado ≤ 30 dias); rastreabilidade finding → ticket → correcção → verificação; findings não resolvidos no SLA com excepção formalizada. |
| TST-004 | Evidência de testes reproduzível, auditável e ligada ao build | ✔ | ✔ | ✔ | Relatórios de testes de segurança associados ao build que os gerou; reproduzíveis a partir do mesmo estado do código; retidos pelo período definido em política; disponíveis para auditoria sem necessidade de re-execução. |
| TST-005 | DAST integrado em ambiente de staging antes de promoção | - | ✔ | ✔ | Scanner DAST activo em ambiente de staging representativo de produção; política de findings definida (o que bloqueia vs. o que alerta); evidência de execução por release; ambiente de staging com dados não reais. |
| TST-006 | Testes de regressão de segurança para vulnerabilidades corrigidas | - | ✔ | ✔ | Cada vulnerabilidade corrigida origina um teste de regressão que comprova a correcção e previne recorrência; testes de regressão integrados no pipeline; evidência de cobertura disponível. |
| TST-007 | Thresholds mínimos de cobertura de testes de segurança por risco | - | ✔ | ✔ | Critérios de cobertura mínima definidos por nível de risco (ex: componentes de autenticação, autorização, validação de input); cobertura medida e reportada; desvios documentados e tratados. |
| TST-008 | Testes de penetração periódicos com escopo e metodologia definidos | - | ✔ | ✔ | Pentesting executado com frequência mínima definida por nível de risco (ex: anual para L2, semestral para L3); escopo documentado; relatório com findings, severidade e plano de correcção; correcções verificadas em reteste. |
| TST-009 | Fuzzing sistemático em componentes de processamento de input complexo | - | - | ✔ | Fuzzing integrado no pipeline ou executado periodicamente para parsers, deserializadores, APIs com input estruturado ou lógica com alta entropia de input; corpus gerido e evidência de execução disponível. |
| TST-010 | IAST em ambiente de staging para validação comportamental em runtime | - | - | ✔ | IAST instrumentado em ambiente de staging para aplicações L3; coverage de fluxos críticos verificada; findings de IAST processados com a mesma política de gestão que outros findings de testes. |

---

## Notas explicativas

- **TST-001**: A estratégia de testes não é um documento único e estático - é um acordo operacional que deve ser actualizado quando muda o risco, a arquitectura ou a stack tecnológica. Uma estratégia não revista há dois anos é provavelmente inadequada.
- **TST-002**: A distinção entre DEV-003 (SAST como gate de desenvolvimento) e TST-002 é de perspectiva: DEV-003 trata do gate no ciclo de coding/PR; TST-002 trata do programa de SAST como controlo de cobertura - quais componentes estão cobertos, qual a qualidade do perfil e como se gere o ruído.
- **TST-003**: A gestão de findings é frequentemente o ponto fraco dos programas de teste: é comum ter ferramentas activas mas findings não tratados. O SLA sem rastreabilidade é ineficaz; a rastreabilidade sem SLA é inauditável.
- **TST-005**: O ambiente de staging deve ser suficientemente representativo de produção para que os resultados do DAST sejam relevantes - staging com configuração substancialmente diferente de produção produz resultados enganadores.
- **TST-008**: O pentesting não substitui os testes automatizados contínuos - complementa-os com validação adversarial contextualizada. O reteste de correcções é um elemento frequentemente omitido mas essencial para fechar o ciclo.

---

> Para estratégia integrada de testes no SDLC, consultar [Estratégia de Testes](./estrategia-testes).
> Para SAST, consultar [Análise Estática (SAST)](./sast).
> Para DAST, consultar [Análise Dinâmica (DAST)](./dast).
> Para gestão de findings, consultar [Gestão de Findings](./gestao-findings).
> Para evidência e reprodutibilidade, consultar [Evidência e Reprodutibilidade](./evidencia-reprodutibilidade).
> Para testes de penetração, consultar [Pen Testing](./pen-testing).
