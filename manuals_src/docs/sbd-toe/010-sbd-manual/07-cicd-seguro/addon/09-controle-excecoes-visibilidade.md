---
id: controle-excecoes-visibilidade
title: Excepções e Visibilidade em CI/CD
sidebar_position: 9
description: Especificidades da gestão de excepções no contexto de pipelines CI/CD - bypass de gates, visibilidade e métricas
tags: [exceções, visibilidade, cicd, governação, auditoria]
---

# Excepções e Visibilidade em CI/CD

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 - `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a gates de segurança, políticas de pipeline e controlos de CI/CD - bypass temporário de validações, desactivação de ferramentas ou desvio a políticas de execução.

---

## Triggers específicos deste domínio

- gate de segurança bloqueante em contexto de incidente crítico com necessidade de deploy urgente e documentado;
- ferramenta de validação indisponível com impacto no ciclo de release;
- aplicação legada integrada no pipeline sem suporte técnico aos controlos exigidos;
- janela de excepção durante migração de pipeline com prazo delimitado.

---

## Visibilidade obrigatória no pipeline

Toda a excepção activa deve ser **explicitamente assinalada** nos logs, artefactos de execução ou metadados do pipeline. Uma excepção invisível no pipeline é equivalente a um bypass não controlado.

Mecanismos de sinalização por ferramenta:

| Ferramenta | Mecanismo sugerido |
|---|---|
| GitHub Actions | Label `bypass-security-gate` no PR; aprovação visível no histórico de execução |
| GitLab CI | Ficheiro `exception.yaml` no MR; revisão por `Security Approval` |
| Azure DevOps | Override em release associado a Work Item com referência ao registo de excepção |
| Jenkins | Flag `bypass=true` comentado no `Jenkinsfile`; integração com Jira ou ServiceNow |

---

## Métricas associadas

As excepções CI/CD contribuem directamente para os KPIs de maturidade (ver Cap. 14 - `kpis-governanca.md`):

- % de pipelines com gates de segurança activos;
- nº de excepções activas por categoria (SAST, SBOM, signing, deploy gates);
- aplicações L3 com enforcement desactivado ou em excepção.

Estes indicadores devem ser reportados no ciclo de governação.

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `addon/06-politicas-gates-pipeline.md` | Gates e políticas de pipeline que podem ser objecto de excepção |
| `addon/07-validacoes-seguranca-integradas.md` | Validações integradas e condições de bypass |
| Cap. 14 - `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
| Cap. 14 - `kpis-governanca.md` | Indicadores de conformidade e excepções activas |
