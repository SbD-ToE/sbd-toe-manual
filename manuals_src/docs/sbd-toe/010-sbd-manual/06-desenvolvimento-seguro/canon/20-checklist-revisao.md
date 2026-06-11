---
id: checklist-revisao
title: Checklist - Desenvolvimento Seguro
sidebar_label: Checklist de Revisão
description: Checklist binário e auditável para avaliar a adoção prática das práticas prescritas no Capítulo 06 - Desenvolvimento Seguro
tags: [checklist, desenvolvimento, validação, auditoria, conformidade]
sidebar_position: 20
---

# Checklist de Revisão Periódica - Desenvolvimento Seguro

Este checklist aplica-se a todas as aplicações sujeitas às práticas definidas no Capítulo 06 - Desenvolvimento Seguro.
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições deste capítulo** (`DEV-001` a `DEV-009`), permitindo:

- Controlo contínuo da aplicação de práticas seguras de desenvolvimento
- Verificação por projeto em momentos-chave do ciclo de vida
- Geração de indicadores operacionais agregáveis por equipa

> 🗓️ **Recomenda-se a sua aplicação a cada release significativa**, ou sempre que existirem alterações de stack, dependências ou zonas críticas de código.

---

## 📋 Itens de Verificação

| Item                                                                                                   | Verificado? |
|--------------------------------------------------------------------------------------------------------|-------------|
| Existe guideline de código seguro versionada e aprovada formalmente (Gestor Técnico e AppSec) por stack, dentro do período de validade? (`DEV-001`) | ☐           |
| Estão configurados linters/rulesets de segurança versionados, com enforcement local e em pipeline, e as violações críticas bloqueiam commit ou merge? (`DEV-002`) | ☐           |
| O SAST está integrado como gate, com findings de severidade alta/crítica a bloquear merge e baseline de falsos positivos aprovada por AppSec? (`DEV-003`) | ☐           |
| O pipeline deteta e bloqueia padrões perigosos (eval/exec, concatenação SQL, XSS, secrets hardcoded)? (`DEV-002`/`DEV-003`) | ☐           |
| As dependências externas estão validadas (SCA/CVE) e justificadas, com registo de SBOM (CycloneDX ou SPDX)? | ☐           |
| Os componentes críticos são revistos com checklist de segurança formal, com evidência por PR? (`DEV-004`) | ☐           |
| As exceções técnicas estão registadas com justificação, mitigação, aprovação por papel autorizado, prazo e owner, e revistas periodicamente? (`DEV-005`) | ☐           |
| A proveniência do código incorporado (reutilizado, adaptado ou gerado por GenAI) é identificada antes da incorporação, com revisão humana para proveniência não interna? (`DEV-006`) | ☐           |
| O uso de GenAI para gerar código está sujeito a constrangimentos técnicos explícitos e versionados, sem incorporação automática sem revisão? (`DEV-007`) | ☐           |
| Os prompts, skill files, agent files e rules são tratados como código (versionados, code review, secret scanning, drift detection, inventário com owner)? | ☐           |
| O output estruturado de modelos é validado lado-servidor (schema versionado, validação sintáctica e semântica) antes de ser consumido? | ☐           |
| Existem perfis de qualidade com thresholds de segurança por nível de risco, versionados, com desvios a bloquear o pipeline ou a exigir aprovação? (`DEV-008`) | ☐           |
| As validações e exceções estão anotadas no código/testes com referência rastreável (`@sec:`) ao requisito ou decisão? (`DEV-009`) | ☐           |
| As evidências de validação (linters, scanners, testes) estão versionadas ou arquivadas, e existe gate de segurança obrigatório antes de cada release? | ☐           |
| Os controlos implementados estão alinhados com o nível de risco da aplicação (L1–L3) definido no Cap. 01? | ☐           |

---

## 🔄 Notas de aplicação prática

- Este checklist pode ser transformado em **formulário digital, step de CI/CD ou dashboard de conformidade técnica**.
- Cada item pode ser convertido em KPI binário (sim/não) por projeto, equipa ou stack tecnológica.
- A validação completa deste checklist permite afirmar **conformidade técnica com o Capítulo 06**, para efeitos de maturidade organizacional SbD-ToE.

> ❗ Este capítulo é **essencial** para a aplicação coerente dos requisitos definidos no Capítulo 2.
> A ausência destas práticas compromete a validação objetiva e auditável da segurança no desenvolvimento.
