---
id: excecoes-deploy
title: Excepções em Deploy Seguro
sidebar_position: 9
description: Especificidades da gestão de excepções no contexto de deploy seguro — emergency deploy, break glass e desvios a gates de promoção
tags: [exceções, deploy, emergency, break-glass, gates, aprovacao, rollback]
---

# Excepções em Deploy Seguro

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 — `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a requisitos do catálogo de deploy seguro: `DPL-001` a `DPL-009`. Inclui o cenário de emergency deploy (break glass) como caso de excepção imediata com evidência post-facto.

---

## Triggers específicos deste domínio

- deploy de emergência (hotfix crítico, resposta a incidente em produção) que não pode aguardar o processo normal de aprovação e gates — "break glass" (DPL-001, DPL-003);
- artefacto sem proveniência verificável em contexto de recuperação de desastre onde o pipeline normal está indisponível (DPL-002);
- staging não suficientemente representativo de produção para determinado tipo de validação, com justificação técnica documentada (DPL-007);
- rollback não testável para determinado componente legado — com compensação operacional (DPL-005);
- deploy progressivo arquitecturalmente inviável para componente específico, com justificação técnica (DPL-009).

---

## Emergency deploy — break glass

O emergency deploy é o único cenário em que a excepção pode ser aprovada *post-facto*, imediatamente após o deploy e antes do término da janela de deploy. Não é um bypass permanente — é uma excepção única e rastreável.

Requisitos específicos:

| Elemento | Obrigatório |
|---|---|
| Referência ao incidente ou motivo de emergência | Sim |
| Notificação ao CISO ou equivalente antes ou durante o deploy | Sim |
| Registo de change de emergência no sistema de change management | Sim |
| Aprovação post-facto no prazo máximo de 24h após o deploy | Sim |
| Post-mortem documentado com análise da causa e acções correctivas | Sim |
| Revisão do processo para prevenir recorrência | Recomendado |

A ausência de registo de change de emergência ou de notificação ao CISO invalida o emergency deploy como excepção — passa a ser um deploy não autorizado.

---

## Campos adicionais obrigatórios (deploy)

| Campo | Obrigatório | Notas |
|---|---|---|
| ID do deploy / release | Sim | Identificador único rastreável |
| Ambiente afectado | Sim | staging / production / etc. |
| Artefacto(s) promovido(s) | Sim | Nome, versão, commit SHA |
| Gates não executados | Sim | Quais gates foram saltados e porquê |
| Referência ao incidente (se emergency) | Condicional | Obrigatório em break glass |

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `00-catalogo-requisitos.md` | Catálogo DPL-001..009 — requisitos que podem ter excepções |
| `04-validacoes-pre-deploy.md` | Gates de segurança que podem ser objecto de excepção |
| `06-controle-versao-e-rollback.md` | Rollback como compensação em excepções de deploy |
| Cap. 07 — `addon/09-controle-excecoes-visibilidade.md` | Bypass de gates CI/CD — distinto do emergency deploy a produção |
| Cap. 14 — `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
