---
id: excecoes-operacoes
title: Excepções em Monitorização e Operações
sidebar_position: 10
description: Especificidades da gestão de excepções no contexto de monitorização e operações — alert silencing, retenção de logs e implicações regulatórias
tags: [exceções, operacoes, monitorizacao, alertas, retencao, DORA, NIS2, SIEM]
---

# Excepções em Monitorização e Operações

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 — `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a requisitos do catálogo de monitorização e operações: `OPS-001` a `OPS-010`. Dois cenários têm especificidades relevantes: alert silencing (OPS-005) e retenção de logs abaixo do mínimo regulatório (OPS-003).

---

## Triggers específicos deste domínio

- alerta silenciado temporariamente por manutenção programada, ruído excessivo de falsos positivos, ou incapacidade técnica de resposta num período definido (OPS-005);
- retenção de logs abaixo do mínimo definido na política ou exigido por regulação — por constrangimento de armazenamento, custo ou conflito com outra obrigação legal (OPS-003);
- fonte de logs não integrada no SIEM por incompatibilidade técnica ou ausência de conector, com compensação de monitorização alternativa (OPS-004);
- SLA de resposta a alertas não cumprível para determinado tipo de evento por falta de capacidade operacional, com plano de reforço (OPS-006).

---

## Alert silencing — requisitos específicos

O silenciamento de alertas é o cenário de maior risco neste domínio: elimina visibilidade activa sem deixar evidência automática. Toda a excepção de silenciamento exige:

- identificação precisa do alerta silenciado (ID, regra, fonte);
- justificação técnica da impossibilidade de manter o alerta activo;
- período de silenciamento com data de fim obrigatória — sem silenciamentos permanentes;
- controlo compensatório de visibilidade activo durante o período (ex: revisão manual periódica, alerta alternativo, monitorização manual da fonte);
- notificação ao responsável de segurança operacional (SOC lead ou equivalente).

Alertas silenciados sem data de fim ou sem controlo compensatório são tratados como não conformidade.

---

## Retenção de logs — implicações regulatórias

Excepções a OPS-003 com retenção abaixo do mínimo regulatório (DORA, NIS2, ou política interna) têm implicações que excedem a aprovação técnica:

- a cadeia de autoridade deve incluir validação jurídica ou de compliance, não apenas AppSec;
- a excepção deve referenciar o requisito regulatório específico que está a ser comprometido;
- o prazo máximo é determinado pelo risco regulatório, não pelo prazo genérico de 90 dias.

---

## Campos adicionais obrigatórios (operações)

| Campo | Obrigatório | Notas |
|---|---|---|
| Fonte / sistema afectado | Sim | Componente, aplicação ou infraestrutura |
| Alerta / regra silenciada (se aplicável) | Condicional | Obrigatório em excepções OPS-005 |
| Período de retenção efectivo vs. mínimo exigido | Condicional | Obrigatório em excepções OPS-003 |
| Regulação ou política comprometida | Condicional | Obrigatório em excepções com implicação regulatória |
| Controlo compensatório de visibilidade | Sim | Mecanismo activo durante a janela de excepção |

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `00-catalogo-requisitos.md` | Catálogo OPS-001..010 — requisitos que podem ter excepções |
| `03-alertas-eventos-criticos.md` | Alertas que podem ser objecto de silenciamento com excepção |
| `08-matriz-controles-por-risco.md` | Matriz de controlos por nível de risco |
| Cap. 14 — `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
