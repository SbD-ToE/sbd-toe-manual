---
id: catalogo-requisitos-desenvolvimento
title: Catálogo de Requisitos de Desenvolvimento Seguro
description: Catálogo canónico de requisitos de segurança para o processo de desenvolvimento (DEV-001 a DEV-009), com aplicabilidade por nível de risco e critérios de aceitação para guidelines de código, linters, revisão formal, gestão de excepções, proveniência e anotações rastreáveis.
requirement_class: dominio
tags: [tipo:catalogo, classe:dominio, tema:desenvolvimento, DEV, secure-coding, guidelines, linters, SAST, revisao-codigo, rastreabilidade, L1, L2, L3, auditoria, proveniencia]
sidebar_position: 0
---

<!--template: sbdtoe-addon -->

# Catálogo de Requisitos de Desenvolvimento Seguro

## Âmbito: práticas e processos durante o desenvolvimento

Este catálogo cobre **requisitos de segurança aplicáveis ao processo de desenvolvimento** - as práticas, mecanismos e controlos que devem estar activos durante a escrita de código, revisão de pull requests e integração de contribuições, garantindo que a segurança é incorporada sistematicamente desde o primeiro commit.

O âmbito inclui: curadoria de guidelines por stack, configuração de linters e rulesets de segurança, análise estática como gate de integração, revisão de código com checklists formais, gestão de excepções técnicas, governação da proveniência do código (incluindo código gerado por ferramentas de IA) e anotações rastreáveis de decisões de segurança.

Para o mapeamento completo de todos os catálogos de requisitos do SbD-ToE por domínio técnico, prefixo canónico e responsável, consultar [Cap. 02 - Mapeamento de Catálogos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/lista-requisitos-base#mapeamento-de-catalogos).

> **Sobre a curadoria:** Consolidado a partir de OWASP SAMM (Practice: Secure Build, Code Review), NIST SSDF (PW.1, PW.2, PW.4), CWE Top 25, OWASP Top 10 e boas práticas de engenharia de software segura. Deve ser adaptado ao contexto tecnológico (stacks, linguagens, ferramentas) e revisto com cada ciclo de curadoria de guidelines.

Para instanciação em projecto e nomenclatura operacional (`SEC-Lx-DEV-CODIGO`), ver [Taxonomia e Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade).

---

## Convenções

| Símbolo | Significado |
|---------|-------------|
| ✔ | Requisito obrigatório para este nível |
| - | Não aplicável ou não obrigatório a este nível |

Os níveis são cumulativos: L3 inclui todos os requisitos de L1 e L2; L2 inclui todos os de L1.

---

## Catálogo DEV - Desenvolvimento Seguro

Requisitos que garantem que as práticas e processos de desenvolvimento incorporam controlos de segurança sistemáticos, verificáveis e proporcionais ao risco.

| ID | Nome | L1 | L2 | L3 | Critério de aceitação |
|----|------|:--:|:--:|:--:|----------------------|
| DEV-001 | Guidelines de código seguro versionadas e aprovadas por stack | ✔ | ✔ | ✔ | Guidelines por linguagem/stack publicadas em repositório versionado; aprovação formal por Gestor Técnico e AppSec documentada; data de última revisão disponível e dentro do período de validade. |
| DEV-002 | Linters e rulesets de segurança configurados e enforced | ✔ | ✔ | ✔ | Linter com regras de segurança activo localmente e em pipeline; ruleset versionado no repositório do projecto; tailoring documentado e aprovado; violações de padrões críticos bloqueiam commit ou merge. |
| DEV-003 | Análise estática (SAST) integrada como gate de integração | ✔ | ✔ | ✔ | Scanner SAST activo em cada PR ou commit; findings de severidade alta ou crítica bloqueam merge; perfil de regras versionado; baseline de falsos positivos documentada e aprovada por AppSec. |
| DEV-004 | Revisão de código com checklist de segurança em componentes críticos | ✔ | ✔ | ✔ | PRs com alterações em componentes de segurança, autenticação, autorização ou dados sensíveis sujeitos a revisão com checklist formal; evidência de checklist preenchido disponível por PR. |
| DEV-005 | Gestão formal de excepções técnicas e desvios a guidelines | - | ✔ | ✔ | Excepções documentadas com: justificação técnica, mitigação definida, aprovação explícita por papel autorizado e prazo de validade; registo de excepções activas revisto periodicamente e disponível para auditoria. |
| DEV-006 | Proveniência do código incorporado identificada e controlada | - | ✔ | ✔ | Código de origem externa (reutilizado, adaptado, gerado por ferramentas de IA) identificado antes de incorporação; política de proveniência documentada; evidência de revisão humana por PR para código de proveniência não interna. |
| DEV-007 | Constrangimentos técnicos explícitos para código gerado por IA | - | ✔ | ✔ | Política de uso de ferramentas de IA generativa no desenvolvimento documentada, versionada e comunicada à equipa; constrangimentos técnicos (âmbito, validação, aprovação) definidos e verificáveis; sem incorporação automática de sugestões sem revisão explícita. |
| DEV-008 | Perfis de qualidade com thresholds mínimos de segurança por nível de risco | - | ✔ | ✔ | Perfis de qualidade (ex: SonarQube Quality Gates) com thresholds mínimos definidos por nível de risco; desvios bloqueam pipeline ou requerem aprovação explícita documentada; perfis versionados. |
| DEV-009 | Anotações de segurança rastreáveis no código e nos testes | - | - | ✔ | Decisões de segurança relevantes e excepções anotadas no código com referência rastreável ao requisito canónico ou decisão documentada (ex: `// SEC-L3-VAL-SQLI`, `@sec:exception:DEV-005`); possível auditar a ligação entre código e requisito sem contexto externo. |

---

## Notas explicativas

- **DEV-001**: A curadoria de guidelines deve ser tratada como um produto interno - com ownership claro, versionamento semântico e ciclo de revisão definido. Guidelines desactualizadas são mais perigosas do que a ausência delas, pois criam falsa confiança.
- **DEV-002**: O tailoring de rulesets (desactivação de regras, ajuste de thresholds) deve ser explicitamente documentado e aprovado - evitando que a "personalização" se torne um mecanismo de contorno de controlos.
- **DEV-003**: A baseline de falsos positivos é crítica para a operacionalização do SAST: sem ela, o ruído de findings irá comprometer a eficácia do gate e criar pressão para o desactivar.
- **DEV-006 e DEV-007**: A proveniência múltipla do código (humano, reutilizado, gerado por IA) é uma realidade que não pode ser ignorada. O critério relevante não é a origem do código, mas a sua compreensão, validação e responsabilização formais - independentemente de quem ou do quê o produziu.
- **DEV-009**: As anotações rastreáveis são particularmente valiosas em contextos de auditoria, resposta a incidentes e rotatividade de equipa - permitem reconstituir a intenção de segurança de uma decisão sem acesso ao contexto original da pessoa que a tomou.

---

> Para boas práticas de escrita de código seguro por stack, consultar [Boas Práticas de Código Seguro](./boas-praticas-codigo).
> Para configuração de linters e validações automáticas, consultar [Linters e Validações](./linters-validacoes).
> Para proveniência e rastreabilidade de código, consultar [Proveniência do Código](./proveniencia-codigo).
> Para gestão de excepções e justificações, consultar [Excepções e Justificações](./excecoes-e-justificacoes).
> Para uso responsável de ferramentas de IA no desenvolvimento, consultar [IA e Segurança](./genia-e-seguranca).
