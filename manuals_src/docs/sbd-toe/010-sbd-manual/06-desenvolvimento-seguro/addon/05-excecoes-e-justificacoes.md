---
id: excecoes-e-justificacoes
title: Excepções em Desenvolvimento Seguro
sidebar_position: 5
description: Especificidades da gestão de excepções no contexto de desenvolvimento seguro — SAST, linters e revisão de código
tags: [exceções, validação, rastreabilidade, segurança, desenvolvimento, sast]
---

# Excepções em Desenvolvimento Seguro

> Processo base, alçadas, campos obrigatórios, cadeia de autoridade e lifecycle estão definidos em **Cap. 14 — `addon/12-processo-excecoes.md`**. Este ficheiro define apenas as especificidades deste domínio.

---

## Âmbito

Excepções a práticas e controlos identificados por ferramentas SAST, linters ou revisão de código durante o desenvolvimento.

---

## Triggers específicos deste domínio

- finding de ferramenta SAST classificado como falso positivo com evidência técnica demonstrável;
- prática obrigatória incompatível com constraint de framework ou biblioteca externa sem alternativa viável;
- retrocompatibilidade com componente que não pode ser modificado no âmbito do projecto;
- desvio temporário aceite em PR com plano de resolução datado e registado.

---

## Mecanismos de registo em ferramentas SAST

As ferramentas SAST permitem marcar findings directamente no relatório — `mute`, `waive`, `false positive accepted`, anotação inline. Estas marcações são válidas como mecanismo de registo técnico, mas **não substituem a aprovação formal** nem a cadeia de autoridade exigida pelo processo canónico.

Ferramentas de referência: Kiuwan, SonarQube, Xygeni, Checkmarx, Semgrep.

---

## Rastreabilidade no repositório

Além do registo no sistema de tracking, a excepção deve ser visível no repositório:

- **Ficheiro versionado:** `excecoes-aprovadas.yml` com referência ao finding, justificação, aprovador e validade;
- **Anotação inline:** comentário `@sec:justificado: <ID-excepção>` no código afectado;
- **PR / merge commit:** link explícito ao registo de excepção no corpo do PR ou na mensagem de commit.

O registo no repositório complementa o registo no sistema de tracking e garante rastreabilidade directa ao código. Não o substitui.

---

## Referências cruzadas

| Documento | Relação |
|---|---|
| `addon/01-boas-praticas-codigo.md` | Práticas que podem ter excepções associadas |
| `addon/02-linters-validacoes.md` | Ferramentas que geram findings candidatos a excepção |
| `addon/08-validacoes-codigo.md` | Revisão de código e bloqueios em PRs |
| Cap. 14 — `addon/12-processo-excecoes.md` | Processo canónico de gestão de excepções |
